# Guide d'installation pour l'acheteur

## 🚀 Déploiement sur Render (Gratuit)

### Étape 1: Créer un compte Render
1. Allez sur https://render.com
2. Créez un compte gratuit

### Étape 2: Connecter le repository
1. Cliquez sur "New +" → "Web Service"
2. Connectez votre compte GitHub
3. Sélectionnez le repository du projet

### Étape 3: Configurer les identifiants admin

**IMPORTANT:** Avant de cliquer sur "Create Web Service", configurez vos identifiants.

**⚠️ IMPORTANT: Choisissez "Environment" (pas "Environment Group")**

Sur Render, vous verrez plusieurs options:
- ✅ **Environment** ← CHOISISSEZ CELUI-CI (simple, pour un seul service)
- ❌ Linked Environment Group (pour plusieurs services liés)
- ❌ Create Environment Group (pour créer un groupe)

**Méthode simple (recommandée):**

1. Dans la section "Environment" (pas "Environment Group"), cliquez sur "Add Environment Variable"
2. Ajoutez les variables une par une:

| Variable | Valeur par défaut | Votre valeur |
|----------|------------------|--------------|
| `DJANGO_SUPERUSER_USERNAME` | `admin` | Votre nom d'utilisateur |
| `DJANGO_SUPERUSER_PASSWORD` | `admin123456` | **CHANGEZ CECI!** Votre mot de passe |
| `DJANGO_SUPERUSER_EMAIL` | `admin@example.com` | Votre email |

**Exemple:**
- Variable: `DJANGO_SUPERUSER_USERNAME` → Valeur: `jean.dupont`
- Variable: `DJANGO_SUPERUSER_PASSWORD` → Valeur: `MonMotDePasseSecure123!`
- Variable: `DJANGO_SUPERUSER_EMAIL` → Valeur: `jean.dupont@entreprise.com`

**Note:** Les autres variables (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL) sont configurées automatiquement par Render via `render.yaml`. Vous n'avez pas besoin de les modifier.

### Étape 4: Lancer le déploiement
1. Cliquez sur "Create Web Service"
2. Attendez 3-5 minutes
3. Votre site sera accessible sur l'URL fournie par Render

### Étape 5: Vérifier les identifiants
1. Allez dans l'onglet "Logs" de votre service
2. Vous verrez un message comme:
   ```
   ============================================================
   SUPERUTILISATEUR CRÉÉ AVEC SUCCÈS!
   ============================================================
   Username: jean.dupont
   Password: MonMotDePasseSecure123!
   Email: jean.dupont@entreprise.com
   ============================================================
   ```

### Étape 6: Se connecter
1. Allez sur l'URL de votre site
2. Connectez-vous avec vos identifiants
3. Vous êtes maintenant administrateur!

---

## 🔐 Changer le mot de passe après déploiement

Si vous voulez changer le mot de passe après le déploiement:

### Option 1: Via Render Dashboard (Simple)

1. Allez sur votre service Render
2. Cliquez sur l'onglet "Environment"
3. Cliquez sur "Add Environment Variable"
4. Modifiez `DJANGO_SUPERUSER_PASSWORD` avec votre nouveau mot de passe
5. Cliquez sur "Save Changes"
6. Render redéployera automatiquement votre application

### Option 2: Via l'application Django
1. Connectez-vous avec l'ancien mot de passe
2. Allez dans l'admin Django (`/admin/`)
3. Changez le mot de passe de l'utilisateur admin

---

## 📝 Variables d'environnement disponibles

| Variable | Description |
|----------|-------------|
| `DJANGO_SUPERUSER_USERNAME` | Nom d'utilisateur admin |
| `DJANGO_SUPERUSER_PASSWORD` | Mot de passe admin |
| `DJANGO_SUPERUSER_EMAIL` | Email de l'admin |
| `SECRET_KEY` | Clé secrète Django (générée automatiquement) |
| `DEBUG` | Mode debug (False en production) |
| `ALLOWED_HOSTS` | Hôtes autorisés |
| `DATABASE_URL` | URL de la base de données (générée automatiquement) |

---

## 🎯 Personnalisation avancée

### Changer le nom de l'application
Modifiez les variables dans Render:
- `ALLOWED_HOSTS`: votre-domaine.com

### Changer la base de données
Render utilise PostgreSQL par défaut. La base de données est créée automatiquement.

---

## 💡 Conseils de sécurité

1. **TOUJOURS** changer le mot de passe par défaut
2. Utilisez un mot de passe fort (min 12 caractères, majuscules, minuscules, chiffres, caractères spéciaux)
3. Ne partagez jamais vos identifiants
4. Changez régulièrement votre mot de passe

---

## 🆘 Support

Si vous avez des problèmes:
1. Vérifiez les logs Render
2. Vérifiez que toutes les variables d'environnement sont configurées
3. Assurez-vous que le déploiement est terminé avant de vous connecter
