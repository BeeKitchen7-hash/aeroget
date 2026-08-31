#!/usr/bin/env python3
"""
Aeroget CLI - Interface en ligne de commande
Pour une utilisation rapide sans GUI
"""

import sys
import argparse
import json
from system_cleaner import SystemCleaner
from data_broker_remover import DataBrokerRemover, WebDataSearcher
from browser_analyzer import BrowserAnalyzer

def print_header():
    """Affiche l'en-tête"""
    print("\n" + "="*60)
    print("✨ Aeroget - Nettoyeur de Données Personnelles CLI ✨")
    print("="*60 + "\n")

def clean_system():
    """Nettoie le système via CLI"""
    print_header()
    print("🧹 Nettoyage du système en cours...\n")
    
    cleaner = SystemCleaner()
    
    print("  1️⃣ Vider la corbeille...")
    result1 = cleaner.clean_recycle_bin()
    print(f"     → {result1['status']}")
    
    print("  2️⃣ Supprimer les fichiers temporaires...")
    result2 = cleaner.clean_temp_files()
    print(f"     → {result2['status']}")
    
    print("  3️⃣ Nettoyer les caches navigateurs...")
    result3 = cleaner.clean_browser_cache()
    print(f"     → {result3['status']}")
    
    print("\n✓ Nettoyage terminé!\n")
    return cleaner.get_results()

def search_personal_data(personal_info: dict):
    """Recherche les données personnelles via CLI"""
    print_header()
    print("🔍 Recherche des données personnelles en cours...\n")
    
    broker_remover = DataBrokerRemover()
    web_searcher = WebDataSearcher()
    
    print("  1️⃣ Recherche dans les data brokers...")
    broker_result = broker_remover.search_personal_data(personal_info)
    print(f"     → {broker_result['status']}")
    
    if broker_result['details']:
        for detail in broker_result['details']:
            if detail['found']:
                print(f"     🚨 {detail['broker_name']}: {detail['reason']}")
                print(f"        Lien de suppression: {detail['remove_url']}")
    
    print("\n  2️⃣ Recherche sur le web...")
    web_result = web_searcher.search_on_web(personal_info)
    print(f"     → {web_result['status']}")
    
    print("\n✓ Recherche terminée!\n")
    return broker_remover.get_results() + web_searcher.get_results()

def analyze_browsers(personal_info: dict):
    """Analyse les navigateurs via CLI"""
    print_header()
    print("🌐 Analyse des navigateurs en cours...\n")
    
    analyzer = BrowserAnalyzer()
    result = analyzer.analyze_all_browsers(personal_info)
    
    print(f"  → {result['status']}")
    
    if result['details']:
        for browser_name, browser_data in result['details'].items():
            print(f"\n  🔸 {browser_name}:")
            if browser_data['history']:
                print(f"     • Historique: {len(browser_data['history'])} match(es)")
                for item in browser_data['history'][:3]:
                    print(f"       - {item['url'][:50]}...")
            if browser_data['cookies']:
                print(f"     • Cookies: {len(browser_data['cookies'])}")
    
    print("\n✓ Analyse terminée!\n")
    return analyzer.get_results()

def interactive_mode():
    """Mode interactif"""
    print_header()
    print("Mode interactif - Veuillez saisir vos informations personnelles:\n")
    
    personal_info = {}
    fields = ['nom', 'prenom', 'email', 'telephone', 'adresse', 'ville', 'code_postal', 'pays']
    
    for field in fields:
        value = input(f"  {field.replace('_', ' ').capitalize()}: ").strip()
        if value:
            personal_info[field] = value
    
    if not personal_info:
        print("\n❌ Aucune information saisie!")
        return
    
    print("\n📋 Informations enregistrées:")
    for key, value in personal_info.items():
        if value:
            print(f"  • {key}: {value}")
    
    print("\nChoisissez une action:")
    print("  1. Nettoyer le système")
    print("  2. Rechercher mes données personnelles")
    print("  3. Analyser les navigateurs")
    print("  4. Tout faire (1+2+3)")
    
    choice = input("\nChoix (1-4): ").strip()
    
    results = []
    if choice == '1':
        results = clean_system()
    elif choice == '2':
        results = search_personal_data(personal_info)
    elif choice == '3':
        results = analyze_browsers(personal_info)
    elif choice == '4':
        results.extend(clean_system())
        results.extend(search_personal_data(personal_info))
        results.extend(analyze_browsers(personal_info))
    
    # Exporter les résultats
    if results and input("\n📊 Exporter les résultats en JSON? (o/n): ").lower() == 'o':
        filename = input("Nom du fichier (défaut: aeroget_results.json): ").strip() or "aeroget_results.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✓ Résultats exportés vers {filename}")

def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(
        description='Aeroget - Nettoyeur de données personnelles CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python cli.py --clean              # Nettoyer le système
  python cli.py --search --name John --email john@example.com  # Rechercher données
  python cli.py --interactive        # Mode interactif
        """
    )
    
    parser.add_argument('--clean', action='store_true', help='Nettoyer le système')
    parser.add_argument('--search', action='store_true', help='Rechercher les données personnelles')
    parser.add_argument('--analyze', action='store_true', help='Analyser les navigateurs')
    parser.add_argument('--interactive', action='store_true', help='Mode interactif')
    
    # Arguments personnels
    parser.add_argument('--name', help='Votre nom')
    parser.add_argument('--firstname', help='Votre prénom')
    parser.add_argument('--email', help='Votre email')
    parser.add_argument('--phone', help='Votre numéro de téléphone')
    parser.add_argument('--address', help='Votre adresse')
    parser.add_argument('--city', help='Votre ville')
    parser.add_argument('--zipcode', help='Votre code postal')
    parser.add_argument('--country', help='Votre pays')
    
    args = parser.parse_args()
    
    # Mode interactif par défaut
    if not (args.clean or args.search or args.analyze or args.interactive):
        args.interactive = True
    
    if args.interactive:
        interactive_mode()
        return
    
    # Préparer les infos personnelles
    personal_info = {}
    if args.name:
        personal_info['nom'] = args.name
    if args.firstname:
        personal_info['prenom'] = args.firstname
    if args.email:
        personal_info['email'] = args.email
    if args.phone:
        personal_info['telephone'] = args.phone
    if args.address:
        personal_info['adresse'] = args.address
    if args.city:
        personal_info['ville'] = args.city
    if args.zipcode:
        personal_info['code_postal'] = args.zipcode
    if args.country:
        personal_info['pays'] = args.country
    
    # Exécuter les actions
    results = []
    
    if args.clean:
        results.extend(clean_system())
    
    if args.search:
        if not personal_info:
            print("❌ Veuillez fournir au moins une information personnelle!")
            return
        results.extend(search_personal_data(personal_info))
    
    if args.analyze:
        if not personal_info:
            print("❌ Veuillez fournir au moins une information personnelle!")
            return
        results.extend(analyze_browsers(personal_info))
    
    # Afficher les résultats
    if results:
        print("\n" + "="*60)
        print("📊 RÉSULTATS")
        print("="*60 + "\n")
        print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
