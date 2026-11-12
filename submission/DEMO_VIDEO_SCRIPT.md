# 🎬 Demo Video Script: AeroMed India
## 3-Minute Flagship Hackathon Pitch & Walkthrough
**Target Award**: $1,000 Best Use of Adaption AI Award  
**Video Length**: Exactly 3 Minutes (180 Seconds)  
**Live Production URL**: `https://innovate-aqi-backend.onrender.com`  

---

### Storyboard & Timestamp Breakdown

| Timestamp | Phase | On-Screen Visual | Spoken Audio / Narration |
|---|---|---|---|
| **0:00 – 0:30** | **The Hook & Problem** | Aerial footage or news clips of severe smog over Delhi NCR and Mumbai; CPCB air quality monitor showing AQI 420; overwhelmed hospital OPD queue. | *"Every winter across India, over 1.4 billion people face an invisible respiratory emergency. In cities like Delhi, Mumbai, and Kolkata, PM2.5 levels spike past 400 micrograms, triggering massive waves of emergency admissions for asthma and COPD. Yet, traditional weather apps only show raw numbers—with zero hospital surge forecasting, zero clinical actionability, and zero support for the 90% of Indians who read in regional languages. Welcome to AeroMed India."* |
| **0:30 – 1:00** | **Live Surveillance & ML Engine** | Browser opens to the live dashboard on Render. Toggle between Delhi and Mumbai. Show live AQI metrics (PM2.5, PM10), CAQM GRAP Stage III badge, and predicted daily hospital admissions. | *"AeroMed India is an end-to-end intelligence platform connecting atmospheric science with emergency clinical surveillance. Here on our live production dashboard, we track 12 major Indian metros in real time. Backing this is our Gradient Boosting Regressor, trained on a decade of CPCB data. It predicts daily hospital admissions with a remarkable R² score of 0.9879 and an MAE of under 1.9 patients per day, giving hospitals 48 hours advance warning before respiratory surge events."* |
| **1:00 – 1:35** | **12-Language Localization** | Click language dropdown in the UI. Switch from English to Hindi (हिन्दी), then Marathi (मराठी), then Tamil (தமிழ்) and Bengali (বাংলা). Show clinical advisory updating instantly in native script. | *"Healthcare must speak the patient's language. AeroMed supports 12 official Indian languages with full native script fidelity—from Devanagari Hindi and Marathi to Tamil, Bengali, Telugu, and Gurmukhi Punjabi. When an advisory is issued, an asthmatic grandmother in Pune or an auto-driver in Chennai receives precise, culturally attuned clinical directives in their mother tongue."* |
| **1:35 – 2:20** | **The 7-Pillar Adaption AI Deep Dive** | Switch screen to `submission/JURY_PROOF_SUMMARY.md` and the Swagger UI `/api/adaption-metrics` endpoint. Show Adaption AI evaluation chart (Grade B, 17.8% → 31.5% percentile leap, +3.8% quality uplift). Show AutoScientist active run `f74f0c2f-dc5f-4d00-913d-cdd8c9dece84`. | *"What makes this possible is our comprehensive implementation of all 7 Adaption AI capability pillars. First, with Adaption Forge, we ingested the official 17-page CAQM GRAP government PDF to codify legal dust and emission directives. Second, using Invent, we synthesized 2,000 clinically grounded training rows across chronic, pediatric, and geriatric domains. Third, our automated Adaption Evaluation verified a jump from the 17.8th to the 31.5th percentile with Grade B certification and a +3.8% quality uplift. And finally, under Pillar G, our AutoScientist LoRA fine-tuning experiment on Qwen 3.5 is actively optimizing domain performance."* |
| **2:20 – 2:45** | **Interactive Clinical Triage & Guardrails** | In the live chat drawer, type: *"My 65-year-old father has COPD and his pulse oximeter shows 89% SpO2 in Delhi smog. What medicine should I give him?"* Show instant response warning of ER emergency and refusing to hallucinate drug doses. | *"Let's test our live Clinical Triage Chat powered by Adaption AI deepseek-v4-flash. Watch how our enforced Blueprint Medical Guardrails trigger: Because oxygen saturation is below 92%, the system immediately flags an emergency room priority and strictly refuses to fabricate drug dosages, advising certified pulmonologist care. Safe, hallucination-free medical intelligence in action."* |
| **2:45 – 3:00** | **Call to Action & Hackathon Pitch** | Full-screen show of repository structure, Vercel UI, live Render link (`https://innovate-aqi-backend.onrender.com`), and closing jury slide. | *"AeroMed India is fully deployed today on Render Cloud with an open API and React frontend monorepo. We are bridging the gap between atmospheric telemetry, predictive machine learning, and linguistic clinical care for 1.4 billion people. Thank you!"* |

---

### Tips for Recording
1. **Audio**: Use a clear microphone or high-quality headset. Keep pacing energetic and confident.
2. **Resolution**: Record screen at 1080p (1920x1080) with 125% zoom for high readability of charts and code.
3. **Pointers**: Use a mouse highlighter or cursor spotlight when clicking the language dropdown and chat drawer.
