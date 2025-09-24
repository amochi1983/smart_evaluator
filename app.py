import streamlit as st
import os
import sys

# Ajouter le répertoire courant au chemin Python pour les imports relatifs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importer les modules utilitaires
from utils.ui_components import set_page_config, sidebar_menu
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
    
    # Sidebar avec menu de navigation
    menu_selection = sidebar_menu()
    
    # Afficher la page sélectionnée
    if menu_selection == "Dashboard":
        show_dashboard()
    elif menu_selection == "Evaluator Matching":
        show_evaluator_matching()
    elif menu_selection == "Document Validator":
        show_document_validator()
    elif menu_selection == "Risk Alerts":
        show_risk_alerts()
    
    # Ajouter un message de débogage pour voir quelle page est sélectionnée
    st.sidebar.markdown(f"**Current page:** {menu_selection}")

if __name__ == "__main__":
    main()
