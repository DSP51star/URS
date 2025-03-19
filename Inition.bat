@echo off
title Cargando...
mode con: cols=50 lines=10
color 4F
cls
setlocal enabledelayedexpansion

:: Dibujo del marco del HUD
echo ==================================
echo =            CARGANDO...          =
echo ==================================
echo.

for /L %%i in (0,5,100) do (
    cls
    echo ==================================
    echo =            CARGANDO...          =
    echo ==================================
    echo.
    echo            [%%i%%]
    timeout /nobreak /t 1 >nul
)

cls
echo ==================================
echo =          ACCESO CONCEDIDO       =
echo ==================================
echo.
echo Password: KKJS
echo Usuario: Adolfo
echo.
echo ==================================
pause
