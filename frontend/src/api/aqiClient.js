/**
 * AeroMed India - API Client Wrapper
 * Connects to live FastAPI backend on Render or localhost.
 * Includes graceful offline / cold-start fallback using frontend_seed_data.json.
 */

import seedData from '../data/frontend_seed_data.json';

const API_BASE_URL = (
  import.meta.env.VITE_API_BASE_URL ||
  'https://innovate-aqi-backend.onrender.com'
).replace(/\/+$/, '');

/**
 * Universal fetch wrapper with JSON parsing and timeout handling
 */
async function fetchJson(endpoint, options = {}, timeoutMs = 15000) {
  const url = `${API_BASE_URL}${endpoint.startsWith('/') ? endpoint : `/${endpoint}`}`;
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: controller.signal,
    });

    clearTimeout(timer);

    if (!response.ok) {
      const errBody = await response.text();
      let parsed;
      try {
        parsed = JSON.parse(errBody);
      } catch {
        parsed = { detail: errBody || `HTTP ${response.status} ${response.statusText}` };
      }
      const error = new Error(parsed.detail || `Request failed with status ${response.status}`);
      error.status = response.status;
      error.body = parsed;
      throw error;
    }

    return await response.json();
  } catch (error) {
    clearTimeout(timer);
    throw error;
  }
}

export const aqiClient = {
  /**
   * 1. GET /api/overview
   * Returns metadata, 12-city comparison, feature importances, and historical trends.
   */
  async getOverview() {
    try {
      return await fetchJson('/api/overview');
    } catch (err) {
      console.warn('Backend overview request failed, falling back to bundled seed data:', err.message);
      return seedData;
    }
  },

  /**
   * 2. GET /api/languages
   * Returns list of all 12 supported Indian regional languages + English with native script labels.
   */
  async getLanguages() {
    try {
      return await fetchJson('/api/languages');
    } catch (err) {
      console.warn('Backend languages request failed, falling back to local list:', err.message);
      return {
        total: 13,
        languages: [
          { code: 'en', name: 'English', native: 'English', script: 'Latin' },
          { code: 'hi', name: 'Hindi', native: 'हिन्दी', script: 'Devanagari' },
          { code: 'mr', name: 'Marathi', native: 'मराठी', script: 'Devanagari' },
          { code: 'bn', name: 'Bengali', native: 'বাংলা', script: 'Bengali' },
          { code: 'ta', name: 'Tamil', native: 'தமிழ்', script: 'Tamil' },
          { code: 'te', name: 'Telugu', native: 'తెలుగు', script: 'Telugu' },
          { code: 'kn', name: 'Kannada', native: 'ಕನ್ನಡ', script: 'Kannada' },
          { code: 'ml', name: 'Malayalam', native: 'മലയാളം', script: 'Malayalam' },
          { code: 'gu', name: 'Gujarati', native: 'ગુજરાતી', script: 'Gujarati' },
          { code: 'pa', name: 'Punjabi', native: 'ਪੰਜਾਬੀ', script: 'Gurmukhi' },
          { code: 'or', name: 'Odia', native: 'ଓଡ଼ିଆ', script: 'Odia' },
          { code: 'as', name: 'Assamese', native: 'অসমীয়া', script: 'Bengali-Assamese' },
          { code: 'ur', name: 'Urdu', native: 'اردو', script: 'Perso-Arabic' },
        ],
      };
    }
  },

  /**
   * 3. GET /api/live-risk
   * Fetches real-time AQI and ML risk score for a selected city in the requested language.
   * @param {string} city - e.g. "Delhi", "Mumbai", "Bengaluru"
   * @param {string} language - ISO code e.g. "hi", "mr", "ta", "en"
   */
  async getLiveRisk(city = 'Delhi', language = 'en') {
    const params = new URLSearchParams({
      city: city.toLowerCase(),
      language: language.toLowerCase(),
    });
    return await fetchJson(`/api/live-risk?${params.toString()}`);
  },

  /**
   * 4. POST /api/simulate-risk
   * Runs the pre-trained ML Gradient Boosting model on custom pollutant inputs.
   * @param {Object} payload - { pm25, pm10, no2, so2, co, o3, temperature, humidity, city, language }
   */
  async simulateRisk(payload) {
    return await fetchJson('/api/simulate-risk', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  /**
   * 5. POST /api/triage-chat
   * AI-powered respiratory clinical triage chat using Adaption AI (deepseek-v4-flash).
   * @param {Array} messages - [{ role: "user" | "assistant", content: string }]
   * @param {string} city - Active user city context
   * @param {string} language - Target response language code (e.g. "hi", "en")
   */
  async triageChat(messages, city = 'Delhi', language = 'en') {
    return await fetchJson('/api/triage-chat', {
      method: 'POST',
      body: JSON.stringify({
        messages,
        city,
        language,
      }),
    });
  },

  /**
   * 6. GET /api/adaption-metrics
   * Retrieves verifiable Adaption AI pipeline metrics, AutoScientist runs, and dataset IDs for jury proof.
   */
  async getAdaptionMetrics() {
    return await fetchJson('/api/adaption-metrics');
  },

  /**
   * 7. GET /api/health
   * Healthcheck endpoint returning server uptime, ML model status, and Adaption AI status.
   */
  async getHealth() {
    return await fetchJson('/api/health');
  },

  /**
   * 8. GET /api/datasets
   * Retrieves full catalog, row counts, and sample preview rows of all datasets in backend/data.
   */
  async getDatasets() {
    return await fetchJson('/api/datasets');
  },
};

export default aqiClient;
