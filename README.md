# 🎯 Gestion RH - Application Django Professionnelle

Application de gestion des ressources humaines avec design moderne et animations professionnelles.

## ✨ Caractéristiques

- 🎨 **Design WAOUH** avec animations et effets visuels premium
- 📊 **Dashboard interactif** avec graphiques Chart.js
- 🔍 **Recherche et pagination** pour les employés
- 🚀 **Déploiement automatique** sur Render (gratuit)
- 🔐 **Authentification sécurisée** avec Django
- 📱 **Responsive** - fonctionne sur tous les appareils
- 🌈 **Thème sombre** avec couleurs néon
- ✨ **Animations AOS** au scroll
- 🖱️ **Curseur personnalisé** (desktop)
- 🫧 **Effets blobs** animés en arrière-plan

## 🚀 Déploiement rapide sur Render

### Pour les acheteurs

Voir le guide complet: **[README_ACHETEUR.md](README_ACHETEUR.md)**

### Résumé rapide

1. Créez un compte sur https://render.com
2. Connectez votre repository GitHub
3. Configurez vos identifiants admin dans les variables d'environnement:
   - `DJANGO_SUPERUSER_USERNAME` = votre username
   - `DJANGO_SUPERUSER_PASSWORD` = votre mot de passe
   - `DJANGO_SUPERUSER_EMAIL` = votre email
4. Cliquez sur "Create Web Service"
5. Attendez 3-5 minutes
6. Connectez-vous avec vos identifiants

## 📋 Fonctionnalités

### Gestion des employés
- Liste des employés avec pagination (10 par page)
- Recherche par matricule, nom, prénom, poste
- Création, modification, suppression d'employés
- Page de détail pour chaque employé

### Gestion des départements
- CRUD complet des départements
- Association avec les employés

### Gestion des contrats
- Types de contrats: CDI, CDD, STAGE
- Dates de début et fin
- Gestion des salaires

### Dashboard
- Statistiques en temps réel
- Graphiques de répartition (départements, contrats)
- Derniers employés ajoutés
- Compteurs animés

## 🛠️ Stack technique

- **Backend:** Django 6.0.6
- **Base de données:** PostgreSQL
- **Frontend:** Bootstrap 5, Bootstrap Icons
- **Graphiques:** Chart.js
- **Animations:** AOS.js
- **Déploiement:** Render (gratuit)
- **Serveur:** Gunicorn

## 📁 Structure du projet

```
GESTION-RH/
├── config/              # Configuration Django
├── rh/                  # Application principale
│   ├── management/      # Commandes personnalisées
│   ├── models.py        # Modèles de données
│   ├── views.py         # Vues
│   ├── templates/       # Templates HTML
│   └── static/          # CSS, JS, images
├── render.yaml          # Configuration Render
├── runtime.txt          # Version Python
├── requirements.txt     # Dépendances
├── README_ACHETEUR.md   # Guide pour les acheteurs
├── GUIDE_ADMIN.md       # Guide de configuration admin
└── seed_data.py         # Script de données de test
```

## 🔧 Installation locale

### Prérequis
- Python 3.11+
- PostgreSQL (optionnel, SQLite par défaut)

### Étapes

1. Cloner le repository
```bash
git clone https://github.com/nito12973-hue/GestionRH.git
cd GESTION-RH
```

2. Créer un environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Configurer la base de données
```bash
python manage.py migrate
```

5. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

6. Lancer le serveur
```bash
python manage.py runserver
```

7. Accéder à l'application
```
http://127.0.0.1:8000
```

## 📝 Données de test

Pour ajouter des données de test (20 employés, 30 contrats, 5 départements):

```bash
python seed_data.py
```

## 🔐 Configuration admin

Pour personnaliser les identifiants admin avant le déploiement, voir:
**[GUIDE_ADMIN.md](GUIDE_ADMIN.md)**

## 🎨 Personnalisation

### Changer les couleurs
Modifiez les variables CSS dans `rh/static/css/style.css`:
```css
:root {
    --neon-cyan: #00f5d4;
    --neon-violet: #9b5de5;
    --neon-bleu: #00bbf9;
    --neon-rose: #f15bb5;
    --neon-or: #fee440;
}
```

### Changer le nombre d'éléments par page
Modifiez `rh/views.py`:
```python
paginator = Paginator(employes_queryset, 10)  # Changez 10 par votre nombre
```

## 📄 Licence

Ce projet est vendu tel quel. L'acheteur a le droit de:
- Utiliser l'application pour son entreprise
- Modifier le code selon ses besoins
- Déployer sur n'importe quel serveur

## 🆘 Support

Pour toute question sur l'installation ou la configuration:
- Consultez [README_ACHETEUR.md](README_ACHETEUR.md)
- Consultez [GUIDE_ADMIN.md](GUIDE_ADMIN.md)

## 🎯 Pour les vendeurs

Ce projet est prêt à être vendu avec:
- ✅ Documentation complète
- ✅ Déploiement automatique
- ✅ Design professionnel
- ✅ Fonctionnalités complètes
- ✅ Guide pour les acheteurs

---

**Version:** 1.0.0  
**Dernière mise à jour:** Juin 2026
