# Automacao_Lista

# 📋 Presença Automática – Alunas de Souza

**Para quê serve:** o computador compara quem respondeu o formulário da aula com a **lista de alunas de Souza** e já deixa a planilha quase pronta. A pessoa que dá a presença só olha as **células coloridas** e decide **P** (presente) ou **F** (falta).

> 🔒 **Tranquilidade:**
> - O programa **só lê** a planilha de respostas do formulário (a "do wpp", compartilhada com outras monitoras). **Nunca escreve nela.**
> - Antes de mexer na lista de Souza, ele guarda uma **cópia de segurança** na pasta `Backup`. Se algo der errado, é só recuperar a cópia.
> - Ele **só preenche as alunas da lista de Souza**. Quem é de João Pessoa ou de outras cidades **não entra** na planilha.

---

## 🗺️ Visão geral

| Parte | Quem faz | Quando |
|---|---|---|
| **PARTE 1 – Escrever os nomes das alunas** | Quem organiza | **Uma vez** (e quando entrar aluna nova) |
| **PARTE 2 – Dar a presença de cada aula** | Quem dá a presença | **Toda aula** (~5 minutos) |

> ✅ O computador já está configurado (Python e ferramentas instalados). **Não é preciso instalar nada.**

## 📁 O que tem dentro da pasta `Presenca`

| Item | O que é |
|---|---|
| `ABRIR_AQUI.bat` | O "botão" que liga o programa (dois cliques). |
| `Alunas_Souza.xlsx` | **A lista de alunas.** É aqui que ficam os nomes e as presenças de todas as aulas. |
| `preencher_presenca.py` | O programa. **Não precisa abrir.** |
| `README.md` | Este guia. |
| `Backup` *(criada sozinha)* | Cópias de segurança da lista, feitas antes de cada uso. |
| `Relatorios` *(criada sozinha)* | Relatórios de conferência de cada aula. |

⚠️ **Não mude esses arquivos de lugar nem renomeie** `Alunas_Souza.xlsx`, `preencher_presenca.py` e `ABRIR_AQUI.bat`. Eles precisam ficar **juntos, na mesma pasta**.

---

# 🅰️ PARTE 1 – Escrever os nomes das alunas

## Passo 1.1 – Abrir a lista

1. Abra a pasta `Presenca`.
2. Dê dois cliques em **`Alunas_Souza.xlsx`**.

Você verá:

| Nome | E-mail | Módulo 5 - Aula 2 | Módulo 6 - Aula 2 |
|---|---|---|---|
| *(escreva aqui)* | *(escreva aqui)* | | |

## Passo 1.2 – Escrever os nomes

1. **Coluna A – Nome:** escreva o nome de **cada aluna de Souza**, **um por linha**, a partir da **linha 2**.
2. **Coluna B – E-mail:** escreva o e-mail que a aluna usa no formulário. É **opcional, mas muito recomendado**: o e-mail funciona como um "CPF" e evita confusão com nomes parecidos. Se não souber, deixe em branco.
3. Há linhas prontas para **100 alunas**. Se tiver mais, continue escrevendo para baixo.

⚠️ **Regras de ouro:**
- **Não apague nem mude** os títulos da **linha 1**.
- **Não deixe linhas em branco** no meio dos nomes.
- Mantenha o arquivo em **`.xlsx`**.

## Passo 1.3 – Salvar e fechar

Aperte **Ctrl + S** e **feche o Excel por completo**. (Com o arquivo aberto, o programa não consegue usá-lo.)

🎉 **Parte 1 pronta!** Só volte aqui quando entrar uma aluna nova: escreva o nome (e e-mail) dela na **primeira linha vazia**.

---

# 🅱️ PARTE 2 – Dar a presença de cada aula

## Passo 2.1 – Baixar a planilha de respostas

Baixe a planilha de respostas **da aula** (a do formulário/wpp) em **`.xlsx`** e deixe na pasta **Downloads** (o programa já abre a janela de escolha por lá).

> ℹ️ **Só tem PDF?** O programa **não lê PDF**. Peça o arquivo em Excel (`.xlsx`) a quem administra o formulário. No Google Forms: **Respostas → três pontinhos → "Baixar respostas (.csv)"**, abra no Excel e **Salvar como `.xlsx`**.

## Passo 2.2 – Fechar o Excel

**Feche todas as planilhas abertas**, principalmente a `Alunas_Souza.xlsx`.

## Passo 2.3 – Ligar o programa

1. Abra a pasta `Presenca`.
2. Dê **dois cliques** em **`ABRIR_AQUI.bat`**.
3. Abre uma **janela preta**. É normal, é o programa funcionando. 🙂

> ⚠️ Se aparecer uma tela azul *"O Windows protegeu o computador"*, clique em **"Mais informações"** → **"Executar assim mesmo"**.

## Passo 2.4 – Escolher a planilha de respostas

Abre **uma janelinha**: *"1) Escolha a planilha de RESPOSTAS do formulário (wpp)"*.

- Clique na planilha baixada **uma vez** e depois em **Abrir**.
- A lista `Alunas_Souza.xlsx` o programa **já encontra sozinho**. Você não escolhe.

> 💡 Se a janelinha não aparecer, olhe a **barra de baixo** do Windows: deve ter um ícone piscando. Clique nele.

## Passo 2.5 – Dizer o nome da aula

Na janela preta aparece:

```
Nome da coluna a preencher (ex: Módulo 6 - Aula 2):
```

Digite o nome da aula e aperte **Enter**. Exemplos: `Módulo 6 - Aula 2`, `Módulo 7 - Aula 1`.

- Se a coluna **já existe** (como as duas que vêm na lista), digite **igualzinho** ao título (mesmos acentos e hífen).
- Se **não existe**, o programa **cria uma coluna nova**, já com a lista suspensa **P / F**.

⚠️ Erro de digitação (por exemplo, sem o acento) cria uma coluna **duplicada**. Na dúvida, copie o título da planilha.

## Passo 2.6 – Ler o resultado

Em poucos segundos aparece:

```
Respostas do grupo Paraíba: 43

Presentes marcadas: 18
Para conferir à mão: 2
Planilha salva em: ...\Presenca\Alunas_Souza.xlsx
Relatório em: ...\Presenca\Relatorios\Relatorio - Módulo 6 - Aula 2 (...).xlsx

===== Terminou. Pode fechar esta janela. =====
```

| Linha | Significado |
|---|---|
| **Respostas do grupo Paraíba: 43** | 43 pessoas de **toda a Paraíba** responderam (inclui João Pessoa etc.). |
| **Presentes marcadas: 18** | 18 alunas **da lista de Souza** foram encontradas e ganharam **P**. |
| **Para conferir à mão: 2** | 2 nomes **parecidos**, mas o programa não teve certeza. |

Feche a janela preta (**X**).

## Passo 2.7 – Abrir a lista e decidir 🎨

Abra **`Alunas_Souza.xlsx`**. A coluna da aula já está preenchida, com **cores**. **Seu trabalho é só olhar as cores:**

| Cor | O que significa | O que fazer |
|---|---|---|
| 🟩 **Verde** com **P** | A aluna respondeu o formulário. | **Nada.** Já está presente. |
| 🟨 **Amarela** (vazia) | Ninguém com esse nome/e-mail respondeu. | **Decida** pelas suas **anotações manuais**: **P** se esteve na aula, **F** se faltou. |
| 🟧 **Laranja** (vazia) | Há alguém **parecida** no formulário, mas o programa não teve certeza. | Veja o nome parecido no **relatório** (passo 2.8). Se for a mesma pessoa, **P**; senão, decida **P** ou **F**. |

**Escolher sem digitar:** clique na célula, aparece uma **setinha** ▼. Clique e escolha **P** ou **F**. (Também pode digitar a letra.)

Quando **não restar célula amarela ou laranja**, a presença da aula está completa. ✅ **Salve (Ctrl + S)** e feche.

## Passo 2.8 – (Só se precisar) Abrir o relatório

Abra a pasta **`Relatorios`** e o arquivo mais recente. Tem **duas abas**:

- **"Conferência":** uma linha por aluna, com o **resultado**, o **critério** (e-mail ou nome) e o **nome parecido** encontrado, com a porcentagem de semelhança.
- **"Sobras (João Pessoa etc.)":** quem respondeu como "Paraíba" mas **não está na lista de Souza**. Normalmente é de **João Pessoa** ou de outras cidades: **pode ignorar**.
  - **Exceção:** se uma aluna de Souza que você **sabe** que foi à aula ficou **amarela**, procure o nome dela aqui. Se estiver, ela escreveu o nome de outro jeito ou usou outro e-mail. Marque **P** à mão e, para a próxima vez, **escreva o e-mail dela** na lista.

**Não há mais nada a fazer.** Na próxima aula, repita a Parte 2: a lista já guarda as presenças anteriores. ✅

---

# 🔁 Resumo rápido (para colar na parede)

1. Baixar a planilha de respostas da aula (`.xlsx`) para **Downloads**.
2. **Fechar o Excel.**
3. Dois cliques em **`ABRIR_AQUI.bat`**.
4. Escolher a planilha de **respostas** → digitar o nome da aula (ex.: `Módulo 6 - Aula 2`) → **Enter**.
5. Abrir **`Alunas_Souza.xlsx`**.
6. 🟩 verde = pronto · 🟨 amarelo = decidir **P/F** · 🟧 laranja = conferir e decidir.
7. **Ctrl + S** e fechar.

---

# 🆘 Deu problema?

### ↩️ Errei algo e quero voltar atrás
Abra a pasta **`Backup`**. Cada vez que o programa roda, ele guarda ali a lista **como estava antes**, com a data e a hora no nome. Para recuperar: feche tudo, **renomeie** a lista atual para `Alunas_Souza_COM_ERRO.xlsx`, copie a cópia desejada para a pasta `Presenca` e renomeie-a para **`Alunas_Souza.xlsx`**.

### ❓ "ERRO: feche a planilha no Excel e rode de novo"
Algum arquivo está aberto. Feche o Excel por completo e tente de novo. Nada foi alterado.

### ❓ "Não achei a coluna de nome na sua planilha"
O título da coluna de nomes foi alterado ou apagado, ou saiu da **linha 1**. Escreva **`Nome`** na célula **A1** e salve.

### ❓ A janelinha de escolher arquivo não apareceu
Abriu **atrás** de outras janelas. Procure o ícone piscando na barra de baixo e clique.

### ❓ "Presentes marcadas: 0" e eu sei que teve gente
1. A planilha de respostas é de **outra aula** ou de **outro grupo**.
2. A planilha de respostas não tem a coluna **"Grupos"** com o valor **"Paraíba"**.
3. Os nomes na lista estão muito diferentes do que as alunas escrevem no formulário (preencha os **e-mails**).

### ❓ Uma aluna que veio ficou 🟨 amarela
Ela escreveu o nome de outro jeito ou usou **outro e-mail**. Marque **P** à mão e, para a próxima, preencha o **e-mail dela** na lista.

### ❓ "`py` não é reconhecido..." ou "ModuleNotFoundError..."
Problema na instalação do computador. Avise quem configurou.

### ❓ Apareceu um erro que não está aqui
Tire um **print** da janela preta e envie a quem te passou o programa. As últimas linhas explicam o que aconteceu.

---

# 📝 Perguntas frequentes

**Posso estragar a planilha do wpp (compartilhada)?**
Não. O programa só lê essa planilha.

**E se eu rodar duas vezes a mesma aula?**
Sem problema. Ele **não apaga nem sobrescreve** o que já está escrito (inclusive os **F** e P que você marcou). Só completa o que estiver vazio.

**Por que o programa não coloca "F" sozinho?**
Por segurança: quem não foi encontrada pode ter participado e só ter escrito o nome diferente. Por isso a célula fica **amarela** para **você** decidir.

**Dá para o programa marcar "F" automaticamente ou escrever "Presente" em vez de "P"?**
Dá. Abra `preencher_presenca.py` com o **Bloco de Notas** e mude as linhas do começo:

```python
MARCA_PRESENTE   = "P"     # troque por "Presente" se preferir
MARCA_AUSENTE    = ""      # troque por "F" para marcar falta automaticamente
```

Cuidado para **não apagar as aspas**. Salve depois.

**Funciona em Mac?**
O `ABRIR_AQUI.bat` é só para Windows. No Mac, abra o **Terminal**, entre na pasta e digite `python3 preencher_presenca.py`.

---

*Feito com carinho para facilitar a vida de quem cuida de gente. 💜*
