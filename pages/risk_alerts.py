import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys
import random

# Ajouter le répertoire courant au chemin Python pour les imports relatifs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importer les modules utilitaires
from utils.ui_components import section_title, info_box, status_badge
from utils.data_generator import load_data
from utils.mock_algorithms import simulate_risk_scoring, algorithm_info_box

def show_risk_alerts():
    """Affiche la page d'alertes de risque"""
    # Charger les données
    data = load_data()
    documents = data["documents"]
    alerts = data["alerts"]
    
    # Titre de la page
    st.title("Risk Alerts & Predictive Analytics")
    
    # Section d'information sur l'algorithme
    algorithm_info_box("risk_scoring")
    
    # Section de tableau de bord des risques
    section_title("Risk Dashboard")
    
    # Calculer les statistiques de risque
    high_risk = len([a for a in alerts if "High" in a["risk_level"]])
    medium_risk = len([a for a in alerts if "Medium" in a["risk_level"]])
    low_risk = len([a for a in alerts if "Low" in a["risk_level"]])
    total_alerts = len(alerts)
    
    # Afficher les statistiques dans une grille
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Alerts", f"{total_alerts}")
    
    with col2:
        st.metric("High Risk", f"{high_risk}", f"{high_risk/total_alerts*100:.1f}%", "inverse")
    
    with col3:
        st.metric("Medium Risk", f"{medium_risk}", f"{medium_risk/total_alerts*100:.1f}%", "inverse")
    
    with col4:
        st.metric("Low Risk", f"{low_risk}", f"{low_risk/total_alerts*100:.1f}%", "off")
    
    # Graphique de distribution des risques
    st.subheader("Risk Distribution")
    
    # Créer le DataFrame pour Plotly
    risk_data = {
        "Risk Level": ["High Risk", "Medium Risk", "Low Risk"],
        "Count": [high_risk, medium_risk, low_risk]
    }
    df_risk = pd.DataFrame(risk_data)
    
    # Définir les couleurs pour chaque niveau de risque
    risk_colors = {
        "High Risk": "#F44336",
        "Medium Risk": "#FF9800",
        "Low Risk": "#4CAF50"
    }
    
    # Créer le graphique à barres
    fig = px.bar(
        df_risk,
        x="Risk Level",
        y="Count",
        color="Risk Level",
        color_discrete_map=risk_colors,
        text="Count"
    )
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=30, b=20),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Section d'analyse de risque pour un document spécifique
    st.markdown("---")
    section_title("Document Risk Analysis")
    
    # Créer une liste de sélection
    doc_options = {f"{doc['id']} - {doc['title']}": doc for doc in documents}
    selected_doc_key = st.selectbox(
        "Select a document to analyze:",
        options=list(doc_options.keys())
    )
    
    # Récupérer le document sélectionné
    selected_doc = doc_options[selected_doc_key]
    
    # Bouton pour lancer l'analyse de risque
    if st.button("Analyze Risk", type="primary"):
        # Simuler l'analyse de risque
        risk_results = simulate_risk_scoring(selected_doc)
        
        # Stocker les résultats dans la session
        st.session_state.risk_results = risk_results
        st.session_state.risk_document = selected_doc
    
    # Afficher les résultats d'analyse de risque s'ils sont disponibles
    if hasattr(st.session_state, 'risk_results'):
        results = st.session_state.risk_results
        doc = st.session_state.risk_document
        
        # Disposition en deux colonnes
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Afficher les détails du document
            st.markdown("### Document Details")
            st.markdown(f"**ID:** {doc['id']}")
            st.markdown(f"**Title:** {doc['title']}")
            st.markdown(f"**Type:** {doc['type']}")
            st.markdown(f"**Organization:** {doc['organization']}")
            st.markdown(f"**Submission Date:** {doc['submission_date']}")
            st.markdown(f"**Compliance Score:** {doc['compliance_score']}%")
            
            # Afficher les facteurs de risque
            st.markdown("### Risk Factors")
            
            for factor in results["risk_factors"]:
                st.markdown(f"- {factor}")
            
            # Afficher les recommandations d'atténuation
            st.markdown("### Mitigation Recommendations")
            
            for recommendation in results["mitigation_recommendations"]:
                st.info(recommendation)
        
        with col2:
            # Afficher le score de risque
            st.markdown("""
            <div style="
                background-color: #f5f5f5;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            ">
                <h3 style="margin-top: 0;">Risk Score</h3>
                <div style="
                    font-size: 48px;
                    font-weight: bold;
                    color: #F44336;
                    margin: 20px 0;
                ">
                    {risk_score}%
                </div>
                <div>
                    {risk_badge}
                </div>
            </div>
            """.format(
                risk_score=results["risk_score"],
                risk_badge=status_badge(results["risk_level"])
            ), unsafe_allow_html=True)
            
            # Afficher une jauge de risque
            st.markdown("### Risk Gauge")
            
            # Créer une jauge avec Plotly
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=results["risk_score"],
                domain={"x": [0, 1], "y": [0, 1]},
                title={"text": "Risk Level"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#F44336" if results["risk_score"] >= 70 else "#FF9800" if results["risk_score"] >= 40 else "#4CAF50"},
                    "steps": [
                        {"range": [0, 40], "color": "#E8F5E9"},
                        {"range": [40, 70], "color": "#FFF3E0"},
                        {"range": [70, 100], "color": "#FFEBEE"}
                    ],
                    "threshold": {
                        "line": {"color": "red", "width": 4},
                        "thickness": 0.75,
                        "value": 70
                    }
                }
            ))
            
            fig.update_layout(
                height=250,
                margin=dict(l=20, r=20, t=30, b=20),
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # Section d'alertes actives
    st.markdown("---")
    section_title("Active Alerts")
    
    # Filtrer les alertes actives
    active_alerts = [a for a in alerts if a["status"] == "Active"]
    
    if active_alerts:
        # Créer un DataFrame pour l'affichage
        alerts_data = []
        for alert in active_alerts:
            # Trouver le document associé
            doc = next((d for d in documents if d["id"] == alert["document_id"]), None)
            
            if doc:
                alerts_data.append({
                    "Alert ID": alert["id"],
                    "Type": alert["type"],
                    "Document": doc["title"],
                    "Organization": doc["organization"],
                    "Date": alert["date"],
                    "Risk Level": alert["risk_level"],
                    "Risk Score": f"{alert['risk_score']}%"
                })
        
        # Convertir en DataFrame
        df_alerts = pd.DataFrame(alerts_data)
        
        # Afficher le tableau
        st.dataframe(df_alerts, use_container_width=True)
    else:
        st.info("No active alerts at the moment.")
    
    # Section d'explication
    st.markdown("---")
    st.markdown("""
    ### How the Risk Scoring Algorithm Works
    
    In the production version, the Smart Evaluator Assistant will use a sophisticated predictive analytics model to assess risks:
    
    1. **Feature Engineering**: Extract 50+ risk indicators from application data
    2. **Machine Learning Model**: XGBoost ensemble model trained on historical accreditation data
    3. **Time Series Analysis**: Detect patterns and trends in historical data
    4. **Anomaly Detection**: Identify unusual patterns that may indicate risks
    
    The system will provide early warnings of potential issues, allowing for proactive intervention.
    """)
    
    # Section de biais algorithmique
    st.markdown("---")
    section_title("Algorithm Fairness & Bias Mitigation")
    
    # Afficher les informations sur la mitigation des biais
    algorithm_info_box("bias_mitigation")
    
    # Pied de page
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Smart Evaluator Assistant - Prototype Version</p>
        <p>© 2025 Saudi Accreditation Center</p>
    </div>
    """, unsafe_allow_html=True)
