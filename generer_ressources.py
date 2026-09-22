# ============================================================
# Générateur automatique des ressources pédagogiques
# Dépôt : OFPPT · ISMO · Développement Digital
# Créateur : KELLOUCH Mahdi
# ============================================================
# Ce script génère :
#   1. Les fichiers index.html (site web GitHub Pages)
#   2. Les fichiers README.md (documentation GitHub)
#
# À partir d'une configuration centralisée (voir CONFIG ci-dessous).
#
# Nécessite : Python 3.8+
# Aucune dépendance externe.
# ============================================================

import os
import re
from pathlib import Path
from datetime import datetime


# ============================================================
# CONFIGURATION CENTRALISÉE
# ============================================================
CONFIG = {
    # ---------- Identité du créateur ----------
    "createur": "KELLOUCH Mahdi",
    "role_createur": "Formateur en Développement Digital",
    "email": "mahdi.kellouch@ofppt-edu.ma",

    # ---------- Établissement ----------
    "etablissement": "ISMO",
    "etablissement_complet": "Institut Spécialisé de Management et d'Informatique",
    "ville": "Casablanca",

    # ---------- Organisme ----------
    "organisme": "OFPPT",
    "organisme_complet": "Office de la Formation Professionnelle et de la Promotion du Travail",
    "ministere": "Ministère de l'Inclusion Économique, de la Petite Entreprise, de l'Emploi et des Compétences",
    "royaume": "Royaume du Maroc",

    # ---------- Formation ----------
    "filiere": "Développement Digital",
    "niveau": "1ère année (tronc commun)",
    "annee_formation": "2025 – 2026",

    # ---------- Dépôt GitHub ----------
    "organisation_github": "ismO-ofppt",
    "nom_depot_github": "ressources-dev-digital",

    # ---------- Style ----------
    "couleur_principale": "#1d5e36",
    "couleur_secondaire": "#2e8b57",
    "couleur_claire": "#d4ecd9",
}


# ============================================================
# DÉFINITION DES MODULES
# ============================================================
MODULES = [
    {
        "code": "M101",
        "dossier": "M101-Metier-Formation",
        "titre": "Métier & Formation",
        "titre_complet": "Se situer au regard du métier et de la démarche de formation",
        "description": "Découvrir le métier de développeur digital, le programme de formation et le règlement intérieur de l'OFPPT.",
        "duree": "15 h",
        "icone": "🎯",
        "objectifs": [
            "Décrire les métiers du Développement Digital et leurs options",
            "Identifier les compétences et aptitudes requises",
            "Comprendre le programme de formation sur 2 ans",
            "Connaître le mode d'évaluation et les règles d'assiduité",
            "Se situer dans le cadre institutionnel de l'OFPPT",
        ],
        "prerequis": "Aucun",
        "niveau": "Débutant",
    },
    {
        "code": "M104",
        "dossier": "M104-Sites-Web-Statiques",
        "titre": "Développer des sites web statiques",
        "titre_complet": "Développer des sites web statiques avec HTML5 et CSS3",
        "description": "Créer des sites web modernes avec HTML5 et CSS3 : structure, mise en forme, responsive design.",
        "duree": "110 h",
        "icone": "🌐",
        "objectifs": [
            "Structurer une page web avec HTML5",
            "Mettre en forme avec CSS3",
            "Utiliser les balises sémantiques",
            "Créer des mises en page responsive (Flexbox, Grid)",
            "Intégrer des médias (images, vidéos)",
            "Publier un site statique",
        ],
        "prerequis": "Aucun",
        "niveau": "Débutant",
    },
    {
        "code": "M105",
        "dossier": "M105-JavaScript",
        "titre": "Programmer en JavaScript",
        "titre_complet": "Programmer en JavaScript : du langage au DOM",
        "description": "Maîtriser le langage JavaScript : variables, fonctions, DOM, événements et API.",
        "duree": "110 h",
        "icone": "⚡",
        "objectifs": [
            "Comprendre les fondamentaux du langage JavaScript",
            "Manipuler des variables, des types et des opérateurs",
            "Écrire des structures conditionnelles et des boucles",
            "Créer et utiliser des fonctions",
            "Manipuler le DOM (Document Object Model)",
            "Gérer les événements utilisateur",
            "Interagir avec des API simples (fetch)",
        ],
        "prerequis": "M104 — Développer des sites web statiques",
        "niveau": "Débutant → Intermédiaire",
    },
    {
        "code": "M106",
        "dossier": "M106-Bases-De-Donnees",
        "titre": "Manipuler des bases de données",
        "titre_complet": "Concevoir et manipuler des bases de données relationnelles",
        "description": "Concevoir et manipuler des bases de données relationnelles avec SQL.",
        "duree": "100 h",
        "icone": "🗄️",
        "objectifs": [
            "Comprendre les concepts de bases de données relationnelles",
            "Concevoir un modèle conceptuel (MCD)",
            "Traduire un MCD en modèle logique (MLD)",
            "Écrire des requêtes SQL (SELECT, INSERT, UPDATE, DELETE)",
            "Utiliser les jointures et les fonctions d'agrégation",
            "Administrer une base simple (MySQL / PostgreSQL)",
        ],
        "prerequis": "Aucun",
        "niveau": "Débutant → Intermédiaire",
    },
]


# ============================================================
# SECTIONS STANDARD
# ============================================================
SECTIONS = [
    {
        "dossier": "supports",
        "titre": "📚 Supports de cours",
        "titre_md": "📚 Supports de cours",
        "description": "Cours, présentations et fiches de révision",
    },
    {
        "dossier": "activites",
        "titre": "🤝 Activités collaboratives",
        "titre_md": "🤝 Activités collaboratives",
        "description": "Activités à réaliser en groupe ou en binôme",
    },
    {
        "dossier": "exercices",
        "titre": "✏️ Exercices",
        "titre_md": "✏️ Exercices",
        "description": "Exercices pratiques à réaliser",
    },
    {
        "dossier": "projets",
        "titre": "🚀 Projets",
        "titre_md": "🚀 Projets",
        "description": "Mini-projets et projets de synthèse",
    },
    {
        "dossier": "corrections",
        "titre": "✅ Corrections",
        "titre_md": "✅ Corrections",
        "description": "Solutions des exercices (à consulter après avoir essayé)",
    },
    {
        "dossier": "evaluations",
        "titre": "📝 Évaluations",
        "titre_md": "📝 Évaluations",
        "description": "Contrôles continus, EFM et corrigés",
    },
]


# ============================================================
# CHEMINS ET VARIABLES DÉRIVÉES
# ============================================================
RACINE = Path(__file__).parent
URL_GITHUB = f"https://github.com/{CONFIG['organisation_github']}/{CONFIG['nom_depot_github']}"
URL_PAGES = f"https://{CONFIG['organisation_github']}.github.io/{CONFIG['nom_depot_github']}"


# ============================================================
# STYLES CSS COMMUNS
# ============================================================
CSS_COMMUN = f"""
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: 'Segoe UI', Calibri, Roboto, system-ui, sans-serif;
      background: #eaf3ec;
      color: #143522;
      line-height: 1.6;
      padding: 2rem 1rem;
      min-height: 100vh;
    }}
    .container {{ max-width: 1100px; margin: 0 auto; }}

    .page-header {{
      background: white;
      border-radius: 20px;
      padding: 2rem;
      margin-bottom: 2rem;
      border-left: 6px solid {CONFIG['couleur_secondaire']};
      box-shadow: 0 6px 20px rgba(20, 50, 30, 0.08);
    }}
    .badge {{
      display: inline-block;
      background: #e6f5eb;
      color: {CONFIG['couleur_principale']};
      padding: 0.3rem 1rem;
      border-radius: 30px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 0.8rem;
      letter-spacing: 0.5px;
    }}
    .page-header h1 {{
      font-size: 2rem;
      color: #144a26;
      margin-bottom: 0.5rem;
      letter-spacing: -0.3px;
      line-height: 1.2;
    }}
    .page-header .sous-titre {{
      color: #3f6b4f;
      font-style: italic;
      font-size: 1rem;
    }}
    .meta-info {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.8rem;
      margin-top: 0.8rem;
      font-size: 0.85rem;
    }}
    .meta-info span {{
      background: #f1faf4;
      padding: 0.2rem 0.9rem;
      border-radius: 20px;
      color: #1a5e33;
      font-weight: 500;
    }}

    .section {{
      background: white;
      border-radius: 20px;
      padding: 1.8rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 6px 20px rgba(20, 50, 30, 0.06);
      border-top: 3px solid {CONFIG['couleur_claire']};
    }}
    .section h2 {{
      font-size: 1.4rem;
      color: {CONFIG['couleur_principale']};
      margin-bottom: 0.3rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid {CONFIG['couleur_claire']};
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section .section-desc {{
      font-size: 0.9rem;
      color: #3f6b4f;
      font-style: italic;
      margin-bottom: 1rem;
    }}
    .section ul {{
      list-style: none;
      padding-left: 0;
    }}
    .section li {{
      padding: 0.7rem 0;
      border-bottom: 1px solid #f1faf4;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}
    .section li:last-child {{ border-bottom: none; }}
    .section a {{
      color: #1d6e3f;
      text-decoration: none;
      font-weight: 600;
      flex: 1;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: color 0.15s;
    }}
    .section a:hover {{
      color: #0f542f;
      text-decoration: underline;
    }}
    .section a::before {{
      content: "📄";
      font-size: 0.9rem;
      opacity: 0.7;
    }}
    .section a.dossier::before {{ content: "📁"; }}
    .section a.pdf::before {{ content: "📕"; }}
    .section a.html::before {{ content: "🌐"; }}
    .section a.docx::before {{ content: "📘"; }}
    .section a.pptx::before {{ content: "📊"; }}
    .section a.sql::before {{ content: "🗃️"; }}
    .section a.zip::before {{ content: "📦"; }}
    .section a.js::before {{ content: "⚡"; }}
    .section a.css::before {{ content: "🎨"; }}

    .file-size {{
      font-size: 0.75rem;
      color: #7aae8b;
      margin-left: auto;
      white-space: nowrap;
    }}
    .empty-section {{
      color: #7aae8b;
      font-style: italic;
      font-size: 0.9rem;
      padding: 0.5rem 0;
    }}

    .back {{
      display: inline-block;
      margin-top: 1rem;
      color: #1d6e3f;
      text-decoration: none;
      font-weight: 600;
      padding: 0.5rem 1.2rem;
      border-radius: 30px;
      background: #f1faf4;
      transition: 0.15s;
    }}
    .back:hover {{
      background: {CONFIG['couleur_claire']};
      transform: translateX(-3px);
    }}

    footer {{
      text-align: center;
      margin-top: 3rem;
      padding-top: 1.5rem;
      border-top: 1px solid #cae0d0;
      font-size: 0.85rem;
      color: #3f6b4f;
    }}
    footer a {{ color: {CONFIG['couleur_principale']}; text-decoration: none; font-weight: 600; }}
    footer a:hover {{ text-decoration: underline; }}

    .modules-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }}
    .module-card {{
      background: white;
      border-radius: 20px;
      padding: 1.8rem;
      box-shadow: 0 6px 20px rgba(20, 50, 30, 0.08);
      border-left: 5px solid {CONFIG['couleur_secondaire']};
      transition: transform 0.2s, box-shadow 0.2s;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
    }}
    .module-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(20, 50, 30, 0.15);
    }}
    .module-card .icon {{
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }}
    .module-card .code {{
      display: inline-block;
      background: #e6f5eb;
      color: {CONFIG['couleur_principale']};
      padding: 0.2rem 0.9rem;
      border-radius: 30px;
      font-size: 0.8rem;
      font-weight: 700;
      margin-bottom: 0.6rem;
      width: fit-content;
    }}
    .module-card h2 {{
      font-size: 1.3rem;
      color: #144a26;
      margin-bottom: 0.5rem;
      line-height: 1.3;
    }}
    .module-card p {{
      font-size: 0.92rem;
      color: #3f6b4f;
      line-height: 1.5;
      flex: 1;
      margin-bottom: 1rem;
    }}
    .module-card .btn {{
      display: inline-block;
      background: #1d6e3f;
      color: white;
      padding: 0.5rem 1.5rem;
      border-radius: 40px;
      font-weight: 600;
      font-size: 0.85rem;
      width: fit-content;
    }}

    @media (max-width: 600px) {{
      .page-header h1 {{ font-size: 1.5rem; }}
      .section h2 {{ font-size: 1.15rem; }}
      .section {{ padding: 1.2rem; }}
    }}
"""


# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================
def format_taille(octets):
    """Convertit une taille en octets vers un format lisible."""
    if octets < 1024:
        return f"{octets} o"
    elif octets < 1024 * 1024:
        return f"{octets / 1024:.1f} Ko"
    else:
        return f"{octets / (1024 * 1024):.1f} Mo"


def get_extension(nom_fichier):
    return Path(nom_fichier).suffix.lower().lstrip('.')


def get_css_class(nom_fichier):
    ext = get_extension(nom_fichier)
    classes_valides = ['pdf', 'html', 'docx', 'pptx', 'sql', 'zip', 'js', 'css']
    return ext if ext in classes_valides else 'fichier'


def get_emoji_fichier(nom_fichier):
    """Retourne l'emoji adapté au type de fichier (pour le Markdown)."""
    ext = get_extension(nom_fichier)
    emojis = {
        'pdf': '📕',
        'html': '🌐',
        'docx': '📘',
        'doc': '📘',
        'pptx': '📊',
        'ppt': '📊',
        'sql': '🗃️',
        'zip': '📦',
        'js': '⚡',
        'css': '🎨',
        'md': '📝',
        'png': '🖼️',
        'jpg': '🖼️',
        'jpeg': '🖼️',
        'svg': '🖼️',
        'txt': '📄',
        'json': '📋',
        'xml': '📋',
    }
    return emojis.get(ext, '📄')


# ============================================================
# GÉNÉRATION DES FICHIERS HTML
# ============================================================
def generer_entete_html(titre):
    """Génère l'en-tête HTML commun."""
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titre}</title>
  <style>
{CSS_COMMUN}
  </style>
</head>
<body>
"""


def generer_pied_html():
    """Génère le pied de page HTML commun."""
    return f"""
  <footer>
    <p>
      <strong>{CONFIG['organisme']}</strong> · {CONFIG['etablissement']}<br>
      Créé par <strong>{CONFIG['createur']}</strong> · {CONFIG['role_createur']}<br>
      Année de formation {CONFIG['annee_formation']}
    </p>
    <p style="margin-top: 0.5rem;">
      <a href="{URL_GITHUB}">📂 Code source sur GitHub</a>
    </p>
  </footer>
</body>
</html>
"""


def lister_fichiers_dossier(dossier):
    """Liste les fichiers et sous-dossiers d'un dossier."""
    elements = []
    if not dossier.exists() or not dossier.is_dir():
        return elements

    for item in sorted(dossier.iterdir()):
        if item.name.startswith('.'):
            continue

        if item.is_dir():
            nb_fichiers = sum(1 for _ in item.rglob('*') if _.is_file())
            elements.append({
                "nom": item.name,
                "chemin": item.name + "/",
                "taille": f"{nb_fichiers} fichier(s)",
                "est_dossier": True,
            })
        else:
            elements.append({
                "nom": item.name,
                "chemin": item.name,
                "taille": format_taille(item.stat().st_size),
                "est_dossier": False,
            })

    return elements


def generer_section_html(section, dossier_module):
    """Génère le bloc HTML d'une section."""
    dossier_section = dossier_module / section["dossier"]

    html = f"""
    <div class="section">
      <h2>{section['titre']}</h2>
      <p class="section-desc">{section['description']}</p>
"""

    if not dossier_section.exists() or not dossier_section.is_dir():
        html += '      <p class="empty-section">Aucun contenu pour le moment.</p>\n'
        html += '    </div>\n'
        return html

    elements = lister_fichiers_dossier(dossier_section)

    if not elements:
        html += '      <p class="empty-section">Aucun contenu pour le moment.</p>\n'
        html += '    </div>\n'
        return html

    html += '      <ul>\n'
    for el in elements:
        chemin = f"{section['dossier']}/{el['chemin']}"
        if el['est_dossier']:
            lien = f"{section['dossier']}/{el['nom']}/index.html"
            classe = "dossier"
        else:
            lien = chemin
            classe = get_css_class(el['nom'])

        nom_affiche = el['nom']
        if el['est_dossier']:
            nom_affiche = el['nom'].replace('-', ' ').replace('_', ' ')

        html += f'        <li>\n'
        html += f'          <a href="{lien}" class="{classe}">{nom_affiche}</a>\n'
        html += f'          <span class="file-size">{el["taille"]}</span>\n'
        html += f'        </li>\n'
    html += '      </ul>\n'
    html += '    </div>\n'

    return html


def generer_index_module(module):
    """Génère le fichier index.html pour un module."""
    dossier_module = RACINE / module["dossier"]

    if not dossier_module.exists():
        return None

    titre_page = f"{module['code']} · {module['titre']} · {CONFIG['organisme']}"

    html = generer_entete_html(titre_page)
    html += '  <div class="container">\n'

    html += f"""
    <div class="page-header">
      <span class="badge">{module['code']} · {module['duree']}</span>
      <h1>{module['icone']} {module['titre']}</h1>
      <p class="sous-titre">{module['description']}</p>
      <div class="meta-info">
        <span>📅 {CONFIG['annee_formation']}</span>
        <span>🏛️ {CONFIG['etablissement']}</span>
        <span>👨‍🏫 {CONFIG['createur']}</span>
        <span>🎓 {CONFIG['filiere']}</span>
      </div>
    </div>
"""

    for section in SECTIONS:
        html += generer_section_html(section, dossier_module)

    html += '    <a href="../" class="back">← Retour à l\'accueil</a>\n'
    html += '  </div>\n'
    html += generer_pied_html()

    chemin_index = dossier_module / "index.html"
    chemin_index.write_text(html, encoding="utf-8")
    return chemin_index


def generer_index_racine():
    """Génère le fichier index.html à la racine."""
    titre_page = f"Ressources pédagogiques · {CONFIG['filiere']} · {CONFIG['organisme']}"

    html = generer_entete_html(titre_page)
    html += '  <div class="container">\n'

    html += f"""
    <div class="page-header">
      <span class="badge">{CONFIG['organisme']} · {CONFIG['etablissement']}</span>
      <h1>📚 Ressources pédagogiques</h1>
      <p class="sous-titre">{CONFIG['filiere']} · {CONFIG['niveau']}</p>
      <div class="meta-info">
        <span>📅 {CONFIG['annee_formation']}</span>
        <span>👨‍🏫 {CONFIG['createur']}</span>
        <span>📖 {len(MODULES)} modules</span>
      </div>
    </div>

    <div class="section">
      <h2>🎯 Bienvenue</h2>
      <p class="section-desc">
        Ce site regroupe l'ensemble des supports de cours, exercices, projets et évaluations
        pour les modules encadrés par <strong>{CONFIG['createur']}</strong> à
        <strong>{CONFIG['etablissement']}</strong>. Cliquez sur un module pour accéder à son contenu.
      </p>
    </div>

    <div class="modules-grid">
"""

    for module in MODULES:
        dossier_module = RACINE / module["dossier"]
        existe = dossier_module.exists()
        lien = f"{module['dossier']}/" if existe else "#"
        style_manquant = "" if existe else 'style="opacity: 0.5; pointer-events: none;"'

        html += f"""
      <a href="{lien}" class="module-card" {style_manquant}>
        <div class="icon">{module['icone']}</div>
        <span class="code">{module['code']} · {module['duree']}</span>
        <h2>{module['titre']}</h2>
        <p>{module['description']}</p>
        <span class="btn">Accéder au module →</span>
      </a>
"""

    html += '    </div>\n'

    html += f"""
    <div class="section" style="margin-top: 2rem;">
      <h2>ℹ️ Informations pratiques</h2>
      <ul>
        <li>
          <a href="{URL_GITHUB}" class="dossier">
            📂 Dépôt GitHub (code source et ressources)
          </a>
        </li>
        <li>
          <a href="{URL_GITHUB}/blob/main/CONTRIBUTING.md" class="dossier">
            📝 Guide de contribution
          </a>
        </li>
        <li>
          <a href="{URL_GITHUB}/issues" class="dossier">
            ❓ Poser une question (Issues GitHub)
          </a>
        </li>
      </ul>
    </div>
"""

    html += '  </div>\n'
    html += generer_pied_html()

    chemin_index = RACINE / "index.html"
    chemin_index.write_text(html, encoding="utf-8")
    return chemin_index


def generer_sous_index(dossier_parent, nom_sous_dossier, contexte):
    """Génère un index.html pour un sous-dossier."""
    dossier_cible = dossier_parent / nom_sous_dossier

    if not dossier_cible.exists() or not dossier_cible.is_dir():
        return None

    if (dossier_cible / "index.html").exists():
        return None

    titre_clean = nom_sous_dossier.replace('-', ' ').replace('_', ' ').title()
    titre_page = f"{contexte} · {titre_clean}"

    html = generer_entete_html(titre_page)
    html += '  <div class="container">\n'
    html += f"""
    <div class="page-header">
      <span class="badge">{contexte}</span>
      <h1>📁 {titre_clean}</h1>
      <p class="sous-titre">Contenu du dossier {nom_sous_dossier}</p>
    </div>

    <div class="section">
      <h2>📂 Fichiers disponibles</h2>
"""

    elements = lister_fichiers_dossier(dossier_cible)

    if not elements:
        html += '      <p class="empty-section">Aucun fichier pour le moment.</p>\n'
    else:
        html += '      <ul>\n'
        for el in elements:
            if el['est_dossier']:
                lien = f"{el['nom']}/"
                classe = "dossier"
                nom_affiche = el['nom'].replace('-', ' ').replace('_', ' ')
            else:
                lien = el['nom']
                classe = get_css_class(el['nom'])
                nom_affiche = el['nom']

            html += f'        <li>\n'
            html += f'          <a href="{lien}" class="{classe}">{nom_affiche}</a>\n'
            html += f'          <span class="file-size">{el["taille"]}</span>\n'
            html += f'        </li>\n'
        html += '      </ul>\n'

    html += '    </div>\n'
    html += '    <a href="../" class="back">← Retour</a>\n'
    html += '  </div>\n'
    html += generer_pied_html()

    chemin_index = dossier_cible / "index.html"
    chemin_index.write_text(html, encoding="utf-8")
    return chemin_index


def generer_tous_sous_index():
    """Génère les sous-index pour chaque sous-dossier."""
    compteur = 0
    for module in MODULES:
        dossier_module = RACINE / module["dossier"]
        if not dossier_module.exists():
            continue

        for section in SECTIONS:
            dossier_section = dossier_module / section["dossier"]
            if not dossier_section.exists():
                continue

            for sous_dossier in dossier_section.iterdir():
                if sous_dossier.is_dir() and not sous_dossier.name.startswith('.'):
                    contexte = f"{module['code']} · {section['titre'].split(' ', 1)[1] if ' ' in section['titre'] else section['titre']}"
                    result = generer_sous_index(
                        dossier_section,
                        sous_dossier.name,
                        contexte
                    )
                    if result:
                        compteur += 1
    return compteur


# ============================================================
# GÉNÉRATION DES FICHIERS MARKDOWN (README.md)
# ============================================================
def generer_readme_racine():
    """Génère le README.md principal du dépôt."""
    contenu = "# 📚 Ressources pédagogiques · " + CONFIG['filiere'] + "\n\n"
    contenu += "Bienvenue sur le dépôt officiel des ressources pédagogiques de la filière **" + CONFIG['filiere'] + "**.\n\n"
    contenu += "Ce dépôt regroupe l'ensemble des supports de cours, exercices, projets et évaluations pour les modules encadrés par **" + CONFIG['createur'] + "** à **" + CONFIG['etablissement'] + "** (" + CONFIG['organisme'] + ").\n\n"
    contenu += "---\n\n"

    contenu += "## 🏛️ Informations institutionnelles\n\n"
    contenu += "| Élément | Détail |\n"
    contenu += "|---------|--------|\n"
    contenu += f"| **Royaume** | {CONFIG['royaume']} |\n"
    contenu += f"| **Ministère** | {CONFIG['ministere']} |\n"
    contenu += f"| **Organisme** | {CONFIG['organisme']} — {CONFIG['organisme_complet']} |\n"
    contenu += f"| **Établissement** | {CONFIG['etablissement']} — {CONFIG['etablissement_complet']} |\n"
    contenu += f"| **Ville** | {CONFIG['ville']} |\n"
    contenu += f"| **Filière** | {CONFIG['filiere']} |\n"
    contenu += f"| **Niveau** | {CONFIG['niveau']} |\n"
    contenu += f"| **Année de formation** | {CONFIG['annee_formation']} |\n"
    contenu += f"| **Créateur** | {CONFIG['createur']} — {CONFIG['role_createur']} |\n\n"
    contenu += "---\n\n"

    contenu += "## 🌐 Site web des ressources\n\n"
    contenu += "Toutes les ressources sont accessibles en ligne via **GitHub Pages** :\n\n"
    contenu += f"👉 **[{URL_PAGES}]({URL_PAGES})**\n\n"
    contenu += "---\n\n"

    contenu += "## 📖 Modules disponibles\n\n"
    contenu += "| Code | Module | Durée | Lien |\n"
    contenu += "|------|--------|-------|------|\n"

    for module in MODULES:
        lien = f"[📁 {module['dossier']}](./{module['dossier']}/)"
        contenu += f"| **{module['code']}** | {module['titre']} | {module['duree']} | {lien} |\n"

    contenu += "\n---\n\n"

    contenu += "## 🎯 Comment utiliser ce dépôt ?\n\n"
    contenu += "### 1. Consulter les ressources en ligne\n"
    contenu += "Le plus simple : ouvrez le **site web** (voir lien ci-dessus).\n\n"
    contenu += "### 2. Consulter les ressources sur GitHub\n"
    contenu += "Cliquez sur le dossier du module qui vous intéresse. Chaque module contient :\n"
    contenu += "- 📂 **`supports/`** : cours, présentations, fiches de révision\n"
    contenu += "- 📂 **`activites/`** : activités collaboratives\n"
    contenu += "- 📂 **`exercices/`** : énoncés d'exercices à réaliser\n"
    contenu += "- 📂 **`projets/`** : mini-projets et projets de synthèse\n"
    contenu += "- 📂 **`corrections/`** : solutions (à consulter après avoir essayé)\n"
    contenu += "- 📂 **`evaluations/`** : sujets de CC, EFM et corrigés\n\n"

    contenu += "### 3. Cloner le dépôt (pour les plus avancés)\n\n"
    contenu += "```bash\n"
    contenu += f"git clone {URL_GITHUB}.git\n"
    contenu += "```\n\n"

    contenu += "---\n\n"
    contenu += "## 📋 Règles de collaboration\n\n"
    contenu += "### Pour poser une question\n"
    contenu += "- Ouvrez une **Issue** (onglet \"Issues\" en haut)\n"
    contenu += "- Exemple de titre : `[M105] Question sur les boucles for`\n"
    contenu += "- Je répondrai dans le fil de discussion\n\n"
    contenu += "### Pour proposer une correction\n"
    contenu += "- Ouvrez une **Pull Request** avec votre proposition\n"
    contenu += "- Expliquez brièvement vos changements\n\n"
    contenu += "### Pour signaler une erreur\n"
    contenu += "- Ouvrez une **Issue** en précisant le module et le fichier concerné\n\n"
    contenu += "---\n\n"

    contenu += "## 📅 Calendrier des modules\n\n"
    contenu += "| Module | Période | Volume horaire |\n"
    contenu += "|--------|---------|----------------|\n"

    periodes = {
        "M101": "Septembre – Octobre",
        "M104": "Octobre – Décembre",
        "M105": "Janvier – Mars",
        "M106": "Mars – Mai",
    }
    for module in MODULES:
        periode = periodes.get(module["code"], "À définir")
        contenu += f"| {module['code']} — {module['titre']} | {periode} | {module['duree']} |\n"

    contenu += "\n---\n\n"
    contenu += "## 📞 Contact\n\n"
    contenu += f"- **Formateur** : {CONFIG['createur']}\n"
    contenu += f"- **Établissement** : {CONFIG['etablissement']}\n"
    contenu += f"- **Email** : [{CONFIG['email']}](mailto:{CONFIG['email']})\n"
    contenu += f"- **GitHub** : [{URL_GITHUB}]({URL_GITHUB})\n\n"
    contenu += "---\n\n"
    contenu += "## 📜 Licence\n\n"
    contenu += "Les supports de cours sont mis à disposition sous licence **CC BY-NC-SA 4.0**.\n"
    contenu += "Vous pouvez les utiliser, les modifier et les partager à des fins non commerciales, en citant l'auteur.\n\n"
    contenu += "---\n\n"
    contenu += "## 🔄 Dernière mise à jour\n\n"
    contenu += f"**{datetime.now().strftime('%B %Y')}** — {CONFIG['createur']}\n"

    chemin = RACINE / "README.md"
    chemin.write_text(contenu, encoding="utf-8")
    return chemin


def generer_readme_module(module):
    """Génère le README.md pour un module donné."""
    dossier_module = RACINE / module["dossier"]

    if not dossier_module.exists():
        return None

    contenu = f"# {module['code']} · {module['titre']}\n\n"
    contenu += f"Bienvenue dans le module **{module['code']} — {module['titre_complet']}**.\n"
    contenu += f"Ce module fait partie de la filière {CONFIG['filiere']} ({CONFIG['niveau']}).\n\n"
    contenu += "---\n\n"
    contenu += "## 🎯 Objectifs du module\n\n"
    contenu += "À l'issue de ce module, vous serez capable de :\n"

    for obj in module["objectifs"]:
        contenu += f"- {obj}\n"

    contenu += f"\n**Durée** : {module['duree']}\n"
    contenu += f"**Niveau** : {module['niveau']}\n"
    contenu += f"**Prérequis** : {module['prerequis']}\n\n"
    contenu += "---\n\n"
    contenu += "## 📂 Contenu du dossier\n"

    for section in SECTIONS:
        dossier_section = dossier_module / section["dossier"]
        contenu += f"\n### {section['titre_md']}\n"
        contenu += f"*{section['description']}*\n\n"

        if not dossier_section.exists():
            contenu += "_Aucun contenu pour le moment._\n"
            continue

        elements = lister_fichiers_dossier(dossier_section)
        if not elements:
            contenu += "_Aucun contenu pour le moment._\n"
            continue

        for el in elements:
            emoji = "📁" if el['est_dossier'] else get_emoji_fichier(el['nom'])
            nom = el['nom'].replace('-', ' ').replace('_', ' ') if el['est_dossier'] else el['nom']
            chemin = f"{section['dossier']}/{el['chemin']}"
            contenu += f"- {emoji} [{nom}]({chemin}) — {el['taille']}\n"

    contenu += "\n---\n\n"
    contenu += "## 🚀 Comment travailler ?\n\n"
    contenu += "### Étape 1 — Lire le support\n"
    contenu += "Chaque séance commence par la lecture du support correspondant dans `supports/`.\n\n"
    contenu += "### Étape 2 — Faire les exercices\n"
    contenu += "Rendez-vous dans `exercices/` et réalisez les exercices dans l'ordre. "
    contenu += "Ne regardez **pas** les corrections avant d'avoir essayé.\n\n"
    contenu += "### Étape 3 — Comparer avec la correction\n"
    contenu += "Une fois l'exercice terminé, ouvrez le dossier `corrections/` pour comparer votre solution.\n\n"
    contenu += "### Étape 4 — Réaliser les projets\n"
    contenu += "Les projets sont l'occasion de mettre en pratique tout ce que vous avez appris.\n\n"
    contenu += "---\n\n"
    contenu += "## 📝 Évaluation\n\n"
    contenu += "| Type | Poids | Période |\n"
    contenu += "|------|-------|---------|\n"
    contenu += "| Contrôles continus | 40 % | En cours de module |\n"
    contenu += "| Exercices pratiques | 20 % | Tout au long du module |\n"
    contenu += "| Examen de fin de module (EFM) | 40 % | Fin du module |\n\n"
    contenu += "**Moyenne minimale pour valider le module** : 10/20\n\n"
    contenu += "---\n\n"
    contenu += "## 💡 Conseils pour réussir\n\n"
    contenu += "1. **Pratiquez tous les jours** : 30 minutes par jour valent mieux que 3 heures une fois par semaine.\n"
    contenu += "2. **Ne copiez pas les corrections** : essayez d'abord, puis comparez.\n"
    contenu += "3. **Posez des questions** : utilisez les Issues GitHub ou le canal Teams.\n"
    contenu += "4. **Documentez votre code** : ajoutez des commentaires pour expliquer votre logique.\n"
    contenu += "5. **Travaillez en groupe** : discuter d'un problème aide à mieux comprendre.\n\n"
    contenu += "---\n\n"
    contenu += "## 📞 Contact\n\n"
    contenu += f"- **Formateur** : {CONFIG['createur']}\n"
    contenu += f"- **Établissement** : {CONFIG['etablissement']} ({CONFIG['organisme']})\n"
    contenu += f"- **Email** : [{CONFIG['email']}](mailto:{CONFIG['email']})\n"
    contenu += f"- **GitHub** : [{URL_GITHUB}]({URL_GITHUB})\n\n"
    contenu += "---\n\n"
    contenu += "## 🔄 Dernière mise à jour\n\n"
    contenu += f"**{datetime.now().strftime('%B %Y')}** — {CONFIG['createur']}\n"

    chemin = dossier_module / "README.md"
    chemin.write_text(contenu, encoding="utf-8")
    return chemin


# ============================================================
# FONCTION PRINCIPALE
# ============================================================
def main():
    print("=" * 65)
    print("GÉNÉRATION DES RESSOURCES PÉDAGOGIQUES")
    print(f"Établissement : {CONFIG['etablissement']} · {CONFIG['organisme']}")
    print(f"Créateur : {CONFIG['createur']}")
    print("=" * 65)
    print(f"Répertoire racine : {RACINE}")
    print()

    # 1. Index principal
    print("📄 Génération de l'index principal...")
    chemin = generer_index_racine()
    print(f"   ✅ {chemin.relative_to(RACINE)}")

    # 2. README principal
    print("\n📘 Génération du README principal...")
    chemin = generer_readme_racine()
    print(f"   ✅ {chemin.relative_to(RACINE)}")

    # 3. Index et README de chaque module
    print("\n📁 Génération des modules :")
    for module in MODULES:
        print(f"\n   ── {module['code']} · {module['titre']} ──")

        chemin_index = generer_index_module(module)
        if chemin_index:
            print(f"      ✅ {chemin_index.relative_to(RACINE)}")

        chemin_readme = generer_readme_module(module)
        if chemin_readme:
            print(f"      ✅ {chemin_readme.relative_to(RACINE)}")

    # 4. Sous-index
    print("\n📂 Génération des sous-index HTML :")
    nb = generer_tous_sous_index()
    print(f"   ✅ {nb} sous-index généré(s)")

    # 5. Bilan
    print()
    print("=" * 65)
    print("✅ GÉNÉRATION TERMINÉE AVEC SUCCÈS")
    print("=" * 65)
    print()
    print("📊 Fichiers générés :")
    print("   • 1 index.html principal")
    print("   • 1 README.md principal")
    print(f"   • {len(MODULES)} index.html de modules")
    print(f"   • {len(MODULES)} README.md de modules")
    print(f"   • {nb} sous-index HTML")
    print()
    print("🌐 Site web (après déploiement) :")
    print(f"   {URL_PAGES}")
    print()
    print("📂 Dépôt GitHub :")
    print(f"   {URL_GITHUB}")
    print()
    print("💡 Prochaines étapes :")
    print("   1. Vérifiez les fichiers générés")
    print("   2. Commitez et poussez sur GitHub")
    print("   3. Le workflow GitHub Actions publiera automatiquement le site")
    print()


if __name__ == "__main__":
    main()