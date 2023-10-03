# Assistant Vocal Python sur Linux

## Description

Un assistant vocal construit en utilisant Python, destiné à être utilisé sur des systèmes Linux. Ce projet vise à créer un assistant capable d'écouter les commandes vocales, de les interpréter, et d'exécuter les actions demandées par l'utilisateur, tout en fournissant un retour vocal.

## Fonctionnalités

- Reconnaissance vocale pour convertir la parole en texte.
- Traitement du langage naturel pour comprendre les commandes de l'utilisateur.
- Exécution automatisée des commandes système.
- Synthèse vocale pour communiquer verbalement avec l'utilisateur.
- (Optionnel) Interface utilisateur graphique pour une interaction supplémentaire.

## Technologies Utilisées

- **Python:** Langage de programmation principal du projet.
- **SpeechRecognition:** Pour la reconnaissance vocale.
- **nltk/spaCy:** Pour le traitement du langage naturel.
- **subprocess:** Pour exécuter des commandes système.
- **gTTS/pyttsx3:** Pour la synthèse vocale.
- **Tkinter/PyQt/Kivy:** Pour le développement de l'interface utilisateur (si implémenté).

## Installation et Utilisation

```bash
pip install -r requirements.txt
python main.py

### Prérequis

- Python 3.x
- Un environnement virtuel (optionnel, mais recommandé)

### Installation

Clonez ce dépôt et naviguez dans le dossier du projet.

```bash
git clone [Your Repository Link]
cd [Your Repository Name]