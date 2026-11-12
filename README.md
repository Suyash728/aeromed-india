# Pan-India Air Pollution & Respiratory Disease Surveillance Backend (v2)

An end-to-end Machine Learning and 7-Pillar Adaption AI clinical surveillance platform built for the Innovate Hackathon.

> **🌐 Live Production API**: `https://innovate-aqi-backend.onrender.com`  
> **📖 Swagger Interactive Docs**: `https://innovate-aqi-backend.onrender.com/docs`  
> **🏆 Award Category**: $1,000 Best Use of Adaption Award  

---

## 🌟 Key Highlights
- **Live Cloud Production**: Deployed on Render with wide CORS enabled for instant React frontend integration.
- **12 Indian Metros Coverage**: Real-time Open-Meteo atmospheric monitoring across Mumbai, Navi Mumbai, Delhi, Bengaluru, Kolkata, Chennai, Hyderabad, Ahmedabad, Pune, Amritsar, Bhubaneswar, and Guwahati.
- **Pan-India 12 Languages**: Native script support for English, हिन्दी (Hindi), मराठी (Marathi), বাংলা (Bengali), தமிழ் (Tamil), తెలుగు (Telugu), ಕನ್ನಡ (Kannada), മലയാളം (Malayalam), ગુજરાતી (Gujarati), ਪੰਜਾਬੀ (Punjabi), ଓଡ଼ିଆ (Odia), অসমীয়া (Assamese), and اردو (Urdu).
- **CAQM GRAP Stage I–IV Enforcement**: Integrated Graded Response Action Plan pollution stages with official public health alerts.
- **ML Disease Surge Engine**: Scikit-Learn Gradient Boosting Regressor trained on 10 years of simulated CPCB air quality and hospital respiratory admissions ($R^2 = 0.988$, $MAE = 1.88$).
- **Official Adaption Evaluation Lift**: Automated quality benchmark verified **Grade B**, improving from **17.8th percentile to 31.5th percentile** (+77.0% relative improvement).
- **Full 7-Pillar Adaption AI Architecture**:
  1. **Forge Unstructured Document Processing**: Official CAQM GRAP PDF (750 KB, 17 pages) ingested into Adaption (`31535351-f429-4240-a8ea-db8af555936e`).
  2. **Scaled Invent Dataset**: 2,000 synthetic clinical Q&A pairs across 6 clinical domains (`3bf58b6b-462c-4412-8171-fa1bed843e67`), safely utilizing 200 credits with estimation validation.
  3. **Cultural Localization**: Multilingual ISO translation and country pairing across 12 Indian regional tongues.
  4. **Blueprint Medical Guardrails**: Brand controls enforcing CPCB/CAQM standards, zero pharmaceutical hallucinations, and mandatory SpO2 < 92% triage triggers.
  5. **Multi-Turn Trajectory Extension**: Conversational doctor-patient clinical follow-ups via `POST /api/triage-chat`.
  6. **Dataset Combine & Validation**: Cross-source compatibility checks with `client.datasets.combine.validate()`.
  7. **AutoScientist Multi-Cycle Optimization**: Active training loop on `Qwen/Qwen3.5-2B` with 1,000 domain augmentation rows (`f74f0c2f-dc5f-4d00-913d-cdd8c9dece84`).

---

## 📁 Repository Structure
```
innovate-aqi-backend/
├── main.py                          # FastAPI REST API server (v2 - 9 endpoints)
├── data_pipeline.py                 # 12-city 10-year historical data generator & ML regressor
├── adaption_pipeline_v2.py          # Full 7-pillar Adaption AI SDK pipeline
├── test_api.py                      # Comprehensive 9-test integration suite (100% pass)
├── start.sh                         # One-click startup script
├── Procfile                         # Render / Railway process definition
├── Dockerfile                       # Hugging Face Spaces / Container definition
├── requirements.txt                 # Production pinned dependencies
├── API_CONTRACT.md                  # Complete frontend API documentation & copy-paste JS snippets
├── JURY_PROOF_SUMMARY.md            # Slide 4 pitch deck fuel & verified artifact IDs
├── frontend_seed_data.json          # Pre-computed 10-year trends, Pearson matrix & 12-city summaries
├── adaption_metrics.json            # Complete 7-pillar proof & evaluation benchmarks
├── risk_model.joblib                # Trained Gradient Boosting risk regressor
└── data/
    ├── CAQM_GRAP_Schedule.pdf       # Official government PDF ingested via Forge
    ├── clinical_respiratory_advisories.csv # Prompt-completion seed dataset
    └── india_air_quality_respiratory_2015_2025.csv # 1,584 historical records
```

---

## ⚡ Quick Verification via Live Render API

```bash
# Health check
curl -s "https://innovate-aqi-backend.onrender.com/api/health"

# 12 Indian languages in native scripts
curl -s "https://innovate-aqi-backend.onrender.com/api/languages"

# Live risk for Mumbai in Marathi
curl -s "https://innovate-aqi-backend.onrender.com/api/live-risk?city=Mumbai&lang=marathi"

# Adaption AI 7-pillar metrics
curl -s "https://innovate-aqi-backend.onrender.com/api/adaption-metrics"
```
