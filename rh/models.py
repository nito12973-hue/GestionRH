from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Employe(models.Model):
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    poste = models.CharField(max_length=100)
    date_embauche = models.DateField()
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.matricule} - {self.nom} {self.prenom}"

class Contrat(models.Model):
    TYPE_CONTRAT = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('STAGE', 'Stage'),
    ]

    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    type_contrat = models.CharField(max_length=20, choices=TYPE_CONTRAT)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employe} - {self.type_contrat}"