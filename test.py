#!/usr/bin/env python3
"""
Tests simples pour Aeroget
"""

import unittest
import sys
import os

# Ajouter le répertoire courant au chemin
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from system_cleaner import SystemCleaner
from data_broker_remover import DataBrokerRemover, WebDataSearcher
from browser_analyzer import BrowserAnalyzer

class TestSystemCleaner(unittest.TestCase):
    """Tests pour SystemCleaner"""
    
    def setUp(self):
        self.cleaner = SystemCleaner()
    
    def test_cleaner_initialization(self):
        """Teste l'initialisation"""
        self.assertEqual(len(self.cleaner.results), 0)
        self.assertEqual(self.cleaner.total_freed, 0)
    
    def test_get_results_empty(self):
        """Teste la récupération de résultats vides"""
        self.assertEqual(self.cleaner.get_results(), [])

class TestDataBrokerRemover(unittest.TestCase):
    """Tests pour DataBrokerRemover"""
    
    def setUp(self):
        self.remover = DataBrokerRemover()
    
    def test_brokers_list(self):
        """Teste que la liste des brokers existe"""
        self.assertTrue(len(self.remover.DATA_BROKERS) > 0)
    
    def test_broker_structure(self):
        """Teste la structure d'un broker"""
        broker = self.remover.DATA_BROKERS[0]
        self.assertIn('name', broker)
        self.assertIn('url', broker)
        self.assertIn('remove_url', broker)
        self.assertIn('type', broker)
    
    def test_personal_data_search(self):
        """Teste la recherche de données personnelles"""
        personal_info = {
            'nom': 'Dupont',
            'prenom': 'Jean',
            'email': 'jean@example.com'
        }
        result = self.remover.search_personal_data(personal_info)
        
        self.assertIn('status', result)
        self.assertIn('brokers_checked', result)
        self.assertIn('profiles_found', result)

class TestWebDataSearcher(unittest.TestCase):
    """Tests pour WebDataSearcher"""
    
    def setUp(self):
        self.searcher = WebDataSearcher()
    
    def test_web_search(self):
        """Teste la recherche web"""
        personal_info = {
            'nom': 'Dupont',
            'prenom': 'Jean',
            'email': 'jean@example.com'
        }
        result = self.searcher.search_on_web(personal_info)
        
        self.assertIn('status', result)
        self.assertIn('pages_found', result)

class TestBrowserAnalyzer(unittest.TestCase):
    """Tests pour BrowserAnalyzer"""
    
    def setUp(self):
        self.analyzer = BrowserAnalyzer()
    
    def test_analyzer_initialization(self):
        """Teste l'initialisation"""
        self.assertEqual(len(self.analyzer.results), 0)
    
    def test_browser_paths_exist(self):
        """Teste que les chemins des navigateurs existent"""
        self.assertIn('Chrome', self.analyzer.BROWSER_PATHS)
        self.assertIn('Firefox', self.analyzer.BROWSER_PATHS)
        self.assertIn('Edge', self.analyzer.BROWSER_PATHS)
        self.assertIn('Safari', self.analyzer.BROWSER_PATHS)

class TestIntegration(unittest.TestCase):
    """Tests d'intégration"""
    
    def test_all_modules_importable(self):
        """Teste que tous les modules peuvent être importés"""
        try:
            from config import COLORS, FONTS
            self.assertIn('sky_blue', COLORS)
            self.assertIn('title', FONTS)
        except ImportError as e:
            self.fail(f"Impossible d'importer config: {e}")
    
    def test_data_broker_removal_request(self):
        """Teste une demande de suppression"""
        remover = DataBrokerRemover()
        result = remover.request_removal(
            'PeopleFinder',
            {'nom': 'Test', 'prenom': 'User', 'email': 'test@example.com'}
        )
        
        self.assertIn('broker', result)
        self.assertIn('status', result)

def run_tests():
    """Lance les tests"""
    print("\n" + "="*60)
    print("🧪 Aeroget - Suite de tests")
    print("="*60 + "\n")
    
    # Créer une suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Ajouter les tests
    suite.addTests(loader.loadTestsFromTestCase(TestSystemCleaner))
    suite.addTests(loader.loadTestsFromTestCase(TestDataBrokerRemover))
    suite.addTests(loader.loadTestsFromTestCase(TestWebDataSearcher))
    suite.addTests(loader.loadTestsFromTestCase(TestBrowserAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Exécuter les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Résumé
    print("\n" + "="*60)
    print("📊 Résumé des tests")
    print("="*60)
    print(f"✓ Tests réussis: {result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print(f"✗ Échecs: {len(result.failures)}")
    print(f"✗ Erreurs: {len(result.errors)}")
    print("="*60 + "\n")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
