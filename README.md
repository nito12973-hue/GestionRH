# 🏢 Gestion RH - Système de Gestion des Ressources Humaines

Application web Django de gestion des ressources humaines avec une architecture simple et académique.

## 📋 Fonctionnalités

### Gestion des Employés
- ✅ Ajouter, modifier, supprimer des employés
- ✅ Liste des employés avec recherche et filtres
- ✅ Affichage détaillé avec contrats associés

### Gestion des Départements
- ✅ Ajouter, modifier, supprimer des départements
- ✅ Liste des départements avec nombre d'employés
- ✅ Affichage des employés par département

### Gestion des Contrats
- ✅ Ajouter, modifier, supprimer des contrats
- ✅ Liste des contrats avec recherche et filtres
- ✅ Types de contrats (CDI, CDD, Stage, Prestataire)

### Dashboard RH
- ✅ Statistiques en temps réel
- ✅ Graphiques Chart.js interactifs
- ✅ Employés par département
- ✅ Contrats par type
- ✅ Liste des employés récents

### Authentification
- ✅ Connexion/Inscription Django
- ✅ Protection des pages par login

## 🛠 Stack Technique

- **Backend**: Django 5
- **Base de données**: SQLite
- **Frontend**: Bootstrap 5
- **Graphiques**: Chart.js
- **Langage**: Python 3.10+

## 📁 Structure du Projet

```
GESTION-RH/
│
├── rh/                          # Application unique
│   ├── migrations/              # Migrations Django
│   ├── templates/               # Templates HTML
│   │   └── rh/                  # Templates de l'application
│   ├── static/                  # Fichiers statiques
│   │   ├── css/                 # CSS personnalisé
│   │   └── js/                  # JavaScript personnalisé
│   ├── __init__.py
│   ├── admin.py                 # Administration Django
│   ├── apps.py                  # Configuration de l'application
│   ├── forms.py                 # Formulaires Django
│   ├── models.py                # Modèles de données
│   ├── tests.py                 # Tests unitaires
│   ├── urls.py                  # URLs de l'application
│   └── views.py                 # Vues Django
│
├── config/                      # Configuration du projet
│   ├── __init__.py
│   ├── settings.py              # Paramètres Django
│   ├── urls.py                  # URLs principales
│   ├── asgi.py                  # Configuration ASGI
│   └── wsgi.py                  # Configuration WSGI
│
├── manage.py                    # Script de gestion Django
├── db.sqlite3                   # Base de données SQLite
├── requirements.txt             # Dépendances Python
└── README.md                    # Documentation
```

## 📦 Installation

### Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de packages Python)

### Étapes d'installation

1. **Créer un environnement virtuel**

```bash
python -m venv venv
```

2. **Activer l'environnement virtuel**

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Exécuter les migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Créer un superutilisateur**

```bash
python manage.py createsuperuser
```

6. **Lancer le serveur de développement**

```bash
python manage.py runserver
```

7. **Accéder à l'application**

Ouvrez votre navigateur et allez à : `http://127.0.0.1:8000`

## 🚀 Utilisation

### Première connexion

1. Allez sur `http://127.0.0.1:8000/login/`
2. Créez un compte ou connectez-vous avec le superutilisateur
3. Accédez au dashboard via `http://127.0.0.1:8000/`

### Créer des départements

1. Allez dans la section "Départements"
2. Cliquez sur "Ajouter un Département"
3. Remplissez le formulaire et sauvegardez

### Ajouter des employés

1. Allez dans la section "Employés"
2. Cliquez sur "Ajouter un Employé"
3. Remplissez tous les champs requis
4. Sélectionnez un département
5. Sauvegardez

### Créer des contrats

1. Allez dans la section "Contrats"
2. Cliquez sur "Ajouter un Contrat"
3. Sélectionnez un employé
4. Remplissez les informations du contrat
5. Sauvegardez

## 🧪 Tests

Pour exécuter les tests unitaires :

```bash
python manage.py test
```

## 📚 Modèles de Données

### Departement
- `nom` (CharField) : Nom du département
- `description` (TextField) : Description du département

### Employe
- `matricule` (CharField) : Matricule unique de l'employé
- `nom` (CharField) : Nom de l'employé
- `prenom` (CharField) : Prénom de l'employé
- `date_naissance` (DateField) : Date de naissance
- `sexe` (CharField) : Sexe (M/F)
- `adresse` (TextField) : Adresse
- `telephone` (CharField) : Téléphone
- `email` (EmailField) : Email
- `poste` (CharField) : Poste
- `date_embauche` (DateField) : Date d'embauche
- `departement` (ForeignKey) : Département

### Contrat
- `employe` (ForeignKey) : Employé associé
- `type_contrat` (CharField) : Type de contrat (CDI, CDD, Stage, Prestataire)
- `date_debut` (DateField) : Date de début
- `date_fin` (DateField) : Date de fin (optionnel pour CDI)
- `salaire` (DecimalField) : Salaire

## 🎨 Design

L'application utilise :
- **Bootstrap 5** pour le design responsive
- **Chart.js** pour les graphiques statistiques
- **Bootstrap Icons** pour les icônes
- **CSS personnalisé** pour le style moderne
- **JavaScript personnalisé** pour l'interactivité

## 🔧 Commandes Django utiles

```bash
# Lancer le serveur
python manage.py runserver

# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Ouvrir le shell Django
python manage.py shell

# Exécuter les tests
python manage.py test

# Accéder à l'administration
python manage.py runserver
# Puis aller sur http://127.0.0.1:8000/admin/
```

## 📝 Notes

- L'application utilise SQLite comme base de données par défaut
- Pour utiliser PostgreSQL, modifiez `config/settings.py`
- Le code est commenté et suit les bonnes pratiques Django
- Structure simple adaptée aux projets académiques

## 🤝 Contribution

Ce projet est destiné à un usage académique. N'hésitez pas à l'améliorer et à l'adapter selon vos besoins.

## 📄 Licence

Ce projet est fourni à des fins éducatives.

---

**Version**: 1.0.0  
**Django**: 5.0.1  
**Python**: 3.10+
