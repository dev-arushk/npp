@echo off
setlocal EnableDelayedExpansion
title START HERE - N++ Welcome and Quick Launcher
color 0B

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

:MENU
cls
echo ===============================================================================
echo                                WELCOME TO N++!
echo           The Programming Language That Reads Like Plain English
echo                     And Builds Webpages Better Than HTML
echo ===============================================================================
echo.
echo   If this is your first time here, YOU ARE IN THE RIGHT PLACE!
echo   Choose an option below to start your interactive journey:
echo.
echo   [1] Beginner Interactive Tutorial  (Learn N++ from scratch step-by-step)
echo   [2] Web Engine Interactive Tutorial (Learn to build websites 1000x faster)
echo   [3] System Walkthrough Tour        (Explore architecture, tests and files)
echo   [4] Code Tester / REPL Sandbox     (Type English code live and test scripts)
echo   [5] Launch Master Hub (play.bat)   (Access all tools, servers and scripts)
echo   [6] Exit
echo.
echo ===============================================================================
set "choice="
set /p "choice=Type a number (1-6) and press ENTER (Default is 1): "
if defined choice set "choice=!choice: =!"
if "!choice!"=="" set "choice=1"

if "!choice!"=="1" goto TUT_BEGINNER
if "!choice!"=="2" goto TUT_WEB
if "!choice!"=="3" goto TUT_WALKTHROUGH
if "!choice!"=="4" goto CODE_TESTER
if "!choice!"=="5" goto MASTER_HUB
if "!choice!"=="6" goto END

echo.
echo [!] Invalid choice "!choice!", please type 1, 2, 3, 4, 5, or 6.
ping 127.0.0.1 -n 2 >nul
goto MENU

:TUT_BEGINNER
cls
call "%~dp0tutorial_beginner.bat"
goto MENU

:TUT_WEB
cls
call "%~dp0tutorial_web.bat"
goto MENU

:TUT_WALKTHROUGH
cls
call "%~dp0walkthrough_tour.bat"
goto MENU

:CODE_TESTER
cls
call "%~dp0npp.bat"
goto MENU

:MASTER_HUB
cls
call "%~dp0play.bat"
goto MENU

:END
cls
echo.
echo Thank you for using N++! Happy coding!
echo.
ping 127.0.0.1 -n 2 >nul
exit /b
