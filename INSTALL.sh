#!/bin/bash

# ============================================================
# Aeroget Installation & Launch Script for Linux/Mac
# Double-click to install dependencies and run the app!
# ============================================================

echo ""
echo "============================================================"
echo "  ✨ Aeroget - Installation et Lancement ✨"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERREUR: Python 3 n'est pas installé"
    echo ""
    echo "Installation sur macOS:"
    echo "  brew install python3"
    echo ""
    echo "Installation sur Ubuntu/Debian:"
    echo "  sudo apt-get install python3 python3-pip python3-venv"
    echo ""
    echo "Installation sur Fedora/RHEL:"
    echo "  sudo dnf install python3 python3-pip"
    echo ""
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

echo "✓ Python détecté: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ ERREUR: pip3 n'est pas installé"
    echo ""
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

echo "✓ pip détecté"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
    echo "✓ Environnement virtuel créé"
    echo ""
fi

# Activate virtual environment
echo "🔄 Activation de l'environnement virtuel..."
source venv/bin/activate
echo "✓ Environnement virtuel activé"
echo ""

# Upgrade pip
echo "📥 Mise à jour de pip..."
python -m pip install --upgrade pip > /dev/null 2>&1

# Install requirements
echo "📥 Installation des dépendances (cela peut prendre 1-2 minutes)..."
echo ""
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ ERREUR lors de l'installation des dépendances"
    echo ""
    read -p "Appuyez sur Entrée pour continuer..."
    exit 1
fi

echo ""
echo "✓ Dépendances installées avec succès"
echo ""

# Launch the application
echo "🚀 Lancement de Aeroget..."
echo ""
python run.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Une erreur s'est produite lors du lancement"
    echo ""
    read -p "Appuyez sur Entrée pour continuer..."
fi

exit 0
