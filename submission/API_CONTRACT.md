# 📑 Pan-India AQI Surveillance Backend — Frontend Integration Guide

> **Live Production API**: `https://innovate-aqi-backend.onrender.com`  
> **Interactive Swagger Docs**: `https://innovate-aqi-backend.onrender.com/docs`  
> **Backend Service**: Pan-India Air Pollution & Respiratory Disease Surveillance API  
> **Target Frontend**: React.js / Next.js / Vite  
> **CORS**: Wide Open (`*`) — Ready for direct client-side fetch across all domains  
> **Regional Scale**: 12 Indian Metros across all zones + 12 Official Indian Languages in Native Scripts  

---

## 🚀 Quick Start for React Teammate

### 1. Environment Variable
In your React project's `.env`:
```env
VITE_API_BASE_URL="https://innovate-aqi-backend.onrender.com"
# For local offline development fallback:
# VITE_API_BASE_URL="http://localhost:8000"
```

### 2. Complete Copy-Paste JavaScript API Client (`src/services/api.js`)

```javascript
const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://innovate-aqi-backend.onrender.com';

export const aqiApi = {
  // 1. Fetch 12 Indian Languages (with native scripts) and 12 Mapped Metros
  async getLanguagesAndCities() {
    const res = await fetch(`${BASE_URL}/api/languages`);
    if (!res.ok) throw new Error(`Languages fetch failed: ${res.statusText}`);
    return await res.json();
  },

  // 2. 10-Year Historical Trends, Pearson Correlation Matrix & 12-City Summaries
  async getOverview() {
    const res = await fetch(`${BASE_URL}/api/overview`);
    if (!res.ok) throw new Error(`Overview fetch failed: ${res.statusText}`);
    return await res.json();
  },

  // 3. Live AQI, ML Surge Risk, CAQM GRAP Stage, and Adaption Clinical Advisory
  async getLiveRisk(city = 'Mumbai', lang = 'english', condition = 'Bronchial Asthma & COPD') {
    const params = new URLSearchParams({ city, lang, condition });
    const res = await fetch(`${BASE_URL}/api/live-risk?${params.toString()}`);
    if (!res.ok) throw new Error(`Live risk fetch failed: ${res.statusText}`);
    return await res.json();
  },

  // 4. Multi-Turn Interactive Respiratory Triage Chat (Doctor-Patient Follow-Up)
  async sendTriageChat(city, lang, condition, messages) {
    const res = await fetch(`${BASE_URL}/api/triage-chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ city, lang, condition, messages })
    });
    if (!res.ok) throw new Error(`Triage chat failed: ${res.statusText}`);
    return await res.json();
  },

  // 5. Interactive Simulation (Sliders for Custom PM2.5, NO2, etc.)
  async simulateRisk(payload) {
    const res = await fetch(`${BASE_URL}/api/simulate-risk`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error(`Simulation failed: ${res.statusText}`);
    return await res.json();
  },

  // 6. Complete 7-Pillar Adaption AI Proof for Jury & Pitch Deck Modal
  async getAdaptionMetrics() {
    const res = await fetch(`${BASE_URL}/api/adaption-metrics`);
    if (!res.ok) throw new Error(`Metrics fetch failed: ${res.statusText}`);
    return await res.json();
  }
};
```

---

## 📡 Endpoints Specification

### 1. `GET /api/languages`
Populates your top-bar language selector and city selector.

#### Response (`200 OK`):
```json
{
  "languages": [
    { "code": "en", "name": "English", "native": "English", "script": "Latin" },
    { "code": "hi", "name": "Hindi", "native": "हिन्दी", "script": "Devanagari" },
    { "code": "mr", "name": "Marathi", "native": "मराठी", "script": "Devanagari" },
    { "code": "bn", "name": "Bengali", "native": "বাংলা", "script": "Bengali" },
    { "code": "ta", "name": "Tamil", "native": "தமிழ்", "script": "Tamil" },
    { "code": "te", "name": "Telugu", "native": "తెలుగు", "script": "Telugu" },
    { "code": "kn", "name": "Kannada", "native": "ಕನ್ನಡ", "script": "Kannada" },
    { "code": "ml", "name": "Malayalam", "native": "മലയാളം", "script": "Malayalam" },
    { "code": "gu", "name": "Gujarati", "native": "ગુજરાતી", "script": "Gujarati" },
    { "code": "pa", "name": "Punjabi", "native": "ਪੰਜਾਬੀ", "script": "Gurmukhi" },
    { "code": "or", "name": "Odia", "native": "ଓଡ଼ିଆ", "script": "Odia" },
    { "code": "as", "name": "Assamese", "native": "অসমীয়া", "script": "Bengali-Assamese" },
    { "code": "ur", "name": "Urdu", "native": "اردو", "script": "Perso-Arabic" }
  ],
  "cities": [
    { "name": "Mumbai", "latitude": 19.076, "longitude": 72.8777, "state": "Maharashtra", "region": "West Coast" },
    { "name": "Navi Mumbai", "latitude": 19.033, "longitude": 73.0297, "state": "Maharashtra", "region": "West Coast" },
    { "name": "Delhi", "latitude": 28.6139, "longitude": 77.209, "state": "Delhi NCR", "region": "North" },
    { "name": "Bengaluru", "latitude": 12.9716, "longitude": 77.5946, "state": "Karnataka", "region": "South" },
    { "name": "Kolkata", "latitude": 22.5726, "longitude": 88.3639, "state": "West Bengal", "region": "East" },
    { "name": "Chennai", "latitude": 13.0827, "longitude": 80.2707, "state": "Tamil Nadu", "region": "South" },
    { "name": "Hyderabad", "latitude": 17.385, "longitude": 78.4867, "state": "Telangana", "region": "South-Central" },
    { "name": "Ahmedabad", "latitude": 23.0225, "longitude": 72.5714, "state": "Gujarat", "region": "West" },
    { "name": "Pune", "latitude": 18.5204, "longitude": 73.8567, "state": "Maharashtra", "region": "West" },
    { "name": "Amritsar", "latitude": 31.634, "longitude": 74.8723, "state": "Punjab", "region": "North-West" },
    { "name": "Bhubaneswar", "latitude": 20.2961, "longitude": 85.8245, "state": "Odisha", "region": "East" },
    { "name": "Guwahati", "latitude": 26.1445, "longitude": 91.7362, "state": "Assam", "region": "North-East" }
  ]
}
```

---

### 2. `POST /api/triage-chat` (Pillar E Trajectory Extension)
Enables an interactive clinical triage copilot drawer where citizens can ask continuous doctor-patient follow-ups.

#### Request Body:
```json
{
  "city": "Mumbai",
  "lang": "english",
  "condition": "Pediatric Asthma",
  "messages": [
    { "role": "user", "content": "My 7-year-old child is coughing and AQI is high in Mumbai." },
    { "role": "assistant", "content": "Keep your child indoors, run HEPA air purifiers, and keep inhalers accessible." },
    { "role": "user", "content": "His wheezing is getting worse. Should I use nebulization or rush to ER?" }
  ]
}
```

#### Response (`200 OK`):
```json
{
  "reply": "If your child's wheezing is worsening, immediately measure SpO2 with a pulse oximeter. If SpO2 drops below 92%, or if you observe chest retractions (skin sucking in between ribs) or rapid breathing, proceed directly to the nearest emergency room. Administer your physician-prescribed bronchodilator/nebulizer immediately as first aid while preparing transit.",
  "city": "Mumbai",
  "language": "english",
  "current_air_quality": {
    "pm25": 28.3,
    "pm10": 31.8,
    "aqi": 173
  },
  "grap_protocol": {
    "stage": "Normal",
    "category": "Moderate / Satisfactory",
    "alert": "Standard baseline air quality guidelines.",
    "color": "#16A34A"
  },
  "triage_urgency": "Standard Clinical Precaution",
  "model_used": "deepseek-v4-flash (Adaption AI)",
  "source": "adaption_multi_turn_triage"
}
```

---

### 3. `GET /api/live-risk`
Query Params: `city` (any of 12 metros), `lang` (any of 12 languages), `condition` (e.g. Asthma, COPD, Pediatric, Elderly).

#### Enhanced Output includes CAQM GRAP Protocol:
```json
{
  "city": "Delhi",
  "state": "Delhi NCR",
  "region": "North",
  "current_air_quality": { "pm25": 142.5, "pm10": 210.0, "aqi": 285, "temperature": 18.2, "humidity": 55.0 },
  "grap_protocol": {
    "stage": "Stage I",
    "category": "Poor",
    "alert": "Standard Alert: Heavy dust control at construction sites, ban open trash burning, advise N95 masks for vulnerable populations.",
    "color": "#D97706"
  },
  "predicted_risk": {
    "risk_score": 68.2,
    "severity": "High",
    "badge_color": "#F97316",
    "expected_hospital_surge": "+54% Hospital Admission Spike"
  },
  "clinical_advisory": {
    "advisory": "स्वास्थ्य परामर्श (दिल्ली): वायु गुणवत्ता सूचकांक AQI 285 (Stage I Poor) पर है...",
    "language": "Hindi (हिन्दी)",
    "model_used": "deepseek-v4-flash (Adaption AI)",
    "source": "live_adaption_inference"
  }
}
```

---

### 4. `GET /api/adaption-metrics`
Returns concrete proof of all **7 Adaption AI Pillars** for the hackathon pitch deck and a dedicated **"Powered by Adaption AI"** modal:

```json
{
  "pipeline_name": "Pan-India Air Pollution & Respiratory Surveillance Adaption AI Pipeline",
  "account_credits": {
    "credits_consumed_approx": 223.0,
    "credits_remaining": 777.0
  },
  "seven_pillars": {
    "pillar_1_forge": { "dataset_id": "31535351-f429-4240-a8ea-db8af555936e", "document": "CAQM_GRAP_Schedule.pdf", "pages": 17 },
    "pillar_2_scaled_invent": { "dataset_id": "3bf58b6b-462c-4412-8171-fa1bed843e67", "rows": 2000, "credits": 200.0 },
    "pillar_3_localization": { "languages_count": 13, "cities_count": 12 },
    "pillar_4_blueprint": { "hallucination_mitigation": true, "safety_categories": ["medical_prescriptions"] },
    "pillar_5_trajectories": { "purpose": "Citizen-Doctor interactive respiratory triage chat" },
    "pillar_6_combine": { "validation_method": "client.datasets.combine.validate()" },
    "pillar_7_autoscientist": { "experiment_id": "4f098c91-a243-4d68-a6ea-6b33c79e11b2", "base_model": "Qwen/Qwen3.5-2B" }
  },
  "hackathon_bonus_proof": {
    "award": "$1,000 Best Use of Adaption Award"
  }
}
```

---

## 💡 Two Key UI Additions for the 3-Minute Demo Video

1. **Top-Bar Native Script Language Selector**:
   - Call `GET /api/languages` on load.
   - Show pills or dropdown: `English | हिन्दी | मराठी | தமிழ் | বাংলা | తెలుగు ...`
   - Switching languages updates live air quality advice immediately.
2. **Slide-Over Triage Chat Drawer**:
   - Floating button: `"Ask AI Pulmonologist"`.
   - Opens drawer calling `POST /api/triage-chat` with conversation history.
   - Shows CAQM GRAP Stage badge (e.g., `Stage II: Very Poor`) and clinical triage warnings.
