@echo off
setlocal enabledelayedexpansion

echo.
echo ============================================================
echo Aeroget - Installation et Lancement
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 goto PythonNotFound

echo OK - Python detecte

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creation de l'environnement virtuel...
    python -m venv venv
    if errorlevel 1 goto VenvError
    echo OK - Environnement virtuel cree
    echo.
)

REM Activate virtual environment
echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat
echo OK - Environnement virtuel active
echo.

REM Upgrade pip
echo Mise a jour de pip...
python -m pip install --upgrade pip >nul 2>&1

REM Install requirements
echo Installation des dependances (cela peut prendre 1-2 minutes)...
echo.
pip install -r requirements.txt
if errorlevel 1 goto InstallError

echo.
echo OK - Dependances installees avec succes
echo.

REM Launch the application
echo Lancement de Aeroget...
echo.
python run.py
goto End

:PythonNotFound
echo.
echo ERREUR: Python n'est pas installe ou pas dans le PATH
echo.
echo Veuillez telecharger Python depuis: https://www.python.org/downloads/
echo IMPORTANT: Cochez "Add Python to PATH" lors de l'installation
echo.
pause
exit /b 1

:VenvError
echo.
echo ERREUR: Impossible de creer l'environnement virtuel
echo.
pause
exit /b 1

:InstallError
echo.
echo ERREUR lors de l'installation des dependances
echo.
pause
exit /b 1

:End
endlocal
exit /b 0
