# Smart Evaluator Assistant - Prototype

A functional prototype of the Smart Evaluator Assistant, showing how the system will work in real accreditation scenarios.

## About
The Smart Evaluator Assistant is an AI-driven solution to transform the accreditation process of the Saudi Accreditation Center (SAC). This prototype demonstrates the system architecture and workflow with dummy data, preparing for future integration of advanced algorithms.

## Features
### Dashboard
- KPI cards (Documents processed, Compliance %, Active Evaluators, Alerts)  
- Compliance chart (bar/pie)  
- Risk alerts list  
- Evaluator assignment table  
- Process timeline  

### Evaluator Matching
- Table with evaluators (name, specialty, location, availability)  
- "Assign" button (simulated)  
- Conflict of interest indicator (dummy logic)  

### Document Validation
- File upload (dummy PDFs)  
- Simulated checks (missing sections, non-compliance)  
- Pass/Fail summary with recommendations  

## Technologies
- **Frontend & Backend**: Streamlit (Python)  
- **Visualization**: Plotly, Matplotlib, Altair  
- **Data management**: Pandas  
- **Document simulation**: PyPDF2  
- **Styling**: CSS + Streamlit theming  
- **RTL support**: CSS for Arabic  

## Installation
```bash
git clone https://github.com/amochi19831/smart-evaluator-prototype.git
cd smart-evaluator-prototype
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure
```
smart_evaluator_prototype/
├── app.py
├── pages/
├── data/
├── utils/
├── assets/
├── requirements.txt
└── README.md
```

## Important Note for Judges
This Phase 1 prototype uses dummy data to demonstrate architecture and workflow. In the next stage, real accreditation data and advanced algorithms (Arabic NLP, predictive analytics, evaluator matching) will replace the simulations.

## Next Steps
- Integrate real NLP for document validation  
- AI-based evaluator matching  
- Predictive risk analysis  
- Connect to real data sources  

## License

