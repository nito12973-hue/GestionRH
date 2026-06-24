from django import forms
from .models import Departement, Employe, Contrat


class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du département'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['matricule', 'nom', 'prenom', 'telephone', 'email', 'poste', 'date_embauche', 'departement']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MAT-001'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '06 00 00 00 00'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'poste': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poste'}),
            'date_embauche': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'departement': forms.Select(attrs={'class': 'form-select select2'}),
        }


class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = ['employe', 'type_contrat', 'date_debut', 'date_fin', 'salaire']
        widgets = {
            'employe': forms.Select(attrs={'class': 'form-select select2'}),
            'type_contrat': forms.Select(attrs={'class': 'form-select'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'salaire': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
