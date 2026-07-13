@echo off
rem Vasundhara Palace - Double-Click Compiler for Windows
cd /d "%~dp0"
echo ----------------------------------------
echo   Vasundhara Palace Menu Compiler       
echo ----------------------------------------
echo.
python update_menu.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error: Python compilation failed. Make sure Python is installed and on your PATH.
)
echo.
echo Compilation complete. Press any key to exit...
pause > nul
