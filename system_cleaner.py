"""
Module de nettoyage du système local
- Vider la corbeille
- Supprimer les fichiers temporaires
"""

import os
import shutil
import tempfile
import subprocess
from pathlib import Path
from typing import List, Dict

class SystemCleaner:
    """Nettoie le système local"""
    
    def __init__(self):
        self.results = []
        self.total_freed = 0
    
    def clean_recycle_bin(self) -> Dict:
        """Vide la corbeille"""
        result = {
            'action': 'Vider la corbeille',
            'status': 'En cours...',
            'items_deleted': 0,
            'space_freed': 0
        }
        
        try:
            if os.name == 'nt':  # Windows
                os.system('rd /s /q %systemdrive%\\$Recycle.bin')
                result['status'] = '✓ Succès'
            else:  # Linux/Mac
                trash_path = os.path.expanduser('~/.local/share/Trash')
                if os.path.exists(trash_path):
                    shutil.rmtree(trash_path)
                    os.makedirs(trash_path, exist_ok=True)
                result['status'] = '✓ Succès'
            
            self.results.append(result)
            return result
        except Exception as e:
            result['status'] = f'✗ Erreur: {str(e)}'
            self.results.append(result)
            return result
    
    def clean_temp_files(self) -> Dict:
        """Supprime les fichiers temporaires"""
        result = {
            'action': 'Supprimer fichiers temporaires',
            'status': 'En cours...',
            'items_deleted': 0,
            'space_freed': 0
        }
        
        try:
            temp_dirs = [
                tempfile.gettempdir(),
                os.path.expanduser('~/.cache'),
            ]
            
            if os.name == 'nt':  # Windows
                temp_dirs.extend([
                    os.path.expandvars('%TEMP%'),
                    os.path.expandvars('%APPDATA%\\Local\\Temp'),
                ])
            
            deleted_count = 0
            for temp_dir in temp_dirs:
                if os.path.exists(temp_dir):
                    for item in os.listdir(temp_dir):
                        try:
                            path = os.path.join(temp_dir, item)
                            if os.path.isfile(path):
                                os.remove(path)
                                deleted_count += 1
                            elif os.path.isdir(path):
                                shutil.rmtree(path, ignore_errors=True)
                                deleted_count += 1
                        except:
                            pass
            
            result['items_deleted'] = deleted_count
            result['status'] = f'✓ {deleted_count} fichier(s) supprimé(s)'
            self.results.append(result)
            return result
        except Exception as e:
            result['status'] = f'✗ Erreur: {str(e)}'
            self.results.append(result)
            return result
    
    def clean_browser_cache(self) -> Dict:
        """Nettoie le cache des navigateurs"""
        result = {
            'action': 'Cache navigateurs',
            'status': 'En cours...',
            'browsers_cleaned': 0
        }
        
        try:
            cleaned_count = 0
            
            # Chrome/Chromium
            chrome_paths = [
                os.path.expanduser('~/.config/google-chrome'),
                os.path.expanduser('~/.config/chromium'),
                os.path.expandvars('%APPDATA%\\Google\\Chrome'),
            ]
            
            # Firefox
            firefox_paths = [
                os.path.expanduser('~/.mozilla/firefox'),
                os.path.expandvars('%APPDATA%\\Mozilla\\Firefox'),
            ]
            
            all_paths = chrome_paths + firefox_paths
            
            for path in all_paths:
                if os.path.exists(path):
                    cache_dir = os.path.join(path, 'Cache')
                    if os.path.exists(cache_dir):
                        shutil.rmtree(cache_dir, ignore_errors=True)
                        cleaned_count += 1
            
            result['browsers_cleaned'] = cleaned_count
            result['status'] = f'✓ {cleaned_count} navigateur(s) nettoyé(s)'
            self.results.append(result)
            return result
        except Exception as e:
            result['status'] = f'✗ Erreur: {str(e)}'
            self.results.append(result)
            return result
    
    def get_results(self) -> List[Dict]:
        """Retourne les résultats du nettoyage"""
        return self.results
