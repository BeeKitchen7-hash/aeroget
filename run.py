#!/usr/bin/env python3
"""
Aeroget - Nettoyeur de données personnelles avec interface Frutiger Aero
Script de lancement
"""

import sys
import os

# Ajouter le répertoire courant au chemin
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Fonction principale"""
    try:
        from main import main as gui_main
        gui_main()
    except ImportError as e:
        print(f"❌ Erreur: Les dépendances ne sont pas installées!")
        print(f"Installez-les avec: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
