# 🎯 SimpleAutomation

Un script simple pour automatiser rapidement des tâches (souris, clavier, ...) sur son ordinateur (utilisation CLI).

---

## 📦 Installation

Commencez par cloner le dépôt, installer les dépendances et initialiser les répertoires :

```bash
# Clonez le dépôt
git clone https://github.com/alexandrecmpgn/SimpleAutomation
cd SimpleAutomation/

# Installez les dépendances
pip3 install -r requirements.txt

# Initialisez les répertoires
python3 init.py
```

## ⚙️ Utilisation

Commencez par mettre en place une touche d'arrêt. C'est une touche qui servira à arrêter l'enregistrement des actions (par exemple la touche Esc | Échap est une bonne idée.)

```bash
python3 save_stop_key.py
```

Les actions sont enregistrées sous forme de sessions (sauvegardées dans PATH_SESSIONS). 
Pour créer une nouvelle session, exécutez recorder.py : 

```bash 
python3 recorder.py
```

Le script vous demandera un nom de session et vous pourrez enregistrer les actions (la touche d'arrêt est celle définie avec save_stop_key.py).

Enfin, pour lancer l'exécution d'une session, exécutez player.py

```bash
python3 player.py
```

Le nom de la session vous sera demandé. Un décompte de 5 secondes aura lieu avant l'exécution de l'entièreté des actions.

Pour nettoyer l'ensemble des données (sessions, stop_key, ...), utilisez le script clean.py

```bash
python3 clean.py
```
