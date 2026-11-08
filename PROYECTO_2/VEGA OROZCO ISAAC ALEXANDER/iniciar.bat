@echo off
title Simulador Proyecto 10 - Isaac Vega
cd /d "%~dp0"
echo ======================================================================
echo   PROYECTO 10: RUIDO DE EMBARCACIONES Y BALLENAS EN GOLFO DULCE
echo   Estudiante: Isaac Alexander Vega Orozco (C-08)
echo ======================================================================
echo.
echo Iniciando el simulador y abriendo el navegador en http://localhost:8501...
echo (Para cerrar el simulador cuando termines, solo cierra esta ventana)
echo.
python -m streamlit run "%~dp0app.py"
pause

