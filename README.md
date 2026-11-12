# Pan-India Air Pollution & Respiratory Disease Surveillance Backend (v2)

An end-to-end Machine Learning and 7-Pillar Adaption AI clinical surveillance platform built for the Innovate Hackathon.

## 🌟 Key Highlights
- **12 Indian Metros Coverage**: Real-time Open-Meteo atmospheric monitoring across Mumbai, Navi Mumbai, Delhi, Bengaluru, Kolkata, Chennai, Hyderabad, Ahmedabad, Pune, Amritsar, Bhubaneswar, and Guwahati.
- **Pan-India 12 Languages**: Native script support for English, हिन्दी (Hindi), मराठी (Marathi), বাংলা (Bengali), தமிழ் (Tamil), తెలుగు (Telugu), ಕನ್ನಡ (Kannada), മലയാളം (Malayalam), ગુજરાતી (Gujarati), ਪੰਜਾਬੀ (Punjabi), ଓଡ଼ିଆ (Odia), অসমীয়া (Assamese), and اردو (Urdu).
- **CAQM GRAP Stage I–IV Enforcement**: Integrated Graded Response Action Plan pollution stages with official public health alerts.
- **ML Disease Surge Engine**: Scikit-Learn Gradient Boosting Regressor trained on 10 years of simulated CPCB air quality and hospital respiratory admissions ($R^2 = 0.988$, $MAE = 1.88$).
- **Full 7-Pillar Adaption AI Architecture**:
  1. **Forge Unstructured Document Processing**: Official CAQM GRAP PDF (750 KB, 17 pages) ingested into Adaption (`31535351-f429-4240-a8ea-db8af555936e`).
  2. **Scaled Invent Dataset**: 2,000 synthetic clinical Q&A pairs across 6 clinical domains (`3bf58b6b-462c-4412-8171-fa1bed843e67`), safely utilizing 200 credits with estimation validation.
  3. **Cultural Localization**: Multilingual ISO translation and country pairing across 12 Indian regional tongues.
  4. **Blueprint Medical Guardrails**: Brand controls enforcing CPCB/CAQM standards, zero pharmaceutical hallucinations, and mandatory SpO2 < 92% triage triggers.
  5. **Multi-Turn Trajectory Extension**: Conversational doctor-patient clinical follow-ups via `POST /api/triage-chat`.
  6. **Dataset Combine & Validation**: Cross-source compatibility checks with `client.datasets.combine.validate()`.
  7. **AutoScientist Multi-Cycle Optimization**: Active training loop on `Qwen/Qwen3.5-2B` with 1,000 domain augmentation rows (`4f098c91-a243-4d68-a6ea-6b33c79e11b2`).

---

## 📁 Repository Structure
```
innovate-aqi-backend/
├── main.py                          # FastAPI REST API server (v2 - 9 endpoints)
├── data_pipeline.py                 # 12-city 10-year historical data generator & ML regressor
├── adaption_pipeline_v2.py          # Full 7-pillar Adaption AI SDK pipeline
├── test_api.py                      # Comprehensive 9-test integration suite (100% pass)
├── start.sh                         # One-click startup script
├── API_CONTRACT.md                  # Complete frontend API documentation & copy-paste JS snippets
├── frontend_seed_data.json          # Pre-computed 10-year trends, Pearson matrix & 12-city summaries
├── adaption_metrics.json            # Complete 7-pillar proof for the $1,000 Adaption Award
├── risk_model.joblib                # Trained Gradient Boosting risk regressor
└── data/
    ├── CAQM_GRAP_Schedule.pdf       # Official government PDF ingested via Forge
    ├── clinical_respiratory_advisories.csv # Prompt-completion seed dataset
    └── india_air_quality_respiratory_2015_2025.csv # 1,584 historical records
```

---

## ⚡ Quick Start

### 1. Run the Server
```bash
./start.sh
```
Or directly:
```bash
source .venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 2. View Interactive Swagger Docs
Open `http://localhost:8000/docs`

### 3. Run the Tests
```bash
.venv/bin/python test_api.py
```
*(Runs all 9 tests covering endpoints, 12 cities, languages, and live Adaption inference)*

### 4. Expose Publicly for Your Remote React Teammate
```bash
cloudflared tunnel --url http://localhost:8000
```
Or:
```bash
ngrok http 8000
```
Share the generated HTTPS URL with your teammate for their `VITE_API_BASE_URL`.
