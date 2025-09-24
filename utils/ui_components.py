import streamlit as st
import os
from PIL import Image

def set_page_config(title):
    """Configure la page Streamlit avec les paramètres appropriés"""
    st.set_page_config(
        page_title=title,
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def sidebar_menu():
    """Affiche le menu de navigation dans la sidebar et retourne la sélection"""
    with st.sidebar:
        # Logo
        logo_path = os.path.join("assets", "images", "sac_logo.png")
        if os.path.exists(logo_path):
            logo = Image.open(logo_path)
            st.image(logo, width=200)
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
        
        # Menu de navigation
        st.sidebar.title("Navigation")
        menu_options = ["Dashboard", "Evaluator Matching", "Document Validator", "Risk Alerts"]
        icons = ["📊", "👥", "📄", "⚠️"]
        
        # Stocker la sélection dans la session state si elle n'existe pas encore
        if 'menu_selection' not in st.session_state:
            st.session_state.menu_selection = "Dashboard"
        
        # Créer les boutons de navigation
        for i, option in enumerate(menu_options):
            if st.sidebar.button(f"{icons[i]} {option}", key=f"nav_{option}"):
                st.session_state.menu_selection = option
        
        # Récupérer la sélection actuelle
        menu_selection = st.session_state.menu_selection
        
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
        
        return menu_selection

def kpi_card(title, value, delta=None, delta_color="normal"):
    """Affiche une carte KPI avec titre, valeur et variation optionnelle"""
    st.metric(
        label=title,
        value=value,
        delta=delta,
        delta_color=delta_color
    )

def section_title(title):
    """Affiche un titre de section formaté"""
    st.markdown(f"## {title}")
    st.markdown("---")

def info_box(message, type="info"):
    """Affiche une boîte d'information avec le style approprié"""
    if type == "info":
        st.info(message)
    elif type == "success":
        st.success(message)
    elif type == "warning":
        st.warning(message)
    elif type == "error":
        st.error(message)

def action_button(label, key=None, help=None):
    """Affiche un bouton d'action stylisé"""
    return st.button(label, key=key, help=help)

def status_badge(status):
    """Retourne un badge HTML pour afficher un statut"""
    colors = {
        "Approved": "#4CAF50",
        "Pending": "#FFC107",
        "Rejected": "#F44336",
        "In Progress": "#2196F3",
        "Completed": "#4CAF50",
        "High Risk": "#F44336",
        "Medium Risk": "#FF9800",
        "Low Risk": "#4CAF50",
    }
    
    color = colors.get(status, "#607D8B")
    
    return f"""
    <span style="
        background-color: {color};
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 0.5rem;
        font-size: 0.8rem;
        font-weight: bold;
    ">
        {status}
    </span>
    """
