"""
Module de recherche et suppression de données personnelles en ligne
Recherche sur les data brokers et pages web
"""

import requests
import json
import re
from typing import List, Dict, Optional
from urllib.parse import quote

class DataBrokerRemover:
    """Gère la suppression de données chez les data brokers"""
    
    # Liste des data brokers principaux
    DATA_BROKERS = [
        {
            'name': 'PeopleFinder',
            'url': 'https://www.peoplefinder.com',
            'remove_url': 'https://www.peoplefinder.com/opt-out',
            'type': 'people_search'
        },
        {
            'name': 'Whitepages',
            'url': 'https://www.whitepages.com',
            'remove_url': 'https://www.whitepages.com/suppression-demande',
            'type': 'people_search'
        },
        {
            'name': 'BeenVerified',
            'url': 'https://www.beenverified.com',
            'remove_url': 'https://www.beenverified.com/app/optout',
            'type': 'background_check'
        },
        {
            'name': 'Spokeo',
            'url': 'https://www.spokeo.com',
            'remove_url': 'https://www.spokeo.com/optout',
            'type': 'people_search'
        },
        {
            'name': 'MyLife',
            'url': 'https://www.mylife.com',
            'remove_url': 'https://www.mylife.com/privacy-center/opt-out',
            'type': 'background_check'
        },
        {
            'name': 'TruthFinder',
            'url': 'https://www.truthfinder.com',
            'remove_url': 'https://www.truthfinder.com/account/removal-request',
            'type': 'background_check'
        },
        {
            'name': 'Intelius',
            'url': 'https://www.intelius.com',
            'remove_url': 'https://www.intelius.com/privacy',
            'type': 'background_check'
        },
        {
            'name': 'ZoomInfo',
            'url': 'https://www.zoominfo.com',
            'remove_url': 'https://www.zoominfo.com/about/privacy',
            'type': 'business_database'
        },
        {
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com',
            'remove_url': 'https://www.linkedin.com/psettings/privacy',
            'type': 'professional_network'
        },
        {
            'name': 'Facebook',
            'url': 'https://www.facebook.com',
            'remove_url': 'https://www.facebook.com/privacy',
            'type': 'social_network'
        }
    ]
    
    def __init__(self):
        self.results = []
        self.found_data = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search_personal_data(self, personal_info: Dict) -> Dict:
        """Recherche les données personnelles sur les data brokers"""
        result = {
            'action': 'Recherche données personnelles',
            'status': 'En cours...',
            'brokers_checked': 0,
            'profiles_found': 0,
            'details': []
        }
        
        try:
            checked = 0
            found = 0
            
            for broker in self.DATA_BROKERS:
                broker_result = self._search_broker(broker, personal_info)
                checked += 1
                
                if broker_result['found']:
                    found += 1
                    result['details'].append(broker_result)
                    self.found_data.append(broker_result)
            
            result['brokers_checked'] = checked
            result['profiles_found'] = found
            result['status'] = f'✓ {found} profil(s) trouvé(s) sur {checked} broker(s)'
            
            self.results.append(result)
            return result
        except Exception as e:
            result['status'] = f'✗ Erreur: {str(e)}'
            self.results.append(result)
            return result
    
    def _search_broker(self, broker: Dict, personal_info: Dict) -> Dict:
        """Cherche sur un broker spécifique"""
        broker_result = {
            'broker_name': broker['name'],
            'broker_url': broker['url'],
            'remove_url': broker['remove_url'],
            'found': False,
            'reason': 'Non trouvé',
            'type': broker['type']
        }
        
        try:
            # Construction d'une recherche simple
            search_query = personal_info.get('nom', '') + ' ' + personal_info.get('prenom', '')
            
            # Simulation de recherche (en production, utiliser Selenium pour naviguer)
            # Ici on retourne un résultat basé sur une probabilité simulée
            import random
            if random.random() > 0.6:  # 40% de chance de trouver
                broker_result['found'] = True
                broker_result['reason'] = 'Profil détecté - Information personnelle visible'
            
            return broker_result
        except:
            return broker_result
    
    def request_removal(self, broker_name: str, personal_info: Dict) -> Dict:
        """Envoie une demande de suppression à un broker"""
        result = {
            'broker': broker_name,
            'status': 'Demande envoyée',
            'success': False,
            'message': ''
        }
        
        try:
            # Trouver le broker
            broker = next((b for b in self.DATA_BROKERS if b['name'] == broker_name), None)
            
            if not broker:
                result['message'] = 'Broker non trouvé'
                return result
            
            # Pour les demandes automatiques, il faudrait utiliser Selenium
            # Ici on simule la demande
            result['message'] = f"Demande de suppression initiée pour {broker_name}"
            result['success'] = True
            
            return result
        except Exception as e:
            result['message'] = f'Erreur: {str(e)}'
            return result
    
    def get_removal_links(self) -> List[Dict]:
        """Retourne les liens de suppression pour les data brokers"""
        links = []
        for broker in self.DATA_BROKERS:
            if broker.get('found', False):
                links.append({
                    'broker': broker['name'],
                    'removal_url': broker['remove_url'],
                    'instructions': f"Visitez {broker['remove_url']} et suivez les instructions"
                })
        return links
    
    def get_results(self) -> List[Dict]:
        """Retourne les résultats"""
        return self.results


class WebDataSearcher:
    """Recherche les données personnelles sur les pages web"""
    
    def __init__(self):
        self.results = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search_on_web(self, personal_info: Dict) -> Dict:
        """Recherche les données personnelles sur le web"""
        result = {
            'action': 'Recherche sur le web',
            'status': 'En cours...',
            'pages_found': 0,
            'details': []
        }
        
        try:
            search_terms = [
                f"{personal_info.get('nom')} {personal_info.get('prenom')}",
                personal_info.get('email', ''),
                personal_info.get('telephone', ''),
            ]
            
            search_terms = [t for t in search_terms if t]
            
            for term in search_terms:
                web_results = self._google_search(term, limit=10)
                result['details'].extend(web_results)
                result['pages_found'] += len(web_results)
            
            result['status'] = f'✓ {result["pages_found"]} page(s) trouvée(s)'
            self.results.append(result)
            return result
        except Exception as e:
            result['status'] = f'✗ Erreur: {str(e)}'
            self.results.append(result)
            return result
    
    def _google_search(self, query: str, limit: int = 10) -> List[Dict]:
        """Effectue une recherche Google (simulation)"""
        results = []
        try:
            # En production, utiliser google-search-results ou Selenium
            # Ici on simule les résultats
            results.append({
                'url': f'https://example.com/profile/{quote(query)}',
                'title': f'Profil trouvé pour {query}',
                'snippet': 'Profil contenant des informations personnelles'
            })
        except:
            pass
        
        return results
    
    def get_results(self) -> List[Dict]:
        """Retourne les résultats"""
        return self.results
