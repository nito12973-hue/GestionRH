from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg, Count, Q
from django.http import HttpResponse, JsonResponse
from openpyxl import Workbook
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string
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
    
    # Nouvelles statistiques
    salaire_moyen = Contrat.objects.aggregate(Avg('salaire'))['salaire__avg'] or 0
    derniers_employes = Employe.objects.select_related('departement').order_by('-date_embauche')[:5]
    
    # Répartition par département
    employes_par_dept = []
    for dept in Departement.objects.annotate(count=Count('employe')):
        if dept.count > 0:
            employes_par_dept.append({'nom': dept.nom, 'count': dept.count})
    
    # Répartition par type de contrat
    contrats_par_type = []
    for type_contrat, label in Contrat.TYPE_CONTRAT:
        count = Contrat.objects.filter(type_contrat=type_contrat).count()
        contrats_par_type.append({'label': label, 'count': count})
    
    context = {
        'total_employes': total_employes,
        'total_departements': total_departements,
        'total_contrats': total_contrats,
        'salaire_moyen': salaire_moyen,
        'derniers_employes': derniers_employes,
        'employes_par_dept': employes_par_dept,
        'contrats_par_type': contrats_par_type,
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
    employes_queryset = Employe.objects.select_related('departement').prefetch_related('contrat_set').all()
    
    # Recherche
    recherche = request.GET.get('recherche', '')
    if recherche:
        employes_queryset = employes_queryset.filter(
            Q(nom__icontains=recherche) |
            Q(prenom__icontains=recherche) |
            Q(matricule__icontains=recherche) |
            Q(poste__icontains=recherche)
        )
    
    # Filtre par département
    departement_id = request.GET.get('departement', '')
    if departement_id:
        employes_queryset = employes_queryset.filter(departement_id=departement_id)
    
    # Filtre par type de contrat
    type_contrat = request.GET.get('type_contrat', '')
    if type_contrat:
        employes_queryset = employes_queryset.filter(contrat__type_contrat=type_contrat)
    
    # Pagination (10 employés par page)
    paginator = Paginator(employes_queryset.order_by('id'), 10)
    page_number = request.GET.get('page', 1)
    employes = paginator.get_page(page_number)
    
    return render(request, 'employes.html', {
        'employes': employes,
        'recherche': recherche,
        'departements': Departement.objects.all(),
        'type_contrat': type_contrat
    })

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

@login_required
def employe_detail(request, pk):
    employe = get_object_or_404(Employe.objects.select_related('departement'), pk=pk)
    contrat = employe.contrat_set.first()
    return render(request, 'employe_detail.html', {
        'employe': employe,
        'contrat': contrat
    })

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

# Export Excel
@login_required
def export_employes_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Employés"
    
    headers = ['Matricule', 'Nom', 'Prénom', 'Email', 'Téléphone', 'Poste', 'Département', 'Date embauche']
    ws.append(headers)
    
    for employe in Employe.objects.select_related('departement').all():
        ws.append([
            employe.matricule,
            employe.nom,
            employe.prenom,
            employe.email,
            employe.telephone,
            employe.poste,
            employe.departement.nom,
            employe.date_embauche.strftime('%d/%m/%Y')
        ])
    
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=employes.xlsx'
    wb.save(response)
    return response

# Fiche de paie PDF
@login_required
def fiche_paie_pdf(request, pk):
    employe = get_object_or_404(Employe.objects.select_related('departement'), pk=pk)
    contrat = employe.contrat_set.first()
    
    if not contrat:
        messages.error(request, "Aucun contrat trouvé pour cet employé.")
        return redirect('employe_detail', pk=pk)
    
    html = render_to_string('fiche_paie_template.html', {
        'employe': employe,
        'contrat': contrat
    })
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=fiche_paie_{employe.matricule}.pdf'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF')
    
    return response