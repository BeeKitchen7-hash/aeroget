"""
Module d'analyse des navigateurs
Liste les données trouvées sur chaque navigateur
"""

import os
import sqlite3
import json
from pathlib import Path
from typing import List, Dict, Optional
import shutil

class BrowserAnalyzer:
    """Analyse les données personnelles dans les navigateurs"""
    
    # Chemins des navigateurs
    BROWSER_PATHS = {
        'Chrome': {
            'windows': os.path.expandvars('%APPDATA%\\Google\\Chrome\\User Data'),
            'linux': os.path.expanduser('~/.config/google-chrome'),
            'darwin': os.path.expanduser('~/Library/Application Support/Google/Chrome')
        },
        'Firefox': {
            'windows': os.path.expandvars('%APPDATA%\\Mozilla\\Firefox'),
            'linux': os.path.expanduser('~/.mozilla/firefox'),
            'darwin': os.path.expanduser('~/Library/Application Support/Firefox')
        },
        'Edge': {
            'windows': os.path.expandvars('%APPDATA%\\Microsoft\\Edge\\User Data'),
            'linux': os.path.expanduser('~/.config/microsoft-edge'),
            'darwin': os.path.expanduser('~/Library/Application Support/Microsoft Edge')
        },
        'Safari': {
            'darwin': os.path.expanduser('~/Library/Safari'),
        }
    }
    
    def __init__(self):
        self.results = []
        self.browser_data = {}
    
    def analyze_all_browsers(self, personal_info: Dict) -> Dict:
        """Analyse tous les navigateurs pour trouver les données personnelles"""
        result = {
            'action': 'Analyse des navigateurs',
            'status': 'En cours...',
            'browsers_analyzed': 0,
            'total_matches': 0,
            'details': {}
        }
        
        try:
            import platform
            system = platform.system().lower()
            if system == 'darwin':
                system = 'darwin'
            elif system == 'windows':
                system = 'windows'
            else:
                system = 'linux'
            
            for browser_name, paths in self.BROWSER_PATHS.items():
                browser_path = paths.get(system)
                if browser_path and os.path.exists(browser_path):
                    browser_result = self._analyze_browser(browser_name, browser_path, personal_info)
                    if browser_result:
                        result['details'][browser_name] = browser_result
                        result['browsers_analyzed'] += 1
                        result['total_matches'] += browser_result.get('matches_count', 0)
            
            result['status'] = f'✓ {result["browsers_analyzed"]} navigateur(s) analysé(s), {result["total_matches"]} résultat(s)'
            self.results.append(result)
            return result
        except Exception as e:
            result['status'] = f'✗ Erreur: {str(e)}'
            self.results.append(result)
            return result
    
    def _analyze_browser(self, browser_name: str, browser_path: str, personal_info: Dict) -> Optional[Dict]:
        """Analyse un navigateur spécifique"""
        browser_result = {
            'name': browser_name,
            'path': browser_path,
            'history': [],
            'cookies': [],
            'autofill': [],
            'matches_count': 0
        }
        
        try:
            if browser_name == 'Chrome' or browser_name == 'Edge':
                return self._analyze_chrome_browser(browser_path, personal_info, browser_result)
            elif browser_name == 'Firefox':
                return self._analyze_firefox_browser(browser_path, personal_info, browser_result)
            elif browser_name == 'Safari':
                return self._analyze_safari_browser(browser_path, personal_info, browser_result)
        except Exception as e:
            browser_result['error'] = str(e)
        
        return browser_result if browser_result['matches_count'] > 0 else None
    
    def _analyze_chrome_browser(self, browser_path: str, personal_info: Dict, result: Dict) -> Dict:
        """Analyse Chrome/Edge"""
        try:
            default_profile = os.path.join(browser_path, 'Default')
            
            # Analyse l'historique
            history_db = os.path.join(default_profile, 'History')
            if os.path.exists(history_db):
                temp_db = history_db + '.temp'
                try:
                    shutil.copy(history_db, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cursor = conn.cursor()
                    
                    cursor.execute("SELECT url, title FROM urls LIMIT 100")
                    for url, title in cursor.fetchall():
                        if self._contains_personal_info(url + ' ' + (title or ''), personal_info):
                            result['history'].append({'url': url, 'title': title})
                            result['matches_count'] += 1
                    
                    conn.close()
                    os.remove(temp_db)
                except:
                    pass
            
            # Analyse les cookies
            cookies_db = os.path.join(default_profile, 'Cookies')
            if os.path.exists(cookies_db):
                temp_db = cookies_db + '.temp'
                try:
                    shutil.copy(cookies_db, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cursor = conn.cursor()
                    
                    cursor.execute("SELECT host_key, name FROM cookies LIMIT 50")
                    for host, name in cursor.fetchall():
                        result['cookies'].append({'domain': host, 'name': name})
                    
                    conn.close()
                    os.remove(temp_db)
                except:
                    pass
        except:
            pass
        
        return result
    
    def _analyze_firefox_browser(self, browser_path: str, personal_info: Dict, result: Dict) -> Dict:
        """Analyse Firefox"""
        try:
            profiles_dir = browser_path
            
            # Trouver le profile par défaut
            for profile_dir in os.listdir(profiles_dir):
                profile_path = os.path.join(profiles_dir, profile_dir)
                if os.path.isdir(profile_path):
                    # Analyse l'historique
                    places_db = os.path.join(profile_path, 'places.sqlite')
                    if os.path.exists(places_db):
                        temp_db = places_db + '.temp'
                        try:
                            shutil.copy(places_db, temp_db)
                            conn = sqlite3.connect(temp_db)
                            cursor = conn.cursor()
                            
                            cursor.execute("SELECT url, title FROM moz_places LIMIT 100")
                            for url, title in cursor.fetchall():
                                if self._contains_personal_info(url + ' ' + (title or ''), personal_info):
                                    result['history'].append({'url': url, 'title': title})
                                    result['matches_count'] += 1
                            
                            conn.close()
                            os.remove(temp_db)
                        except:
                            pass
        except:
            pass
        
        return result
    
    def _analyze_safari_browser(self, browser_path: str, personal_info: Dict, result: Dict) -> Dict:
        """Analyse Safari"""
        try:
            history_db = os.path.join(browser_path, 'History.db')
            if os.path.exists(history_db):
                temp_db = history_db + '.temp'
                try:
                    shutil.copy(history_db, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cursor = conn.cursor()
                    
                    cursor.execute("SELECT url, title FROM history_items LIMIT 100")
                    for url, title in cursor.fetchall():
                        if self._contains_personal_info(url + ' ' + (title or ''), personal_info):
                            result['history'].append({'url': url, 'title': title})
                            result['matches_count'] += 1
                    
                    conn.close()
                    os.remove(temp_db)
                except:
                    pass
        except:
            pass
        
        return result
    
    def _contains_personal_info(self, text: str, personal_info: Dict) -> bool:
        """Vérifie si le texte contient des infos personnelles"""
        text_lower = text.lower()
        
        checks = [
            personal_info.get('nom', '').lower(),
            personal_info.get('prenom', '').lower(),
            personal_info.get('email', '').lower(),
            personal_info.get('telephone', '').lower(),
            personal_info.get('adresse', '').lower(),
            personal_info.get('ville', '').lower(),
            personal_info.get('code_postal', '').lower(),
        ]
        
        for check in checks:
            if check and len(check) > 2 and check in text_lower:
                return True
        
        return False
    
    def get_results(self) -> List[Dict]:
        """Retourne les résultats"""
        return self.results
    
    def export_to_json(self, filepath: str) -> bool:
        """Exporte les résultats en JSON"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            return True
        except:
            return False
