# ✨ Aeroget - Nettoyeur de Données Personnelles Frutiger Aero ✨

Aeroget est une application complète dans le style **Frutiger Aero** (années 2000) qui vous permet de:

- 🧹 **Nettoyer votre système** (corbeille, fichiers temporaires, caches navigateur)
- 🔍 **Rechercher vos données personnelles** chez les data brokers et sur le web
- 🌐 **Analyser tous vos navigateurs** pour trouver vos données sensibles
- 🗑️ **Demander la suppression** de vos informations en ligne
- 📊 **Exporter des rapports** détaillés de toutes les données trouvées

## 🎨 Caractéristiques

### Interface Frutiger Aero
- Design années 2000 avec gradients colorés et effets brillants
- Palette de couleurs vive (bleu ciel, orange, violet, vert)
- Buttons avec effets hover et animations
- 4 onglets intuitifs pour une expérience complète

### Fonctionnalités Principales

#### 1. 📋 Informations Personnelles
Saisissez vos informations:
- Nom et prénom
- Email
- Numéro de téléphone
- Adresse, ville, code postal, pays

#### 2. 🧹 Nettoyage Système
Automatise le nettoyage de votre système:
- Vider la corbeille
- Supprimer les fichiers temporaires (Windows/Linux/Mac)
- Nettoyer le cache des navigateurs (Chrome, Firefox, Edge, Safari)

#### 3. 🔍 Recherche de Données Personnelles
Cherche vos informations chez les data brokers:
- PeopleFinder
- Whitepages
- BeenVerified
- Spokeo
- MyLife
- TruthFinder
- Intelius
- ZoomInfo
- LinkedIn
- Facebook
- Et plus...

#### 4. 🌐 Analyse des Navigateurs
Analyse tous vos navigateurs pour trouver:
- Historique contenant vos données personnelles
- Cookies associés
- Données d'autofill
- Liste complète des pages visitées

## 📦 Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

```bash
# Cloner le repository
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget

# Installer les dépendances
pip install -r requirements.txt
```

## 🚀 Utilisation

### Mode GUI (Graphique) - Recommandé

```bash
python run.py
```

Ou directement:

```bash
python main.py
```

### Mode CLI (Ligne de Commande)

#### Mode Interactif
```bash
python cli.py --interactive
```

#### Nettoyage du système
```bash
python cli.py --clean
```

#### Recherche de données avec arguments
```bash
python cli.py --search --name "Jean Dupont" --email "jean@example.com" --phone "0612345678"
```

#### Analyser les navigateurs
```bash
python cli.py --analyze --name "Jean" --firstname "Dupont"
```

#### Tout faire à la fois
```bash
python cli.py --clean --search --analyze --name "Jean" --email "jean@example.com"
```

#### Aide complète
```bash
python cli.py --help
```

## 🛠️ Architecture

```
aeroget/
├── main.py                    # Interface GUI Frutiger Aero
├── cli.py                     # Interface CLI
├── run.py                     # Script de lancement
├── config.py                  # Configuration (couleurs, styles)
├── system_cleaner.py          # Module de nettoyage système
├── data_broker_remover.py     # Recherche et demande suppression
├── browser_analyzer.py        # Analyse des navigateurs
├── requirements.txt           # Dépendances
└── README.md                  # Ce fichier
```

## 📚 Modules

### SystemCleaner
Gère le nettoyage du système:
- `clean_recycle_bin()` - Vide la corbeille
- `clean_temp_files()` - Supprime les fichiers temporaires
- `clean_browser_cache()` - Nettoie les caches navigateurs

### DataBrokerRemover
Cherche et supprime les données chez les brokers:
- `search_personal_data()` - Recherche sur les data brokers
- `request_removal()` - Envoie une demande de suppression
- `get_removal_links()` - Retourne les liens de suppression

### WebDataSearcher
Recherche sur le web:
- `search_on_web()` - Recherche vos données sur Google et autres

### BrowserAnalyzer
Analyse les navigateurs:
- `analyze_all_browsers()` - Analyse tous les navigateurs détectés
- Supporte: Chrome, Firefox, Edge, Safari

## ⚙️ Configuration

Modifiez `config.py` pour personnaliser:
- Les couleurs Aero
- Les fonts
- Les paramètres UI

## 🔒 Sécurité

- Les informations personnelles restent sur votre appareil
- Aucune donnée n'est envoyée à des serveurs externes
- Le logiciel fonctionne hors ligne (sauf pour les recherches web)
- Les demandes de suppression sont envoyées directement aux data brokers

## ⚠️ Avertissements

- Certaines opérations nécessitent les privilèges administrateur
- Le nettoyage de la corbeille est irréversible
- Les données supprimées ne peuvent pas être récupérées
- Testez d'abord sur une copie de votre système

## 📋 Résultats

Les résultats peuvent être exportés en JSON avec:
- Données recherchées
- Brokers trouvés avec liens de suppression
- Données dans les navigateurs
- Historique complet d'analyse

## 🤝 Contribution

Les contributions sont bienvenues! Veuillez:
1. Fork le projet
2. Créer une branche feature
3. Commiter vos changements
4. Pousser vers la branche
5. Créer une Pull Request

## 📄 Licence

MIT License - Voir LICENSE file

## 👤 Auteur

**BeeKitchen7-hash**

## 🙏 Remerciements

- Inspiré par le design Frutiger Aero des années 2000
- Merci à tous les contributeurs
- Merci PyQt6 pour l'interface graphique

## 📞 Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub.

## 🔗 Liens Utiles

- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Python Documentation](https://docs.python.org/3/)
- [Frutiger Aero Design](https://en.wikipedia.org/wiki/Frutiger_Aero)

---

⭐ Si ce projet vous plaît, n'hésitez pas à laisser une star! 
