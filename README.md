# Simulateur de Moyenne

## Description

Cette application permet de calculer la moyenne nécessaire au 3e trimestre pour atteindre une moyenne annuelle souhaitée. Elle prend en compte les notes et coefficients des différentes matières et propose des suggestions pour améliorer les matières non notées.

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/simulateur_moyenne.git
   cd simulateur_moyenne
   ```

2. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Lancer l'application :**
   ```bash
   python main.py
   ```

2. **Fonctionnalités principales :**
   - Saisie des notes et coefficients.
   - Calcul de la moyenne nécessaire au 3e trimestre.
   - Suggestions pour améliorer les matières non notées.
   - Exportation des résultats en fichier texte.

## Fonctionnalités

- **Interface utilisateur :** Une interface graphique intuitive pour saisir les données et afficher les résultats.
- **Calculs précis :** Prend en compte les coefficients pour chaque matière.
- **Exportation :** Permet d'exporter les résultats dans un fichier texte pour une consultation ultérieure.

## Structure du Projet

```
simulateur_moyenne/
├── main.py          # Point d'entrée principal de l'application
├── calculs.py       # Contient les fonctions de calcul et d'exportation
├── README.md        # Documentation du projet
├── requirements.txt # Liste des dépendances Python
├── resultats.txt    # Exemple de fichier exporté
├── assets/          # Contient les ressources (icônes, images, etc.)
└── utils/           # Contient les utilitaires supplémentaires
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour proposer des améliorations.

## Licence

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT).
