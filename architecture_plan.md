# Architecture du Prototype Smart Evaluator Assistant

## Vue d'ensemble

Le prototype Smart Evaluator Assistant sera développé en utilisant Streamlit, une bibliothèque Python qui permet de créer rapidement des applications web interactives. Cette approche nous permettra de:

1. Développer rapidement une interface utilisateur fonctionnelle
2. Intégrer facilement des visualisations de données
3. Simuler des interactions avec des données factices
4. Déployer facilement l'application sur Streamlit Cloud

## Structure du Projet

```
smart_evaluator_prototype/
│
├── app.py                  # Point d'entrée principal de l'application
├── pages/                  # Pages supplémentaires de l'application
│   ├── dashboard.py        # Tableau de bord principal
│   ├── evaluator_matching.py # Page de correspondance des évaluateurs
│   └── document_validator.py # Page de validation de documents
│
├── data/                   # Données factices
│   ├── documents.json      # Données sur les documents
│   ├── evaluators.json     # Données sur les évaluateurs
│   └── alerts.json         # Données sur les alertes de risque
│
├── utils/                  # Fonctions utilitaires
│   ├── data_generator.py   # Générateur de données factices
│   ├── mock_algorithms.py  # Simulations des algorithmes
│   └── ui_components.py    # Composants d'interface utilisateur réutilisables
│
├── assets/                 # Ressources statiques
│   ├── css/                # Styles CSS personnalisés
│   ├── images/             # Images et icônes
│   └── sample_docs/        # Documents PDF d'exemple
│
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet
```

## Technologies Utilisées

- **Frontend & Backend**: Streamlit (Python)
- **Visualisation de données**: Plotly, Matplotlib, Altair
- **Gestion des données**: Pandas
- **Simulation de documents**: PyPDF2 (pour manipuler des PDF factices)
- **Styles**: CSS personnalisé + Streamlit Theming
- **Support RTL**: CSS personnalisé pour l'arabe

## Fonctionnalités Principales

### 1. Tableau de Bord Principal

- **KPI Cards**: Affichage des métriques clés
  - Documents traités
  - Pourcentage de conformité
  - Évaluateurs actifs
  - Alertes
- **Graphique de Conformité**: Visualisation des taux de conformité
- **Liste des Alertes de Risque**: Affichage des alertes générées
- **Tableau d'Affectation des Évaluateurs**: Vue d'ensemble des affectations
- **Chronologie du Processus**: Visualisation des étapes du processus d'accréditation

### 2. Page de Correspondance des Évaluateurs

- **Tableau des Évaluateurs**: Liste des évaluateurs avec leurs attributs
  - Nom
  - Spécialité
  - Emplacement
  - Disponibilité
- **Bouton "Assigner"**: Simulation d'affectation d'évaluateurs
- **Indicateur de Conflit d'Intérêts**: Simulation de détection de conflits

### 3. Page de Validation de Documents

- **Zone de Téléchargement**: Pour les documents PDF factices
- **Simulation de Vérifications**: Affichage de résultats simulés
  - Sections manquantes
  - Non-conformité aux normes
- **Résumé Réussite/Échec**: Avec recommandations

## Données Factices

### Documents
- 10-15 documents fictifs avec différents niveaux de conformité
- Métadonnées: ID, titre, type, date de soumission, score de conformité

### Évaluateurs
- 10 profils d'évaluateurs fictifs
- Attributs: nom, spécialité, région, disponibilité, expérience

### Alertes
- 2-3 alertes de risque générées aléatoirement
- Types: document incomplet, conflit d'intérêts, retard dans le processus

## Design & Langue

- **Style**: Cohérent avec la présentation (mêmes couleurs, icônes)
- **Couleurs**: Dégradé Vision 2030 (vert → bleu → gris)
- **Langue**: Interface en arabe (RTL) avec option de basculement vers l'anglais

## Déploiement

- **Développement Local**: Streamlit run app.py
- **Déploiement**: Streamlit Cloud ou GitHub Pages
- **Contrôle de Version**: GitHub Repository

## Prochaines Étapes (Post-Prototype)

- Intégration d'algorithmes réels de NLP pour la validation de documents
- Implémentation d'un moteur de correspondance d'évaluateurs basé sur l'IA
- Développement d'un système d'analyse prédictive des risques
- Connexion à des sources de données réelles
