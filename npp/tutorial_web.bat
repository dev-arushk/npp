@echo off
setlocal EnableDelayedExpansion
title N++ Web Engine Interactive Tutorial
color 03
cls

cd /d "%~dp0"
chcp 65001 >nul
set "PYTHONIOENCODING=utf-8"
set "PYTHONUTF8=1"

set "PY_CMD="
where python >nul 2>nul
if !errorlevel! equ 0 (
    set "PY_CMD=python"
) else (
    where py >nul 2>nul
    if !errorlevel! equ 0 (
        set "PY_CMD=py"
    )
)

if "%PY_CMD%"=="" (
    echo ===============================================================================
    echo [ERROR] Python is not installed or not found in your system PATH!
    echo.
    echo Please install Python 3.9+ from https://python.org
    echo IMPORTANT: Make sure to check the box "Add Python to PATH" during installation.
    echo ===============================================================================
    echo.
    pause
    exit /b 1
)

"%PY_CMD%" "%~dp0tutorials\interactive_web.py"
if %errorlevel% neq 0 (
    echo.
    echo [Notice] The tutorial ended with code %errorlevel%.
)
echo.
pause
