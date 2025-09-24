import streamlit as st
import pandas as pd
import os
import sys
import random

# Ajouter le répertoire courant au chemin Python pour les imports relatifs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importer les modules utilitaires
from utils.ui_components import section_title, info_box, action_button, status_badge
from utils.data_generator import load_data
from utils.mock_algorithms import simulate_evaluator_matching, algorithm_info_box

def show_evaluator_matching():
    """Affiche la page de correspondance des évaluateurs"""
    # Charger les données
    data = load_data()
    documents = data["documents"]
    evaluators = data["evaluators"]
    
    # Titre de la page
    st.title("Evaluator Matching")
    
    # Section d'information sur l'algorithme
    algorithm_info_box("evaluator_matching")
    
    # Disposition en deux colonnes
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Section de sélection de document
        section_title("Select Document")
        
        # Filtrer les documents en attente
        pending_docs = [d for d in documents if d["status"] == "Pending"]
        
        if not pending_docs:
            st.info("No pending documents available for evaluator assignment.")
            return
        
        # Créer une liste de sélection
        doc_options = {f"{doc['id']} - {doc['title']}": doc for doc in pending_docs}
        selected_doc_key = st.selectbox(
            "Select a document to assign an evaluator:",
            options=list(doc_options.keys())
        )
        
        # Récupérer le document sélectionné
        selected_doc = doc_options[selected_doc_key]
        
        # Afficher les détails du document
        st.markdown("### Document Details")
        st.markdown(f"**ID:** {selected_doc['id']}")
        st.markdown(f"**Title:** {selected_doc['title']}")
        st.markdown(f"**Type:** {selected_doc['type']}")
        st.markdown(f"**Organization:** {selected_doc['organization']}")
        st.markdown(f"**Submission Date:** {selected_doc['submission_date']}")
        st.markdown(f"**Compliance Score:** {selected_doc['compliance_score']}%")
        
        # Bouton pour lancer la correspondance
        if st.button("Find Matching Evaluators", type="primary"):
            # Simuler la correspondance d'évaluateurs
            matches = simulate_evaluator_matching(selected_doc, evaluators)
            
            # Stocker les résultats dans la session
            st.session_state.evaluator_matches = matches
            st.session_state.selected_document = selected_doc
    
    with col2:
        # Section des résultats de correspondance
        section_title("Matching Results")
        
        # Vérifier si des correspondances sont disponibles
        if hasattr(st.session_state, 'evaluator_matches') and st.session_state.evaluator_matches:
            matches = st.session_state.evaluator_matches
            selected_doc = st.session_state.selected_document
            
            # Afficher les correspondances
            for i, match in enumerate(matches[:5]):  # Limiter à 5 correspondances
                evaluator = match["evaluator"]
                
                # Créer une carte pour chaque évaluateur
                st.markdown(f"""
                <div class="evaluator-card">
                    <div class="evaluator-header">
                        <div class="evaluator-name">{evaluator['name']}</div>
                        <div class="evaluator-rating">{'⭐' * int(evaluator['performance_rating'])} ({evaluator['performance_rating']})</div>
                    </div>
                    <div class="evaluator-details">
                        <div class="evaluator-detail">
                            <span class="evaluator-detail-label">Specialties:</span> {', '.join(evaluator['specialties'])}
                        </div>
                        <div class="evaluator-detail">
                            <span class="evaluator-detail-label">Region:</span> {evaluator['region']}
                        </div>
                        <div class="evaluator-detail">
                            <span class="evaluator-detail-label">Experience:</span> {evaluator['experience']} years
                        </div>
                        <div class="evaluator-detail">
                            <span class="evaluator-detail-label">Availability:</span> {evaluator['availability']}
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="font-weight: bold;">Match Score:</span> 
                                <span style="font-size: 1.2rem; color: {'#4CAF50' if match['match_score'] >= 80 else '#FFC107' if match['match_score'] >= 60 else '#F44336'};">
                                    {match['match_score']}%
                                </span>
                            </div>
                            <div>
                                {status_badge('High Risk' if match['conflict_of_interest'] else 'Approved')}
                            </div>
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <span style="font-weight: bold;">Match Reasons:</span>
                        <ul style="margin-top: 5px;">
                            {' '.join(f'<li>{reason}</li>' for reason in match['match_reasons'])}
                        </ul>
                    </div>
                    <div style="display: flex; justify-content: flex-end; margin-top: 10px;">
                        <button style="background-color: {'#F44336' if match['conflict_of_interest'] else '#4CAF50'}; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer;">
                            {'Cannot Assign' if match['conflict_of_interest'] else 'Assign Evaluator'}
                        </button>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Ajouter un espace entre les cartes
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        else:
            st.info("Select a document and click 'Find Matching Evaluators' to see results.")
    
    # Section d'explication
    st.markdown("---")
    st.markdown("""
    ### How the Matching Algorithm Works
    
    In the production version, the Smart Evaluator Assistant will use a sophisticated AI algorithm to match evaluators with accreditation applications. The algorithm will consider:
    
    1. **Expertise Matching**: Aligns evaluator specialties with document requirements
    2. **Availability**: Considers evaluator workload and schedule
    3. **Geographic Proximity**: Optimizes for location to reduce travel costs
    4. **Performance History**: Prioritizes evaluators with strong track records
    5. **Conflict of Interest Detection**: Identifies potential conflicts using relationship analysis
    
    The algorithm will continuously learn from feedback to improve matching quality over time.
    """)
    
    # Pied de page
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Smart Evaluator Assistant - Prototype Version</p>
        <p>© 2025 Saudi Accreditation Center</p>
    </div>
    """, unsafe_allow_html=True)
