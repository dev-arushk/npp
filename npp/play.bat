@echo off
title N++ Master Control Hub
color 0F
cls

:MENU
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
echo   --- WEB STUDIO & LIVE PREVIEWS ---
echo   [4] Build & View All HTML5 Tags Site   (showcase.html)
echo   [5] Build & View SaaS Landing Page     (saas_landing.html)
echo   [6] Start Embedded Web Server          (Port 8080 with auto-launch)
echo.
echo   --- CODING & EXPERIMENTATION ---
echo   [7] Live Interactive Sandbox (REPL)    (Type and run English code live)
echo   [8] Run Any Custom .npp Script         (Enter a file path to run)
echo   [9] Run Full Automated Test Suite      (All 20 unit tests)
echo   [0] Exit
echo.
echo ===============================================================================
set /p choice="Enter your choice (0-9) and press ENTER: "

if "%choice%"=="1" goto TUT_BEGINNER
if "%choice%"=="2" goto TUT_WEB
if "%choice%"=="3" goto TUT_TOUR
if "%choice%"=="4" goto PREVIEW_SHOWCASE
if "%choice%"=="5" goto PREVIEW_SAAS
if "%choice%"=="6" goto RUN_SERVER
if "%choice%"=="7" goto RUN_REPL
if "%choice%"=="8" goto RUN_CUSTOM
if "%choice%"=="9" goto RUN_TESTS
if "%choice%"=="0" goto END

echo.
echo [!] Invalid choice! Please enter a number between 0 and 9.
echo.
pause
cls
goto MENU

:TUT_BEGINNER
cls
call "%~dp0\tutorial_beginner.bat"
cls
goto MENU

:TUT_WEB
cls
call "%~dp0\tutorial_web.bat"
cls
goto MENU

:TUT_TOUR
cls
call "%~dp0\walkthrough_tour.bat"
cls
goto MENU

:PREVIEW_SHOWCASE
cls
echo Compiling and previewing All HTML5 Tags showcase...
python "%~dp0\main.py" "%~dp0\examples\web_all_html_tags.npp"
start "" "%~dp0\showcase.html"
echo.
echo [OK] Opened showcase.html in your default web browser!
echo.
pause
cls
goto MENU

:PREVIEW_SAAS
cls
echo Compiling and previewing SaaS Landing Page...
python "%~dp0\main.py" "%~dp0\examples\web_saas_landing.npp"
start "" "%~dp0\saas_landing.html"
echo.
echo [OK] Opened saas_landing.html in your default web browser!
echo.
pause
cls
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
python "%~dp0\main.py" serve "%~dp0\examples\web_all_html_tags.npp" 8080
pause
cls
goto MENU

:RUN_REPL
cls
python "%~dp0\main.py" repl
cls
goto MENU

:RUN_CUSTOM
cls
echo.
set /p script_path="Enter path to your .npp file (e.g. examples\fizzbuzz.npp): "
if not exist "%script_path%" (
    if exist "%~dp0\%script_path%" (
        set "script_path=%~dp0\%script_path%"
    )
)
echo.
echo Running: %script_path% ...
echo -------------------------------------------------------------------------------
python "%~dp0\main.py" "%script_path%"
echo -------------------------------------------------------------------------------
echo.
pause
cls
goto MENU

:RUN_TESTS
cls
echo Running automated verification tests ...
echo -------------------------------------------------------------------------------
python "%~dp0\main.py" test
echo -------------------------------------------------------------------------------
echo.
pause
cls
goto MENU

:END
cls
echo.
echo ===============================================================================
echo             Thank you for using N++! Happy coding and web designing!
echo ===============================================================================
echo.
pause
exit /b
