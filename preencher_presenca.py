"""
Preenchimento automático de presença (Defensoras Populares - Souza/PB)

O que faz:
  1. Lê a planilha de respostas do formulário (a "do wpp") - SOMENTE LEITURA, nunca é alterada.
  2. Lê a planilha da própria usuária (a que ela edita, com as alunas de Souza).
  3. Marca "P" na coluna da aula para quem respondeu o formulário (por e-mail ou nome).
  4. Salva uma CÓPIA nova da planilha dela + um relatório de conferência.

Como usar:  python preencher_presenca.py
(abrem janelas para escolher os arquivos) 
Instalar uma vez:  pip install pandas openpyxl
"""
import sys, re, unicodedata
from difflib import SequenceMatcher
from pathlib import Path
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

# ===================== CONFIGURAÇÕES (ajuste se precisar) =====================
GRUPO_FORMULARIO = "Paraíba"      # valor da coluna "Grupos" que inclui Souza + João Pessoa
MARCA_PRESENTE   = "P"            # o que escrever quando presente
MARCA_AUSENTE    = ""             # "" = deixa vazio (mais seguro). Use "F" se quiser marcar falta
LIMITE_CERTO     = 0.88           # similaridade de nome para marcar automaticamente
LIMITE_DUVIDA    = 0.75           # entre este valor e o anterior: vai para "conferir", não marca
VERDE   = PatternFill("solid", start_color="C6EFCE")   # presente
AMARELO = PatternFill("solid", start_color="FFEB9C")   # não encontrada: decidir P ou F
LARANJA = PatternFill("solid", start_color="F8CBAD")   # nome parecido: conferir
# ==============================================================================


def normaliza(txt):
    txt = unicodedata.normalize("NFKD", str(txt)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", " ", txt.lower())).strip()


def acha_coluna(colunas, *palavras):
    for c in colunas:
        n = normaliza(c)
        if all(p in n for p in palavras):
            return c
    return None


def similaridade(a, b):
    a, b = normaliza(a), normaliza(b)
    if not a or not b:
        return 0.0
    ta, tb = a.split(), b.split()
    # primeiro + último nome iguais = quase certeza
    if len(ta) > 1 and len(tb) > 1 and ta[0] == tb[0] and ta[-1] == tb[-1]:
        return max(0.9, SequenceMatcher(None, a, b).ratio())
    # nome curto contido no longo (ex: "Edivanha Dias" x "Edivanha Dias Pereira")
    if min(len(ta), len(tb)) >= 2 and (set(ta) <= set(tb) or set(tb) <= set(ta)):
        return 0.9
    return SequenceMatcher(None, a, b).ratio()


def escolher_arquivo(titulo, argv_idx):
    if len(sys.argv) > argv_idx:
        return sys.argv[argv_idx]
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk(); root.withdraw(); root.attributes("-topmost", True)
    return filedialog.askopenfilename(title=titulo, filetypes=[("Excel", "*.xlsx")])


def main():
    f_form = escolher_arquivo("1) Escolha a planilha de RESPOSTAS do formulário (wpp)", 1)
    f_minha = escolher_arquivo("2) Escolha a SUA planilha (alunas de Souza)", 2)
    if not f_form or not f_minha:
        sys.exit("Cancelado.")
    nome_coluna = sys.argv[3] if len(sys.argv) > 3 else input(
        "Nome da coluna a preencher (ex: Módulo 6 - Aula 2): ").strip()

    # ---- respostas do formulário
    form = pd.read_excel(f_form, dtype=str).fillna("")
    c_nome = acha_coluna(form.columns, "nome")
    c_mail = acha_coluna(form.columns, "mail")
    c_grupo = acha_coluna(form.columns, "grupo")
    if c_grupo:
        form = form[form[c_grupo].str.strip().str.lower() == GRUPO_FORMULARIO.lower()]
    print(f"Respostas do grupo {GRUPO_FORMULARIO}: {len(form)}")
    form_emails = {e.strip().lower(): n for e, n in zip(form[c_mail], form[c_nome]) if e.strip()}
    form_nomes = list(form[c_nome])

    # ---- planilha dela (preserva formatação e o que ela já digitou)
    wb = load_workbook(f_minha)
    ws = wb.active
    cab = {str(c.value).strip(): c.column for c in ws[1] if c.value}
    m_nome = acha_coluna(cab, "nome")
    m_mail = acha_coluna(cab, "mail")
    if not m_nome:
        sys.exit("Não achei a coluna de nome na sua planilha (cabeçalho precisa ter 'Nome').")
    if nome_coluna not in cab:
        col_dest = ws.max_column + 1
        ws.cell(1, col_dest, nome_coluna)
        ws.cell(1, col_dest)._style = ws.cell(1, col_dest - 1)._style
        ws.column_dimensions[ws.cell(1, col_dest).column_letter].width = 20
        dv = DataValidation(type="list", formula1='"P,F"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{ws.cell(2, col_dest).coordinate}:{ws.cell(max(ws.max_row, 300), col_dest).coordinate}")
        print(f"Coluna nova criada: {nome_coluna}")
    else:
        col_dest = cab[nome_coluna]

    relatorio, usados = [], set()
    for r in range(2, ws.max_row + 1):
        nome = ws.cell(r, cab[m_nome]).value
        if not nome:
            continue
        atual = ws.cell(r, col_dest).value
        if atual not in (None, ""):          # já preenchido (anotação manual): não mexe
            relatorio.append((nome, "já preenchido - mantido", atual, ""))
            continue

        email = str(ws.cell(r, cab[m_mail]).value or "").strip().lower() if m_mail else ""
        achou, motivo, ref = False, "", ""
        if email and email in form_emails:
            achou, motivo, ref = True, "e-mail", form_emails[email]
        else:
            melhor = max(form_nomes, key=lambda n: similaridade(nome, n), default="")
            s = similaridade(nome, melhor) if melhor else 0
            if s >= LIMITE_CERTO:
                achou, motivo, ref = True, f"nome ({s:.0%})", melhor
            elif s >= LIMITE_DUVIDA:
                motivo, ref = f"CONFERIR nome parecido ({s:.0%})", melhor
        if achou:
            ws.cell(r, col_dest, MARCA_PRESENTE)
            ws.cell(r, col_dest).fill = VERDE
            usados.add(ref)
            relatorio.append((nome, "PRESENTE", motivo, ref))
        else:
            if MARCA_AUSENTE:
                ws.cell(r, col_dest, MARCA_AUSENTE)
            # amarelo = decidir (P ou F); laranja = conferir nome parecido
            ws.cell(r, col_dest).fill = LARANJA if motivo else AMARELO
            relatorio.append((nome, "não encontrada" if not motivo else "CONFERIR", motivo, ref))

    saida = Path(f_minha).with_name(Path(f_minha).stem + f" - preenchida ({nome_coluna}).xlsx")
    wb.save(saida)

    rel = pd.DataFrame(relatorio, columns=["Nome na sua planilha", "Resultado", "Critério", "Nome no formulário"])
    sobras = pd.DataFrame({"Respondeu o form (Paraíba) e não está na sua lista": 
                           [n for n in form_nomes if n not in usados]})
    rel_path = saida.with_name(saida.stem + " - RELATORIO.xlsx")
    with pd.ExcelWriter(rel_path) as w:
        rel.to_excel(w, sheet_name="Conferência", index=False)
        sobras.to_excel(w, sheet_name="Sobras (João Pessoa etc.)", index=False)

    print(f"\nPresentes marcadas: {(rel['Resultado']=='PRESENTE').sum()}")
    print(f"Para conferir à mão: {(rel['Resultado']=='CONFERIR').sum()}")
    print(f"Planilha salva em: {saida}\nRelatório em: {rel_path}")


if __name__ == "__main__":
    main()
