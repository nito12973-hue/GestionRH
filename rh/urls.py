from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('', views.dashboard, name='dashboard'),
    
    path('departements/', views.departement_list, name='departement_list'),
    path('departements/ajouter/', views.departement_create, name='departement_create'),
    path('departements/<int:pk>/modifier/', views.departement_update, name='departement_update'),
    path('departements/<int:pk>/supprimer/', views.departement_delete, name='departement_delete'),
    
    path('employes/', views.employe_list, name='employe_list'),
    path('employes/<int:pk>/', views.employe_detail, name='employe_detail'),
    path('employes/ajouter/', views.employe_create, name='employe_create'),
    path('employes/<int:pk>/modifier/', views.employe_update, name='employe_update'),
    path('employes/<int:pk>/supprimer/', views.employe_delete, name='employe_delete'),
    
    path('contrats/', views.contrat_list, name='contrat_list'),
    path('contrats/ajouter/', views.contrat_create, name='contrat_create'),
    path('contrats/<int:pk>/modifier/', views.contrat_update, name='contrat_update'),
    path('contrats/<int:pk>/supprimer/', views.contrat_delete, name='contrat_delete'),
    
    path('export/employes/', views.export_employes_excel, name='export_employes_excel'),
    path('fiche-paie/<int:pk>/', views.fiche_paie_pdf, name='fiche_paie_pdf'),
]
