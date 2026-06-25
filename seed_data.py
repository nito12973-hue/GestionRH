import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from rh.models import Departement, Employe, Contrat

# Nettoyer les données existantes
print("Nettoyage des données existantes...")
Contrat.objects.all().delete()
Employe.objects.all().delete()
Departement.objects.all().delete()

# Créer 5 départements
departements_data = [
    {"nom": "Ressources Humaines", "description": "Gestion du personnel et recrutement"},
    {"nom": "Informatique", "description": "Développement et maintenance des systèmes"},
    {"nom": "Marketing", "description": "Stratégie marketing et communication"},
    {"nom": "Finance", "description": "Gestion financière et comptabilité"},
    {"nom": "Production", "description": "Fabrication et logistique"},
]

print("Création des départements...")
departements = []
for dept_data in departements_data:
    dept = Departement.objects.create(**dept_data)
    departements.append(dept)
    print(f"  - {dept.nom}")

# Créer 20 employés
prenoms = ["Jean", "Marie", "Pierre", "Sophie", "Luc", "Emma", "Thomas", "Camille", "Hugo", "Léa", 
           "Antoine", "Chloé", "Maxime", "Julie", "Nicolas", "Sarah", "Alexandre", "Manon", "Romain", "Laura"]
noms = ["Dupont", "Martin", "Bernard", "Petit", "Robert", "Richard", "Durand", "Moreau", "Simon", "Laurent",
        "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier", "Morel", "Girard"]
postes = ["Développeur", "Chef de projet", "Analyste", "Designer", "Comptable", "Responsable RH", 
          "Commercial", "Ingénieur", "Technicien", "Manager"]

print("Création des employés...")
employes = []
for i in range(20):
    matricule = f"EMP-{i+1:03d}"
    nom = random.choice(noms)
    prenom = random.choice(prenoms)
    telephone = f"06{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(10, 99)}"
    email = f"{prenom.lower()}.{nom.lower()}@entreprise.com"
    poste = random.choice(postes)
    date_embauche = datetime.now() - timedelta(days=random.randint(30, 1825))
    departement = random.choice(departements)
    
    employe = Employe.objects.create(
        matricule=matricule,
        nom=nom,
        prenom=prenom,
        telephone=telephone,
        email=email,
        poste=poste,
        date_embauche=date_embauche,
        departement=departement
    )
    employes.append(employe)
    print(f"  - {matricule}: {prenom} {nom} ({poste})")

# Créer 30 contrats
types_contrat = ['CDI', 'CDD', 'STAGE']

print("Création des contrats...")
for i in range(30):
    employe = random.choice(employes)
    type_contrat = random.choice(types_contrat)
    date_debut = employe.date_embauche + timedelta(days=random.randint(0, 30))
    
    if type_contrat == 'CDD':
        duree = random.randint(6, 24)
        date_fin = date_debut + timedelta(days=duree * 30)
    elif type_contrat == 'STAGE':
        duree = random.randint(2, 6)
        date_fin = date_debut + timedelta(days=duree * 30)
    else:
        date_fin = None
    
    salaire = random.randint(2000, 8000) + random.randint(0, 99) / 100
    
    contrat = Contrat.objects.create(
        employe=employe,
        type_contrat=type_contrat,
        date_debut=date_debut,
        date_fin=date_fin,
        salaire=salaire
    )
    print(f"  - Contrat {i+1}: {employe.prenom} {employe.nom} - {type_contrat} - {salaire}€")

print("\n✅ Insertion terminée !")
print(f"📊 Résumé:")
print(f"   - Départements: {Departement.objects.count()}")
print(f"   - Employés: {Employe.objects.count()}")
print(f"   - Contrats: {Contrat.objects.count()}")
