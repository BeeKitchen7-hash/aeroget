#!/usr/bin/env python3
"""
EXAMPLES.md - Exemples d'utilisation d'Aeroget

Cet fichier montre comment utiliser Aeroget de différentes façons
"""

# ================================================================================
# EXEMPLE 1: Utiliser l'Interface Graphique
# ================================================================================

# ✨ Le moyen le plus simple et beau d'utiliser Aeroget!
# 
# Juste exécuter:
#   python run.py
# ou
#   python main.py
#
# L'interface Frutiger Aero s'ouvrira avec 4 onglets:
# 1. Saisir les informations personnelles
# 2. Nettoyer le système
# 3. Rechercher les données personnelles
# 4. Analyser les navigateurs

# ================================================================================
# EXEMPLE 2: Utiliser l'Interface CLI - Mode Interactif
# ================================================================================

# Lancer le mode interactif:
#   python cli.py --interactive
#
# L'app vous guidera étape par étape:
# 1. Saisir vos informations
# 2. Choisir l'action (nettoyer / rechercher / analyser / tout)
# 3. Voir les résultats
# 4. Exporter en JSON (optionnel)

# ================================================================================
# EXEMPLE 3: Nettoyer le Système (CLI)
# ================================================================================

# python cli.py --clean
#
# Résultat attendu:
# ============================================================
# ✨ Aeroget - Nettoyeur de Données Personnelles CLI ✨
# ============================================================
# 
# 🧹 Nettoyage du système en cours...
# 
#   1️⃣ Vider la corbeille...
#      → ✓ Succès
#   2️⃣ Supprimer les fichiers temporaires...
#      → ✓ 153 fichier(s) supprimé(s)
#   3️⃣ Nettoyer les caches navigateurs...
#      → ✓ 3 navigateur(s) nettoyé(s)
# 
# ✓ Nettoyage terminé!

# ================================================================================
# EXEMPLE 4: Rechercher Données Personnelles (CLI)
# ================================================================================

# python cli.py --search --name "Jean Dupont" --email "jean@example.com" --phone "0612345678"
#
# Résultat attendu:
# ============================================================
# ✨ Aeroget - Nettoyeur de Données Personnelles CLI ✨
# ============================================================
# 
# 🔍 Recherche des données personnelles en cours...
# 
#   1️⃣ Recherche dans les data brokers...
#      → ✓ 5 profil(s) trouvé(s) sur 10 broker(s)
#      🚨 PeopleFinder: Profil détecté - Information personnelle visible
#         Lien de suppression: https://www.peoplefinder.com/opt-out
#      🚨 Whitepages: Profil détecté
#         Lien de suppression: https://www.whitepages.com/suppression-demande
# 
#   2️⃣ Recherche sur le web...
#      → ✓ 8 page(s) trouvée(s)
# 
# ✓ Recherche terminée!

# ================================================================================
# EXEMPLE 5: Analyser les Navigateurs (CLI)
# ================================================================================

# python cli.py --analyze --name "Jean" --firstname "Dupont"
#
# Résultat attendu:
# ============================================================
# ✨ Aeroget - Nettoyeur de Données Personnelles CLI ✨
# ============================================================
# 
# 🌐 Analyse des navigateurs en cours...
# 
#   → ✓ 2 navigateur(s) analysé(s), 12 résultat(s)
# 
#   🔸 Chrome:
#      • Historique: 8 match(es)
#        - https://www.example.com/profile/jean-dupont...
#        - https://www.facebook.com/jean.dupont...
#        - https://www.linkedin.com/in/jeandupont...
#      • Cookies: 23
# 
#   🔸 Firefox:
#      • Historique: 4 match(es)
#        - https://www.twitter.com/jeandupont...
#
# ✓ Analyse terminée!

# ================================================================================
# EXEMPLE 6: Tout Faire à la Fois (CLI)
# ================================================================================

# python cli.py --clean --search --analyze --name "Jean" --email "jean@example.com"
#
# Cela va:
# 1. Nettoyer le système
# 2. Rechercher les données personnelles
# 3. Analyser les navigateurs
# Tout en une seule commande!

# ================================================================================
# EXEMPLE 7: Utilisation Programmtique (Python)
# ================================================================================

from system_cleaner import SystemCleaner
from data_broker_remover import DataBrokerRemover
from browser_analyzer import BrowserAnalyzer
from report_generator import ReportGenerator, RemovalRequestGenerator

# 7.1: Nettoyer le système
print("🧹 Nettoyage du système...")
cleaner = SystemCleaner()
cleaner.clean_recycle_bin()
cleaner.clean_temp_files()
cleaner.clean_browser_cache()
results = cleaner.get_results()
print(f"✓ {len(results)} opération(s) complétée(s)")

# 7.2: Rechercher les données
print("\n🔍 Recherche données personnelles...")
personal_info = {
    'nom': 'Dupont',
    'prenom': 'Jean',
    'email': 'jean@example.com',
    'telephone': '0612345678',
    'adresse': '123 Rue de la Paix',
    'ville': 'Paris',
    'code_postal': '75000',
    'pays': 'France'
}

remover = DataBrokerRemover()
broker_results = remover.search_personal_data(personal_info)
print(f"✓ {broker_results['profiles_found']} profil(s) trouvé(s)")

# 7.3: Analyser les navigateurs
print("\n🌐 Analyse des navigateurs...")
analyzer = BrowserAnalyzer()
browser_results = analyzer.analyze_all_browsers(personal_info)
print(f"✓ {browser_results['total_matches']} données trouvées")

# 7.4: Générer un rapport
print("\n📊 Génération rapport...")
gen = ReportGenerator()
report = gen.generate_summary_report(
    personal_info,
    cleaner.get_results(),
    remover.get_results(),
    analyzer.get_results()
)
print(f"Niveau de risque: {report['summary']['risk_level']}")
gen.export_to_html('report.html')
print("✓ Rapport exporté en HTML")

# 7.5: Générer les demandes de suppression
print("\n📧 Génération demandes RGPD...")
removal_gen = RemovalRequestGenerator()
gdpr_requests = removal_gen.generate_bulk_requests(personal_info, 'gdpr')
print(f"✓ {len(gdpr_requests)} demande(s) RGPD générée(s)")
removal_gen.export_requests_to_file('demandes_suppression.json')

# ================================================================================
# EXEMPLE 8: Extension Personnalisée
# ================================================================================

class MyCustomCleaner(SystemCleaner):
    """Nettoyeur personnalisé avec fonctionnalités additionnelles"""
    
    def clean_downloads(self):
        """Nettoie le dossier Téléchargements"""
        import os
        import shutil
        
        result = {'action': 'Nettoyer les téléchargements', 'status': 'En cours...'}
        
        try:
            downloads = os.path.expanduser('~/Downloads')
            if os.path.exists(downloads):
                for item in os.listdir(downloads):
                    try:
                        path = os.path.join(downloads, item)
                        if os.path.isfile(path):
                            os.remove(path)
                        elif os.path.isdir(path):
                            shutil.rmtree(path)
                    except:
                        pass
            result['status'] = '✓ Succès'
        except Exception as e:
            result['status'] = f'✗ Erreur: {e}'
        
        self.results.append(result)
        return result

# Utilisation
my_cleaner = MyCustomCleaner()
my_cleaner.clean_downloads()
print(my_cleaner.results)

# ================================================================================
# EXEMPLE 9: Intégration avec Flask (API)
# ================================================================================

# À utiliser avec: pip install flask
# 
# from flask import Flask, jsonify, request
# from system_cleaner import SystemCleaner
# from data_broker_remover import DataBrokerRemover
# 
# app = Flask(__name__)
# 
# @app.route('/api/clean', methods=['POST'])
# def clean_system():
#     cleaner = SystemCleaner()
#     cleaner.clean_recycle_bin()
#     cleaner.clean_temp_files()
#     return jsonify({'status': 'success', 'results': cleaner.get_results()})
# 
# @app.route('/api/search', methods=['POST'])
# def search_data():
#     personal_info = request.json
#     remover = DataBrokerRemover()
#     results = remover.search_personal_data(personal_info)
#     return jsonify(results)
# 
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
#
# Utilisation:
#   curl -X POST http://localhost:5000/api/clean
#   curl -X POST http://localhost:5000/api/search -H "Content-Type: application/json" \
#        -d '{"nom":"Dupont","prenom":"Jean","email":"jean@example.com"}'

# ================================================================================
# EXEMPLE 10: Utilisation avec Threads (Multi-threading)
# ================================================================================

import threading
from queue import Queue

def clean_system_thread(queue):
    """Exécute le nettoyage dans un thread"""
    cleaner = SystemCleaner()
    cleaner.clean_recycle_bin()
    cleaner.clean_temp_files()
    queue.put(('clean', cleaner.get_results()))

def search_data_thread(queue, personal_info):
    """Exécute la recherche dans un thread"""
    remover = DataBrokerRemover()
    results = remover.search_personal_data(personal_info)
    queue.put(('search', results))

def analyze_browsers_thread(queue, personal_info):
    """Exécute l'analyse dans un thread"""
    analyzer = BrowserAnalyzer()
    results = analyzer.analyze_all_browsers(personal_info)
    queue.put(('browser', results))

# Utiliser
queue = Queue()
personal_info = {'nom': 'Test', 'prenom': 'User', 'email': 'test@example.com'}

t1 = threading.Thread(target=clean_system_thread, args=(queue,))
t2 = threading.Thread(target=search_data_thread, args=(queue, personal_info))
t3 = threading.Thread(target=analyze_browsers_thread, args=(queue, personal_info))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# Récupérer les résultats
while not queue.empty():
    action, result = queue.get()
    print(f"{action}: {result}")

# ================================================================================
# EXEMPLE 11: Exporter en Différents Formats
# ================================================================================

import json
from report_generator import ReportGenerator

personal_info = {'nom': 'Dupont', 'prenom': 'Jean'}
gen = ReportGenerator()

# Générer rapport
report = gen.generate_summary_report(personal_info)

# Export JSON
gen.export_to_json('rapport.json')
print("✓ Exporté en JSON")

# Export HTML
gen.export_to_html('rapport.html')
print("✓ Exporté en HTML")

# Afficher au terminal
print("\n" + "="*50)
print("RAPPORT")
print("="*50)
print(json.dumps(report, indent=2, ensure_ascii=False))

# ================================================================================
# EXEMPLE 12: Utiliser les Demandes RGPD/CCPA
# ================================================================================

from report_generator import RemovalRequestGenerator
from brokers_config import EMAIL_TEMPLATES

personal_info = {
    'nom': 'Dupont',
    'prenom': 'Jean',
    'email': 'jean@example.com',
    'telephone': '0612345678',
    'adresse': '123 Rue',
    'ville': 'Paris',
    'code_postal': '75000',
    'pays': 'France'
}

gen = RemovalRequestGenerator()

# 12.1: Générer une demande RGPD
print("📧 Demande RGPD:")
gdpr_msg = gen.generate_gdpr_request(personal_info)
print(gdpr_msg)
print("\n" + "="*50 + "\n")

# 12.2: Générer une demande CCPA
print("📧 Demande CCPA:")
ccpa_msg = gen.generate_ccpa_request(personal_info)
print(ccpa_msg)
print("\n" + "="*50 + "\n")

# 12.3: Générer pour un broker spécifique
print("📧 Demande pour PeopleFinder (RGPD):")
broker_msg = gen.generate_for_broker('PeopleFinder', personal_info, 'gdpr')
print(broker_msg['message'])

# 12.4: Générer pour tous les brokers
print("\n📧 Génération en masse...")
all_requests = gen.generate_bulk_requests(personal_info, 'gdpr')
print(f"✓ {len(all_requests)} demande(s) générée(s)")

# 12.5: Sauvegarder
gen.export_requests_to_file('all_removal_requests.json')
print("✓ Toutes les demandes sauvegardées en JSON")

# ================================================================================
# CONCLUSION
# ================================================================================

"""
Vous avez maintenant des exemples de:
1. ✓ Interface GUI (lancer simplement)
2. ✓ Interface CLI (avec arguments)
3. ✓ Mode interactif
4. ✓ Utilisation programmmatique
5. ✓ Extensions personnalisées
6. ✓ API REST
7. ✓ Multi-threading
8. ✓ Génération de rapports
9. ✓ Demandes RGPD/CCPA

Pour plus d'informations:
- README.md - Guide complet
- INSTALLATION.md - Installation détaillée
- ADVANCED.md - Guide développeur

Aeroget est flexible et puissant! 🚀✨
"""
