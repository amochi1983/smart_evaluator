# Smart Evaluator Assistant - Version Simplifiée

Cette version simplifiée du Smart Evaluator Assistant a été créée pour résoudre les problèmes de navigation rencontrés dans la version originale.

## Différences avec la version originale

1. **Navigation simplifiée** : Utilisation d'un menu radio au lieu de boutons pour une navigation plus fiable
2. **Dépendances réduites** : Versions non spécifiées pour une meilleure compatibilité
3. **Pas de gestion d'état complexe** : Évite les problèmes liés à `st.session_state`

## Comment exécuter l'application

1. **Installer les dépendances**
```bash
pip install -r requirements_simplified.txt
```

2. **Lancer l'application simplifiée**
```bash
streamlit run app_simplified.py
```

3. **Naviguer dans l'application**
Utilisez le menu radio dans la barre latérale pour naviguer entre les différentes pages :
- Dashboard (Tableau de bord)
- Evaluator Matching (Correspondance des évaluateurs)
- Document Validator (Validation de documents)
- Risk Alerts (Alertes de risque)

## Résolution des problèmes courants

### Si les pages ne s'affichent pas correctement
Assurez-vous que tous les fichiers sont dans la structure de répertoires correcte :
```
smart_evaluator_prototype/
│
├── app_simplified.py
├── pages/
│   ├── dashboard.py
│   ├── evaluator_matching.py
│   ├── document_validator.py
│   └── risk_alerts.py
│
├── utils/
│   ├── ui_components.py
│   ├── data_generator.py
│   └── mock_algorithms.py
│
├── data/
├── assets/
└── requirements_simplified.txt
```

### Si vous rencontrez des erreurs d'importation
Vérifiez que vous exécutez l'application depuis le répertoire principal :
```bash
cd smart_evaluator_prototype
streamlit run app_simplified.py
```

### Si les images ne s'affichent pas
Vérifiez que le répertoire `assets/images/` contient bien les images nécessaires, notamment `sac_logo.png`.
