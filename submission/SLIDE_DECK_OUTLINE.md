# 🎯 Pitch Deck Outline: AeroMed India
## Pan-India Air Quality & Respiratory Disease Surveillance Platform
**Target Award**: $1,000 Best Use of Adaption AI Award (INNOVATE Hackathon)  
**Live Production URL**: `https://innovate-aqi-backend.onrender.com`  
**Swagger Docs**: `https://innovate-aqi-backend.onrender.com/docs`  

---

### Slide 1: The Problem — India's Dual Health & Air Crisis
- **Headline**: *Breathing Shouldn't Be a Health Hazard — But For 1.4 Billion People, It Is.*
- **The Core Crisis**:
  - Over 1.4 billion citizens across India breathe air exceeding WHO safety guidelines by 5x to 15x.
  - Winter inversions, crop residue burning, and vehicular emissions trigger massive, unpredicted spikes in emergency hospital admissions for COPD, Bronchial Asthma, and Acute Bronchitis.
  - Existing AQI portals only display raw sensor numbers without actionable medical context, early hospital surge predictions, or localized linguistic guidance.
- **The Language Barrier**: Over 90% of affected populations consume health information in regional Indian languages, yet existing digital health tools are predominantly English-only.
- **Visual**: Map of India highlighting the 12 major metros with AQI heat-zones and hospital admission surge indicators.

---

### Slide 2: The Solution — AeroMed India
- **Headline**: *From Atmospheric Data to Clinical Action in Under 50 Milliseconds.*
- **Three Core Pillars**:
  1. **Real-Time Pan-India Met Engine**: Live environmental feeds (PM2.5, PM10, NO2, SO2, CO, O3, Temp, Humidity) covering 12 major metros across every geographical zone.
  2. **Predictive ML Surge Engine**: Pre-trained Gradient Boosting Regressor predicting daily hospital admissions ($R^2 = 0.9879$).
  3. **Adaption AI Clinical Intelligence**: 7-Pillar Adaption AI pipeline delivering localized clinical triage across 12 Indian regional languages with strict medical guardrails.
- **Regulatory Grounding**: Official Central Pollution Control Board (CPCB) standards and Commission for Air Quality Management (CAQM) Graded Response Action Plan (GRAP Stages I–IV).
- **Visual**: End-to-end architecture diagram: Atmospheric Sensors $\rightarrow$ FastAPI ML Core $\rightarrow$ Adaption AI Guardrails $\rightarrow$ Vite/React Multilingual Dashboard.

---

### Slide 3: The ML Predictive Engine — Precision Clinical Forecasting
- **Headline**: *Trained on 10 Years of Continuous Surveillance Data (2015–2025).*
- **Empirical Rigor**:
  - **Algorithm**: Scikit-Learn `GradientBoostingRegressor(n_estimators=160, learning_rate=0.08, max_depth=4)`.
  - **Dataset**: 1,584 curated historical records across 12 Indian Metros.
  - **Model Accuracy ($R^2$)**: **0.9879** (98.8% explained variance).
  - **Mean Absolute Error (MAE)**: **1.8806** admissions/day.
- **Top Feature Importances**:
  - `PM2.5`: **96.48%** (Dominant physiological trigger for respiratory distress).
  - `NO2`: **2.94%** (Combustion proxy correlating with airway inflammation).
  - `PM10`, `SO2`, `CO`, `O3`, `Temperature`, `Humidity`: Balance.
- **Clinical Utility**: Enables municipal health authorities and hospital ICUs to mobilize oxygen, nebulizers, and beds 24–48 hours ahead of smog events.
- **Visual**: Correlation heatmap, feature importance bar chart, and Actual vs. Predicted admissions curve.

---

### Slide 4: Adaption AI Deep Dive — The 7 Pillars of Domain Mastery
- **Headline**: *Not Generic LLM Chat — Rigorous, Certified Adaption AI Engineering.*
- **Evaluation Benchmark Highlights (Official Adaption Evaluation SDK)**:
  - **Dataset Percentile Jump**: Leaped from **17.8th percentile $\rightarrow$ 31.5th percentile** (+77% relative climb, Grade B certification).
  - **Overall Quality Uplift**: Boosted from **8.0 $\rightarrow$ 8.3** (+3.8% direct evaluation lift).
  - **Completion Depth**: 5.4x expansion (156 characters $\rightarrow$ 848 characters) of medically rigorous advisory text.
- **The 7 Pillars Breakdown**:
  1. **Forge**: Extracted CAQM GRAP Stage I–IV rules straight from a 17-page government PDF (`CAQM_GRAP_Schedule.pdf`, Dataset ID `31535351-f429-4240-a8ea-db8af555936e`).
  2. **Invent**: Generated 2,000 synthetic clinical rows across 5 vulnerable subdomains (Dataset ID `3bf58b6b-462c-4412-8171-fa1bed843e67`).
  3. **Adapt**: Supervised domain adaptation with custom clinical personas and schema validation.
  4. **Localize**: Full cultural and native script localization into 12 Indian languages (`hi`, `mr`, `bn`, `ta`, `te`, `kn`, `ml`, `gu`, `pa`, `or`, `as`, `ur`).
  5. **Blueprint Guardrails**: Strict hallucination mitigation, zero pharmaceutical prescription dosages, and mandatory SpO2 < 92% ER emergency triage routing.
  6. **Trajectories**: Multi-turn conversational doctor-patient clinical follow-up loops.
  7. **AutoScientist**: LoRA fine-tuning experiment on Qwen/Qwen3.5-2B (Run ID `f74f0c2f-dc5f-4d00-913d-cdd8c9dece84`) trained on dataset `e103924c-e864-4322-b2b5-013675d1f5c6`.
- **Visual**: Side-by-side Adaption AI Quality score badges and AutoScientist progress dashboard.

---

### Slide 5: Live Demo, Public Cloud Deployment & Impact
- **Headline**: *Production-Ready Today, Serving 12 Metros in Real Time.*
- **Production Infrastructure**:
  - **Backend**: Live on Render Cloud (`https://innovate-aqi-backend.onrender.com`), FastAPI, automated Swagger UI documentation, sub-50ms latency.
  - **Frontend**: React + Vite SPA, mobile-first responsive layout, zero-latency bundled offline fallback dataset (`frontend_seed_data.json`).
  - **Full-Stack Monorepo**: Unified codebase with single-command local runner (`./dev.sh`) and zero-config Vercel/Render Blueprints.
- **Target Beneficiaries & Impact**:
  - **Citizens**: Free, localized early warnings in their mother tongue with preventive steps (N95 vs. cloth masks, indoor air filtering).
  - **Hospitals & Emergency Rooms**: Accurate 48-hour respiratory surge forecasting to staff pulmonologists and allocate oxygen beds.
  - **State Pollution Boards (SPCBs)**: Automated enforcement notifications tied to CAQM GRAP Stages I–IV.
- **Visual**: Live interactive UI screenshot showing the Mumbai/Delhi dashboard, native Marathi/Tamil script selector, and the AI clinical triage drawer.
