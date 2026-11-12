"""
Data Pipeline for Pan-India Air Pollution & Respiratory Disease Surveillance
Generates high-fidelity historical data (2015-2025) across 12 Indian Metros,
computes Pearson correlation matrices, trains disease risk regressors, and exports
React-ready frontend seed data.
"""

import json
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(WORKSPACE, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 12 Major Indian Metros across all geographic zones
CITIES = {
    "Mumbai": {"lat": 19.0760, "lon": 72.8777, "state": "Maharashtra", "base_pm25": 65, "winter_mult": 1.7, "monsoon_mult": 0.45},
    "Navi Mumbai": {"lat": 19.0330, "lon": 73.0297, "state": "Maharashtra", "base_pm25": 60, "winter_mult": 1.65, "monsoon_mult": 0.48},
    "Delhi": {"lat": 28.6139, "lon": 77.2090, "state": "Delhi NCR", "base_pm25": 115, "winter_mult": 2.8, "monsoon_mult": 0.35},
    "Bengaluru": {"lat": 12.9716, "lon": 77.5946, "state": "Karnataka", "base_pm25": 38, "winter_mult": 1.25, "monsoon_mult": 0.65},
    "Kolkata": {"lat": 22.5726, "lon": 88.3639, "state": "West Bengal", "base_pm25": 78, "winter_mult": 2.1, "monsoon_mult": 0.40},
    "Chennai": {"lat": 13.0827, "lon": 80.2707, "state": "Tamil Nadu", "base_pm25": 42, "winter_mult": 1.3, "monsoon_mult": 0.70},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867, "state": "Telangana", "base_pm25": 52, "winter_mult": 1.45, "monsoon_mult": 0.55},
    "Ahmedabad": {"lat": 23.0225, "lon": 72.5714, "state": "Gujarat", "base_pm25": 68, "winter_mult": 1.75, "monsoon_mult": 0.50},
    "Pune": {"lat": 18.5204, "lon": 73.8567, "state": "Maharashtra", "base_pm25": 48, "winter_mult": 1.4, "monsoon_mult": 0.58},
    "Amritsar": {"lat": 31.6340, "lon": 74.8723, "state": "Punjab", "base_pm25": 92, "winter_mult": 2.5, "monsoon_mult": 0.38},
    "Bhubaneswar": {"lat": 20.2961, "lon": 85.8245, "state": "Odisha", "base_pm25": 45, "winter_mult": 1.35, "monsoon_mult": 0.60},
    "Guwahati": {"lat": 26.1445, "lon": 91.7362, "state": "Assam", "base_pm25": 50, "winter_mult": 1.5, "monsoon_mult": 0.52}
}

np.random.seed(42)

def generate_historical_dataset():
    """Generates 10-year monthly city-level dataset (2015-2025) simulating CPCB + ICMR stats for 12 cities."""
    records = []
    
    for city, config in CITIES.items():
        base_pm = config["base_pm25"]
        winter_m = config["winter_mult"]
        monsoon_m = config["monsoon_mult"]
        
        for year in range(2015, 2026):
            for month in range(1, 13):
                # Seasonal curve
                if month in [11, 12, 1]:
                    season_factor = winter_m + np.random.uniform(-0.15, 0.25)
                elif month in [2, 10]:
                    season_factor = (winter_m * 0.7) + np.random.uniform(-0.1, 0.15)
                elif month in [6, 7, 8, 9]:
                    season_factor = monsoon_m + np.random.uniform(-0.05, 0.1)
                else:
                    season_factor = 1.0 + np.random.uniform(-0.1, 0.1)
                
                trend = 1.0 + (year - 2015) * 0.015
                if year == 2020 and month in [3, 4, 5]:
                    trend *= 0.55

                pm25 = max(12.0, base_pm * season_factor * trend + np.random.normal(0, 5.5))
                pm10 = pm25 * np.random.uniform(1.6, 2.1)
                no2 = pm25 * np.random.uniform(0.35, 0.55) + np.random.normal(0, 3.0)
                so2 = pm25 * np.random.uniform(0.15, 0.30) + np.random.normal(0, 2.0)
                co = pm25 * 0.012 + np.random.uniform(0.4, 1.2)
                o3 = max(15.0, 45.0 - (season_factor * 8.0) + np.random.normal(0, 5.0))
                
                # Regional temperature & humidity
                is_north = city in ["Delhi", "Amritsar"]
                if month in [5, 6]:
                    temp = (41.0 if is_north else 34.0) + np.random.uniform(-2, 3)
                    humidity = 50.0 + np.random.uniform(-10, 10)
                elif month in [7, 8]:
                    temp = 29.0 + np.random.uniform(-2, 3)
                    humidity = 82.0 + np.random.uniform(-5, 10)
                elif month in [12, 1]:
                    temp = (12.0 if is_north else 23.0) + np.random.uniform(-2, 3)
                    humidity = 65.0 + np.random.uniform(-8, 8)
                else:
                    temp = 28.0 + np.random.uniform(-3, 3)
                    humidity = 60.0 + np.random.uniform(-10, 10)

                aqi = pm25 * 1.85 + np.random.normal(0, 5.0)

                # Clinical respiratory admissions per 100k population
                baseline_admission = 18.0
                pm25_impact = (pm25 / 25.0) ** 1.35 * 4.2
                no2_impact = (no2 / 20.0) * 2.5
                temp_stress = max(0, (22.0 - temp) * 0.8)
                
                admission_rate = baseline_admission + pm25_impact + no2_impact + temp_stress + np.random.normal(0, 2.0)
                admission_rate = max(10.0, admission_rate)
                
                asthma_rate = admission_rate * 0.38
                copd_rate = admission_rate * 0.28
                pediatric_rate = admission_rate * 0.22
                elderly_rate = admission_rate * 0.30
                risk_score = min(100.0, max(5.0, (admission_rate / 90.0) * 100.0))

                records.append({
                    "city": city,
                    "state": config["state"],
                    "year": year,
                    "month": month,
                    "date": f"{year}-{month:02d}-01",
                    "pm25": round(pm25, 2),
                    "pm10": round(pm10, 2),
                    "no2": round(no2, 2),
                    "so2": round(so2, 2),
                    "co": round(co, 2),
                    "o3": round(o3, 2),
                    "temperature": round(temp, 1),
                    "humidity": round(humidity, 1),
                    "aqi": round(aqi, 1),
                    "admission_rate_per_100k": round(admission_rate, 2),
                    "asthma_admissions": round(asthma_rate, 2),
                    "copd_admissions": round(copd_rate, 2),
                    "pediatric_admissions": round(pediatric_rate, 2),
                    "elderly_admissions": round(elderly_rate, 2),
                    "risk_score": round(risk_score, 1)
                })

    df = pd.DataFrame(records)
    csv_path = os.path.join(DATA_DIR, "india_air_quality_respiratory_2015_2025.csv")
    df.to_csv(csv_path, index=False)
    print(f"Generated {len(df)} historical records for 12 cities saved to {csv_path}")
    return df

def train_risk_regressor(df):
    """Trains Gradient Boosting Regressor."""
    features = ["pm25", "pm10", "no2", "so2", "co", "o3", "temperature", "humidity"]
    target = "risk_score"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingRegressor(
        n_estimators=160,
        learning_rate=0.08,
        max_depth=4,
        random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Model Training Complete! R^2 Score: {r2:.4f}, MAE: {mae:.4f}")

    importances = dict(zip(features, [round(float(v), 4) for v in model.feature_importances_]))
    model_path = os.path.join(WORKSPACE, "risk_model.joblib")
    joblib.dump({"model": model, "features": features, "r2": r2, "mae": mae, "importances": importances}, model_path)
    print(f"Model saved to {model_path}")
    return model, importances, r2, mae

def generate_frontend_seed_data(df, importances, r2, mae):
    """Computes correlation matrices, seasonal trends, and 12-city summaries for React dashboard."""
    numeric_cols = ["pm25", "pm10", "no2", "so2", "co", "o3", "temperature", "humidity",
                    "admission_rate_per_100k", "asthma_admissions", "copd_admissions", "risk_score"]
    corr_matrix = df[numeric_cols].corr().round(3).to_dict()

    city_summaries = {}
    for city, config in CITIES.items():
        cdf = df[df["city"] == city]
        city_summaries[city] = {
            "state": config["state"],
            "avg_pm25": round(float(cdf["pm25"].mean()), 1),
            "avg_pm10": round(float(cdf["pm10"].mean()), 1),
            "peak_pm25": round(float(cdf["pm25"].max()), 1),
            "avg_admissions": round(float(cdf["admission_rate_per_100k"].mean()), 1),
            "peak_admissions": round(float(cdf["admission_rate_per_100k"].max()), 1),
            "avg_risk_score": round(float(cdf["risk_score"].mean()), 1),
            "lat": config["lat"],
            "lon": config["lon"]
        }

    monthly_cycle = df.groupby(["city", "month"]).agg({
        "pm25": "mean",
        "aqi": "mean",
        "admission_rate_per_100k": "mean",
        "risk_score": "mean"
    }).round(1).reset_index().to_dict(orient="records")

    recent_timeline = df[df["year"] >= 2023].sort_values("date")[
        ["city", "date", "pm25", "pm10", "no2", "admission_rate_per_100k", "asthma_admissions", "copd_admissions", "risk_score"]
    ].to_dict(orient="records")

    seed_data = {
        "metadata": {
            "title": "Pan-India Air Quality & Respiratory Disease Surveillance",
            "period": "2015 - 2025",
            "cities_count": len(CITIES),
            "source": "CPCB & National Health Surveillance Simulation",
            "model_performance": {
                "r2_score": round(r2, 4),
                "mae": round(mae, 4),
                "algorithm": "Gradient Boosting Regressor",
                "feature_importances": importances
            }
        },
        "cities": city_summaries,
        "correlation_matrix": corr_matrix,
        "monthly_seasonal_trends": monthly_cycle,
        "recent_timeline": recent_timeline
    }

    out_file = os.path.join(WORKSPACE, "frontend_seed_data.json")
    with open(out_file, "w") as f:
        json.dump(seed_data, f, indent=2)
    print(f"Exported React seed data with {len(CITIES)} cities to {out_file}")
    return seed_data

if __name__ == "__main__":
    df = generate_historical_dataset()
    model, importances, r2, mae = train_risk_regressor(df)
    generate_frontend_seed_data(df, importances, r2, mae)
    print("Data Pipeline Completed Successfully!")
