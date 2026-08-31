# ADVANCED.md - Guide Avancé d'Aeroget

## 📚 Table des matières

1. [Architecture Avancée](#architecture-avancée)
2. [Développement](#développement)
3. [Configuration Personnalisée](#configuration-personnalisée)
4. [Intégration API](#intégration-api)
5. [Génération de Rapports](#génération-de-rapports)
6. [Gestion des Data Brokers](#gestion-des-data-brokers)
7. [Troubleshooting](#troubleshooting)

---

## Architecture Avancée

### Structure du Projet

```
aeroget/
├── Core Modules
│   ├── system_cleaner.py          # Nettoyage système
│   ├── data_broker_remover.py     # Gestion data brokers
│   ├── browser_analyzer.py        # Analyse navigateurs
│   └── report_generator.py        # Génération rapports
│
├── UI Modules
│   └── main.py                    # Interface PyQt6
│
├── CLI Module
│   └── cli.py                     # Interface CLI
│
├── Configuration
│   ├── config.py                  # Couleurs, fonts, UI
│   └── brokers_config.py          # Data brokers, templates email
│
├── Testing
│   └── test.py                    # Suite de tests
│
└── Deployment
    ├── setup.py                   # Package setup
    ├── run.py                     # Launcher
    └── requirements.txt           # Dépendances
```

### Flux de Données

```
User Input
    ↓
┌─────────────────────┐
│ Data Input Dialog   │
└─────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│         Main Processing                 │
├─────────────────────────────────────────┤
│ • System Cleaner                        │
│ • Data Broker Remover                   │
│ • Browser Analyzer                      │
│ • Report Generator                      │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│         Result Display                  │
├─────────────────────────────────────────┤
│ • Results Table                         │
│ • JSON Export                           │
│ • HTML Report                           │
└─────────────────────────────────────────┘
```

---

## Développement

### Installation pour les Développeurs

```bash
# Clone et setup
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget

# Créer un virtualenv
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer en mode développement
pip install -e .
pip install -r requirements.txt

# Installer les dépendances de dev
pip install pytest pytest-cov black flake8
```

### Exécuter les Tests

```bash
# Tests simples
python test.py

# Tests avec pytest
pytest test.py -v

# Coverage
pytest test.py --cov=. --cov-report=html
```

### Code Style

```bash
# Formater le code
black *.py

# Vérifier le style
flake8 *.py

# Analyser la qualité
pylint *.py
```

---

## Configuration Personnalisée

### Personnaliser les Couleurs Aero

Modifiez `config.py`:

```python
COLORS = {
    'sky_blue': '#87CEEB',      # Bleu ciel
    'dark_blue': '#1E90FF',      # Bleu foncé
    'light_purple': '#DDA0DD',   # Violet léger
    'lime': '#00FF00',           # Vert citron
    'orange': '#FF8C00',         # Orange
    'silver': '#C0C0C0',         # Argent
    'white': '#FFFFFF',          # Blanc
    'gradient_start': '#87CEEB', # Dégradé début
    'gradient_end': '#E0FFFF',   # Dégradé fin
    'orange_gradient': '#FFD700',# Orange dégradé
}
```

### Personnaliser les Fonts

```python
FONTS = {
    'title': ('Segoe UI', 24, 'bold'),
    'header': ('Segoe UI', 14, 'bold'),
    'normal': ('Segoe UI', 10),
    'small': ('Segoe UI', 8),
}
```

### Ajouter des Data Brokers Personnalisés

Dans `brokers_config.py`:

```python
DATA_BROKERS_CONFIG = {
    'custom_brokers': [
        {
            'name': 'MonBroker',
            'url': 'https://www.monbroker.com',
            'remove_url': 'https://www.monbroker.com/optout',
            'type': 'people_search',
            'method': 'web_form'
        }
    ]
}
```

---

## Intégration API

### Créer une Extension Personnalisée

```python
# extension.py
from system_cleaner import SystemCleaner
from data_broker_remover import DataBrokerRemover

class CustomCleaner(SystemCleaner):
    """Nettoyeur personnalisé"""
    
    def custom_clean(self) -> dict:
        """Méthode personnalisée"""
        result = {
            'action': 'Nettoyage personnalisé',
            'status': 'En cours...',
        }
        
        # Votre logique ici
        result['status'] = '✓ Succès'
        self.results.append(result)
        return result

# Utilisation
cleaner = CustomCleaner()
cleaner.clean_recycle_bin()
cleaner.custom_clean()
results = cleaner.get_results()
```

### Intégrer avec d'autres Applications

```python
# api.py - Simple REST API
from flask import Flask, jsonify
from system_cleaner import SystemCleaner
from browser_analyzer import BrowserAnalyzer

app = Flask(__name__)

@app.route('/api/clean-system', methods=['POST'])
def clean_system():
    cleaner = SystemCleaner()
    cleaner.clean_recycle_bin()
    cleaner.clean_temp_files()
    return jsonify({
        'status': 'success',
        'results': cleaner.get_results()
    })

@app.route('/api/analyze/<browser>', methods=['GET'])
def analyze_browser(browser):
    analyzer = BrowserAnalyzer()
    # Analyser un navigateur spécifique
    return jsonify({'browser': browser})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## Génération de Rapports

### Utiliser le Générateur de Rapports

```python
from report_generator import ReportGenerator, RemovalRequestGenerator

# Créer un rapport complet
generator = ReportGenerator()
report = generator.generate_summary_report(
    personal_info={'nom': 'Dupont', 'prenom': 'Jean'},
    system_clean_results=[...],
    data_broker_results=[...],
    browser_results=[...]
)

# Exporter
generator.export_to_json('report.json')
generator.export_to_html('report.html')
```

### Générer des Demandes de Suppression

```python
from report_generator import RemovalRequestGenerator

generator = RemovalRequestGenerator()

# Générer pour RGPD
personal_info = {
    'nom': 'Dupont',
    'prenom': 'Jean',
    'email': 'jean@example.com',
    'adresse': '123 Rue de la Paix',
    'code_postal': '75000',
    'ville': 'Paris',
    'pays': 'France'
}

# Pour tous les brokers
requests = generator.generate_bulk_requests(personal_info, 'gdpr')

# Exporter
generator.export_requests_to_file('demandes.json')
```

---

## Gestion des Data Brokers

### Format des Data Brokers

```python
{
    'name': 'NomDuBroker',
    'url': 'https://www.brokerurl.com',
    'remove_url': 'https://www.brokerurl.com/remove',
    'type': 'people_search|background_check|credit_bureau|social_network',
    'method': 'web_form|email|account_settings|phone'
}
```

### Ajouter un Broker

```python
# Dans brokers_config.py
new_broker = {
    'name': 'NewBroker',
    'url': 'https://www.newbroker.com',
    'remove_url': 'https://www.newbroker.com/privacy/remove',
    'type': 'people_search',
    'method': 'web_form'
}

DATA_BROKERS_CONFIG['us_brokers'].append(new_broker)
```

### Utiliser Selenium pour l'Automatisation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def automated_removal(broker_name, personal_info):
    driver = webdriver.Chrome()
    
    try:
        broker = next(b for b in DATA_BROKERS if b['name'] == broker_name)
        driver.get(broker['remove_url'])
        
        # Remplir le formulaire
        name_field = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.NAME, 'name')
        )
        name_field.send_keys(personal_info['nom'])
        
        # Continuer avec les autres champs...
        
        # Soumettre le formulaire
        submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit_btn.click()
        
        return {'status': 'success', 'broker': broker_name}
    
    finally:
        driver.quit()
```

---

## Troubleshooting

### Problèmes Courants

#### PyQt6 ne se lance pas

```bash
# Réinstaller PyQt6
pip uninstall PyQt6
pip install PyQt6==6.6.0

# Sur Linux, peut nécessiter:
sudo apt-get install python3-pyqt6
```

#### Les navigateurs ne sont pas détectés

- Vérifier que les chemins dans `browser_analyzer.py` correspondent à votre système
- Sur Linux, les chemins doivent être `/home/user/.config/google-chrome`
- Sur macOS, `/Users/user/Library/Application Support/Google/Chrome`

#### Erreur de permission (système_cleaner)

```bash
# Exécuter avec les droits administrateur
sudo python main.py  # Linux/Mac
# ou exécuter le terminal en admin (Windows)
```

#### Données non trouvées dans les navigateurs

- Les navigateurs doivent être fermés avant l'analyse
- Les bases de données SQLite peuvent être verrouillées par le processus navigateur

#### Problèmes de performance

```python
# Limiter l'analyse à certains navigateurs
analyzer = BrowserAnalyzer()
# Modifier BROWSER_PATHS pour désactiver certains navigateurs
```

---

## Performance et Optimisation

### Profiler le Code

```python
import cProfile
import pstats

def profile_code():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Votre code ici
    from system_cleaner import SystemCleaner
    cleaner = SystemCleaner()
    cleaner.clean_temp_files()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(20)

if __name__ == '__main__':
    profile_code()
```

### Optimiser les Requêtes Web

```python
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import requests

def create_session_with_retries():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

# Utilisation
session = create_session_with_retries()
response = session.get('https://example.com')
```

---

## Déploiement

### Créer un Installateur Windows

```bash
# Installer PyInstaller
pip install pyinstaller

# Créer l'exécutable
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

### Packager pour Linux

```bash
# Créer un .deb
python setup.py sdist
# Ou utiliser fpm
fpm -s python -t deb setup.py
```

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "cli.py"]
CMD ["--interactive"]
```

---

## Support et Contribution

- **Issues**: [GitHub Issues](https://github.com/BeeKitchen7-hash/aeroget/issues)
- **Discussions**: [GitHub Discussions](https://github.com/BeeKitchen7-hash/aeroget/discussions)
- **Pull Requests**: Bienvenues avec description détaillée

---

## Ressources

- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [RGPD - Article 17](https://gdpr-info.eu/art-17-gdpr/)
- [CCPA - California Consumer Privacy Act](https://cppa.ca.gov/)

---

**Version**: 1.0.0  
**Dernière mise à jour**: 2024  
**Auteur**: BeeKitchen7-hash
