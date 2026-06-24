/**
 * GESTION RH — Script Principal JavaScript
 * Gère : chargeur de page, barre latérale, animations, thème sombre
 */

/* ── Chargeur de page (Preloader) ── */
document.addEventListener('DOMContentLoaded', () => {
  const chargeur = document.getElementById('chargeur');
  if (chargeur) {
    // Masquer le chargeur après le chargement complet
    window.addEventListener('load', () => {
      setTimeout(() => {
        chargeur.classList.add('cache');
        // Supprimer du DOM après la transition
        setTimeout(() => chargeur.remove(), 600);
      }, 300);
    });
    // Sécurité : masquer après 3 secondes max
    setTimeout(() => {
      if (chargeur) {
        chargeur.classList.add('cache');
        setTimeout(() => chargeur.remove(), 600);
      }
    }, 3000);
  }
});


document.addEventListener('DOMContentLoaded', () => {
  const boutonMenu = document.getElementById('bouton-menu-mobile');
  const barreLatérale = document.getElementById('barre-laterale');

  if (boutonMenu && barreLatérale) {
    boutonMenu.addEventListener('click', () => {
      barreLatérale.classList.toggle('visible');
    });

    document.addEventListener('click', (e) => {
      if (!barreLatérale.contains(e.target) && !boutonMenu.contains(e.target)) {
        barreLatérale.classList.remove('visible');
      }
    });
  }
});


document.addEventListener('DOMContentLoaded', () => {
  const alertes = document.querySelectorAll('.alerte-auto-fermeture, .alert');
  alertes.forEach(alerte => {
    setTimeout(() => {
      alerte.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      alerte.style.opacity = '0';
      alerte.style.transform = 'translateY(-10px)';
      setTimeout(() => alerte.remove(), 500);
    }, 5000);
  });
});

/* ── Lien actif dans la barre latérale ── */
document.addEventListener('DOMContentLoaded', () => {
  const cheminActuel = window.location.pathname;
  const liensNav = document.querySelectorAll('.lien-sidebar');

  liensNav.forEach(lien => {
    const href = lien.getAttribute('href');
    if (href && cheminActuel.includes(href) && href !== '/') {
      lien.classList.add('actif');
    }
  });
});

/* ── Animation d'apparition des cartes ── */
document.addEventListener('DOMContentLoaded', () => {
  const cartes = document.querySelectorAll('.carte, .card, .carte-statistique');
  if ('IntersectionObserver' in window) {
    const observateur = new IntersectionObserver((entrees) => {
      entrees.forEach((entree, index) => {
        if (entree.isIntersecting) {
          setTimeout(() => {
            entree.target.style.opacity = '1';
            entree.target.style.transform = 'translateY(0)';
          }, index * 80);
          observateur.unobserve(entree.target);
        }
      });
    }, { threshold: 0.1 });

    cartes.forEach(carte => {
      carte.style.opacity = '0';
      carte.style.transform = 'translateY(16px)';
      carte.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
      observateur.observe(carte);
    });
  }
});

/* ── Compteurs animés pour les statistiques ── */
function animerCompteur(element, cible, duree = 1200) {
  const debut = 0;
  const pasDeTemps = 16;
  const totalPas = duree / pasDeTemps;
  const incrementPas = (cible - debut) / totalPas;
  let valeurActuelle = debut;
  let pas = 0;

  const minuterie = setInterval(() => {
    pas++;
    valeurActuelle += incrementPas;
    if (pas >= totalPas) {
      element.textContent = cible;
      clearInterval(minuterie);
    } else {
      element.textContent = Math.round(valeurActuelle);
    }
  }, pasDeTemps);
}

document.addEventListener('DOMContentLoaded', () => {
  const valeursStats = document.querySelectorAll('.valeur-stat[data-cible]');
  valeursStats.forEach(el => {
    const cible = parseInt(el.getAttribute('data-cible'), 10);
    if (!isNaN(cible)) {
      animerCompteur(el, cible);
    }
  });
});

/* ── Confirmation de suppression ── */
document.addEventListener('DOMContentLoaded', () => {
  const formulairesSuppression = document.querySelectorAll('.formulaire-suppression');
  formulairesSuppression.forEach(form => {
    form.addEventListener('submit', (e) => {
      const confirmé = confirm('Êtes-vous sûr de vouloir supprimer cet élément ? Cette action est irréversible.');
      if (!confirmé) e.preventDefault();
    });
  });
});

/* ── Tooltip Bootstrap ── */
document.addEventListener('DOMContentLoaded', () => {
  const élémentsTip = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  élémentsTip.map(el => new bootstrap.Tooltip(el));
});
