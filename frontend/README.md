# AeroMed India — React (Vite) Frontend

Welcome to the frontend workspace for **AeroMed India**, the Pan-India Air Quality & Respiratory Disease Surveillance Platform built for the INNOVATE Hackathon.

---

## 🚀 Quickstart for Frontend Teammate

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Configure Environment
Copy `.env.example` to `.env.local`:
```bash
cp .env.example .env.local
```
By default, `.env.local` points to our live production backend on Render:
```env
VITE_API_BASE_URL=https://innovate-aqi-backend.onrender.com
```
*(If you want to test against a local backend daemon running on port 8000, set `VITE_API_BASE_URL=http://localhost:8000`).*

### 3. Run Dev Server
```bash
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## ⚡ Deployment to Vercel (Zero Config)

The repository is structured so Vercel can deploy this frontend directly:

1. Import the GitHub repository in [Vercel](https://vercel.com).
2. Set **Root Directory** to `frontend`.
3. Vercel will automatically detect **Vite**:
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`
4. Add Environment Variable in Vercel Project Settings:
   - `VITE_API_BASE_URL`: `https://innovate-aqi-backend.onrender.com`
5. Click **Deploy**. SPA routing is pre-configured via `frontend/vercel.json`.

---

## 🔌 API Client Reference (`src/api/aqiClient.js`)

All 7 backend FastAPI endpoints are wrapped and ready for use with automatic JSON parsing and graceful fallback to offline seed data (`src/data/frontend_seed_data.json`):

| Method | Endpoint | Description |
|---|---|---|
| `aqiClient.getOverview()` | `GET /api/overview` | Metadata, 12-city baseline stats, ML feature importances ($R^2 = 0.9879$), historical trends |
| `aqiClient.getLanguages()` | `GET /api/languages` | 13 supported languages (12 Indic regional languages with native scripts + English) |
| `aqiClient.getLiveRisk(city, lang)` | `GET /api/live-risk` | Real-time Open-Meteo AQI, ML predicted admissions, CAQM GRAP stage, localized advisory |
| `aqiClient.simulateRisk(payload)` | `POST /api/simulate-risk` | What-if ML scenario simulator for custom pollutant values |
| `aqiClient.triageChat(messages, city, lang)` | `POST /api/triage-chat` | Multi-turn clinical triage chat powered by Adaption AI (`deepseek-v4-flash`) |
| `aqiClient.getAdaptionMetrics()` | `GET /api/adaption-metrics` | Verifiable Adaption AI pipeline metrics, AutoScientist runs, dataset IDs for jury proof |
| `aqiClient.getHealth()` | `GET /api/health` | Service uptime and model healthcheck |

---

## 📁 Folder Structure
```
frontend/
├── .env.example
├── index.html
├── package.json
├── README.md
├── vercel.json
├── vite.config.js
└── src/
    ├── api/
    │   └── aqiClient.js          # Unified FastAPI client
    ├── data/
    │   └── frontend_seed_data.json # Zero-latency offline fallback dataset
    ├── App.jsx                   # Main dashboard component
    ├── index.css                 # Dark theme styling
    └── main.jsx                  # React DOM mount point
```
