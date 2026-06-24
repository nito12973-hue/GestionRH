from django.contrib import admin
from .models import Departement, Employe, Contrat


@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom', 'description')
    ordering = ('nom',)


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom', 'departement', 'poste', 'date_embauche')
    list_filter = ('departement', 'date_embauche')
    search_fields = ('matricule', 'nom', 'prenom', 'email', 'telephone')
    ordering = ('nom', 'prenom')


@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ('employe', 'type_contrat', 'date_debut', 'date_fin', 'salaire')
    list_filter = ('type_contrat', 'date_debut', 'date_fin')
    search_fields = ('employe__nom', 'employe__prenom', 'employe__matricule')
    ordering = ('-date_debut',)
