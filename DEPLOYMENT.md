# Déploiement du Smart Evaluator Assistant

Ce document explique comment déployer le prototype Smart Evaluator Assistant sur différentes plateformes.

## Option 1: Déploiement sur Streamlit Cloud

Streamlit Cloud est la méthode la plus simple pour déployer l'application et la rendre accessible publiquement.

### Prérequis
- Un compte GitHub
- Un compte Streamlit Cloud (gratuit)

### Étapes de déploiement

1. **Créer un dépôt GitHub**
   ```bash
   # Initialiser un dépôt Git local
   cd /home/ubuntu/smart_evaluator_prototype
   git init
   git add .
   git commit -m "Initial commit"
   
   # Créer un dépôt GitHub et pousser le code
   gh repo create smart-evaluator-prototype --public
   git remote add origin https://github.com/username/smart-evaluator-prototype.git
   git push -u origin main
   ```

2. **Déployer sur Streamlit Cloud**
   - Connectez-vous à [Streamlit Cloud](https://streamlit.io/cloud)
   - Cliquez sur "New app"
   - Sélectionnez votre dépôt GitHub
   - Spécifiez le fichier principal: `app.py`
   - Cliquez sur "Deploy"

3. **Accéder à l'application**
   - Une fois le déploiement terminé, vous recevrez une URL publique
   - Partagez cette URL avec les juges du GovJam

## Option 2: Déploiement sur Heroku

### Prérequis
- Un compte Heroku
- Heroku CLI installé

### Étapes de déploiement

1. **Créer un fichier Procfile**
   ```
   web: streamlit run app.py --server.port $PORT
   ```

2. **Créer un fichier runtime.txt**
   ```
   python-3.11.0
   ```

3. **Déployer sur Heroku**
   ```bash
   # Installer Heroku CLI si nécessaire
   curl https://cli-assets.heroku.com/install.sh | sh
   
   # Se connecter à Heroku
   heroku login
   
   # Créer une application Heroku
   heroku create smart-evaluator-prototype
   
   # Déployer l'application
   git push heroku main
   
   # Ouvrir l'application
   heroku open
   ```

## Option 3: Déploiement sur GitHub Pages (Version statique)

Pour une version statique (sans interactivité complète), vous pouvez utiliser GitHub Pages.

### Étapes de déploiement

1. **Créer des captures d'écran de l'application**
   ```bash
   # Installer un outil de capture d'écran
   sudo apt-get install -y scrot
   
   # Prendre des captures d'écran
   scrot -u dashboard.png
   scrot -u evaluator_matching.png
   scrot -u document_validator.png
   scrot -u risk_alerts.png
   ```

2. **Créer une page HTML simple**
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Smart Evaluator Assistant - Prototype</title>
       <style>
           body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
           img { max-width: 100%; border: 1px solid #ddd; margin: 20px 0; }
       </style>
   </head>
   <body>
       <h1>Smart Evaluator Assistant - Prototype</h1>
       <p>This is a static preview of the Smart Evaluator Assistant prototype.</p>
       
       <h2>Dashboard</h2>
       <img src="dashboard.png" alt="Dashboard">
       
       <h2>Evaluator Matching</h2>
       <img src="evaluator_matching.png" alt="Evaluator Matching">
       
       <h2>Document Validator</h2>
       <img src="document_validator.png" alt="Document Validator">
       
       <h2>Risk Alerts</h2>
       <img src="risk_alerts.png" alt="Risk Alerts">
   </body>
   </html>
   ```

3. **Déployer sur GitHub Pages**
   - Créez une branche `gh-pages`
   - Poussez le fichier HTML et les images
   - Activez GitHub Pages dans les paramètres du dépôt

## Option 4: Déploiement local pour la démonstration

### Prérequis
- Python 3.11 ou supérieur
- pip

### Étapes de déploiement

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/username/smart-evaluator-prototype.git
   cd smart-evaluator-prototype
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Exécuter l'application**
   ```bash
   streamlit run app.py
   ```

4. **Accéder à l'application**
   - Ouvrez un navigateur et accédez à `http://localhost:8501`
