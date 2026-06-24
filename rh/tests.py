"""
Tests de l'application Gestion RH
"""
from django.test import TestCase
from .models import Departement, Employe, Contrat
from django.contrib.auth.models import User


class DepartementModelTest(TestCase):
    """Tests pour le modèle Departement"""
    
    def setUp(self):
        """Configuration des tests"""
        self.departement = Departement.objects.create(
            nom="Informatique",
            description="Département technique"
        )
    
    def test_creation_departement(self):
        """Test de création d'un département"""
        self.assertEqual(self.departement.nom, "Informatique")
        self.assertEqual(self.departement.description, "Département technique")
    
    def test_str_departement(self):
        """Test de la méthode __str__"""
        self.assertEqual(str(self.departement), "Informatique")
    
    def test_nombre_employes(self):
        """Test de la propriété nombre_employes"""
        self.assertEqual(self.departement.nombre_employes, 0)


class EmployeModelTest(TestCase):
    """Tests pour le modèle Employe"""
    
    def setUp(self):
        """Configuration des tests"""
        self.departement = Departement.objects.create(
            nom="Informatique",
            description="Département technique"
        )
        self.employe = Employe.objects.create(
            matricule="EMP001",
            nom="Dupont",
            prenom="Jean",
            date_naissance="1990-01-01",
            sexe="M",
            adresse="123 Rue de la Paix",
            telephone="06 12 34 56 78",
            email="jean.dupont@example.com",
            poste="Développeur",
            departement=self.departement
        )
    
    def test_creation_employe(self):
        """Test de création d'un employé"""
        self.assertEqual(self.employe.matricule, "EMP001")
        self.assertEqual(self.employe.nom, "Dupont")
        self.assertEqual(self.employe.prenom, "Jean")
    
    def test_str_employe(self):
        """Test de la méthode __str__"""
        expected = "EMP001 - Dupont Jean"
        self.assertEqual(str(self.employe), expected)
    
    def test_nom_complet(self):
        """Test de la propriété nom_complet"""
        self.assertEqual(self.employe.nom_complet, "Jean Dupont")
    
    def test_relation_departement(self):
        """Test de la relation avec le département"""
        self.assertEqual(self.employe.departement.nom, "Informatique")


class ContratModelTest(TestCase):
    """Tests pour le modèle Contrat"""
    
    def setUp(self):
        """Configuration des tests"""
        self.departement = Departement.objects.create(
            nom="Informatique",
            description="Département technique"
        )
        self.employe = Employe.objects.create(
            matricule="EMP001",
            nom="Dupont",
            prenom="Jean",
            date_naissance="1990-01-01",
            sexe="M",
            adresse="123 Rue de la Paix",
            telephone="06 12 34 56 78",
            email="jean.dupont@example.com",
            poste="Développeur",
            departement=self.departement
        )
        self.contrat = Contrat.objects.create(
            employe=self.employe,
            type_contrat="CDI",
            date_debut="2023-01-01",
            date_fin=None,
            salaire=3000.00
        )
    
    def test_creation_contrat(self):
        """Test de création d'un contrat"""
        self.assertEqual(self.contrat.type_contrat, "CDI")
        self.assertEqual(self.contrat.salaire, 3000.00)
    
    def test_str_contrat(self):
        """Test de la méthode __str__"""
        expected = "Jean Dupont - CDI - Contrat à Durée Indéterminée"
        self.assertEqual(str(self.contrat), expected)
    
    def test_relation_employe(self):
        """Test de la relation avec l'employé"""
        self.assertEqual(self.contrat.employe.nom_complet, "Jean Dupont")
    
    def test_duree_jours(self):
        """Test de la propriété duree_jours"""
        self.assertIsNone(self.contrat.duree_jours)
        
        # Test avec date de fin
        self.contrat.date_fin = "2023-12-31"
        self.contrat.save()
        self.assertEqual(self.contrat.duree_jours, 364)


class ViewTest(TestCase):
    """Tests pour les vues"""
    
    def setUp(self):
        """Configuration des tests"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.departement = Departement.objects.create(
            nom="Informatique",
            description="Département technique"
        )
    
    def test_login_view(self):
        """Test de la vue de connexion"""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_register_view(self):
        """Test de la vue d'inscription"""
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_redirect(self):
        """Test de la redirection vers le dashboard sans connexion"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/')
    
    def test_dashboard_with_login(self):
        """Test du dashboard avec connexion"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
