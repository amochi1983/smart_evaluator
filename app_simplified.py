import streamlit as st
import os
import sys

# Ajouter le répertoire courant au chemin Python pour les imports relatifs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importer les modules utilitaires
from utils.ui_components import set_page_config
from pages.dashboard import show_dashboard
from pages.evaluator_matching import show_evaluator_matching
from pages.document_validator import show_document_validator
from pages.risk_alerts import show_risk_alerts

def main():
    """Point d'entrée principal de l'application"""
    # Configuration de la page
    set_page_config("Smart Evaluator Assistant")
    
    # Vérifier si le fichier CSS existe
    css_path = os.path.join("assets", "css", "style.css")
    if os.path.exists(css_path):
        # Ajouter CSS personnalisé
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Sidebar avec logo
    with st.sidebar:
        # Logo
        logo_path = os.path.join("assets", "images", "sac_logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path, width=200)
        else:
            st.title("Smart Evaluator")
        
        st.sidebar.markdown("---")
        
        # Sélection de la langue
        language = st.sidebar.selectbox(
            "Language / اللغة",
            ["English", "العربية"],
            index=0
        )
        
        st.sidebar.markdown("---")
        
        # Menu de navigation simplifié
        st.sidebar.title("Navigation")
        
        # Utiliser un selectbox pour la navigation
        page = st.sidebar.radio(
            "Select a page:",
            ["Dashboard", "Evaluator Matching", "Document Validator", "Risk Alerts"],
            label_visibility="collapsed"
        )
        
        st.sidebar.markdown("---")
        
        # Informations sur le prototype
        st.sidebar.info(
            "This is a prototype with dummy data. "
            "In the next phase, real algorithms will replace the mock functions."
        )
        
        # Ajouter un badge "Prototype"
        st.sidebar.markdown("""
        <div style="
            background-color: #FF9800;
            color: white;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
            margin-top: 20px;
        ">
            PROTOTYPE VERSION
        </div>
        """, unsafe_allow_html=True)
    
    # Afficher la page sélectionnée
    if page == "Dashboard":
        show_dashboard()
    elif page == "Evaluator Matching":
        show_evaluator_matching()
    elif page == "Document Validator":
        show_document_validator()
    elif page == "Risk Alerts":
        show_risk_alerts()

if __name__ == "__main__":
    main()
