# DemoApp - Application WPF .NET 8

Application de démonstration pour le déploiement avec InnoSetup.

## 🚀 Compilation

```bash
# Restaurer les dépendances
dotnet restore

# Compiler en mode Debug
dotnet build

# Compiler en mode Release
dotnet build -c Release

# Publier l'application
dotnet publish -c Release -r win-x64 --self-contained false
```

## 📦 Créer l'installeur avec InnoSetup

1. Installez InnoSetup depuis https://jrsoftware.org/isinfo.php
2. Ouvrez le fichier `setup.iss` avec InnoSetup Compiler
3. Cliquez sur "Compile" (ou appuyez sur F9)
4. L'installeur sera créé dans le dossier `Setup/`

## 📋 Prérequis

- .NET 8.0 SDK pour la compilation
- .NET 8.0 Desktop Runtime pour l'exécution
- InnoSetup pour créer l'installeur

## 📝 Structure du projet

```
DemoApp/
├── DemoApp.csproj          # Fichier de projet
├── App.xaml                # Application XAML
├── App.xaml.cs             # Code-behind de l'application
├── MainWindow.xaml         # Fenêtre principale XAML
├── MainWindow.xaml.cs      # Code-behind de la fenêtre
├── LICENSE.txt             # Licence
├── setup.iss               # Script InnoSetup
└── README.md               # Ce fichier
```

## ✨ Fonctionnalités

- Interface WPF moderne
- Pas de base de données (application autonome)
- Affichage d'informations système
- Compteur d'interactions
- Prête pour le déploiement

## 📄 Licence

MIT License - Voir LICENSE.txt
