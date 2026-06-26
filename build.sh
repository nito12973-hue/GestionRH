#!/bin/bash

# Script de déploiement pour Render
# Exécute les migrations automatiquement

python manage.py migrate --noinput
python manage.py collectstatic --noinput
