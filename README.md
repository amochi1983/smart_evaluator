# Smart Evaluator Assistant - Prototype

Un prototype fonctionnel pour le Smart Evaluator Assistant, démontrant comment le système fonctionnera dans des scénarios d'accréditation réels.

## À propos du projet

Le Smart Evaluator Assistant est une solution basée sur l'IA conçue pour transformer le processus d'accréditation du Saudi Accreditation Center (SAC). Ce prototype présente l'architecture et le flux de travail du système avec des données factices, en préparation de l'intégration future d'algorithmes avancés.

## Fonctionnalités

### Tableau de bord principal
- Cartes KPI (Documents traités, Conformité %, Évaluateurs actifs, Alertes)
- Graphique de conformité (barres/secteurs)
- Liste des alertes de risque
- Tableau d'affectation des évaluateurs
- Chronologie du processus (soumission → examen → décision)

### Page de correspondance des évaluateurs
- Tableau avec évaluateurs (nom, spécialité, emplacement, disponibilité)
- Bouton "Assigner" (action simulée)
- Indicateur de conflit d'intérêts (logique factice)

### Page de validation de documents
- Zone de téléchargement (accepte des PDF factices)
- Simulation de vérifications (ex. "Section manquante", "Non-conformité aux normes")
- Résumé Réussite/Échec avec recommandations

## Technologies utilisées

- **Frontend & Backend**: Streamlit (Python)
- **Visualisation de données**: Plotly, Matplotlib, Altair
- **Gestion des données**: Pandas
- **Simulation de documents**: PyPDF2
- **Styles**: CSS personnalisé + Streamlit Theming
- **Support RTL**: CSS personnalisé pour l'arabe

## Installation et exécution

1. Cloner le dépôt
```bash
git clone https://github.com/username/smart-evaluator-prototype.git
cd smart-evaluator-prototype
```

2. Installer les dépendances
```bash
pip install -r requirements.txt
```

3. Lancer l'application
```bash
streamlit run app.py
```

## Structure du projet

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
├── utils/                  # Fonctions utilitaires
├── assets/                 # Ressources statiques
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet
```

## Note importante pour les juges

Ce prototype de Phase 1 utilise des données factices pour démontrer l'architecture et le flux de travail du système. Dans la prochaine étape, des données d'accréditation réelles et des algorithmes avancés (NLP arabe, analyse prédictive, correspondance d'évaluateurs) remplaceront les fonctions simulées pour fournir des capacités d'IA complètes.

## Prochaines étapes

- Intégration d'algorithmes réels de NLP pour la validation de documents
- Implémentation d'un moteur de correspondance d'évaluateurs basé sur l'IA
- Développement d'un système d'analyse prédictive des risques
- Connexion à des sources de données réelles

## Licence

Ce projet est sous licence [MIT](LICENSE).
