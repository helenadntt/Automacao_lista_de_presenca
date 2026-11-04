@echo off
chcp 65001 >nul
cd /d "%~dp0"
py preencher_presenca.py
echo.
echo ===== Terminou. Pode fechar esta janela. =====
pause
