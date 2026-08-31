# 🚀 Guide d'Installation - Aeroget

Guide complet pour installer et lancer **Aeroget** sur tous les systèmes d'exploitation.

## 📋 Prérequis

- **Python 3.8+** (télécharger de [python.org](https://www.python.org/downloads/))
- **pip** (généralement inclus avec Python)
- **Git** (optionnel, pour cloner le repository)

### Vérifier votre version Python

```bash
python --version
# ou
python3 --version
```

---

## 🔧 Installation Rapide

### 1. Cloner le Repository (recommandé)

```bash
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget
```

### 2. Créer un Environnement Virtuel (recommandé)

#### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les Dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'Application

#### Interface Graphique (recommandé)
```bash
python run.py
```

Ou directement:
```bash
python main.py
```

#### Interface Ligne de Commande
```bash
python cli.py --interactive
```

---

## 💻 Installation par Système d'Exploitation

### Windows 10/11

#### Méthode 1: Avec Git

1. **Installer Git**: Télécharger de [git-scm.com](https://git-scm.com)
2. **Ouvrir PowerShell ou CMD**
3. **Cloner et installer**:
   ```bash
   git clone https://github.com/BeeKitchen7-hash/aeroget.git
   cd aeroget
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python run.py
   ```

#### Méthode 2: Sans Git

1. **Télécharger** le ZIP du repository depuis GitHub
2. **Extraire** le dossier
3. **Ouvrir PowerShell** dans le dossier
4. **Exécuter**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python run.py
   ```

#### Méthode 3: Installation Directe (Simple)

```bash
pip install .
python main.py
```

### macOS

```bash
# Installer Homebrew si nécessaire
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Cloner le repository
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget

# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer
python run.py
```

**Note**: Vous devrez peut-être autoriser l'accès aux fichiers/dossiers système lors de l'exécution d'Aeroget.

### Linux (Ubuntu/Debian)

```bash
# Installer les dépendances système
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# Cloner le repository
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget

# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer (peut nécessiter des droits admin pour certaines opérations)
python run.py

# Ou avec sudo pour les opérations sensibles:
sudo -E python run.py
```

### Linux (Fedora/Red Hat)

```bash
# Installer les dépendances
sudo dnf install python3 python3-devel

# Suite similaire à Ubuntu
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

---

## 📦 Installation Avancée

### Utiliser pip directement

```bash
pip install git+https://github.com/BeeKitchen7-hash/aeroget.git
```

### Utiliser setup.py

```bash
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget
pip install .
```

### Mode Développement

```bash
git clone https://github.com/BeeKitchen7-hash/aeroget.git
cd aeroget
pip install -e .  # Installation éditable
pip install -r requirements.txt
```

---

## ✅ Vérifier l'Installation

### Tester l'importation des modules

```bash
python -c "from main import *; print('✓ Main OK')"
python -c "from system_cleaner import *; print('✓ System Cleaner OK')"
python -c "from data_broker_remover import *; print('✓ Data Broker OK')"
python -c "from browser_analyzer import *; print('✓ Browser Analyzer OK')"
```

### Exécuter les tests

```bash
python test.py
```

Vous devriez voir:
```
✓ Tests réussis: X/Y
✗ Échecs: 0
✗ Erreurs: 0
```

---

## 🐛 Dépannage

### Erreur: "ModuleNotFoundError: No module named 'PyQt6'"

```bash
# Réinstaller PyQt6
pip uninstall PyQt6 -y
pip install PyQt6==6.6.0
```

### Erreur: "Permission denied" (Linux/Mac)

```bash
# Pour les opérations sensibles, utiliser sudo
sudo python run.py

# Ou donner les permissions
chmod +x run.py
chmod +x main.py
chmod +x cli.py
```

### Erreur: "SSL certificate verify failed"

```bash
# Si vous êtes derrière un proxy/firewall
pip install --cert /path/to/cert.pem -r requirements.txt
```

### L'interface graphique ne s'affiche pas

- Vérifier que PyQt6 est installé: `python -m PyQt6`
- Sur Linux, peut nécessiter: `sudo apt-get install python3-pyqt6`
- Essayer la version CLI: `python cli.py`

### Les navigateurs ne sont pas détectés

- S'assurer que les navigateurs sont fermés
- Vérifier les chemins dans `browser_analyzer.py`
- Tester manuellement: `python -c "from browser_analyzer import *; BrowserAnalyzer().analyze_all_browsers({})"`

---

## 🎯 Premier Lancement

### 1. Lancer l'Application

```bash
python run.py
```

### 2. Interface Accueil

Vous verrez une belle interface Frutiger Aero avec 4 onglets:
- 📋 **Informations** - Saisir vos données
- 🧹 **Nettoyage Système** - Nettoyer votre PC
- 🔍 **Données Personnelles** - Chercher vos données
- 🌐 **Navigateurs** - Analyser les navigateurs

### 3. Commencer

1. **Onglet 1**: Entrez vos informations personnelles
2. **Onglet 2**: Nettoyez votre système
3. **Onglet 3**: Recherchez vos données personnelles
4. **Onglet 4**: Analysez vos navigateurs

### 4. Exporter

Cliquez sur "📊 Exporter le rapport" pour sauvegarder un rapport JSON.

---

## 🔒 Sécurité

### ⚠️ Recommandations

1. **Toujours exécuter depuis un répertoire de confiance**
2. **Vérifier le code avant d'exécuter (open source)**
3. **Créer une sauvegarde avant de nettoyer**
4. **Utiliser un compte non-administrateur quand possible**
5. **Vérifier les permissions du logiciel**

### Droits Administrateur

Certaines opérations nécessitent les droits administrateur:
- Vider la corbeille
- Supprimer les fichiers temporaires système
- Accéder à certains chemins

Vous serez invité à fournir votre mot de passe si nécessaire.

---

## 🆘 Obtenir de l'Aide

### Documentation

- [README.md](README.md) - Guide principal
- [ADVANCED.md](ADVANCED.md) - Guide avancé
- [GitHub Issues](https://github.com/BeeKitchen7-hash/aeroget/issues) - Signaler un bug

### Commandes d'Aide

```bash
# Interface CLI
python cli.py --help

# Mode interactif
python cli.py --interactive
```

### Logs et Diagnostics

```bash
# Afficher les logs de Python
python -v run.py 2>&1 | tee aeroget.log

# Tester les modules individuellement
python -c "from system_cleaner import SystemCleaner; SystemCleaner().clean_temp_files()"
```

---

## 📊 Vérifications après Installation

### Checklist ✅

- [ ] Python 3.8+ installé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Tests passent (`python test.py`)
- [ ] Application lance (`python run.py`)
- [ ] Interface s'affiche correctement
- [ ] Onglets accessibles
- [ ] Boutons cliquables

---

## 🔄 Mise à Jour

### Mettre à jour vers la dernière version

```bash
cd aeroget
git pull origin main
pip install -r requirements.txt --upgrade
```

### Vérifier la version

```bash
grep "version=" setup.py
```

---

## 🚀 Prochaines Étapes

1. **Personnaliser** les paramètres dans `config.py`
2. **Ajouter des data brokers** dans `brokers_config.py`
3. **Lire** [ADVANCED.md](ADVANCED.md) pour des features avancées
4. **Contribuer** au projet sur GitHub

---

## 📝 Notes

- **Première exécution**: Peut être plus lente (téléchargement de dépendances)
- **Navigateurs**: Doivent être fermés avant l'analyse
- **Admin**: Recommandé pour le nettoyage système complet
- **Backups**: Créer une sauvegarde avant de nettoyer

---

**✨ Bienvenue dans Aeroget! Profitez du nettoyage avec style Frutiger Aero! ✨**

Pour toute question: [GitHub Issues](https://github.com/BeeKitchen7-hash/aeroget/issues)
