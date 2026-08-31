# 🪟 GUIDE INSTALLATION WINDOWS - AEROGET

## ⚡ Installation Super Facile (3 étapes)

### **Étape 1: Prérequis - Installer Python**

1. Allez sur https://www.python.org/downloads/
2. Téléchargez **Python 3.10+** (dernière version)
3. Lancez le .exe et **TRÈS IMPORTANT**:
   - ✅ Cochez "Add Python to PATH" (en bas)
   - ✅ Cliquez "Install Now"
4. Attendez que ça se termine
5. **Redémarrez votre ordinateur** (important!)

### **Étape 2: Télécharger Aeroget**

1. Allez sur GitHub: https://github.com/BeeKitchen7-hash/aeroget
2. Cliquez "Code" → "Download ZIP"
3. Extrayez le ZIP dans un dossier
4. Ouvrez le dossier `aeroget-main`

### **Étape 3: Lancer l'installation**

1. **Double-cliquez** sur `INSTALL.bat`
2. Une fenêtre CMD noire s'ouvre
3. Attendez les messages:
   ```
   OK - Python detecte
   OK - pip detecte
   Creation de l'environnement virtuel...
   OK - Environnement virtuel cree
   ```
4. Attendez l'installation des dependances (1-2 minutes)
5. L'application Aeroget se lance automatiquement! 🎉

---

## ⚠️ Si Ça ne Marche Pas...

### Erreur: "Python n'est pas installe"
**Solution:**
1. Reinstallez Python depuis https://www.python.org
2. **TRÈS IMPORTANT**: Cochez "Add Python to PATH"
3. Redémarrez Windows
4. Relancez INSTALL.bat

### Erreur: "pip n'est pas installe"
**Solution:**
```
1. Ouvrez "Invite de Commandes" (CMD)
2. Tapez: python -m ensurepip
3. Attendez
4. Relancez INSTALL.bat
```

### La fenêtre CMD ferme immédiatement
**Solution:**
1. Ouvrez "Invite de Commandes" (CMD)
2. Tapez: `cd chemin\vers\aeroget`
3. Tapez: `INSTALL.bat`
4. Vous verrez les messages d'erreur

### "Accès refusé" ou "Permission"
**Solution:**
1. Cliquez-droit sur INSTALL.bat
2. "Proprietes" → "Compatibilite"
3. Cochez "Executer ce programme en mode compatibilite"
4. Cliquez "Executer ce programme en tant qu'administrateur"
5. Cliquez OK puis relancez

---

## ✅ Après Installation Réussie

### Lancer l'app chaque jour
Double-cliquez `INSTALL.bat` et attendez 30 secondes.

### Lancer directement sans script
1. Ouvrez CMD
2. Tapez: `cd chemin\vers\aeroget`
3. Tapez: `venv\Scripts\activate`
4. Tapez: `python run.py`

### Utiliser la version CLI
Ouvrez CMD et tapez:
```
cd chemin\vers\aeroget
venv\Scripts\activate
python cli.py --interactive
```

---

## 🆘 Support Rapide

| Probleme | Solution |
|----------|----------|
| Python pas trouvé | Reinstaller + Add to PATH + Redemarrer |
| pip pas trouvé | Ouvrir CMD et taper: `python -m ensurepip` |
| CMD se ferme | Ouvrir CMD manuellement et relancer le script |
| Access refusé | Cliquer-droit → "Executer en tant qu'admin" |
| Autre erreur | Consulter README.md ou INSTALLATION.md |

---

## 💻 Version Alternative (Sans Script)

Si INSTALL.bat ne marche pas, procédez manuellement:

```
1. Ouvrez "Invite de Commandes" (CMD)

2. Naviguez vers le dossier:
   cd C:\Users\VOTRE_NOM\Downloads\aeroget-main

3. Creer l'environnement virtuel:
   python -m venv venv

4. L'activer:
   venv\Scripts\activate

5. Installer les dependances:
   pip install -r requirements.txt

6. Lancer l'app:
   python run.py
```

---

## ✨ Ca Marche!

Si vous voyez l'interface Aeroget avec les onglets bleus/orange, c'est bon! 🎉

Profitez du nettoyage! 🧹✨

---

## 🔗 Liens Utiles

- GitHub: https://github.com/BeeKitchen7-hash/aeroget
- Python: https://www.python.org/downloads/
- FAQ: Voir README.md

**Questions?** Ouvrez une issue sur GitHub!

---

**Happy Cleaning on Windows! 🧹💫**
