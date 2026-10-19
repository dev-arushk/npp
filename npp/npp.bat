@echo off
setlocal EnableDelayedExpansion
title N++ Interactive Code Tester
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

:: If arguments were passed from command line, run directly
if not "%~1"=="" (
    "%PY_CMD%" "%~dp0main.py" %*
    if !errorlevel! neq 0 (
        echo.
        echo [N++] Script finished with exit code !errorlevel!.
        pause
    )
    exit /b
)

:: No arguments passed (e.g. double-clicked from Explorer): Launch Interactive Code Tester
:MENU
cls
echo ===============================================================================
echo                      N++ INTERACTIVE CODE TESTER
echo          The Plain English Language That Compiles Faster Than HTML
echo ===============================================================================
echo.
echo   Welcome! Use this testing hub to experiment with N++ English code live:
echo.
echo   [1] Start Live Interactive REPL (type English commands line-by-line)
echo   [2] Test Run: Beginner Basics    (examples\intro_basics.npp)
echo   [3] Test Run: Step-by-Step Tour  (examples\guided_tour.npp)
echo   [4] Test Run: All 20 Unit Tests  (verify full engine health)
echo   [5] Test Run: HTML5 Web Showcase (examples\web_all_html_tags.npp)
echo   [6] Test Run: SaaS Landing Page  (examples\web_saas_landing.npp)
echo   [7] Quick Test: Run Custom Code Line
echo   [8] Run Any Custom .npp File
echo   [0] Exit
echo.
echo ===============================================================================
set "choice="
set /p "choice=Type your choice [1-8, 0] (Default is 1): "
if defined choice set "choice=!choice: =!"
if "!choice!"=="" set "choice=1"

if "!choice!"=="1" goto RUN_REPL
if "!choice!"=="2" goto RUN_INTRO
if "!choice!"=="3" goto RUN_TOUR
if "!choice!"=="4" goto RUN_TESTS
if "!choice!"=="5" goto RUN_SHOWCASE
if "!choice!"=="6" goto RUN_SAAS
if "!choice!"=="7" goto RUN_ONELINE
if "!choice!"=="8" goto RUN_CUSTOM_FILE
if "!choice!"=="0" goto EXIT_HUB

echo.
echo [!] Invalid selection "!choice!". Please type a number from 0 to 8.
ping 127.0.0.1 -n 2 >nul
goto MENU

:RUN_REPL
cls
echo Starting Live N++ Interactive REPL...
echo (Type 'exit' or 'quit' when you want to return to this menu)
echo.
"%PY_CMD%" "%~dp0main.py" repl
echo.
echo [REPL session ended]
pause
goto MENU

:RUN_INTRO
cls
echo ===============================================================================
echo   TESTING: examples\intro_basics.npp
echo ===============================================================================
echo.
"%PY_CMD%" "%~dp0main.py" "%~dp0examples\intro_basics.npp"
echo.
echo ===============================================================================
echo [Done] Execution finished!
echo ===============================================================================
pause
goto MENU

:RUN_TOUR
cls
echo ===============================================================================
echo   TESTING: examples\guided_tour.npp (Interactive)
echo ===============================================================================
echo.
"%PY_CMD%" "%~dp0main.py" "%~dp0examples\guided_tour.npp"
echo.
echo ===============================================================================
echo [Done] Guided tour finished!
echo ===============================================================================
pause
goto MENU

:RUN_TESTS
cls
echo ===============================================================================
echo   RUNNING ALL 20 AUTOMATED UNIT TESTS
echo ===============================================================================
echo.
"%PY_CMD%" "%~dp0main.py" test
echo.
echo ===============================================================================
echo [Done] Test run complete!
echo ===============================================================================
pause
goto MENU

:RUN_SHOWCASE
cls
echo ===============================================================================
echo   TESTING: examples\web_all_html_tags.npp
echo ===============================================================================
echo.
"%PY_CMD%" "%~dp0main.py" "%~dp0examples\web_all_html_tags.npp"
if exist "%~dp0showcase.html" (
    echo.
    echo [OK] showcase.html compiled successfully!
    set /p "open_showcase=Would you like to open showcase.html in your browser? (Y/n): "
    if not "!open_showcase!"=="n" if not "!open_showcase!"=="N" (
        start "" "%~dp0showcase.html"
    )
)
echo.
pause
goto MENU

:RUN_SAAS
cls
echo ===============================================================================
echo   TESTING: examples\web_saas_landing.npp
echo ===============================================================================
echo.
"%PY_CMD%" "%~dp0main.py" "%~dp0examples\web_saas_landing.npp"
if exist "%~dp0saas_landing.html" (
    echo.
    echo [OK] saas_landing.html compiled successfully!
    set /p "open_saas=Would you like to open saas_landing.html in your browser? (Y/n): "
    if not "!open_saas!"=="n" if not "!open_saas!"=="N" (
        start "" "%~dp0saas_landing.html"
    )
)
echo.
pause
goto MENU

:RUN_ONELINE
cls
echo ===============================================================================
echo   QUICK ONE-LINE N++ CODE TESTER
echo ===============================================================================
echo Examples:
echo   say "Hello from N++!"
echo   say 100 * 25
echo   repeat 3 times say "Testing!" end
echo.
set "user_code="
set /p "user_code=Enter N++ code: "
if not "!user_code!"=="" (
    echo.
    echo Output:
    echo -------------------------------------------------------------------------------
    "%PY_CMD%" -c "from npp import run_code; run_code('''!user_code!''')"
    echo -------------------------------------------------------------------------------
)
echo.
pause
goto MENU

:RUN_CUSTOM_FILE
cls
echo.
set "custom_file="
set /p "custom_file=Enter path to your .npp file: "
if not "!custom_file!"=="" (
    if not exist "!custom_file!" (
        if exist "%~dp0!custom_file!" (
            set "custom_file=%~dp0!custom_file!"
        )
    )
    echo.
    echo Running: !custom_file! ...
    echo -------------------------------------------------------------------------------
    "%PY_CMD%" "%~dp0main.py" "!custom_file!"
    echo -------------------------------------------------------------------------------
)
echo.
pause
goto MENU

:EXIT_HUB
cls
echo.
echo Thank you for testing N++! Have a great day.
echo.
ping 127.0.0.1 -n 2 >nul
exit /b
