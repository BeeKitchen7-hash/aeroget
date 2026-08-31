@echo off
setlocal enabledelayedexpansion

echo.
echo Aeroget - Generateur d'executable Windows
echo.
echo Verification de Python...

python --version >nul 2>&1
if errorlevel 1 goto PythonNotFound

echo OK - Python detecte
echo.
echo Installation de PyInstaller...

pip install pyinstaller -q
if errorlevel 1 goto PyInstallerError

echo OK - PyInstaller installe
echo.
echo Construction de aeroget.exe...
echo (Cela peut prendre 1-2 minutes)
echo.

pyinstaller aeroget.spec --noconfirm

if errorlevel 1 goto BuildError

echo.
echo OK - aeroget.exe cree avec succes!
echo.
echo Fichier: dist\aeroget.exe
echo.
echo Vous pouvez maintenant:
echo  1. Double-cliquer sur dist\aeroget.exe pour lancer l'app
echo  2. Copier aeroget.exe n'importe ou
echo  3. Le partager a d'autres utilisateurs
echo.
echo L'executable fonctionne sur n'importe quel Windows!
echo.
pause
exit /b 0

:PythonNotFound
echo ERREUR: Python n'est pas installe ou pas dans le PATH
echo.
echo Installez Python depuis: https://www.python.org/downloads/
echo N'oubliez pas de cocher "Add Python to PATH"
echo.
pause
exit /b 1

:PyInstallerError
echo ERREUR: Impossible d'installer PyInstaller
echo.
echo Verifiez votre connexion internet
echo.
pause
exit /b 1

:BuildError
echo ERREUR: Echec de la construction de l'executable
echo.
echo Verifiez que tous les fichiers Python sont presents
echo.
pause
exit /b 1
