@echo off
setlocal EnableDelayedExpansion
title N++ Master Control Hub
color 0F

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
echo        _   _       _         _             
echo       ^| \ ^| ^|  _ _^| ^|_ _   _^| ^|_ _   _ _   
echo       ^|  \^| ^|_^| ^|_   _^| ^|_^| ^|_   _^| ^| ^| ^|  
echo       ^|_^| \_^|___^| ^|_^| ^|___^|_^| ^|_^|   ^|_^| ^|  
echo                                       ^|___/ 
echo                      N++ MASTER CONTROL HUB v1.0.0
echo       The Plain English Language That Builds Websites Better Than HTML
echo ===============================================================================
echo.
echo   --- TUTORIALS (HIGHLY RECOMMENDED FIRST STEP) ---
echo   [1] Beginner Interactive Tutorial      (Learn N++ from scratch)
echo   [2] Web Engine Interactive Tutorial    (Build modern sites 1000x faster)
echo   [3] System Walkthrough Tour            (Architecture, tests, and showcase tour)
echo.
echo   --- WEB STUDIO and LIVE PREVIEWS ---
echo   [4] Build and View All HTML5 Tags Site (showcase.html)
echo   [5] Build and View SaaS Landing Page   (saas_landing.html)
echo   [6] Build and View Analytics Dashboard (dashboard.html)
echo   [7] Start Embedded Web Server          (Port 8080 with auto-launch)
echo.
echo   --- CODING and EXPERIMENTATION ---
echo   [8] Live Interactive Code Tester (npp) (Type and run English code live)
echo   [9] Run Full Automated Test Suite      (All 21 unit tests)
echo   [0] Exit
echo.
echo ===============================================================================
set "choice="
set /p "choice=Enter your choice (0-9) and press ENTER (Default is 1): "
if defined choice set "choice=!choice: =!"
if "!choice!"=="" set "choice=1"

if "!choice!"=="1" goto TUT_BEGINNER
if "!choice!"=="2" goto TUT_WEB
if "!choice!"=="3" goto TUT_TOUR
if "!choice!"=="4" goto PREVIEW_SHOWCASE
if "!choice!"=="5" goto PREVIEW_SAAS
if "!choice!"=="6" goto PREVIEW_DASHBOARD
if "!choice!"=="7" goto RUN_SERVER
if "!choice!"=="8" goto RUN_REPL
if "!choice!"=="9" goto RUN_TESTS
if "!choice!"=="0" goto END

echo.
echo [!] Invalid choice "!choice!"! Please enter a number between 0 and 9.
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

:TUT_TOUR
cls
call "%~dp0walkthrough_tour.bat"
goto MENU

:PREVIEW_SHOWCASE
cls
echo Compiling and previewing All HTML5 Tags showcase...
"%PY_CMD%" "%~dp0main.py" "%~dp0examples\web_all_html_tags.npp"
if exist "%~dp0showcase.html" (
    start "" "%~dp0showcase.html"
    echo.
    echo [OK] Opened showcase.html in your default web browser!
) else (
    echo [!] Could not locate showcase.html
)
echo.
pause
goto MENU

:PREVIEW_SAAS
cls
echo Compiling and previewing SaaS Landing Page...
"%PY_CMD%" "%~dp0main.py" "%~dp0examples\web_saas_landing.npp"
if exist "%~dp0saas_landing.html" (
    start "" "%~dp0saas_landing.html"
    echo.
    echo [OK] Opened saas_landing.html in your default web browser!
) else (
    echo [!] Could not locate saas_landing.html
)
echo.
pause
goto MENU

:PREVIEW_DASHBOARD
cls
echo Compiling and previewing Analytics Dashboard...
"%PY_CMD%" "%~dp0main.py" "%~dp0examples\interactive_dashboard.npp"
if exist "%~dp0dashboard.html" (
    start "" "%~dp0dashboard.html"
    echo.
    echo [OK] Opened dashboard.html in your default web browser!
) else (
    echo [!] Could not locate dashboard.html
)
echo.
pause
goto MENU

:RUN_SERVER
cls
echo ===============================================================================
echo                STARTING N++ EMBEDDED DEVELOPMENT WEB SERVER
echo ===============================================================================
echo   Local Directory: %~dp0
echo   Default Port:    8080
echo   Press Ctrl+C in the window to stop the server when done.
echo ===============================================================================
echo.
"%PY_CMD%" "%~dp0main.py" serve "%~dp0examples\web_all_html_tags.npp" 8080
pause
goto MENU

:RUN_REPL
cls
call "%~dp0npp.bat"
goto MENU

:RUN_CUSTOM
cls
echo.
set "script_path="
set /p "script_path=Enter path to your .npp file (e.g. examples\fizzbuzz.npp): "
if not "!script_path!"=="" (
    if not exist "!script_path!" (
        if exist "%~dp0!script_path!" (
            set "script_path=%~dp0!script_path!"
        )
    )
    echo.
    echo Running: !script_path! ...
    echo -------------------------------------------------------------------------------
    "%PY_CMD%" "%~dp0main.py" "!script_path!"
    echo -------------------------------------------------------------------------------
)
echo.
pause
goto MENU

:RUN_TESTS
cls
echo Running automated verification tests ...
echo -------------------------------------------------------------------------------
"%PY_CMD%" "%~dp0main.py" test
echo -------------------------------------------------------------------------------
echo.
pause
goto MENU

:END
cls
echo.
echo ===============================================================================
echo             Thank you for using N++! Happy coding and web designing!
echo ===============================================================================
echo.
ping 127.0.0.1 -n 2 >nul
exit /b
