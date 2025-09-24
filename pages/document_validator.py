import streamlit as st
import pandas as pd
import os
import sys
import time
import random

# Ajouter le répertoire courant au chemin Python pour les imports relatifs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importer les modules utilitaires
from utils.ui_components import section_title, info_box, action_button
from utils.data_generator import load_data
from utils.mock_algorithms import simulate_document_validation, algorithm_info_box

def show_document_validator():
    """Affiche la page de validation de documents"""
    # Charger les données
    data = load_data()
    documents = data["documents"]
    
    # Titre de la page
    st.title("Document Validator")
    
    # Section d'information sur l'algorithme
    algorithm_info_box("document_validation")
    
    # Section de téléchargement de document
    section_title("Upload Document")
    
    # Zone de téléchargement
    st.markdown("""
    <div class="upload-container">
        <div class="upload-icon">📄</div>
        <div class="upload-text">Drag and drop a document here or click to browse</div>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "doc"], label_visibility="collapsed")
    
    # Ou sélectionner un document existant
    st.markdown("### Or select an existing document")
    
    # Créer une liste de sélection
    doc_options = {f"{doc['id']} - {doc['title']}": doc for doc in documents}
    selected_doc_key = st.selectbox(
        "Select a document to validate:",
        options=list(doc_options.keys())
    )
    
    # Récupérer le document sélectionné
    selected_doc = doc_options[selected_doc_key]
    
    # Bouton pour lancer la validation
    if st.button("Validate Document", type="primary"):
        # Simuler la validation du document
        validation_results = simulate_document_validation(selected_doc)
        
        # Stocker les résultats dans la session
        st.session_state.validation_results = validation_results
        st.session_state.validated_document = selected_doc
    
    # Afficher les résultats de validation s'ils sont disponibles
    if hasattr(st.session_state, 'validation_results'):
        results = st.session_state.validation_results
        doc = st.session_state.validated_document
        
        st.markdown("---")
        section_title("Validation Results")
        
        # Afficher le score de conformité
        st.markdown(f"""
        <div class="validation-result">
            <div class="validation-score" style="color: {'#4CAF50' if results['compliance_score'] >= 90 else '#FFC107' if results['compliance_score'] >= 75 else '#F44336'};">
                {results['compliance_score']}%
            </div>
            <div class="validation-status">
                <span style="
                    background-color: {'#4CAF50' if results['compliance_score'] >= 90 else '#FFC107' if results['compliance_score'] >= 75 else '#F44336'};
                    color: white;
                    padding: 5px 15px;
                    border-radius: 15px;
                    font-weight: 600;
                ">
                    {results['status']}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Disposition en deux colonnes
        col1, col2 = st.columns(2)
        
        with col1:
            # Afficher les sections manquantes
            st.markdown("### Missing Sections")
            
            if results["missing_sections"]:
                for section in results["missing_sections"]:
                    st.markdown(f"""
                    <div class="issue-item">
                        <div class="issue-icon">❌</div>
                        <div>{section}</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.success("No missing sections detected.")
        
        with col2:
            # Afficher les problèmes de conformité
            st.markdown("### Compliance Issues")
            
            if results["compliance_issues"]:
                for issue in results["compliance_issues"]:
                    st.markdown(f"""
                    <div class="issue-item">
                        <div class="issue-icon">⚠️</div>
                        <div>{issue}</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.success("No compliance issues detected.")
        
        # Afficher les recommandations
        st.markdown("### Recommendations")
        
        if results["recommendations"]:
            for recommendation in results["recommendations"]:
                st.info(recommendation)
        else:
            st.success("No recommendations needed. Document meets all requirements.")
        
        # Afficher les détails du document
        st.markdown("### Document Details")
        
        # Créer un DataFrame pour l'affichage
        doc_details = pd.DataFrame({
            "Property": ["ID", "Title", "Type", "Organization", "Submission Date"],
            "Value": [doc["id"], doc["title"], doc["type"], doc["organization"], doc["submission_date"]]
        })
        
        st.dataframe(doc_details, use_container_width=True, hide_index=True)
    
    # Section d'explication
    st.markdown("---")
    st.markdown("""
    ### How the Document Validation Works
    
    In the production version, the Smart Evaluator Assistant will use advanced Natural Language Processing (NLP) to validate accreditation documents:
    
    1. **Document Structure Analysis**: Identifies sections and their completeness
    2. **Standard Compliance Check**: Verifies alignment with relevant accreditation standards
    3. **Missing Information Detection**: Identifies gaps in required documentation
    4. **Cross-Reference Validation**: Ensures consistency across related documents
    
    The system will support both Arabic and English documents, with specialized models trained on accreditation terminology.
    """)
    
    # Pied de page
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Smart Evaluator Assistant - Prototype Version</p>
        <p>© 2025 Saudi Accreditation Center</p>
    </div>
    """, unsafe_allow_html=True)
