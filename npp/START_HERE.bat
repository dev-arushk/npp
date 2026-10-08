@echo off
title START HERE - N++ Welcome & Quick Launcher
color 0B
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
echo   [3] System Walkthrough Tour        (Explore architecture, tests & files)
echo   [4] Launch Master Hub (play.bat)   (Access all tools, servers & scripts)
echo   [5] Live Interactive Sandbox       (Type English code live in the REPL)
echo   [6] Exit
echo.
echo ===============================================================================
set /p choice="Type a number (1-6) and press ENTER: "

if "%choice%"=="1" goto TUT_BEGINNER
if "%choice%"=="2" goto TUT_WEB
if "%choice%"=="3" goto TUT_WALKTHROUGH
if "%choice%"=="4" goto MASTER_HUB
if "%choice%"=="5" goto REPL
if "%choice%"=="6" goto END

echo.
echo Invalid choice, please type 1, 2, 3, 4, 5, or 6.
pause
cls
"%~dp0\START_HERE.bat"

:TUT_BEGINNER
cls
call "%~dp0\tutorial_beginner.bat"
goto END

:TUT_WEB
cls
call "%~dp0\tutorial_web.bat"
goto END

:TUT_WALKTHROUGH
cls
call "%~dp0\walkthrough_tour.bat"
goto END

:MASTER_HUB
cls
call "%~dp0\play.bat"
goto END

:REPL
cls
python "%~dp0\main.py" repl
goto END

:END
exit /b
