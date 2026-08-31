@echo off
REM ============================================================
REM Aeroget Installation & Launch Script for Windows
REM Double-click to install dependencies and run the app!
REM ============================================================

echo.
echo ============================================================
echo  ✨ Aeroget - Installation et Lancement ✨
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERREUR: Python n'est pas installé ou pas dans le PATH
    echo.
    echo Veuillez télécharger Python depuis: https://www.python.org/downloads/
    echo Assurez-vous de cocher "Add Python to PATH" lors de l'installation
    echo.
    pause
    exit /b 1
)

echo ✓ Python détecté

REM Check if pip is installed
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERREUR: pip n'est pas installé
    echo.
    pause
    exit /b 1
)

echo ✓ pip détecté
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Création de l'environnement virtuel...
    python -m venv venv
    echo ✓ Environnement virtuel créé
    echo.
)

REM Activate virtual environment
echo 🔄 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat
echo ✓ Environnement virtuel activé
echo.

REM Install requirements
echo 📥 Installation des dépendances (cela peut prendre 1-2 minutes)...
echo.
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ❌ ERREUR lors de l'installation des dépendances
    echo.
    pause
    exit /b 1
)

echo.
echo ✓ Dépendances installées avec succès
echo.

REM Launch the application
echo 🚀 Lancement de Aeroget...
echo.
python run.py

REM If the app closes, show the window for a moment
if errorlevel 1 (
    echo.
    echo ❌ Une erreur s'est produite lors du lancement
    echo.
    pause
)

exit /b 0
