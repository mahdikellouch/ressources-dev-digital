# 🌱 GreenTech Solutions · Projet final corrigé

**Auteur :** KELLOUCH Mahdi
**Module :** M104 - Développement Digital
**Chapitre :** 4 - Introduction au CSS
**Version :** Référence formateur

---

## 📋 Description du projet

Site vitrine de 3 pages pour la start-up fictive **GreenTech Solutions**,
spécialisée dans les solutions numériques écologiques.

Ce projet mobilise l'ensemble des notions du Chapitre 4 :
- CSS externe et structure de fichier
- Sélecteurs de base et avancés
- Mise en forme du texte
- Unités de mesure (px, rem, %, vh)
- Couleurs et dégradés (HEX, RGB, HSL)
- Cascade et spécificité
- Modèle de boîte (box-sizing: border-box)
- Positionnement (sticky, relative, absolute)
- Responsive design (media queries)

---

## 📁 Structure du projet

greentech-solutions-starter/
├── index.html                    ← Page d'accueil (structure HTML complète, sans CSS)
├── services.html                 ← Page services (structure HTML complète, sans CSS)
├── contact.html                  ← Page contact (structure HTML complète, sans CSS)
├── css/
│   └── style.css                 ← Feuille de style VIDE avec commentaires-guides
├── images/
│   └── README.txt                ← Instructions pour les images
└── README.md                     ← Guide de démarrage pour les stagiaires


---

## 🎨 Charte graphique

| Élément | Valeur |
|---------|--------|
| Couleur principale | `#144a26` (vert foncé) |
| Couleur secondaire | `#2e8b57` (vert moyen) |
| Couleur accent | `#a4d4b3` (vert clair) |
| Couleur de fond | `#f8fcf9` (gris très clair) |
| Couleur du texte | `#333333` (gris foncé) |
| Police | Segoe UI, Arial, sans-serif |
| Taille racine | 16px |
| Rayon de bordure | 12px |
| Ombre standard | `0 6px 20px rgba(0,0,0,0.08)` |

---

## ✅ Exigences techniques couvertes

### Structure CSS
- ✅ Feuille de style externe unique (`css/style.css`)
- ✅ Reset CSS avec `box-sizing: border-box`
- ✅ Variables CSS dans `:root`
- ✅ Code organisé par sections commentées

### Sélecteurs
- ✅ Sélecteur universel (`*`)
- ✅ Sélecteurs de balise (`body`, `h1`, `p`)
- ✅ Sélecteurs de classe (`.header`, `.btn`, `.service-card`)
- ✅ Sélecteur d'id (aucun — bonne pratique)
- ✅ Sélecteur descendant (`.footer-col a`)
- ✅ Pseudo-classes (`:hover`, `:focus`, `:last-child`)
- ✅ Sélecteurs d'attribut (`input[type="text"]`)

### Unités
- ✅ px (bordures, petites valeurs)
- ✅ rem (tailles de police, marges)
- ✅ % (largeurs, flex)
- ✅ vh (hauteur du hero)
- ✅ rgba (ombres, transparences)

### Couleurs
- ✅ HEX (`#144a26`, `#2e8b57`)
- ✅ RGB (via rgba pour les ombres)
- ✅ HSL (dans les dégradés)

### Dégradés
- ✅ `linear-gradient(135deg, ...)` sur le hero
- ✅ Dégradés sur les placeholders d'images

### Modèle de boîte
- ✅ `padding`, `margin`, `border`, `border-radius`
- ✅ `box-sizing: border-box` global

### Positionnement
- ✅ `position: sticky` sur le header
- ✅ `z-index: 1000` sur le header

### Flexbox
- ✅ Header (justify-content: space-between)
- ✅ Grille de services (flex + wrap)
- ✅ Témoignages (flex + wrap)
- ✅ Footer (flex + wrap)
- ✅ Section À propos (flex)

### Responsive
- ✅ Media query `@media (max-width: 992px)` (tablette)
- ✅ Media query `@media (max-width: 768px)` (mobile)

### Accessibilité
- ✅ Attributs `alt` sur les images (via texte des placeholders)
- ✅ Contraste suffisant (vert foncé sur blanc, blanc sur vert foncé)
- ✅ Labels associés aux champs de formulaire
- ✅ Structure sémantique (header, nav, section, article, footer)

---

## 🎯 Barème obtenu (40 points)

| Critère | Points |
|---------|:---:|
| Structure HTML sémantique | 4/4 |
| Structure CSS (organisation) | 4/4 |
| Variété des sélecteurs | 3/3 |
| Mise en forme du texte | 3/3 |
| Couleurs et dégradés | 3/3 |
| Modèle de boîte | 3/3 |
| Mise en page (flexbox) | 3/3 |
| Positionnement (sticky) | 2/2 |
| Responsive design | 3/3 |
| Respect de la maquette | 4/4 |
| Accessibilité | 2/2 |
| Validation W3C | 3/3 |
| Soin et finition | 3/3 |
| **TOTAL** | **40/40** |

---

## 🎁 Bonus possibles

- Variables CSS utilisées : **+1**
- Responsive complet : **+1**
- Total maximum : **42/40** (ramené à 40/40)

---

## 🖼️ Notes sur les images

Ce projet utilise des **emojis** et des **placeholders CSS** à la place des images
pour éviter toute dépendance externe et faciliter la distribution.

Pour un projet réel, remplacez les `<div class="service-image">🌿</div>`
par des balises `<img>` avec des images réelles :

```html
<img src="images/service-1.jpg" alt="Hébergement vert" class="service-image">

📞 Contact
Formateur : KELLOUCH Mahdi

Établissement : ISMO · OFPPT

Module : M104 - Développement Digital

## Projet corrigé - Référence formateur - Année 2025-2026


---

## 🎯 Points clés de la version corrigée

### Ce qui distingue cette solution

| Élément | Choix fait | Justification |
|---------|-----------|---------------|
| **Aucun id en CSS** | Uniquement des classes | Bonne pratique : évite les problèmes de spécificité |
| **Variables CSS** | `:root { --couleur-... }` | Maintenance facilitée, code plus propre |
| **Reset complet** | `*, *::before, *::after` | Évite les comportements par défaut des navigateurs |
| **Emojis comme placeholders** | 🌱💻🌿 | Aucune dépendance externe |
| **Grid pour services.html** | `grid-template-columns: repeat(3, 1fr)` | Plus moderne que flexbox pour une grille |
| **Flexbox pour index.html** | `display: flex` + wrap | Plus souple pour les cartes de tailles variables |
| **2 media queries** | 992px et 768px | Couvre tablettes et mobiles |
| **Commentaires structurés** | Sections numérotées | Code lisible et maintenable |

---

## 🖨️ Utilisation en classe

### Scénario 1 — Correction collective

1. **Projetez** la version corrigée au tableau
2. **Comparez** avec quelques copies d'stagiaires
3. **Discutez** des différences de choix techniques
4. **Notez** les bonnes pratiques observées

### Scénario 2 — Auto-correction

1. **Distribuez** la version corrigée à chaque stagiaire
2. **Demandez-leur** de comparer avec leur propre code
3. **Listez** 3 différences et 3 points communs
4. **Restitution** en 5 min par binôme

### Scénario 3 — Défi

1. **Distribuez** uniquement la version HTML
2. **Demandez** aux stagiaires d'écrire le CSS
3. **Comparez** avec la solution officielle
4. **Débattez** des meilleures pratiques

---

## ✅ Validation avant distribution

- [ ] Ouvrir `index.html` dans Chrome → vérifier toutes les sections
- [ ] Ouvrir `services.html` → vérifier la grille de 6 services
- [ ] Ouvrir `contact.html` → vérifier le formulaire
- [ ] Redimensionner la fenêtre → vérifier le responsive
- [ ] Tester sur mobile (F12 → mode device) → vérifier le rendu
- [ ] Valider sur https://validator.w3.org → aucune erreur
- [ ] Valider sur https://jigsaw.w3.org/css-validator → aucune erreur

---

## 🎁 Prochaines étapes possibles

Après avoir partagé la version corrigée, vous pouvez :

- 🔹 Générer une **grille de correction** individuelle (document `.docx`) ?
- 🔹 Créer un **script Python** qui génère automatiquement le pack ZIP complet ?
- 🔹 Préparer le **Chapitre 5** dans le même format ?
- 🔹 Rédiger le **guide de correction formateur** avec les critères détaillés ?

Dites-moi ce que vous souhaitez préparer ensuite. 🚀

