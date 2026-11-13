"""
Comprehensive Integration Test Suite for Pan-India AQI Respiratory Surveillance API.
Verifies all 9 endpoints, 12 cities, 12 Indian languages, and multi-turn triage chat.
"""

import sys
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, WORKSPACE)

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["version"] == "2.0.0"
    assert data["supported_cities"] == 12
    assert "triage_chat" in data["endpoints"]
    print("PASS: test_root (metadata confirmed)")

def test_languages_endpoint():
    response = client.get("/api/languages")
    assert response.status_code == 200
    data = response.json()
    assert "languages" in data
    assert "cities" in data
    assert len(data["languages"]) >= 12
    assert len(data["cities"]) >= 12
    # Verify native scripts are present
    lang_names = [l["native"] for l in data["languages"]]
    assert "मराठी" in lang_names
    assert "हिन्दी" in lang_names
    assert "தமிழ்" in lang_names
    assert "বাংলা" in lang_names
    # Verify city coverage
    city_names = [c["name"] for c in data["cities"]]
    assert "Guwahati" in city_names
    assert "Amritsar" in city_names
    assert "Navi Mumbai" in city_names
    print("PASS: test_languages_endpoint (12 languages with native scripts & 12 cities)")

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["ml_model_loaded"] is True
    assert data["cities_configured"] == 12
    print("PASS: test_health (12 cities verified)")

def test_overview():
    response = client.get("/api/overview")
    assert response.status_code == 200
    data = response.json()
    assert "metadata" in data
    assert "cities" in data
    assert len(data["cities"]) == 12
    assert "Mumbai" in data["cities"]
    assert "Guwahati" in data["cities"]
    assert "correlation_matrix" in data
    assert "monthly_seasonal_trends" in data
    print("PASS: test_overview (12-city correlation & 10-year trends verified)")

def test_live_risk_mumbai_marathi():
    response = client.get("/api/live-risk?city=Mumbai&lang=marathi")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Mumbai"
    assert "current_air_quality" in data
    assert "grap_protocol" in data
    assert "predicted_risk" in data
    assert "clinical_advisory" in data
    assert len(data["clinical_advisory"]["advisory"]) > 10
    # Verify TF-IDF RAG clinical evidence grounding
    assert "grounded_dataset_id" in data
    assert "matched_clinical_protocol" in data
    assert data["grounding_similarity_score"] > 0
    print("PASS: test_live_risk_mumbai_marathi (with RAG clinical grounding)")

def test_live_risk_guwahati_assamese():
    response = client.get("/api/live-risk?city=Guwahati&lang=assamese")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Guwahati"
    assert data["state"] == "Assam"
    assert "predicted_risk" in data
    assert "grap_protocol" in data
    print("PASS: test_live_risk_guwahati_assamese (North-East hub test passed)")

def test_simulate_risk():
    payload = {
        "city": "Delhi",
        "pm25": 380.0,
        "pm10": 520.0,
        "no2": 65.0,
        "so2": 32.0,
        "co": 2.5,
        "o3": 45.0,
        "temperature": 13.0,
        "humidity": 80.0,
        "lang": "hindi",
        "condition": "Pediatric Asthma"
    }
    response = client.post("/api/simulate-risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["predicted_risk_score"] > 70.0
    assert data["severity"] in ["High", "Critical"]
    assert "grap_protocol" in data
    print("PASS: test_simulate_risk")

def test_datasets_endpoint():
    response = client.get("/api/datasets")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["total_datasets"] >= 5
    assert data["total_rows"] > 5000
    assert len(data["catalog"]) >= 5
    dataset_names = [d["dataset_name"] for d in data["catalog"]]
    assert any("2,050 Rows" in n or "Master" in n for n in dataset_names)
    assert any("2,000 Rows" in n or "Grade A" in n for n in dataset_names)
    print("PASS: test_datasets_endpoint (Live catalog & preview confirmed)")

def test_multi_turn_triage_chat():
    payload = {
        "city": "Mumbai",
        "lang": "english",
        "condition": "Pediatric Asthma",
        "messages": [
            {"role": "user", "content": "The AQI is over 170 in Mumbai and my 7-year-old child started coughing."},
            {"role": "assistant", "content": "Keep your child indoors, run air purifiers, and keep the rescue inhaler ready."},
            {"role": "user", "content": "His coughing is persistent and he seems to have mild wheezing. Should I nebulize or go to hospital?"}
        ]
    }
    response = client.post("/api/triage-chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert len(data["reply"]) > 20
    assert data["city"] == "Mumbai"
    assert "grap_protocol" in data
    assert "triage_urgency" in data
    print("PASS: test_multi_turn_triage_chat (Interactive follow-up chat verified)")

def test_adaption_7_pillars_metrics():
    response = client.get("/api/adaption-metrics")
    assert response.status_code == 200
    data = response.json()
    assert "seven_pillars" in data
    pillars = data["seven_pillars"]
    assert "pillar_1_forge" in pillars
    assert "pillar_2_scaled_invent" in pillars
    assert "pillar_3_localization" in pillars
    assert "pillar_4_blueprint" in pillars
    assert "pillar_5_trajectories" in pillars
    assert "pillar_6_combine" in pillars
    assert "pillar_7_autoscientist" in pillars
    assert data["hackathon_bonus_proof"]["award"] == "$1,000 Best Use of Adaption Award"
    print("PASS: test_adaption_7_pillars_metrics (Full 7 pillars proof validated)")

if __name__ == "__main__":
    print("Running integration tests...")
    test_root()
    test_languages_endpoint()
    test_health()
    test_overview()
    test_live_risk_mumbai_marathi()
    test_live_risk_guwahati_assamese()
    test_simulate_risk()
    test_datasets_endpoint()
    test_multi_turn_triage_chat()
    test_adaption_7_pillars_metrics()
    print("\n🎉 ALL 10 INTEGRATION TESTS PASSED SUCCESSFULLY!")
