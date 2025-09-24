import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import sys
import datetime
import random

# Ajouter le répertoire courant au chemin Python pour les imports relatifs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importer les modules utilitaires
from utils.ui_components import kpi_card, section_title, info_box, status_badge
from utils.data_generator import load_data
from utils.mock_algorithms import algorithm_info_box

def show_dashboard():
    """Affiche le tableau de bord principal"""
    # Charger les données
    data = load_data()
    documents = data["documents"]
    evaluators = data["evaluators"]
    alerts = data["alerts"]
    
    # Titre de la page
    st.title("Smart Evaluator Assistant Dashboard")
    
    # Section KPI
    st.markdown("## Key Performance Indicators")
    
    # Calculer les KPIs
    total_documents = len(documents)
    active_evaluators = len([e for e in evaluators if e["availability"] == "Available"])
    avg_compliance = sum(doc["compliance_score"] for doc in documents) / total_documents if total_documents > 0 else 0
    active_alerts = len([a for a in alerts if a["status"] == "Active"])
    
    # Afficher les KPIs dans une grille
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        kpi_card("Documents Processed", f"{total_documents}")
    
    with col2:
        kpi_card("Compliance Rate", f"{avg_compliance:.1f}%", "+2.5%" if avg_compliance > 80 else "-1.2%")
    
    with col3:
        kpi_card("Active Evaluators", f"{active_evaluators}/{len(evaluators)}")
    
    with col4:
        kpi_card("Risk Alerts", f"{active_alerts}", "+2" if active_alerts > 3 else "-1", "inverse")
    
    # Section Graphiques
    st.markdown("---")
    section_title("Performance Analytics")
    
    # Disposition en deux colonnes pour les graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        # Graphique de conformité par type de document
        st.subheader("Compliance by Document Type")
        
        # Préparer les données pour le graphique
        doc_types = {}
        for doc in documents:
            doc_type = doc["type"]
            if doc_type not in doc_types:
                doc_types[doc_type] = {"count": 0, "total_score": 0}
            doc_types[doc_type]["count"] += 1
            doc_types[doc_type]["total_score"] += doc["compliance_score"]
        
        # Calculer les moyennes
        doc_type_avg = {
            doc_type: data["total_score"] / data["count"] 
            for doc_type, data in doc_types.items()
        }
        
        # Créer le DataFrame pour Plotly
        df_compliance = pd.DataFrame({
            "Document Type": list(doc_type_avg.keys()),
            "Average Compliance": list(doc_type_avg.values())
        })
        
        # Créer le graphique à barres
        fig = px.bar(
            df_compliance, 
            x="Document Type", 
            y="Average Compliance",
            color="Average Compliance",
            color_continuous_scale=["red", "yellow", "green"],
            range_color=[60, 100],
            labels={"Average Compliance": "Compliance Score (%)"}
        )
        
        fig.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=30, b=20),
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Graphique de statut des documents
        st.subheader("Document Status Distribution")
        
        # Compter les statuts
        status_counts = {}
        for doc in documents:
            status = doc["status"]
            if status not in status_counts:
                status_counts[status] = 0
            status_counts[status] += 1
        
        # Créer le DataFrame pour Plotly
        df_status = pd.DataFrame({
            "Status": list(status_counts.keys()),
            "Count": list(status_counts.values())
        })
        
        # Définir les couleurs pour chaque statut
        status_colors = {
            "Approved": "#4CAF50",
            "Pending": "#FFC107",
            "Rejected": "#F44336",
            "In Progress": "#2196F3",
            "Completed": "#4CAF50"
        }
        
        # Créer le graphique en secteurs
        fig = px.pie(
            df_status,
            values="Count",
            names="Status",
            color="Status",
            color_discrete_map=status_colors,
            hole=0.4
        )
        
        fig.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=30, b=20),
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section Alertes de Risque
    st.markdown("---")
    section_title("Risk Alerts")
    
    # Filtrer les alertes actives
    active_alerts_data = [a for a in alerts if a["status"] == "Active"]
    
    if active_alerts_data:
        # Afficher les alertes dans un tableau
        for alert in active_alerts_data:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # Trouver le document associé
                doc = next((d for d in documents if d["id"] == alert["document_id"]), None)
                
                st.markdown(f"""
                <div class="risk-alert risk-{'high' if 'High' in alert['risk_level'] else 'medium' if 'Medium' in alert['risk_level'] else 'low'}">
                    <h4>{alert['type']} - {alert['document_id']}</h4>
                    <p><strong>Description:</strong> {alert['description']}</p>
                    <p><strong>Organization:</strong> {doc['organization'] if doc else 'Unknown'}</p>
                    <p><strong>Date:</strong> {alert['date']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div style="height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    <div style="font-size: 24px; font-weight: bold; margin-bottom: 10px;">
                        {alert['risk_score']}%
                    </div>
                    <div>
                        {status_badge(alert['risk_level'])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No active risk alerts at the moment.")
    
    # Section Affectation des Évaluateurs
    st.markdown("---")
    section_title("Evaluator Assignments")
    
    # Filtrer les documents avec des évaluateurs assignés
    assigned_docs = [d for d in documents if d["assigned_evaluator"]]
    
    if assigned_docs:
        # Créer un DataFrame pour l'affichage
        assignments_data = []
        for doc in assigned_docs:
            # Trouver l'évaluateur assigné
            evaluator = next((e for e in evaluators if e["id"] == doc["assigned_evaluator"]), None)
            
            if evaluator:
                assignments_data.append({
                    "Document ID": doc["id"],
                    "Document Title": doc["title"],
                    "Organization": doc["organization"],
                    "Evaluator": evaluator["name"],
                    "Status": doc["status"],
                    "Submission Date": doc["submission_date"]
                })
        
        # Convertir en DataFrame
        df_assignments = pd.DataFrame(assignments_data)
        
        # Afficher le tableau
        st.dataframe(df_assignments, use_container_width=True)
    else:
        st.info("No evaluator assignments at the moment.")
    
    # Section Chronologie du Processus
    st.markdown("---")
    section_title("Process Timeline")
    
    # Définir les étapes du processus
    process_steps = [
        {"icon": "📝", "label": "Submission"},
        {"icon": "🔍", "label": "Document Validation"},
        {"icon": "👥", "label": "Evaluator Assignment"},
        {"icon": "📊", "label": "Assessment"},
        {"icon": "✅", "label": "Decision"}
    ]
    
    # Créer la chronologie
    st.markdown("""
    <div class="timeline-container">
    """, unsafe_allow_html=True)
    
    for step in process_steps:
        st.markdown(f"""
        <div class="timeline-step">
            <div class="timeline-step-icon">{step['icon']}</div>
            <div class="timeline-step-label">{step['label']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
    
    # Section Algorithmes
    st.markdown("---")
    section_title("AI Algorithms")
    
    # Afficher les informations sur les algorithmes
    algorithm_info_box("risk_scoring")
    
    # Pied de page
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Smart Evaluator Assistant - Prototype Version</p>
        <p>© 2025 Saudi Accreditation Center</p>
    </div>
    """, unsafe_allow_html=True)
