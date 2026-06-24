from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Departement, Employe, Contrat
from .forms import DepartementForm, EmployeForm, ContratForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue, {username} !")
                return redirect('dashboard')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec succès !")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('login')

@login_required
def dashboard(request):
    total_employes = Employe.objects.count()
    total_departements = Departement.objects.count()
    total_contrats = Contrat.objects.count()
    context = {
        'total_employes': total_employes,
        'total_departements': total_departements,
        'total_contrats': total_contrats,
    }
    return render(request, 'dashboard.html', context)

# Départements
@login_required
def departement_list(request):
    departements = Departement.objects.all()
    return render(request, 'departements.html', {'departements': departements})

@login_required
def departement_create(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Département ajouté avec succès.")
            return redirect('departement_list')
    else:
        form = DepartementForm()
    return render(request, 'departement_ajouter.html', {'form': form})

@login_required
def departement_update(request, pk):
    departement = get_object_or_404(Departement, pk=pk)
    if request.method == 'POST':
        form = DepartementForm(request.POST, instance=departement)
        if form.is_valid():
            form.save()
            messages.success(request, "Département modifié avec succès.")
            return redirect('departement_list')
    else:
        form = DepartementForm(instance=departement)
    return render(request, 'departement_modifier.html', {'form': form, 'departement': departement})

@login_required
def departement_delete(request, pk):
    departement = get_object_or_404(Departement, pk=pk)
    if request.method == 'POST':
        departement.delete()
        messages.success(request, "Département supprimé.")
        return redirect('departement_list')
    return render(request, 'departement_supprimer.html', {'departement': departement})

# Employés
@login_required
def employe_list(request):
    employes = Employe.objects.all()
    return render(request, 'employes.html', {'employes': employes})

@login_required
def employe_create(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employé ajouté avec succès.")
            return redirect('employe_list')
    else:
        form = EmployeForm()
    return render(request, 'employe_ajouter.html', {'form': form})

@login_required
def employe_update(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            messages.success(request, "Employé modifié avec succès.")
            return redirect('employe_list')
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'employe_modifier.html', {'form': form, 'employe': employe})

@login_required
def employe_delete(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employe.delete()
        messages.success(request, "Employé supprimé.")
        return redirect('employe_list')
    return render(request, 'employe_supprimer.html', {'employe': employe})

# Contrats
@login_required
def contrat_list(request):
    contrats = Contrat.objects.all()
    return render(request, 'contrats.html', {'contrats': contrats})

@login_required
def contrat_create(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contrat ajouté avec succès.")
            return redirect('contrat_list')
    else:
        form = ContratForm()
    return render(request, 'contrat_ajouter.html', {'form': form})

@login_required
def contrat_update(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    if request.method == 'POST':
        form = ContratForm(request.POST, instance=contrat)
        if form.is_valid():
            form.save()
            messages.success(request, "Contrat modifié avec succès.")
            return redirect('contrat_list')
    else:
        form = ContratForm(instance=contrat)
    return render(request, 'contrat_modifier.html', {'form': form, 'contrat': contrat})

@login_required
def contrat_delete(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    if request.method == 'POST':
        contrat.delete()
        messages.success(request, "Contrat supprimé.")
        return redirect('contrat_list')
    return render(request, 'contrat_supprimer.html', {'contrat': contrat})