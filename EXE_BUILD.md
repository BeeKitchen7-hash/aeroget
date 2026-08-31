# Comment Générer aeroget.exe

Ce guide vous montre comment créer un executable Windows (`aeroget.exe`) que vous pouvez lancer en double-cliquant.

## Prérequis

- Windows 7, 8, 10, 11, ou Server
- Python 3.8+ installé avec "Add Python to PATH" coché
- 500 MB d'espace disque libre

## Étape 1: Télécharger le repository

Allez sur: https://github.com/BeeKitchen7-hash/aeroget

Cliquez: `Code → Download ZIP`

Extrayez le dossier `aeroget-main` sur votre ordinateur.

## Étape 2: Ouvrir Command Prompt

1. Ouvrez l'Explorateur de fichiers
2. Allez dans le dossier `aeroget-main`
3. Clic droit → "Ouvrir le terminal ici" (ou "Open Command Prompt here" en anglais)

OU manuellement:
- Appuyez sur `Win + R`
- Tapez: `cmd`
- Appuyez sur Entrée
- Tapez: `cd chemin\vers\aeroget-main`

## Étape 3: Générer l'executable

Une fois dans le dossier `aeroget-main`, tapez:

```bash
build_exe.bat
```

Le script va:
1. ✅ Vérifier que Python est installé
2. ✅ Installer PyInstaller
3. ✅ Générer `aeroget.exe`
4. ✅ Afficher un message de succès

**Cela prend 1-2 minutes. Attendez que le message "OK" s'affiche!**

## Étape 4: Utiliser l'executable

Après la génération, vous verrez un dossier `dist`:

```
aeroget-main/
  ├── dist/
  │   └── aeroget.exe        ← VOTRE EXECUTABLE!
  ├── build/
  └── ...
```

### Option A: Lancer depuis le dossier

Double-cliquez sur `dist/aeroget.exe`

L'application se lance immédiatement! 🎉

### Option B: Copier partout

Vous pouvez copier `aeroget.exe` n'importe où:
- Sur le Bureau
- Dans un autre dossier
- L'envoyer à quelqu'un d'autre

Et le lancer en double-cliquant. Ça fonctionne partout!

### Option C: Créer un raccourci

1. Clic droit sur `dist/aeroget.exe`
2. "Envoyer vers → Bureau (créer un raccourci)"
3. Vous avez un raccourci sur le Bureau!

## ✅ C'est fini!

Vous pouvez maintenant:
- ✅ Lancer Aeroget en double-cliquant sur l'exe
- ✅ Mettre l'exe sur le Bureau
- ✅ L'envoyer à d'autres utilisateurs Windows
- ✅ Le placer où vous voulez

## 🐛 Résolution de problèmes

### "Python n'est pas installe"
→ Installez Python depuis https://www.python.org/downloads/
→ Cochez "Add Python to PATH" lors de l'installation
→ Redémarrez Windows

### "PyInstaller n'a pas pu être installé"
→ Vérifiez votre connexion internet
→ Essayez à nouveau le script `build_exe.bat`

### "L'executable refuse de se lancer"
→ Cela peut être un problème d'antivirus
→ Ajoutez `aeroget.exe` aux exceptions d'antivirus
→ Essayez de relancer

### "Erreur: File not found"
→ Assurez-vous que tous les fichiers Python (.py) sont dans le même dossier
→ N'effacez pas les fichiers originaux avant la génération

## 📝 Détails techniques

- **Fichier de configuration**: `aeroget.spec` (PyInstaller config)
- **Script de build**: `build_exe.bat` (lanceur automatique)
- **Taille du .exe**: ~80-120 MB (inclut Python et toutes les dépendances)
- **Dépendances incluses**: PyQt6, requests, beautifulsoup4, selenium, Pillow, lxml, psutil

## 🔄 Mettre à jour l'executable

Si vous téléchargez une nouvelle version:

1. Téléchargez le nouveau ZIP depuis GitHub
2. Extrayez-le dans un nouveau dossier
3. Lancez `build_exe.bat` à nouveau
4. Vous avez un nouvel `aeroget.exe` avec les dernières features!

## 📦 Partager l'executable

Vous pouvez envoyer uniquement le fichier `dist/aeroget.exe` à d'autres utilisateurs:
- Il fonctionne sur n'importe quel Windows 7+
- Aucune installation supplémentaire nécessaire
- L'autre personne double-clique et c'est tout!

---

**Besoin d'aide?** Consultez [README.md](README.md) ou [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md)
