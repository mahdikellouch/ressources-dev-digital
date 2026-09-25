# Projet GreenTech Flexbox

# 🚀 Projet GreenTech Solutions · Version Flexbox

Bienvenue dans votre projet final du **Chapitre 5 (Flexbox approfondi)**.

Ce projet consiste à **refondre** le site GreenTech Solutions en utilisant
**massivement Flexbox** pour toutes les mises en page.

---

## 🎯 Objectif

Transformer une structure HTML existante en un **site moderne, responsive
et entièrement basé sur Flexbox**.

---

## 📁 Structure du projet
greentech-flexbox-starter/
├── index.html              ← HTML complet (CSS à compléter)
├── services.html           ← HTML complet (CSS à compléter)
├── contact.html            ← HTML complet (CSS à compléter)
├── css/
│   └── style.css          ← Feuille de style VIDE avec commentaires-guides
└── README.md              ← Guide de démarrage


---

## 🛠️ Ce que vous devez faire

### 1. Lier la feuille de style
Dans chaque fichier HTML, décommentez la ligne :
```html
<link rel="stylesheet" href="css/style.css">

2. Compléter css/style.css
Le fichier contient 15 sections commentées. Suivez les instructions
pour écrire les règles Flexbox attendues.

3. Utiliser Flexbox partout
Chaque section du site doit utiliser Flexbox :

Header → justify-content: space-between + align-items: center

Hero → flex-direction: column + centrage parfait

Services → display: flex + flex: 1 sur les cartes

Footer → display: flex + flex-wrap: wrap

4. Ajouter le responsive
Créez au moins 2 media queries :

@media (max-width: 992px) (tablette)

@media (max-width: 768px) (mobile)

5. Valider votre code
HTML : https://validator.w3.org

CSS : https://jigsaw.w3.org/css-validator

📋 Exigences Flexbox
Élément	Propriétés attendues
Header	display: flex + space-between + align-items: center
Hero	display: flex + column + justify-content: center + align-items: center
Services	display: flex + flex-wrap: wrap + gap + flex: 1 1 300px
À propos	display: flex + gap + flex: 1 1 300px
Témoignages	display: flex + flex-wrap: wrap + flex: 1 1 280px
Footer	display: flex + flex-wrap: wrap + flex: 1 1 200px
Contact	display: flex + flex-wrap: wrap + gap
Formulaire	display: flex + flex-direction: column + gap
📅 Planning conseillé (3 semaines)
Semaine	Tâches	Livrable
1	Analyse + liaison CSS + styles de base	Structure HTML + CSS de base
2	Application de Flexbox sur toutes les sections	Site fonctionnel sans responsive
3	Responsive + tests + validation W3C	Livrable final
✅ Checklist avant remise
□ Le header utilise display: flex + justify-content: space-between
□ Le hero est parfaitement centré
□ Les cartes utilisent flex: 1
□ Les galeries utilisent flex-wrap: wrap
□ Les espacements utilisent gap (pas margin)
□ Au moins 2 media queries
□ Testé sur 3 tailles d'écran
□ Code validé W3C
□ CSS commenté (10+ commentaires)
□ README.md complété
📞 Contact
Formateur : KELLOUCH Mahdi

Établissement : ISMO · OFPPT

Module : M104

Bon courage ! 🚀