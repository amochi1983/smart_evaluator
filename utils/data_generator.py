import json
import random
import os
import datetime
from pathlib import Path

# Constantes pour la génération de données
DOCUMENT_TYPES = ["ISO 17025", "ISO 15189", "ISO 17020", "ISO 17043", "ISO 17065"]
EVALUATOR_SPECIALTIES = ["Chemical Testing", "Medical Testing", "Calibration", "Inspection", "Certification"]
REGIONS = ["Riyadh", "Jeddah", "Dammam", "Makkah", "Madinah", "Abha", "Tabuk"]
RISK_TYPES = ["Document Incomplete", "Conflict of Interest", "Process Delay", "Compliance Issue"]
STATUSES = ["Approved", "Pending", "Rejected", "In Progress", "Completed"]
RISK_LEVELS = ["High Risk", "Medium Risk", "Low Risk"]

def generate_documents(count=15):
    """Génère des données factices pour les documents"""
    documents = []
    
    for i in range(1, count + 1):
        # Générer une date de soumission aléatoire dans les 6 derniers mois
        days_ago = random.randint(0, 180)
        submission_date = (datetime.datetime.now() - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%d")
        
        # Générer un score de conformité aléatoire
        compliance_score = random.randint(60, 100)
        
        # Déterminer le statut en fonction du score de conformité
        if compliance_score >= 90:
            status = "Approved"
        elif compliance_score >= 75:
            status = "In Progress"
        else:
            status = random.choice(["Pending", "Rejected"])
        
        # Générer des sections manquantes aléatoires
        missing_sections = []
        if compliance_score < 90:
            possible_sections = ["Quality Manual", "Technical Records", "Personnel Records", "Equipment Calibration", "Method Validation"]
            num_missing = random.randint(0, 3)
            missing_sections = random.sample(possible_sections, num_missing)
        
        document = {
            "id": f"DOC-{i:03d}",
            "title": f"Accreditation Application {i}",
            "type": random.choice(DOCUMENT_TYPES),
            "organization": f"Organization {i}",
            "submission_date": submission_date,
            "compliance_score": compliance_score,
            "status": status,
            "missing_sections": missing_sections,
            "assigned_evaluator": f"EVA-{random.randint(1, 10):03d}" if status != "Pending" else None,
            "review_comments": f"Review comments for document {i}" if status != "Pending" else "",
            "arabic": {
                "title": f"طلب اعتماد {i}",
                "organization": f"مؤسسة {i}",
                "status": {
                    "Approved": "معتمد",
                    "Pending": "قيد الانتظار",
                    "Rejected": "مرفوض",
                    "In Progress": "قيد التنفيذ",
                    "Completed": "مكتمل"
                }.get(status, "")
            }
        }
        
        documents.append(document)
    
    return documents

def generate_evaluators(count=10):
    """Génère des données factices pour les évaluateurs"""
    evaluators = []
    
    for i in range(1, count + 1):
        # Générer une disponibilité aléatoire
        availability = random.choice(["Available", "Busy", "On Leave"])
        
        # Générer une expérience aléatoire (1-15 ans)
        experience = random.randint(1, 15)
        
        # Générer un nombre aléatoire d'évaluations effectuées
        evaluations_completed = random.randint(5, 50)
        
        # Générer une note de performance aléatoire
        performance_rating = round(random.uniform(3.0, 5.0), 1)
        
        # Générer des spécialités aléatoires (1-3)
        num_specialties = random.randint(1, 3)
        specialties = random.sample(EVALUATOR_SPECIALTIES, num_specialties)
        
        evaluator = {
            "id": f"EVA-{i:03d}",
            "name": f"Evaluator {i}",
            "arabic_name": f"مقيّم {i}",
            "specialties": specialties,
            "region": random.choice(REGIONS),
            "availability": availability,
            "experience": experience,
            "evaluations_completed": evaluations_completed,
            "performance_rating": performance_rating,
            "arabic": {
                "specialties": [
                    {"Chemical Testing": "الاختبارات الكيميائية",
                     "Medical Testing": "الاختبارات الطبية",
                     "Calibration": "المعايرة",
                     "Inspection": "التفتيش",
                     "Certification": "الشهادات"
                    }.get(specialty, specialty) for specialty in specialties
                ],
                "region": {
                    "Riyadh": "الرياض",
                    "Jeddah": "جدة",
                    "Dammam": "الدمام",
                    "Makkah": "مكة",
                    "Madinah": "المدينة",
                    "Abha": "أبها",
                    "Tabuk": "تبوك"
                }.get(random.choice(REGIONS), ""),
                "availability": {
                    "Available": "متاح",
                    "Busy": "مشغول",
                    "On Leave": "في إجازة"
                }.get(availability, "")
            }
        }
        
        evaluators.append(evaluator)
    
    return evaluators

def generate_alerts(count=5):
    """Génère des données factices pour les alertes de risque"""
    alerts = []
    
    for i in range(1, count + 1):
        # Générer une date aléatoire dans les 30 derniers jours
        days_ago = random.randint(0, 30)
        alert_date = (datetime.datetime.now() - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%d")
        
        # Générer un niveau de risque aléatoire
        risk_level = random.choice(RISK_LEVELS)
        
        # Générer un score de risque aléatoire
        risk_score = random.randint(1, 100)
        if risk_level == "High Risk":
            risk_score = random.randint(75, 100)
        elif risk_level == "Medium Risk":
            risk_score = random.randint(40, 74)
        else:
            risk_score = random.randint(1, 39)
        
        # Générer un document associé aléatoire
        document_id = f"DOC-{random.randint(1, 15):03d}"
        
        alert = {
            "id": f"ALERT-{i:03d}",
            "type": random.choice(RISK_TYPES),
            "description": f"Risk alert {i} description",
            "document_id": document_id,
            "date": alert_date,
            "risk_level": risk_level,
            "risk_score": risk_score,
            "status": "Active" if random.random() > 0.3 else "Resolved",
            "arabic": {
                "type": {
                    "Document Incomplete": "وثيقة غير مكتملة",
                    "Conflict of Interest": "تضارب المصالح",
                    "Process Delay": "تأخير في العملية",
                    "Compliance Issue": "مشكلة في الامتثال"
                }.get(random.choice(RISK_TYPES), ""),
                "description": f"وصف تنبيه المخاطر {i}",
                "risk_level": {
                    "High Risk": "مخاطر عالية",
                    "Medium Risk": "مخاطر متوسطة",
                    "Low Risk": "مخاطر منخفضة"
                }.get(risk_level, ""),
                "status": "نشط" if random.random() > 0.3 else "تم الحل"
            }
        }
        
        alerts.append(alert)
    
    return alerts

def generate_all_data():
    """Génère toutes les données factices et les enregistre dans des fichiers JSON"""
    # Créer le répertoire de données s'il n'existe pas
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Générer les données
    documents = generate_documents(15)
    evaluators = generate_evaluators(10)
    alerts = generate_alerts(5)
    
    # Enregistrer les données dans des fichiers JSON
    with open(data_dir / "documents.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)
    
    with open(data_dir / "evaluators.json", "w", encoding="utf-8") as f:
        json.dump(evaluators, f, ensure_ascii=False, indent=2)
    
    with open(data_dir / "alerts.json", "w", encoding="utf-8") as f:
        json.dump(alerts, f, ensure_ascii=False, indent=2)
    
    return {
        "documents": documents,
        "evaluators": evaluators,
        "alerts": alerts
    }

def load_data():
    """Charge les données depuis les fichiers JSON ou les génère si elles n'existent pas"""
    data_dir = Path("data")
    
    # Vérifier si les fichiers existent
    documents_file = data_dir / "documents.json"
    evaluators_file = data_dir / "evaluators.json"
    alerts_file = data_dir / "alerts.json"
    
    # Si l'un des fichiers n'existe pas, générer toutes les données
    if not (documents_file.exists() and evaluators_file.exists() and alerts_file.exists()):
        return generate_all_data()
    
    # Charger les données depuis les fichiers
    with open(documents_file, "r", encoding="utf-8") as f:
        documents = json.load(f)
    
    with open(evaluators_file, "r", encoding="utf-8") as f:
        evaluators = json.load(f)
    
    with open(alerts_file, "r", encoding="utf-8") as f:
        alerts = json.load(f)
    
    return {
        "documents": documents,
        "evaluators": evaluators,
        "alerts": alerts
    }

if __name__ == "__main__":
    # Si ce script est exécuté directement, générer les données
    generate_all_data()
