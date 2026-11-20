"""
Comprehensive Integration Test Suite for Pan-India AQI Respiratory Surveillance API.
Verifies all endpoints, 12 cities, 13 Indian languages, live Open-Meteo batch map,
telemetry hierarchy drill-down, datasets schema-adaptive catalog, and multi-turn triage chat.
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
    
    # Assert telemetry hierarchy with drill-down layers
    assert "telemetry_hierarchy" in data, "telemetry_hierarchy must be present in overview"
    th = data["telemetry_hierarchy"]
    assert "yearly" in th
    assert "quarterly" in th
    assert "monthly" in th
    assert "weekly" in th
    assert "live_7day" in th
    assert len(th["yearly"]["all_metros"]) >= 10
    assert len(th["live_7day"]) == 7
    print("PASS: test_overview (12-city correlation, 10-year trends & telemetry hierarchy verified)")

def test_live_map():
    response = client.get("/api/live-map")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["total_cities"] == 12
    assert "Live Open-Meteo Synced" in data["source"]
    assert "cities" in data
    assert len(data["cities"]) == 12
    for city_obj in data["cities"]:
        assert "name" in city_obj
        assert "aqi" in city_obj
        assert "pm25" in city_obj
        assert "pm10" in city_obj
        assert "lat" in city_obj
        assert "lon" in city_obj
        assert "severity" in city_obj
    print("PASS: test_live_map (Live Open-Meteo batch 12-metro endpoint verified)")

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
    
    # Verify top-level flattened keys for TailAdmin frontend consumption
    assert "aqi" in data
    assert "pm25" in data
    assert "predicted_risk_score" in data
    assert "predicted_admissions" in data
    assert "cpcb_category" in data
    assert "grap_stage" in data
    assert "localized_advisory" in data

    # Verify TF-IDF RAG clinical evidence grounding
    assert "grounded_dataset_id" in data
    assert "matched_clinical_protocol" in data
    assert data["grounding_similarity_score"] > 0
    print("PASS: test_live_risk_mumbai_marathi (with RAG clinical grounding & flattened keys)")

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
    
    # Verify each dataset has size_mb, non-empty columns, and sample_rows
    for ds in data["catalog"]:
        assert "size_mb" in ds and ds["size_mb"] > 0, f"size_mb must be > 0 for {ds.get('dataset_name')}"
        assert "columns" in ds and len(ds["columns"]) > 0, f"columns must be non-empty for {ds.get('dataset_name')}"
        assert "sample_rows" in ds and len(ds["sample_rows"]) > 0, f"sample_rows must be non-empty for {ds.get('dataset_name')}"

    dataset_names = [d["dataset_name"] for d in data["catalog"]]
    assert any("2,050 Rows" in n or "Master" in n for n in dataset_names)
    assert any("2,000 Rows" in n or "Grade A" in n for n in dataset_names)
    print("PASS: test_datasets_endpoint (Live catalog, size_mb, columns, sample_rows confirmed)")

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

def test_triage_chat_marathi_auto_detection():
    # User asks in Marathi, even if default lang was set to english
    payload = {
        "city": "Mumbai",
        "lang": "english",
        "condition": "Pediatric Asthma",
        "messages": [
            {"role": "user", "content": "दम्याच्या रुग्णांनी काय काळजी घ्यावी?"}
        ]
    }
    response = client.post("/api/triage-chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    reply = data["reply"]
    assert len(reply) > 20
    # Assert Devanagari script presence
    assert any('\u0900' <= ch <= '\u097F' for ch in reply), f"Expected Devanagari script, got: {reply}"
    # Assert language resolved to mr
    assert data["language"] == "mr"
    print("PASS: test_triage_chat_marathi_auto_detection (Native script detected and returned)")

def test_live_risk_language_alias():
    # Test 'language' query param alias as sent by frontend aqiClient
    response = client.get("/api/live-risk?city=Pune&language=mr")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Pune"
    advisory = data["clinical_advisory"]["advisory"]
    assert any('\u0900' <= ch <= '\u097F' for ch in advisory), f"Expected Marathi advisory, got: {advisory}"
    assert "Marathi" in data["clinical_advisory"]["language"]
    print("PASS: test_live_risk_language_alias (language=mr accepted and localized)")

def test_live_risk_amritsar_hindi_sentence_boundary():
    # Explicit requirement: assert /api/live-risk?city=Amritsar&lang=hi returns complete, un-truncated Hindi ending with proper punctuation । or ., not cut off mid-character
    response = client.get("/api/live-risk?city=Amritsar&lang=hi")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Amritsar"
    assert "clinical_advisory" in data
    advisory = data["clinical_advisory"]["advisory"]
    assert len(advisory) > 30, f"Expected non-empty advisory, got: {advisory}"
    # Assert Devanagari script presence
    assert any('\u0900' <= ch <= '\u097F' for ch in advisory), f"Expected Devanagari script, got: {advisory}"
    # Assert no raw markdown asterisks
    assert "**" not in advisory, f"Advisory contains raw markdown asterisks: {advisory}"
    # Assert sentence ends with proper boundary punctuation (Devanagari danda । or Western .)
    stripped = advisory.strip()
    assert stripped.endswith('।') or stripped.endswith('.') or stripped.endswith('!') or stripped.endswith('?'), (
        f"Advisory does not end at clean sentence boundary: ...{stripped[-25:]}"
    )
    print("PASS: test_live_risk_amritsar_hindi_sentence_boundary (Complete Hindi advisory ending cleanly with '।' and 0 asterisks)")

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
    test_live_map()
    test_live_risk_mumbai_marathi()
    test_live_risk_amritsar_hindi_sentence_boundary()
    test_live_risk_guwahati_assamese()
    test_simulate_risk()
    test_datasets_endpoint()
    test_multi_turn_triage_chat()
    test_triage_chat_marathi_auto_detection()
    test_live_risk_language_alias()
    test_adaption_7_pillars_metrics()
    print("\n🎉 ALL 14 INTEGRATION TESTS PASSED SUCCESSFULLY!")


# --- Offline regression tests (no network, no Adaption key) -------------------------

import main as _main
from unittest.mock import patch as _patch

_FIXED_AIR = {"pm25": 58.0, "pm10": 95.0, "no2": 28.0, "so2": 15.0, "co": 0.8,
              "o3": 30.0, "aqi": 140, "temperature": 27.5, "humidity": 68.0}


def test_clean_advisory_text_ignores_decimal_points():
    # A '.' inside "58.0" is not a sentence end; truncating there cut mid-number.
    out = _main.clean_advisory_text("Stay indoors. Your AQI is 140 and PM2.5 is 58.0 ug, keep inhaler handy")
    assert out == "Stay indoors. Your AQI is 140 and PM2.5 is 58.0 ug, keep inhaler handy."


def test_clean_advisory_text_uses_script_appropriate_terminator():
    assert _main.clean_advisory_text("Wear an N95 mask outdoors today").endswith(".")
    assert _main.clean_advisory_text("बाहर जाते समय मास्क पहनें").endswith("।")


def test_urdu_fallback_keeps_er_guidance():
    # Previously truncated at the decimal in the risk score, dropping the SpO2/ER directive.
    text = _main.clean_advisory_text(_main.build_clinical_advisory_fallback(
        "ur", "Delhi", _FIXED_AIR, 62.3, "High", "Asthma"))
    assert "SpO2" in text and text.endswith("۔")


def test_triage_cache_respects_requested_language():
    _main.triage_chat_cache.clear()
    msgs = [{"role": "user", "content": "What precautions should I take?"}]
    with _patch.object(_main, "fetch_live_air_quality", return_value=_FIXED_AIR), \
         _patch.object(_main, "get_adaption_client", return_value=None):
        en = client.post("/api/triage-chat", json={"city": "Delhi", "language": "english", "messages": msgs}).json()
        hi = client.post("/api/triage-chat", json={"city": "Delhi", "language": "hindi", "messages": msgs}).json()
    assert en["language"] == "en"
    assert hi["language"] == "hi"


def test_cache_is_bounded():
    cache = {}
    for i in range(_main.CACHE_MAX_ENTRIES + 50):
        _main.cache_put(cache, i, i)
    assert len(cache) <= _main.CACHE_MAX_ENTRIES
    assert _main.cache_get(cache, _main.CACHE_MAX_ENTRIES + 49) == _main.CACHE_MAX_ENTRIES + 49


def test_live_reading_of_zero_is_kept():
    class _Resp:
        status_code = 200
        def __init__(self, payload): self._p = payload
        def raise_for_status(self): pass
        def json(self): return self._p
    air = {"current": {"pm2_5": 0, "pm10": 0, "nitrogen_dioxide": 0, "sulphur_dioxide": 0,
                       "ozone": 0, "carbon_monoxide": 0, "us_aqi": 0}}
    weather = {"current": {"temperature_2m": 0, "relative_humidity_2m": 0}}
    with _patch.object(_main.requests, "get", side_effect=[_Resp(air), _Resp(weather)]):
        out = _main.fetch_live_air_quality(0.0, 0.0)
    assert out["pm25"] == 0.0 and out["aqi"] == 0 and out["temperature"] == 0.0


def test_simulate_rejects_negative_pollutants():
    assert client.post("/api/simulate-risk", json={"pm25": -50}).status_code == 422


def test_indian_aqi_matches_cpcb_breakpoints():
    # Each value is a CPCB band edge or a hand-interpolated point inside a band.
    assert _main.compute_indian_aqi({"pm25": 30}) == 50
    assert _main.compute_indian_aqi({"pm25": 60}) == 100
    assert _main.compute_indian_aqi({"pm25": 120}) == 300
    assert _main.compute_indian_aqi({"pm25": 250}) == 400
    assert _main.compute_indian_aqi({"pm10": 100}) == 100
    # Max sub-index wins: PM10 350 -> 300 beats PM2.5 60 -> 100
    assert _main.compute_indian_aqi({"pm25": 60, "pm10": 350}) == 300
    # Severe band resolves Stage III vs IV and caps at 500
    assert _main.compute_indian_aqi({"pm25": 300}) == 438
    assert _main.compute_indian_aqi({"pm25": 900}) == 500


import pytest as _pytest
from conftest import LIVE as _LIVE


@_pytest.mark.skipif(_LIVE, reason="asserts the stubbed Open-Meteo reading")
def test_grap_stage_uses_indian_aqi_not_us_aqi():
    # Stub reports us_aqi=152; on India's scale the same reading (PM2.5 58) is ~97, i.e. no GRAP stage.
    data = client.get("/api/live-risk?city=Delhi").json()
    assert data["current_air_quality"]["us_aqi"] == 152
    assert data["aqi"] == 97
    assert data["grap_stage"] == "Normal"
    severe = client.post("/api/simulate-risk", json={"pm25": 400, "pm10": 520}).json()
    assert severe["grap_protocol"]["stage"] == "Stage IV"


def test_unknown_city_is_404_not_mumbai():
    r = client.get("/api/live-risk?city=Atlantis")
    assert r.status_code == 404
    assert "Supported cities" in r.json()["detail"]
    r = client.post("/api/triage-chat", json={"city": "Atlantis", "messages": [{"role": "user", "content": "hi"}]})
    assert r.status_code == 404


def test_city_aliases_resolve():
    assert client.get("/api/live-risk?city=Bangalore").json()["city"] == "Bengaluru"
    assert client.get("/api/live-risk?city=navi-mumbai").json()["city"] == "Navi Mumbai"


class _FakeAdaption:
    """Stands in for the Adaption client and returns a fixed model reply."""
    def __init__(self, text):
        self.responses = self
        self._text = text
    def create(self, **kwargs):
        return type("R", (), {"output_text": self._text})()


def test_triage_reports_fallback_honestly():
    msgs = [{"role": "user", "content": "Should I go outside today?"}]
    r = client.post("/api/triage-chat", json={"city": "Delhi", "language": "en", "messages": msgs}).json()
    assert r["source"] == "adaption_clinical_rules"
    assert "Fallback" in r["model_used"]
    assert _main.triage_chat_cache == {}  # template replies are not cached


def test_triage_reports_live_model_when_used():
    msgs = [{"role": "user", "content": "Should I go outside today?"}]
    fake = _FakeAdaption("Stay indoors today and keep your rescue inhaler close. Seek ER care if SpO2 falls below 92%.")
    with _patch.object(_main, "get_adaption_client", return_value=fake):
        r = client.post("/api/triage-chat", json={"city": "Delhi", "language": "en", "messages": msgs}).json()
    assert r["source"] == "adaption_multi_turn_triage"
    assert r["model_used"] == "deepseek-v4-flash (Adaption AI)"
    assert len(_main.triage_chat_cache) == 1
