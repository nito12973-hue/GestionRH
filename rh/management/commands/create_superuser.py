from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Crée un superutilisateur automatiquement si aucun existe'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superutilisateur "{username}" créé avec succès!'))
            self.stdout.write(self.style.WARNING(f'Username: {username}'))
            self.stdout.write(self.style.WARNING(f'Password: {password}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superutilisateur "{username}" existe déjà.'))
