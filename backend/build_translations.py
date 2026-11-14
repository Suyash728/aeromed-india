# -*- coding: utf-8 -*-
"""
AeroMed India - 13 Indic Languages Translation Dictionary Generator
Generates frontend/src/i18n/translations.js with 100% full translations across all 13 languages.
"""

import json

en = {
    "dir": "ltr",
    "cities": {
        "delhi": "Delhi", "mumbai": "Mumbai", "navi mumbai": "Navi Mumbai", "bengaluru": "Bengaluru",
        "kolkata": "Kolkata", "chennai": "Chennai", "hyderabad": "Hyderabad", "ahmedabad": "Ahmedabad",
        "pune": "Pune", "amritsar": "Amritsar", "bhubaneswar": "Bhubaneswar", "guwahati": "Guwahati",
        "delhi ncr": "Delhi NCR", "maharashtra": "Maharashtra", "karnataka": "Karnataka",
        "west bengal": "West Bengal", "tamil nadu": "Tamil Nadu", "telangana": "Telangana",
        "gujarat": "Gujarat", "punjab": "Punjab", "odisha": "Odisha", "assam": "Assam"
    },
    "chrome": {
        "brand_name": "AeroMed",
        "brand_suffix": "India",
        "brand_sub": "Clinical Surveillance",
        "active_metro": "Active Metro",
        "search_metros": "Search 12 Indian Metros...",
        "select_language": "Select Surveillance Language",
        "indic_scripts_note": "13 Indic scripts with verified medical lexicons",
        "more_languages": "+10 More",
        "export_advisory": "Export Advisory",
        "bulletin": "Bulletin",
        "render_connected": "Render API Connected • R² = 0.988",
        "live_api": "Live API",
        "seed_mode": "Instant Seed Mode (0ms)",
        "instant_seed": "Seed Mode",
        "cpcb_caqm_grounding": "CPCB & CAQM Statutory Grounding",
        "live_projection": "Live 48h Projection"
    },
    "nav": {
        "workspaces": "Clinical Workspaces",
        "surveillance": "Surveillance Overview",
        "surveillance_sub": "Bento Grid & Telemetry",
        "simulator": "What-If Simulator",
        "simulator_sub": "ML Sensitivity Lab",
        "triage": "Clinical Triage Copilot",
        "triage_sub": "Vector RAG Grounding",
        "datasets": "Dataset Explorer",
        "datasets_sub": "10 Materialized CSVs",
        "jury": "Adaption AI 7-Pillar Proof",
        "jury_sub": "Hackathon Award Suite",
        "precision_title": "Model Precision",
        "mae_label": "Mean Abs Error",
        "autoscientist_label": "AutoScientist Win",
        "autoscientist_win": "AutoScientist Win",
        "adaption_eval_label": "Adaption Eval",
        "adaption_eval": "Adaption Eval"
    },
    "overview": {
        "kpi_current_aqi": "Atmospheric AQI Index",
        "kpi_aqi": "Real-Time Air Quality (AQI)",
        "kpi_aqi_sub": "Open-Meteo Multi-Station Sensors",
        "kpi_pm25": "Ambient PM2.5 Concentration",
        "kpi_pm25_sub": "Fine Particulate Matter (µg/m³)",
        "kpi_surge_risk": "48h Surge Risk Score",
        "kpi_risk": "Respiratory Admission Risk",
        "kpi_risk_sub": "ML Gradient Boosting Prediction",
        "kpi_grap_stage": "Statutory GRAP Stage",
        "kpi_dominant_trigger": "Dominant Trigger & Temp",
        "kpi_admissions": "Projected Hospital Admissions",
        "kpi_admissions_sub": "48h Surge Capacity Dispatch",
        "projected_admissions": "Projected Admissions",
        "pts_day": "pts/day",
        "grap_sub": "Civic vehicle restrictions & primary school warnings active.",
        "caqm_schedule": "CAQM Statutory Schedule (17 Pages)",
        "airway_penetration": "Airway Penetration:",
        "alveolar_deep": "Alveolar (Deep)",
        "capacity_strain": "Capacity Target & Hospital Strain",
        "capacity_sub": "48-hour projected ICU & emergency bed threshold",
        "surge_score": "Surge Score",
        "safe_capacity": "Safe Capacity",
        "moderate_strain": "Moderate Strain",
        "high_surge_risk": "High Surge Risk",
        "critical_surge_alert": "Critical Surge Alert",
        "high_surge": "High Surge",
        "severe": "Severe",
        "very_poor": "Very Poor",
        "poor": "Poor",
        "moderate": "Moderate",
        "satisfactory": "Satisfactory",
        "good": "Good",
        "localized_advisory": "Localized Clinical Advisory",
        "rag_match": "RAG Match",
        "vector_source": "Vector Source",
        "map_title": "Pan-India Metro Geographic AQI Map",
        "map_sub": "Atmospheric telemetry across 12 CPCB monitoring hubs. Click pin to fly & focus.",
        "basemap_canvas": "Canvas Light",
        "basemap_streets": "Streets",
        "reset_view": "Reset View",
        "live_open_meteo_synced": "Live Open-Meteo Synced",
        "cpcb_scale": "CPCB AQI Scale",
        "severity_ranking": "Regional AQI Severity Ranking (12 Metros)",
        "regional_severity_ranking": "12-Metro Regional AQI Severity Ranking (Real-Time)",
        "focus_dashboard": "Focus Dashboard",
        "click_to_fly": "Click to Fly",
        "chart_title": "Epidemiological Surveillance & Predictive Telemetry",
        "tab_seasonal": "Temporal Telemetry",
        "tab_cities": "12-City Benchmark",
        "tab_weights": "ML Importance",
        "granularity_years": "Years (2015–2025)",
        "granularity_quarters": "Quarters (Q1–Q4)",
        "granularity_months": "Months (Jan–Dec)",
        "granularity_weeks": "Weeks (W1–W4)",
        "granularity_7day": "7-Day Live",
        "all_years": "All Years",
        "all_years_range": "All Years (2015-2025)",
        "all_months": "All Months",
        "all_metros_avg": "All 12 Metros Avg",
        "drill_path": "Drill Path",
        "drill_up": "↑ Drill Up",
        "legend_aqi": "Average US AQI",
        "legend_admissions": "Daily Hospital Admissions",
        "pm25_conc": "PM2.5 Concentration (µg/m³)",
        "click_to_drill": "💡 Click any bar to drill down",
        "heatmap_title": "Pearson Epidemiological Correlation Matrix (8×8)",
        "heatmap_desc": "Pairwise correlation coefficients (r) between criteria pollutants, meteorology, and ICU admissions.",
        "temp_label": "Temp",
        "admissions_label": "Admit",
        "key_epidemiological_finding": "Key Epidemiological Finding:",
        "dispatch_title": "Live Hospital Surge & Emergency Dispatch Queue",
        "dispatch_desc": "Automated bed, ventilator, and oxygen van allocation triggered by real-time ML risk & CAQM GRAP stages.",
        "hospital_name": "Hospital Name",
        "metro": "Metro Hub",
        "col_trigger": "Atmospheric Trigger",
        "col_resource": "Resource Allocation",
        "col_grap": "CAQM GRAP Stage",
        "col_eta": "Dispatch ETA",
        "icu_strain": "ICU Strain",
        "priority": "Priority",
        "action": "Action",
        "export_csv": "Export Dispatch Queue CSV"
    },
    "copilot": {
        "floating_button": "Ask AeroMed Copilot",
        "ai_triage": "AI Triage",
        "rag_live": "RAG Live",
        "title": "AeroMed Clinical Copilot",
        "ask_placeholder": "Ask in Marathi, Hindi, Tamil, or English...",
        "send": "Send"
    },
    "simulator": {
        "title": "What-If Atmospheric Sensitivity & Hospital Surge Simulator",
        "subtitle": "Real-time sensitivity analysis powered by Gradient Boosting Regressor (R² = 0.9879). Alter pollutant concentrations to project emergency ward admissions and trigger CAQM GRAP stages.",
        "active_city_baseline": "Active City Baseline",
        "presets_title": "One-Click Extreme Smog & Weather Presets",
        "reset_defaults": "Reset Sliders",
        "adjust_pollutants": "Adjust Ambient Criteria Pollutants & Meteorology",
        "pm25_weight": "96.5% ML Weight",
        "hospital_surge_forecast": "Hospital Surge Forecast",
        "predicted_daily_admissions": "Projected Daily Respiratory Emergency Admissions",
        "projected_surge_delta": "Projected Surge Delta",
        "critical_care_demands": "Critical Care & Medical Demands",
        "icu_beds": "ICU Beds Needed",
        "nebulizers": "Nebulizers",
        "oxygen_cylinders": "Emergency O₂ Units",
        "statutory_grap_stage": "Statutory CAQM GRAP Stage:"
    },
    "datasets": {
        "title": "Pan-India Adaption Labs Exported Dataset Catalog",
        "subtitle": "Audit of all materialized datasets via Adaption Labs SDK and tracked under backend/data/adaption_exports/ (<25MB each).",
        "total_synced": "Total Synchronized",
        "datasets_label": "Datasets",
        "protocols_label": "Protocols",
        "search_placeholder": "Search datasets, pillars, filenames...",
        "filter_label": "Filter",
        "filter_all": "All",
        "col_name": "Dataset Name & File",
        "col_pillar": "Adaption Capability Pillar",
        "col_rows": "Rows",
        "col_size": "Size",
        "col_quality": "Quality Grade",
        "col_id": "Adaption Dataset ID",
        "col_preview": "Preview",
        "view_rows": "View Rows",
        "table_view": "Table View",
        "protocol_view": "Protocol Card View",
        "close_drawer": "Close Drawer"
    },
    "jury": {
        "title": "Adaption AI Full 7-Pillar Capability Suite — Jury Proof Hub",
        "subtitle": "Verifiable evidence of all 7 core Adaption Labs SDK pillars utilized in building AeroMed India. Every Dataset ID, Run ID, and Quality Evaluation is live and verifiable via SDK.",
        "quality_grade_card": "Adaption Quality Grade",
        "autoscientist_gain_card": "AutoScientist Win Rate",
        "predictive_fit_card": "ML Predictive Fit",
        "credit_reserve_card": "SDK Credit Reserve",
        "verified_proof": "Verified Proof: 7 Pillars",
        "copy_id": "Copy exact Adaption ID",
        "copied": "Copied!",
        "copy_command": "Copy Command"
    }
}

# Complete localized dictionaries for each of the 12 other languages:
hi = {
    "dir": "ltr",
    "cities": {
        "delhi": "दिल्ली", "mumbai": "मुंबई", "navi mumbai": "नवी मुंबई", "bengaluru": "बेंगलुरु",
        "kolkata": "कोलकाता", "chennai": "चेन्नई", "hyderabad": "हैदराबाद", "ahmedabad": "अहमदाबाद",
        "pune": "पुणे", "amritsar": "अमृतसर", "bhubaneswar": "भुवनेश्वर", "guwahati": "गुवाहाटी",
        "delhi ncr": "दिल्ली एनसीआर", "maharashtra": "महाराष्ट्र", "karnataka": "कर्नाटक",
        "west bengal": "पश्चिम बंगाल", "tamil nadu": "तमिलनाडु", "telangana": "तेलंगाना",
        "gujarat": "गुजरात", "punjab": "पंजाब", "odisha": "ओडिशा", "assam": "असम"
    },
    "chrome": {
        "brand_name": "एरोमेड", "brand_suffix": "इंडिया", "brand_sub": "चिकित्सीय निगरानी",
        "active_metro": "सक्रिय मेट्रो", "search_metros": "१२ भारतीय मेट्रो खोजें...",
        "select_language": "निगरानी भाषा चुनें", "indic_scripts_note": "१३ भारतीय लिपियों में सत्यापित चिकित्सा शब्दावली",
        "more_languages": "+१० अन्य", "export_advisory": "परामर्श निर्यात करें", "bulletin": "बुलेटिन",
        "render_connected": "रेंडर एपीआई कनेक्टेड • R² = ०.९८८", "live_api": "लाइव एपीआई",
        "seed_mode": "त्वरित सीड मोड (० मिलीसेकंड)", "instant_seed": "सीड मोड",
        "cpcb_caqm_grounding": "सीपीसीबी और सीएक्यूएम वैधानिक आधार", "live_projection": "लाइव ४८ घंटे का अनुमान"
    },
    "nav": {
        "workspaces": "चिकित्सीय कार्यक्षेत्र", "surveillance": "निगरानी अवलोकन", "surveillance_sub": "बेंटो ग्रिड और टेलीमेट्री",
        "simulator": "व्हाट-इफ सिम्युलेटर", "simulator_sub": "एमएल संवेदनशीलता प्रयोगशाला",
        "triage": "क्लीनिकल ट्रायज कोपायलट", "triage_sub": "वेक्टर आरएजी आधार",
        "datasets": "डेटासेट एक्सप्लोरर", "datasets_sub": "१० संकलित सीएसवी",
        "jury": "अडैप्शन एआई ७-स्तंभ प्रमाण", "jury_sub": "हैकाथॉन पुरस्कार सुइट",
        "precision_title": "मॉडल सटीकता", "mae_label": "औसत त्रुटि", "autoscientist_label": "ऑटो-साइंटिस्ट जीत",
        "autoscientist_win": "ऑटो-साइंटिस्ट जीत", "adaption_eval_label": "अडैप्शन मूल्यांकन", "adaption_eval": "अडैप्शन मूल्यांकन"
    },
    "overview": {
        "kpi_current_aqi": "वायु गुणवत्ता सूचकांक (AQI)", "kpi_aqi": "वास्तविक समय वायु गुणवत्ता",
        "kpi_aqi_sub": "ओपन-मेटियो मल्टी-स्टेशन सेंसर", "kpi_pm25": "परिवेशी PM2.5 सांद्रता",
        "kpi_pm25_sub": "बारीक कण सांद्रता (µg/m³)", "kpi_surge_risk": "४८ घंटे का अस्पताल वृद्धि जोखिम",
        "kpi_risk": "श्वसन भर्ती जोखिम", "kpi_risk_sub": "एमएल ग्रेडिएंट बूस्टिंग भविष्यवाणी",
        "kpi_grap_stage": "वैधानिक ग्रैप (GRAP) चरण", "kpi_dominant_trigger": "प्रमुख कारक और तापमान",
        "kpi_admissions": "अनुमानित अस्पताल भर्तियां", "kpi_admissions_sub": "४८ घंटे की आपातकालीन क्षमता",
        "projected_admissions": "अनुमानित भर्तियां", "pts_day": "मरीज/दिन",
        "grap_sub": "वाहन प्रतिबंध और प्राथमिक विद्यालयों के लिए चेतावनी सक्रिय।",
        "caqm_schedule": "सीएक्यूएम वैधानिक अनुसूची (१७ पृष्ठ)",
        "airway_penetration": "श्वसन तंत्र प्रवेश:", "alveolar_deep": "एल्वियोलर (गहरा)",
        "capacity_strain": "क्षमता लक्ष्य और अस्पताल दबाव", "capacity_sub": "४८ घंटे की अनुमानित आईसीयू और आपातकालीन बिस्तर सीमा",
        "surge_score": "वृद्धि स्कोर", "safe_capacity": "सुरक्षित क्षमता", "moderate_strain": "मध्यम दबाव",
        "high_surge_risk": "उच्च वृद्धि जोखिम", "critical_surge_alert": "गंभीर आपातकालीन चेतावनी",
        "high_surge": "उच्च वृद्धि", "severe": "गंभीर", "very_poor": "बहुत खराब", "poor": "खराब",
        "moderate": "मध्यम", "satisfactory": "संतोषजनक", "good": "अच्छा",
        "localized_advisory": "स्थानीयकृत चिकित्सीय परामर्श", "rag_match": "आरएजी मिलान", "vector_source": "वेक्टर स्रोत",
        "map_title": "अखिल भारतीय मेट्रो भौगोलिक AQI मानचित्र",
        "map_sub": "१२ सीपीसीबी निगरानी केंद्रों पर वायुमंडलीय टेलीमेट्री। फोकस करने हेतु पिन पर क्लिक करें।",
        "basemap_canvas": "कैनवास लाइट", "basemap_streets": "सड़कें", "reset_view": "रीसेट व्यू",
        "live_open_meteo_synced": "लाइव ओपन-मेटियो सिंक", "cpcb_scale": "सीपीसीबी AQI पैमाना",
        "severity_ranking": "क्षेत्रीय AQI गंभीरता रैंकिंग (१२ मेट्रो)",
        "regional_severity_ranking": "१२-मेट्रो क्षेत्रीय AQI गंभीरता रैंकिंग (लाइव)",
        "focus_dashboard": "डैशबोर्ड फोकस करें", "click_to_fly": "नेविगेट करने हेतु क्लिक करें",
        "chart_title": "महामारी विज्ञान निगरानी और भविष्य कहनेवाला टेलीमेट्री",
        "tab_seasonal": "सामयिक टेलीमेट्री", "tab_cities": "१२-शहर तुलना", "tab_weights": "एमएल विशेषता महत्व",
        "granularity_years": "वर्ष (२०१५–२०२५)", "granularity_quarters": "तिमाही (Q1–Q4)",
        "granularity_months": "महीने (जनवरी–दिसंबर)", "granularity_weeks": "सप्ताह (W1–W4)", "granularity_7day": "७-दिवसीय लाइव",
        "all_years": "सभी वर्ष", "all_years_range": "सभी वर्ष (२०१५-२०२५)", "all_months": "सभी महीने",
        "all_metros_avg": "सभी १२ मेट्रो का औसत", "drill_path": "ड्रिल पथ", "drill_up": "↑ ऊपर जाएं",
        "legend_aqi": "औसत AQI", "legend_admissions": "दैनिक अस्पताल भर्तियां", "pm25_conc": "PM2.5 सांद्रता (µg/m³)",
        "click_to_drill": "💡 विस्तार से देखने के लिए किसी भी बार पर क्लिक करें",
        "heatmap_title": "पियर्सन महामारी सहसंबंध मैट्रिक्स (८×८)",
        "heatmap_desc": "प्रदूषकों, मौसम विज्ञान और आईसीयू भर्तियों के बीच युग्मित सहसंबंध गुणांक (r)।",
        "temp_label": "तापमान", "admissions_label": "भर्तियां", "key_epidemiological_finding": "प्रमुख महामारी विज्ञान निष्कर्ष:",
        "dispatch_title": "लाइव अस्पताल वृद्धि और आपातकालीन प्रेषण कतार",
        "dispatch_desc": "वास्तविक समय एमएल जोखिम और ग्रैप चरणों द्वारा स्वचालित बेड, वेंटिलेटर और ऑक्सीजन वैन आवंटन।",
        "hospital_name": "अस्पताल का नाम", "metro": "मेट्रो हब", "col_trigger": "वायुमंडलीय कारक",
        "col_resource": "संसाधन आवंटन", "col_grap": "सीएक्यूएम ग्रैप चरण", "col_eta": "प्रेषण समय",
        "icu_strain": "आईसीयू दबाव", "priority": "प्राथमिकता", "action": "कार्रवाई",
        "export_csv": "प्रेषण कतार सीएसवी निर्यात करें"
    },
    "copilot": {
        "floating_button": "एरोमेड कोपायलट से पूछें", "ai_triage": "एआई ट्रायज", "rag_live": "आरएजी लाइव",
        "title": "एरोमेड क्लीनिकल कोपायलट", "ask_placeholder": "मराठी, हिन्दी, तमिल या अंग्रेज़ी में पूछें...", "send": "भेजें"
    },
    "simulator": {
        "title": "व्हाट-इफ वायुमंडलीय संवेदनशीलता और अस्पताल वृद्धि सिम्युलेटर",
        "subtitle": "ग्रेडिएंट बूस्टिंग रिग्रेसर द्वारा संचालित वास्तविक समय संवेदनशीलता विश्लेषण। आपातकालीन वार्ड में भर्ती का अनुमान लगाएं।",
        "active_city_baseline": "सक्रिय शहर बेसलाइन", "presets_title": "अत्यधिक स्मॉग और मौसम प्रीसेट",
        "reset_defaults": "स्लाइडर रीसेट करें", "adjust_pollutants": "परिवेशी प्रदूषकों और मौसम को समायोजित करें",
        "pm25_weight": "९६.५% एमएल महत्व", "hospital_surge_forecast": "अस्पताल वृद्धि पूर्वानुमान",
        "predicted_daily_admissions": "अनुमानित दैनिक श्वसन आपातकालीन भर्तियां", "projected_surge_delta": "अनुमानित वृद्धि अंतर",
        "critical_care_demands": "क्रिटिकल केयर और चिकित्सा आवश्यकताएं", "icu_beds": "आवश्यक आईसीयू बेड",
        "nebulizers": "नेबुलाइजर", "oxygen_cylinders": "आपातकालीन ऑक्सीजन सिलेंडर", "statutory_grap_stage": "वैधानिक सीएक्यूएम ग्रैप चरण:"
    },
    "datasets": {
        "title": "अखिल भारतीय अडैप्शन लैब्स निर्यातित डेटासेट कैटलॉग",
        "subtitle": "अडैप्शन लैब्स एसडीके के माध्यम से निर्यात किए गए सभी डेटासेट का ऑडिट।",
        "total_synced": "कुल सिंक्रनाइज़", "datasets_label": "डेटासेट", "protocols_label": "प्रोटोकॉल",
        "search_placeholder": "डेटासेट, स्तंभ या फ़ाइल नाम खोजें...", "filter_label": "फ़िल्टर", "filter_all": "सभी",
        "col_name": "डेटासेट नाम और फ़ाइल", "col_pillar": "अडैप्शन क्षमता स्तंभ", "col_rows": "पंक्तियाँ",
        "col_size": "आकार", "col_quality": "गुणवत्ता ग्रेड", "col_id": "अडैप्शन डेटासेट आईडी",
        "col_preview": "पूर्वावलोकन", "view_rows": "पंक्तियाँ देखें", "table_view": "तालिका दृश्य",
        "protocol_view": "प्रोटोकॉल कार्ड दृश्य", "close_drawer": "दराज बंद करें"
    },
    "jury": {
        "title": "अडैप्शन एआई संपूर्ण ७-स्तंभ क्षमता सुइट — जूरी प्रमाण हब",
        "subtitle": "एरोमेड इंडिया के निर्माण में उपयोग किए गए सभी ७ मुख्य अडैप्शन लैब्स एसडीके स्तंभों का सत्यापन योग्य प्रमाण।",
        "quality_grade_card": "अडैप्शन गुणवत्ता ग्रेड", "autoscientist_gain_card": "ऑटो-साइंटिस्ट जीत दर",
        "predictive_fit_card": "एमएल प्रिडिक्टिव फिट", "credit_reserve_card": "एसडीके क्रेडिट रिज़र्व",
        "verified_proof": "सत्यापित प्रमाण: ७ स्तंभ", "copy_id": "सटीक अडैप्शन आईडी कॉपी करें",
        "copied": "कॉपी किया गया!", "copy_command": "कमांड कॉपी करें"
    }
}

mr = {
    "dir": "ltr",
    "cities": {
        "delhi": "दिल्ली", "mumbai": "मुंबई", "navi mumbai": "नवी मुंबई", "bengaluru": "बंगळुरू",
        "kolkata": "कोलकाता", "chennai": "चेन्नई", "hyderabad": "हैदराबाद", "ahmedabad": "अहमदाबाद",
        "pune": "पुणे", "amritsar": "अमृतसर", "bhubaneswar": "भुवनेश्वर", "guwahati": "गुवाहाटी",
        "delhi ncr": "दिल्ली एनसीआर", "maharashtra": "महाराष्ट्र", "karnataka": "कर्नाटक",
        "west bengal": "पश्चिम बंगाल", "tamil nadu": "तमिळनाडू", "telangana": "तेलंगणा",
        "gujarat": "गुजरात", "punjab": "पंजाब", "odisha": "ओडिशा", "assam": "आसाम"
    },
    "chrome": {
        "brand_name": "एरोमेड", "brand_suffix": "इंडिया", "brand_sub": "क्लिनिकल पाळत",
        "active_metro": "सक्रिय मेट्रो", "search_metros": "१२ भारतीय मेट्रो शोधा...",
        "select_language": "पाळत भाषा निवडा", "indic_scripts_note": "१३ भारतीय लिपींमध्ये प्रमाणित वैद्यकीय शब्दकोश",
        "more_languages": "+१० अधिक", "export_advisory": "सल्ला निर्यात करा", "bulletin": "बुलेटिन",
        "render_connected": "रेंडर एपीआय कनेक्टेड • R² = ०.९८८", "live_api": "थेट एपीआय",
        "seed_mode": "झटपट सीड मोड (० मि.से.)", "instant_seed": "सीड मोड",
        "cpcb_caqm_grounding": "सीपीसीबी व सीएक्यूएम वैधानिक अधिष्ठान", "live_projection": "थेट ४८ तासांचा अंदाज"
    },
    "nav": {
        "workspaces": "क्लिनिकल कार्यक्षेत्र", "surveillance": "पाळत विहंगावलोकन", "surveillance_sub": "बेंटो ग्रिड आणि टेलिमेट्री",
        "simulator": "व्हॉट-इफ सिम्युलेटर", "simulator_sub": "एमएल संवेदनशीलता लॅब",
        "triage": "क्लिनिकल ट्रायज कोपायलट", "triage_sub": "व्हेक्टर आरएजी अधिष्ठान",
        "datasets": "डेटासेट एक्सप्लोरर", "datasets_sub": "१० संकलित सीएसव्ही",
        "jury": "अडॅप्शन एआई ७-स्तंभ पुरावा", "jury_sub": "हॅकाथॉन पुरस्कार संच",
        "precision_title": "मॉडेल अचूकता", "mae_label": "सरासरी त्रुटी", "autoscientist_label": "ऑटो-सायंटिस्ट विजय",
        "autoscientist_win": "ऑटो-सायंटिस्ट विजय", "adaption_eval_label": "अडॅप्शन मूल्यांकन", "adaption_eval": "अडॅप्शन मूल्यांकन"
    },
    "overview": {
        "kpi_current_aqi": "हवेचा गुणवत्ता निर्देशांक (AQI)", "kpi_aqi": "थेट हवेची गुणवत्ता",
        "kpi_aqi_sub": "ओपन-मेटिओ बहु-केंद्र सेन्सर्स", "kpi_pm25": "परिसरातील PM2.5 प्रमाण",
        "kpi_pm25_sub": "सूक्ष्म धूलिकण प्रमाण (µg/m³)", "kpi_surge_risk": "४८ तासांचा रुग्णालय वाढ धोका",
        "kpi_risk": "श्वसन भरती जोखीम", "kpi_risk_sub": "एमएल ग्रेडियंट बूस्टिंग अंदाज",
        "kpi_grap_stage": "वैधानिक ग्रॅप (GRAP) टप्पा", "kpi_dominant_trigger": "प्रमुख घटक व तापमान",
        "kpi_admissions": "अंदाजित रुग्णालय भरती", "kpi_admissions_sub": "४८ तास आपत्कालीन क्षमता",
        "projected_admissions": "अंदाजित भरती", "pts_day": "रुग्ण/दिवस",
        "grap_sub": "वाहनांवर निर्बंध आणि शाळांसाठी दक्षतेचा इशारा सक्रिय.",
        "caqm_schedule": "सीएक्यूएम वैधानिक वेळापत्रक (१७ पाने)",
        "airway_penetration": "श्वसनमार्ग प्रवेश:", "alveolar_deep": "अल्व्हिओलर (खोल)",
        "capacity_strain": "क्षमता लक्ष्य व रुग्णालय ताण", "capacity_sub": "४८ तासांची अंदाजित आयसीयू व आपत्कालीन खाटांची मर्यादा",
        "surge_score": "वाढ धावसंख्या", "safe_capacity": "सुरक्षित क्षमता", "moderate_strain": "मध्यम ताण",
        "high_surge_risk": "उच्च वाढ जोखीम", "critical_surge_alert": "गंभीर आपत्कालीन इशारा",
        "high_surge": "उच्च वाढ", "severe": "अतिगंभीर", "very_poor": "खूप वाईट", "poor": "वाईट",
        "moderate": "मध्यम", "satisfactory": "समाधानकारक", "good": "चांगली",
        "localized_advisory": "स्थानिक क्लिनिकल वैद्यकीय सल्ला", "rag_match": "आरएजी जुळणी", "vector_source": "व्हेक्टर स्रोत",
        "map_title": "अखिल भारतीय मेट्रो भौगोलिक AQI नकाशा",
        "map_sub": "१२ सीपीसीबी केंद्रांवरील वातावरणीय टेलिमेट्री. लक्ष केंद्रित करण्यासाठी पिनवर क्लिक करा.",
        "basemap_canvas": "कॅनव्हास लाइट", "basemap_streets": "रस्ते", "reset_view": "रीसेट व्ह्यू",
        "live_open_meteo_synced": "थेट ओपन-मेटिओ सिंक", "cpcb_scale": "सीपीसीबी AQI प्रमाण",
        "severity_ranking": "प्रादेशिक AQI तीव्रता क्रमवारी (१२ मेट्रो)",
        "regional_severity_ranking": "१२-मेट्रो प्रादेशिक AQI तीव्रता क्रमवारी (थेट)",
        "focus_dashboard": "डॅशबोर्डवर लक्ष केंद्रित करा", "click_to_fly": "उड्डाण करण्यासाठी क्लिक करा",
        "chart_title": "रोगराई पाळत आणि भाकित टेलिमेट्री",
        "tab_seasonal": "हंगामी टेलिमेट्री", "tab_cities": "१२-शहर तुलना", "tab_weights": "एमएल महत्त्व",
        "granularity_years": "वर्षे (२०१५–२०२५)", "granularity_quarters": "तिमाही (Q1–Q4)",
        "granularity_months": "महिने (जानेवारी–डिसेंबर)", "granularity_weeks": "आठवडे (W1–W4)", "granularity_7day": "७-दिवस थेट",
        "all_years": "सर्व वर्षे", "all_years_range": "सर्व वर्षे (२०१५-२०२५)", "all_months": "सर्व महिने",
        "all_metros_avg": "सर्व १२ मेट्रोची सरासरी", "drill_path": "ड्रिल मार्ग", "drill_up": "↑ वर जा",
        "legend_aqi": "सरासरी AQI", "legend_admissions": "दैनिक रुग्णालय भरती", "pm25_conc": "PM2.5 प्रमाण (µg/m³)",
        "click_to_drill": "💡 सविस्तर पाहण्यासाठी कोणत्याही बारवर क्लिक करा",
        "heatmap_title": "पिअर्सन रोगराई सहसंबंध मॅट्रिक्स (८×८)",
        "heatmap_desc": "प्रदूषक, हवामान आणि आयसीयू भरती यांच्यातील सहसंबंध गुणांक (r).",
        "temp_label": "तापमान", "admissions_label": "भरती", "key_epidemiological_finding": "प्रमुख रोगराई निष्कर्ष:",
        "dispatch_title": "थेट रुग्णालय वाढ व आपत्कालीन वाटप रांग",
        "dispatch_desc": "रिअल-टाइम एमएल जोखीम आणि ग्रॅप टप्प्यांद्वारे स्वयंचलित बेड्स, व्हेंटिलेटर आणि ऑक्सिजन व्हॅन वाटप.",
        "hospital_name": "रुग्णालयाचे नाव", "metro": "मेट्रो केंद्र", "col_trigger": "वातावरणीय कारण",
        "col_resource": "संसाधन वाटप", "col_grap": "सीएक्यूएम ग्रॅप टप्पा", "col_eta": "वाटप वेळ",
        "icu_strain": "आयसीयू ताण", "priority": "प्राधान्य", "action": "कृती",
        "export_csv": "वाटप रांग सीएसव्ही निर्यात करा"
    },
    "copilot": {
        "floating_button": "एरोमेड कोपायलटला विचारा", "ai_triage": "एआय ट्रायज", "rag_live": "आरएजी थेट",
        "title": "एरोमेड क्लिनिकल कोपायलट", "ask_placeholder": "मराठी, हिन्दी, तमिळ किंवा इंग्रजीत विचारा...", "send": "पाठवा"
    },
    "simulator": {
        "title": "व्हॉट-इफ वातावरणीय संवेदनशीलता व रुग्णालय वाढ सिम्युलेटर",
        "subtitle": "ग्रेडियंट बूस्टिंग रिग्रेसरद्वारे संचलित संवेदनशीलता विश्लेषण. आपत्कालीन कक्षातील रुग्णांचा अंदाज घ्या.",
        "active_city_baseline": "सक्रिय शहर बेसलाइन", "presets_title": "तीव्र धूर व हवामान प्रीसेट्स",
        "reset_defaults": "स्लायडर्स पूर्ववत करा", "adjust_pollutants": "प्रदूषक आणि हवामान समायोजित करा",
        "pm25_weight": "९६.५% एमएल महत्त्व", "hospital_surge_forecast": "रुग्णालय वाढ अंदाज",
        "predicted_daily_admissions": "अंदाजित दैनिक श्वसन आपत्कालीन भरती", "projected_surge_delta": "अंदाजित वाढ फरक",
        "critical_care_demands": "क्रिटिकल केअर आणि वैद्यकीय गरजा", "icu_beds": "आवश्यक आयसीयू बेड्स",
        "nebulizers": "नेब्युलायझर्स", "oxygen_cylinders": "आपत्कालीन ऑक्सिजन सिलिंडर", "statutory_grap_stage": "वैधानिक सीएक्यूएम ग्रॅप टप्पा:"
    },
    "datasets": {
        "title": "अखिल भारतीय अडैप्शन लॅब्स निर्यात डेटासेट कॅटलॉग",
        "subtitle": "अडैप्शन लॅब्स एसडीकेद्वारे निर्यात केलेल्या सर्व डेटासेट्सचे ऑडिट.",
        "total_synced": "एकूण सिंक केलेले", "datasets_label": "डेटासेट्स", "protocols_label": "प्रोटोकॉल्स",
        "search_placeholder": "डेटासेट, स्तंभ किंवा नाव शोधा...", "filter_label": "फिल्टर", "filter_all": "सर्व",
        "col_name": "डेटासेट नाव व फाईल", "col_pillar": "अडैप्शन क्षमता स्तंभ", "col_rows": "ओळी",
        "col_size": "आकार", "col_quality": "गुणवत्ता श्रेणी", "col_id": "अडैप्शन डेटासेट आयडी",
        "col_preview": "पूर्वावलोकन", "view_rows": "ओळी पहा", "table_view": "तक्ता दृश्य",
        "protocol_view": "प्रोटोकॉल कार्ड दृश्य", "close_drawer": "बंद करा"
    },
    "jury": {
        "title": "अडैप्शन एआई संपूर्ण ७-स्तंभ क्षमता संच — ज्युरी पुरावा केंद्र",
        "subtitle": "एरोमेड इंडियाच्या निर्मितीमध्ये वापरलेल्या सर्व ७ मुख्य अडैप्शन लॅब्स एसडीके स्तंभांचा पुरावा.",
        "quality_grade_card": "अडैप्शन गुणवत्ता श्रेणी", "autoscientist_gain_card": "ऑटो-सायंटिस्ट विजय दर",
        "predictive_fit_card": "एमएल प्रेडिक्टिव्ह तंदुरुस्ती", "credit_reserve_card": "एसडीके क्रेडिट राखीव",
        "verified_proof": "सत्यापित पुरावा: ७ स्तंभ", "copy_id": "अडैप्शन आयडी कॉपी करा",
        "copied": "कॉपी केले!", "copy_command": "कमांड कॉपी करा"
    }
}

from generate_all_translations import cities_data

# Bengali (bn)
bn_cities = cities_data["bn"]
bn = {
    "dir": "ltr",
    "cities": bn_cities,
    "chrome": {
        "brand_name": "অ্যারোমেড", "brand_suffix": "ইন্ডিয়া", "brand_sub": "ক্লিনিক্যাল নজরদারি",
        "active_metro": "সক্রিয় মেট্রো", "search_metros": "১২টি ভারতীয় মেট্রো অনুসন্ধান করুন...",
        "select_language": "নজরদারি ভাষা নির্বাচন করুন", "indic_scripts_note": "১৩টি ভারতীয় লিপিতে যাচাইকৃত চিকিৎসা পরিভাষা",
        "more_languages": "+১০টি আরো", "export_advisory": "পরামর্শ রপ্তানি করুন", "bulletin": "বুলেটিন",
        "render_connected": "রেন্ডার এপিআই সংযুক্ত • R² = ০.৯৮৮", "live_api": "লাইভ এপিআই",
        "seed_mode": "তাত্ক্ষণিক সিড মোড (০ms)", "instant_seed": "সিড মোড",
        "cpcb_caqm_grounding": "সিপিসিবি ও সিএকিউএম সংবিধিবদ্ধ ভিত্তি", "live_projection": "লাইভ ৪৮ ঘণ্টার পূর্বাভাস"
    },
    "nav": {
        "workspaces": "ক্লিনিক্যাল কর্মক্ষেত্র", "surveillance": "নজরদারি ওভারভিউ", "surveillance_sub": "বেন্টো গ্রিড এবং টেলিমেট্রি",
        "simulator": "হোয়াট-ইফ সিমুলেটর", "simulator_sub": "এমএল সংবেদনশীলতা ল্যাব",
        "triage": "ক্লিনিক্যাল ট্রায়াজ কোপাইলট", "triage_sub": "ভেক্টর আরএজি ভিত্তি",
        "datasets": "ডেটাবেস এক্সপ্লোরার", "datasets_sub": "১০টি সিএসভি ফাইল",
        "jury": "অ্যাডাপশন এআই ৭-স্তম্ভ প্রমাণ", "jury_sub": "হ্যাকাতন পুরস্কার স্যুট",
        "precision_title": "মডেল নির্ভুলতা", "mae_label": "গড় পরম ত্রুটি", "autoscientist_label": "অটো-সায়েন্টিস্ট বিজয়",
        "autoscientist_win": "অটো-সায়েন্টিস্ট বিজয়", "adaption_eval_label": "অ্যাডাপশন মূল্যায়ন", "adaption_eval": "অ্যাডাপশন মূল্যায়ন"
    },
    "overview": {
        "kpi_current_aqi": "বায়ু গুণমান সূচক (AQI)", "kpi_aqi": "রিয়েল-টাইম বায়ু গুণমান",
        "kpi_aqi_sub": "ওপেন-মেটিও মাল্টি-স্টেশন সেন্সর", "kpi_pm25": "বায়ুমণ্ডলীয় PM2.5 ঘনত্ব",
        "kpi_pm25_sub": "সূক্ষ্ম কণা উপাদান (µg/m³)", "kpi_surge_risk": "৪৮ ঘণ্টার হাসপাতালে ভর্তির ঝুঁকি",
        "kpi_risk": "শ্বাসযন্ত্রের ভর্তির ঝুঁকি", "kpi_risk_sub": "এমএল গ্রেডিয়েন্ট বুস্টিং পূর্বাভাস",
        "kpi_grap_stage": "সংবিধিবদ্ধ গ্র্যাপ (GRAP) পর্যায়", "kpi_dominant_trigger": "প্রধান কারণ ও তাপমাত্রা",
        "kpi_admissions": "প্রত্যাশিত হাসপাতালে ভর্তি", "kpi_admissions_sub": "৪৮ ঘণ্টা জরুরি প্রতিক্রিয়া ক্ষমতা",
        "projected_admissions": "প্রত্যাশিত ভর্তি", "pts_day": "রোগী/দিন",
        "grap_sub": "যানবাহন নিয়ন্ত্রণ ও প্রাথমিক বিদ্যালয় সতর্কতা সক্রিয়।",
        "caqm_schedule": "সিএকিউএম সংবিধিবদ্ধ সময়সূচী (১৭ পৃষ্ঠা)",
        "airway_penetration": "শ্বাসনালী অনুপ্রবেশ:", "alveolar_deep": "অ্যালভিওলার (গভীর)",
        "capacity_strain": "ধারণক্ষমতা লক্ষ্য এবং হাসপাতাল চাপ", "capacity_sub": "৪৮ ঘণ্টার প্রত্যাশিত আইসিইউ এবং জরুরি বেড সীমা",
        "surge_score": "বৃদ্ধি স্কোর", "safe_capacity": "নিরাপদ ক্ষমতা", "moderate_strain": "মাঝারি চাপ",
        "high_surge_risk": "উচ্চ বৃদ্ধি ঝুঁকি", "critical_surge_alert": "জরুরি সতর্কতা",
        "high_surge": "উচ্চ বৃদ্ধি", "severe": "গুরুতর", "very_poor": "খুব খারাপ", "poor": "খারাপ",
        "moderate": "মাঝারি", "satisfactory": "সন্তোষজনক", "good": "ভালো",
        "localized_advisory": "স্থানীয় ক্লিনিক্যাল পরামর্শ", "rag_match": "আরএজি মিল", "vector_source": "ভেক্টর উৎস",
        "map_title": "সর্বভারতীয় মেট্রো ভৌগোলিক একিউআই মানচিত্র",
        "map_sub": "১২টি সিপিসিবি পর্যবেক্ষণ কেন্দ্র জুড়ে বায়ুমণ্ডলীয় টেলিমেট্রি। ফোকাস করতে পিনে ক্লিক করুন।",
        "basemap_canvas": "ক্যানভাস লাইট", "basemap_streets": "রাস্তাঘাট", "reset_view": "রিসেট ভিউ",
        "live_open_meteo_synced": "লাইভ ওপেন-মেটিও সিঙ্ক", "cpcb_scale": "সিপিসিবি একিউআই স্কেল",
        "severity_ranking": "আঞ্চলিক একিউআই তীব্রতা র‍্যাঙ্কিং (১২ মেট্রো)",
        "regional_severity_ranking": "১২-মেট্রো আঞ্চলিক একিউআই তীব্রতা র‍্যাঙ্কিং (লাইভ)",
        "focus_dashboard": "ড্যাশবোর্ড ফোকাস করুন", "click_to_fly": "ন্যাভিগেট করতে ক্লিক করুন",
        "chart_title": "মহামারী সংক্রান্ত নজরদারি ও পূর্বাভাস টেলিমেট্রি",
        "tab_seasonal": "সাময়িক টেলিমেট্রি", "tab_cities": "১২-শহরের তুলনা", "tab_weights": "এমএল গুরুত্ব",
        "granularity_years": "বছর (২০১৫–২০২৫)", "granularity_quarters": "ত্রৈমাসিক (Q1–Q4)",
        "granularity_months": "মাস (জানু–ডিসেম্বর)", "granularity_weeks": "সপ্তাহ (W1–W4)", "granularity_7day": "৭-দিনের লাইভ",
        "all_years": "সকল বছর", "all_years_range": "সকল বছর (২০১৫-২০২৫)", "all_months": "সকল মাস",
        "all_metros_avg": "১২টি মেট্রোর গড়", "drill_path": "ড্রিল পাথ", "drill_up": "↑ উপরে যান",
        "legend_aqi": "গড় একিউআই", "legend_admissions": "দৈনিক হাসপাতালে ভর্তি", "pm25_conc": "PM2.5 ঘনত্ব (µg/m³)",
        "click_to_drill": "💡 বিস্তারিত দেখতে যেকোনো বারে ক্লিক করুন",
        "heatmap_title": "পিয়ারসন মহামারীবিদ্যা পারস্পরিক সম্পর্ক ম্যাট্রিক্স (৮×৮)",
        "heatmap_desc": "দূষণকারী, আবহাওয়া এবং আইসিইউ ভর্তির মধ্যে পারস্পরিক সম্পর্ক সহগ (r)।",
        "temp_label": "তাপমাত্রা", "admissions_label": "ভর্তি", "key_epidemiological_finding": "মূল মহামারী সংক্রান্ত অনুসন্ধান:",
        "dispatch_title": "লাইভ হাসপাতাল জরুরি প্রেরণ সারি",
        "dispatch_desc": "রিয়েল-টাইম এমএল ঝুঁকি এবং গ্র্যাপ পর্যায় দ্বারা স্বয়ংক্রিয় বেড ও অক্সিজেন ভ্যান বরাদ্দ।",
        "hospital_name": "হাসপাতালের নাম", "metro": "মেট্রো হাব", "col_trigger": "বায়ুমণ্ডলীয় কারণ",
        "col_resource": "সম্পদ বরাদ্দ", "col_grap": "সিএকিউএম গ্র্যাপ পর্যায়", "col_eta": "প্রেরণ সময়",
        "icu_strain": "আইসিইউ চাপ", "priority": "অগ্রাধিকার", "action": "পদক্ষেপ",
        "export_csv": "প্রেরণ সারি সিএসভি রপ্তানি করুন"
    },
    "copilot": {
        "floating_button": "অ্যারোমেড কোপাইলটকে জিজ্ঞাসা করুন", "ai_triage": "এআই ট্রায়াজ", "rag_live": "আরএজি লাইভ",
        "title": "অ্যারোমেড ক্লিনিক্যাল কোপাইলট", "ask_placeholder": "মারাঠি, হিন্দি, তামিল বা ইংরেজিতে জিজ্ঞাসা করুন...", "send": "পাঠান"
    },
    "simulator": {
        "title": "হোয়াট-ইফ বায়ুমণ্ডলীয় সংবেদনশীলতা ও হাসপাতাল বৃদ্ধি সিমুলেটর",
        "subtitle": "গ্রেডিয়েন্ট বুস্টিং রিগ্রেসর দ্বারা চালিত রিয়েল-টাইম বিশ্লেষণ। জরুরি ওয়ার্ডে ভর্তির পূর্বাভাস দিন।",
        "active_city_baseline": "সক্রিয় শহর বেসলাইন", "presets_title": "তীব্র ধোঁয়াশা ও আবহাওয়া প্রিসেট",
        "reset_defaults": "স্লাইডার রিসেট করুন", "adjust_pollutants": "দূষণকারী ও আবহাওয়া সামঞ্জস্য করুন",
        "pm25_weight": "৯৬.৫% এমএল গুরুত্ব", "hospital_surge_forecast": "হাসপাতাল বৃদ্ধি পূর্বাভাস",
        "predicted_daily_admissions": "প্রত্যাশিত দৈনিক শ্বাসযন্ত্রের জরুরি ভর্তি", "projected_surge_delta": "প্রত্যাশিত বৃদ্ধি পার্থক্য",
        "critical_care_demands": "জরুরি যত্ন এবং চিকিৎসা চাহিদা", "icu_beds": "প্রয়োজনীয় আইসিইউ বেড",
        "nebulizers": "নেবুলাইজার", "oxygen_cylinders": "জরুরি অক্সিজেন ইউনিট", "statutory_grap_stage": "সংবিধিবদ্ধ সিএকিউএম গ্র্যাপ পর্যায়:"
    },
    "datasets": {
        "title": "সর্বভারতীয় অ্যাডাপশন ল্যাবস এক্সপোর্টেড ক্যাটালগ",
        "subtitle": "অ্যাডাপশন ল্যাবস এসডিকে-এর মাধ্যমে সিঙ্ক করা ডেটাবেসের অডিট।",
        "total_synced": "মোট সিঙ্ক করা হয়েছে", "datasets_label": "ডেটাবেস", "protocols_label": "প্রোটোকল",
        "search_placeholder": "অনুসন্ধান করুন...", "filter_label": "ফিল্টার", "filter_all": "সকল",
        "col_name": "নাম ও ফাইল", "col_pillar": "অ্যাডাপশন স্তম্ভ", "col_rows": "সারি",
        "col_size": "আকার", "col_quality": "গ্রেড", "col_id": "আইডি",
        "col_preview": "প্রাকদর্শন", "view_rows": "সারি দেখুন", "table_view": "টেবিল ভিউ",
        "protocol_view": "কার্ড ভিউ", "close_drawer": "বন্ধ করুন"
    },
    "jury": {
        "title": "অ্যাডাপশন এআই পূর্ণ ৭-স্তম্ভ স্যুট — জুরি প্রমাণ কেন্দ্র",
        "subtitle": "অ্যারোমেড ইন্ডিয়ায় ব্যবহৃত ৭টি মূল স্তম্ভের প্রমাণ।",
        "quality_grade_card": "গুণমান গ্রেড", "autoscientist_gain_card": "বিজয় হার",
        "predictive_fit_card": "এমএল ভবিষ্যদ্বাণী ফিট", "credit_reserve_card": "এসডিকে ক্রেডিট রিজার্ভ",
        "verified_proof": "যাচাইকৃত প্রমাণ: ৭ স্তম্ভ", "copy_id": "আইডি কপি করুন",
        "copied": "কপি করা হয়েছে!", "copy_command": "কমান্ড কপি করুন"
    }
}

# Tamil (ta)
ta_cities = cities_data["ta"]
ta = {
    "dir": "ltr",
    "cities": ta_cities,
    "chrome": {
        "brand_name": "ஏரோமெட்", "brand_suffix": "இந்தியா", "brand_sub": "மருத்துவ கண்காணிப்பு",
        "active_metro": "செயலில் உள்ள பெருநகரம்", "search_metros": "12 இந்திய பெருநகரங்களைத் தேடுங்கள்...",
        "select_language": "கண்காணிப்பு மொழியைத் தேர்ந்தெடுக்கவும்", "indic_scripts_note": "13 இந்திய மொழிகளில் சரிபார்க்கப்பட்ட மருத்துவச் சொற்கள்",
        "more_languages": "+10 மேலும்", "export_advisory": "ஆலோசனையை ஏற்றுமதி செய்", "bulletin": "அறிக்கை",
        "render_connected": "ரெண்டர் API இணைக்கப்பட்டது • R² = 0.988", "live_api": "நேரலை API",
        "seed_mode": "உடனடி விதை முறை (0ms)", "instant_seed": "விதை முறை",
        "cpcb_caqm_grounding": "CPCB மற்றும் CAQM சட்டப்பூர்வ அடிப்படை", "live_projection": "நேரலை 48 மணிநேர கணிப்பு"
    },
    "nav": {
        "workspaces": "மருத்துவ பணிவெளிகள்", "surveillance": "கண்காணிப்பு கண்ணோட்டம்", "surveillance_sub": "பென்டோ கிரிட் & டெலிமெட்ரி",
        "simulator": "வாட்-இஃப் சிமுலேட்டர்", "simulator_sub": "ML உணர்திறன் ஆய்வகம்",
        "triage": "மருத்துவ ட்ரியேஜ் கோபைலட்", "triage_sub": "வெக்டர் RAG அடிப்படை",
        "datasets": "தரவுத்தொகுப்பு ஆய்வாளர்", "datasets_sub": "10 materialized CSVs",
        "jury": "அடாப்ஷன் AI 7-தூண்கள் ஆதாரம்", "jury_sub": "ஹேக்கத்தான் விருது தொகுப்பு",
        "precision_title": "மாதிரி துல்லியம்", "mae_label": "சராசரி பிழை", "autoscientist_label": "ஆட்டோ சயின்டிஸ்ட் வெற்றி",
        "autoscientist_win": "ஆட்டோ சயின்டிஸ்ட் வெற்றி", "adaption_eval_label": "அடாப்ஷன் மதிப்பீடு", "adaption_eval": "அடாப்ஷன் மதிப்பீடு"
    },
    "overview": {
        "kpi_current_aqi": "காற்றுத் தரக் குறியீடு (AQI)", "kpi_aqi": "நேரலை காற்றுத் தரம்",
        "kpi_aqi_sub": "ஓபன்-மீட்டியோ சென்சார்கள்", "kpi_pm25": "சுற்றுச்சூழல் PM2.5 செறிவு",
        "kpi_pm25_sub": "நுண்ணிய துகள் அளவு (µg/m³)", "kpi_surge_risk": "48 மணிநேர மருத்துவமனை சேர்க்கை ஆபத்து",
        "kpi_risk": "சுவாச சேர்க்கை ஆபத்து", "kpi_risk_sub": "ML கணிப்பு",
        "kpi_grap_stage": "சட்டப்பூர்வ GRAP நிலை", "kpi_dominant_trigger": "முக்கிய காரணி & வெப்பநிலை",
        "kpi_admissions": "கணிக்கப்பட்ட மருத்துவமனை சேர்க்கைகள்", "kpi_admissions_sub": "48 மணி அவசர திறன் ஒதுக்கீடு",
        "projected_admissions": "கணிக்கப்பட்ட சேர்க்கைகள்", "pts_day": "நோயாளிகள்/நாள்",
        "grap_sub": "வாகனக் கட்டுப்பாடுகள் மற்றும் பள்ளி எச்சரிக்கைகள் செயலில் உள்ளன.",
        "caqm_schedule": "CAQM சட்டப்பூர்வ அட்டவணை (17 பக்கங்கள்)",
        "airway_penetration": "சுவாசப்பாதை ஊடுருவல்:", "alveolar_deep": "ஆல்வியோலர் (ஆழமான)",
        "capacity_strain": "கொள்ளளவு இலக்கு & மருத்துவமனை அழுத்தம்", "capacity_sub": "48 மணி ICU மற்றும் அவசர படுக்கை வரம்பு",
        "surge_score": "எழுச்சி மதிப்பெண்", "safe_capacity": "பாதுகாப்பான கொள்ளளவு", "moderate_strain": "மிதமான அழுத்தம்",
        "high_surge_risk": "அதிக எழுச்சி ஆபத்து", "critical_surge_alert": "அவசர தீவிர எச்சரிக்கை",
        "high_surge": "அதிக எழுச்சி", "severe": "தீவிரமானது", "very_poor": "மிகவும் மோசம்", "poor": "மோசம்",
        "moderate": "மிதமானது", "satisfactory": "திருப்திகரமானது", "good": "நன்று",
        "localized_advisory": "உள்ளூர் மருத்துவ ஆலோசனை", "rag_match": "RAG பொருத்தம்", "vector_source": "வெக்டர் மூலம்",
        "map_title": "அகில இந்திய மெட்ரோ புவியியல் AQI வரைபடம்",
        "map_sub": "12 CPCB மையங்களின் வளிமண்டல அளவீடுகள். கவனம் செலுத்த பின்களைக் கிளிக் செய்க.",
        "basemap_canvas": "கேன்வாஸ் லைட்", "basemap_streets": "தெருக்கள்", "reset_view": "மீட்டமை",
        "live_open_meteo_synced": "நேரலை Open-Meteo ஒத்திசைவு", "cpcb_scale": "CPCB AQI அளவு",
        "severity_ranking": "பிராந்திய AQI தீவிர தரவரிசை (12 பெருநகரங்கள்)",
        "regional_severity_ranking": "12-பெருநகர AQI தீவிர தரவரிசை (நேரலை)",
        "focus_dashboard": "டாஷ்போர்டில் கவனம் செலுத்து", "click_to_fly": "செல்ல கிளிக் செய்க",
        "chart_title": "தொற்றுநோயியல் கண்காணிப்பு & முன்னறிவிப்பு டெலிமெட்ரி",
        "tab_seasonal": "பருவகால டெலிமெட்ரி", "tab_cities": "12-நகர ஒப்பீடு", "tab_weights": "ML முக்கியத்துவம்",
        "granularity_years": "ஆண்டுகள் (2015–2025)", "granularity_quarters": "காலாண்டுகள் (Q1–Q4)",
        "granularity_months": "மாதங்கள் (ஜன–டிச)", "granularity_weeks": "வாரங்கள் (W1–W4)", "granularity_7day": "7-நாள் நேரலை",
        "all_years": "அனைத்து ஆண்டுகள்", "all_years_range": "அனைத்து ஆண்டுகள் (2015-2025)", "all_months": "அனைத்து மாதங்கள்",
        "all_metros_avg": "அனைத்து 12 பெருநகர சராசரி", "drill_path": "வழித்தடம்", "drill_up": "↑ மேலே செல்",
        "legend_aqi": "சராசரி AQI", "legend_admissions": "தினசரி சேர்க்கைகள்", "pm25_conc": "PM2.5 செறிவு (µg/m³)",
        "click_to_drill": "💡 மேலும் விவரங்களை அறிய எந்த பட்டையையும் கிளிக் செய்க",
        "heatmap_title": "பியர்சன் தொடர்பு மேட்ரிக்ஸ் (8×8)",
        "heatmap_desc": "மாசுபடுத்திகள், வானிலை மற்றும் சேர்க்கைகளுக்கு இடையிலான தொடர்பு குணகங்கள் (r).",
        "temp_label": "வெப்பநிலை", "admissions_label": "சேர்க்கைகள்", "key_epidemiological_finding": "முக்கிய தொற்றுநோயியல் முடிவு:",
        "dispatch_title": "நேரலை மருத்துவமனை அவசர ஒதுக்கீடு வரிசை",
        "dispatch_desc": "நிகழ்நேர ML ஆபத்து மற்றும் GRAP நிலைகளால் தூண்டப்பட்ட தானியங்கி படுக்கைகள் & ஆக்ஸிஜன் ஒதுக்கீடு.",
        "hospital_name": "மருத்துவமனை பெயர்", "metro": "பெருநகர மையம்", "col_trigger": "வளிமண்டல தூண்டுதல்",
        "col_resource": "வள ஒதுக்கீடு", "col_grap": "CAQM GRAP நிலை", "col_eta": "சேரும் நேரம்",
        "icu_strain": "ICU அழுத்தம்", "priority": "முன்னுரிமை", "action": "நடவடிக்கை",
        "export_csv": "வரிசையை CSV ஆக ஏற்றுமதி செய்"
    },
    "copilot": {
        "floating_button": "ஏரோமெட் கோபைலட்டிடம் கேளுங்கள்", "ai_triage": "AI ட்ரியேஜ்", "rag_live": "RAG நேரலை",
        "title": "ஏரோமெட் மருத்துவ கோபைலட்", "ask_placeholder": "மராத்தி, இந்தி, தமிழ் அல்லது ஆங்கிலத்தில் கேளுங்கள்...", "send": "அனுப்பு"
    },
    "simulator": {
        "title": "வளிமண்டல உணர்திறன் & மருத்துவமனை எழுச்சி சிமுலேட்டர்",
        "subtitle": "கிரேடியன்ட் பூஸ்டிங் ரிக்ரஸரால் இயக்கப்படும் நிகழ்நேர பகுப்பாய்வு. அவசர சிகிச்சைப் பிரிவு சேர்க்கைகளைக் கணிக்கவும்.",
        "active_city_baseline": "செயலில் உள்ள நகர அடிப்படை", "presets_title": "தீவிர புகைமூட்டம் மற்றும் வானிலை அமைப்புகள்",
        "reset_defaults": "மீட்டமை", "adjust_pollutants": "மாசுபடுத்திகளை சரிசெய்யவும்",
        "pm25_weight": "96.5% ML முக்கியத்துவம்", "hospital_surge_forecast": "மருத்துவமனை எழுச்சி முன்னறிவிப்பு",
        "predicted_daily_admissions": "கணிக்கப்பட்ட தினசரி சுவாச அவசர சேர்க்கைகள்", "projected_surge_delta": "கணிக்கப்பட்ட எழுச்சி வேறுபாடு",
        "critical_care_demands": "தீவிர சிகிச்சை & மருத்துவ தேவைகள்", "icu_beds": "தேவைப்படும் ICU படுக்கைகள்",
        "nebulizers": "நெபுலைசர்கள்", "oxygen_cylinders": "அவசர ஆக்ஸிஜன் சிலிண்டர்கள்", "statutory_grap_stage": "சட்டப்பூர்வ CAQM GRAP நிலை:"
    },
    "datasets": {
        "title": "அகில இந்திய அடாப்ஷன் ஆய்வக ஏற்றுமதி அட்டவணை",
        "subtitle": "அடாப்ஷன் லேப்ஸ் SDK மூலம் ஏற்றுமதி செய்யப்பட்ட தரவுத்தொகுப்புகள்.",
        "total_synced": "மொத்தம் ஒத்திசைக்கப்பட்டது", "datasets_label": "தரவுத்தொகுப்புகள்", "protocols_label": "நெறிமுறைகள்",
        "search_placeholder": "தேடுங்கள்...", "filter_label": "வடிகட்டி", "filter_all": "அனைத்தும்",
        "col_name": "பெயர் & கோப்பு", "col_pillar": "திறன் தூண்", "col_rows": "வரிசைகள்",
        "col_size": "அளவு", "col_quality": "தரம்", "col_id": "ஐடி",
        "col_preview": "முன்னோட்டம்", "view_rows": "வரிசைகளைக் காண்க", "table_view": "அட்டவணை பார்வை",
        "protocol_view": "அட்டை பார்வை", "close_drawer": "மூடு"
    },
    "jury": {
        "title": "அடாப்ஷன் AI முழு 7-தூண்கள் திறன் தொகுப்பு — நடுவர் சான்று மையம்",
        "subtitle": "ஏரோமெட் இந்தியாவை உருவாக்குவதில் பயன்படுத்தப்பட்ட அனைத்து 7 தூண்களுக்கான சான்றுகள்.",
        "quality_grade_card": "தர மதிப்பீடு", "autoscientist_gain_card": "வெற்றி விகிதம்",
        "predictive_fit_card": "ML கணிப்பு பொருத்தம்", "credit_reserve_card": "SDK இருப்பு",
        "verified_proof": "சரிபார்க்கப்பட்ட ஆதாரம்: 7 தூண்கள்", "copy_id": "ஐடியை நகலெடு",
        "copied": "நகலெடுக்கப்பட்டது!", "copy_command": "கட்டளையை நகலெடு"
    }
}

# Telugu (te)
te_cities = cities_data["te"]
te = {
    "dir": "ltr",
    "cities": te_cities,
    "chrome": {
        "brand_name": "ఏరోమెడ్", "brand_suffix": "ఇండియా", "brand_sub": "క్లినికల్ నిఘా",
        "active_metro": "క్రియాశీల మెట్రో", "search_metros": "12 భారతీయ మెట్రోలను శోధించండి...",
        "select_language": "నిఘా భాషను ఎంచుకోండి", "indic_scripts_note": "13 భారతీయ లిపులలో ధృవీకరించబడిన వైద్య నిఘంటువు",
        "more_languages": "+10 మరిన్ని", "export_advisory": "సలహాను ఎగుమతి చేయండి", "bulletin": "బులెటిన్",
        "render_connected": "రెండర్ API అనుసంధానించబడింది • R² = 0.988", "live_api": "లైవ్ API",
        "seed_mode": "తక్షణ సీడ్ మోడ్ (0ms)", "instant_seed": "సీడ్ మోడ్",
        "cpcb_caqm_grounding": "CPCB & CAQM చట్టబద్ధమైన ఆధారం", "live_projection": "లైవ్ 48 గంటల అంచనా"
    },
    "nav": {
        "workspaces": "క్లినికల్ వర్క్‌స్పేస్‌లు", "surveillance": "నిఘా అవలోకనం", "surveillance_sub": "బెంటో గ్రిడ్ & టెలిమెట్రీ",
        "simulator": "వాట్-ఇఫ్ సిమ్యులేటర్", "simulator_sub": "ML సున్నితత్వ ప్రయోగశాల",
        "triage": "క్లినికల్ ట్రియాజ్ కోపైలట్", "triage_sub": "వెక్టర్ RAG ఆధారం",
        "datasets": "డేటాసెట్ ఎక్స్‌ప్లోరర్", "datasets_sub": "10 మెటీరియలైజ్డ్ CSVలు",
        "jury": "అడాప్షన్ AI 7-స్తంభాల రుజువు", "jury_sub": "హ్యాకథాన్ అవార్డుల సూట్",
        "precision_title": "మోడల్ ఖచ్చితత్వం", "mae_label": "సగటు సంపూర్ణ లోపం", "autoscientist_label": "ఆటో సైంటిస్ట్ విజయం",
        "autoscientist_win": "ఆటో సైంటిస్ట్ విజయం", "adaption_eval_label": "అడాప్షన్ మూల్యాంకనం", "adaption_eval": "అడాప్షన్ మూల్యాంకనం"
    },
    "overview": {
        "kpi_current_aqi": "గాలి నాణ్యత సూచిక (AQI)", "kpi_aqi": "రియల్ టైమ్ గాలి నాణ్యత",
        "kpi_aqi_sub": "ఓపెన్-మెటియో సెన్సార్లు", "kpi_pm25": "పరిసర PM2.5 సాంద్రత",
        "kpi_pm25_sub": "సూక్ష్మ కణాల పరిమాణం (µg/m³)", "kpi_surge_risk": "48 గంటల ఆసుపత్రి చేరికల ప్రమాదం",
        "kpi_risk": "శ్వాసకోశ చేరికల ప్రమాదం", "kpi_risk_sub": "ML గ్రేడియంట్ బూస్టింగ్ అంచనా",
        "kpi_grap_stage": "చట్టబద్ధమైన GRAP దశ", "kpi_dominant_trigger": "ప్రధాన కారకం & ఉష్ణోగ్రత",
        "kpi_admissions": "అంచనా వేసిన ఆసుపత్రి చేరికలు", "kpi_admissions_sub": "48 గంటల అత్యవసర సామర్థ్య కేటాయింపు",
        "projected_admissions": "అంచనా వేసిన చేరికలు", "pts_day": "రోగులు/రోజు",
        "grap_sub": "వాహనాల ఆంక్షలు మరియు పాఠశాల హెచ్చరికలు క్రియాశీలంగా ఉన్నాయి.",
        "caqm_schedule": "CAQM చట్టబద్ధమైన షెడ్యూల్ (17 పేజీలు)",
        "airway_penetration": "శ్వాసనాళ ప్రవేశం:", "alveolar_deep": "అల్వియోలార్ (లోతైన)",
        "capacity_strain": "సామర్థ్య లక్ష్యం & ఆసుపత్రి ఒత్తిడి", "capacity_sub": "48 గంటల అంచనా వేసిన ICU మరియు అత్యవసర పడకల పరిమితి",
        "surge_score": "సర్జ్ స్కోర్", "safe_capacity": "సురక్షిత సామర్థ్యం", "moderate_strain": "మితమైన ఒత్తిడి",
        "high_surge_risk": "అధిక సర్జ్ ప్రమాదం", "critical_surge_alert": "తీవ్రమైన అత్యవసర హెచ్చరిక",
        "high_surge": "అధిక పెరుగుదల", "severe": "తీవ్రమైనది", "very_poor": "చాలా పేలవమైనది", "poor": "పేలవమైనది",
        "moderate": "మితమైనది", "satisfactory": "సంతృప్తికరమైనది", "good": "మంచిది",
        "localized_advisory": "స్థానికీకరించిన క్లినికల్ సలహా", "rag_match": "RAG సరిపోలిక", "vector_source": "వెక్టర్ మూలం",
        "map_title": "అఖిల భారత మెట్రో భౌగోళిక AQI మ్యాప్",
        "map_sub": "12 CPCB కేంద్రాల వాతావరణ టెలిమెట్రీ. వివరాల కోసం పిన్‌పై క్లిక్ చేయండి.",
        "basemap_canvas": "కాన్వాస్ లైట్", "basemap_streets": "వీధులు", "reset_view": "మ్యాప్‌ను రీసెట్ చేయండి",
        "live_open_meteo_synced": "లైవ్ ఓపెన్-మెటియో సమకాలీకరించబడింది", "cpcb_scale": "CPCB AQI స్కేల్",
        "severity_ranking": "ప్రాంతీయ AQI తీవ్రత ర్యాంకింగ్ (12 మెట్రోలు)",
        "regional_severity_ranking": "12-మెట్రో ప్రాంతీయ AQI తీవ్రత ర్యాంకింగ్ (లైవ్)",
        "focus_dashboard": "డాష్‌బోర్డ్‌ను ఫోకస్ చేయండి", "click_to_fly": "నావిగేట్ చేయడానికి క్లిక్ చేయండి",
        "chart_title": "ఎపిడెమియోలాజికల్ నిఘా & ప్రిడిక్టివ్ టెలిమెట్రీ",
        "tab_seasonal": "సీజనల్ టెలిమెట్రీ", "tab_cities": "12-నగరాల పోలిక", "tab_weights": "ML ప్రాముఖ్యత",
        "granularity_years": "సంవత్సరాలు (2015–2025)", "granularity_quarters": "త్రైమాసికాలు (Q1–Q4)",
        "granularity_months": "నెలలు (జనవరి–డిసెంబర్)", "granularity_weeks": "వారాలు (W1–W4)", "granularity_7day": "7-రోజుల లైవ్",
        "all_years": "అన్ని సంవత్సరాలు", "all_years_range": "అన్ని సంవత్సరాలు (2015-2025)", "all_months": "అన్ని నెలలు",
        "all_metros_avg": "అన్ని 12 మెట్రోల సగటు", "drill_path": "డ్రిల్ మార్గం", "drill_up": "↑ పైకి వెళ్లండి",
        "legend_aqi": "సగటు AQI", "legend_admissions": "రోజువారీ చేరికలు", "pm25_conc": "PM2.5 సాంద్రత (µg/m³)",
        "click_to_drill": "💡 వివరాలను చూడటానికి ఏదైనా బార్‌పై క్లిక్ చేయండి",
        "heatmap_title": "పియర్సన్ కోరిలేషన్ మ్యాట్రిక్స్ (8×8)",
        "heatmap_desc": "కాలుష్య కారకాలు, వాతావరణం మరియు ఆసుపత్రి చేరికల మధ్య సంబంధం (r).",
        "temp_label": "ఉష్ణోగ్రత", "admissions_label": "చేరికలు", "key_epidemiological_finding": "కీలక ఎపిడెమియోలాజికల్ ఫలితం:",
        "dispatch_title": "లైవ్ ఆసుపత్రి అత్యవసర కేటాయింపు క్యూ",
        "dispatch_desc": "నిజ-సమయ ML ప్రమాదం మరియు GRAP దశల ద్వారా పడకలు, వెంటిలేటర్లు మరియు ఆక్సిజన్ వ్యాన్ కేటాయింపు.",
        "hospital_name": "ఆసుపత్రి పేరు", "metro": "మెట్రో కేంద్రం", "col_trigger": "వాతావరణ కారకం",
        "col_resource": "వనరుల కేటాయింపు", "col_grap": "CAQM GRAP దశ", "col_eta": "చేరుకునే సమయం",
        "icu_strain": "ICU ఒత్తిడి", "priority": "ప్రాధాన్యత", "action": "చర్య",
        "export_csv": "క్యూను CSVగా ఎగుమతి చేయండి"
    },
    "copilot": {
        "floating_button": "ఏరోమెడ్ కోపైలట్‌ను అడగండి", "ai_triage": "AI ట్రియాజ్", "rag_live": "RAG లైవ్",
        "title": "ఏరోమెడ్ క్లినికల్ కోపైలట్", "ask_placeholder": "మరాఠీ, హిందీ, తమిళం లేదా ఇంగ్లీషులో అడగండి...", "send": "పంపండి"
    },
    "simulator": {
        "title": "వాతావరణ సున్నితత్వం & ఆసుపత్రి సర్జ్ సిమ్యులేటర్",
        "subtitle": "గ్రేడియంట్ బూస్టింగ్ రిగ్రెసర్ ద్వారా నడిచే నిజ-సమయ విశ్లేషణ. అత్యవసర వార్డులో చేరికలను అంచనా వేయండి.",
        "active_city_baseline": "క్రియాశీల నగర బేస్‌లైన్", "presets_title": "తీవ్రమైన పొగమంచు & వాతావరణ ప్రీసెట్లు",
        "reset_defaults": "స్లైడర్‌లను రీసెట్ చేయండి", "adjust_pollutants": "కాలుష్య కారకాలను సర్దుబాటు చేయండి",
        "pm25_weight": "96.5% ML ప్రాముఖ్యత", "hospital_surge_forecast": "ఆసుపత్రి సర్జ్ సూచన",
        "predicted_daily_admissions": "అంచనా వేసిన రోజువారీ శ్వాసకోశ అత్యవసర చేరికలు", "projected_surge_delta": "అంచనా వేసిన వ్యత్యాసం",
        "critical_care_demands": "క్రిటికల్ కేర్ & వైద్య అవసరాలు", "icu_beds": "అవసరమైన ICU పడకలు",
        "nebulizers": "నెబ్యులైజర్లు", "oxygen_cylinders": "అత్యవసర ఆక్సిజన్ యూనిట్లు", "statutory_grap_stage": "చట్టబద్ధమైన CAQM GRAP దశ:"
    },
    "datasets": {
        "title": "అఖిల భారత అడాప్షన్ ల్యాబ్స్ ఎగుమతి కేటలాగ్",
        "subtitle": "అడాప్షన్ ల్యాబ్స్ SDK ద్వారా సమకాలీకరించబడిన డేటాసెట్‌ల ఆడిట్.",
        "total_synced": "మొత్తం సమకాలీకరించబడింది", "datasets_label": "డేటాసెట్‌లు", "protocols_label": "ప్రోటోకాల్‌లు",
        "search_placeholder": "శోధించండి...", "filter_label": "ఫిల్టర్", "filter_all": "అన్నీ",
        "col_name": "పేరు & ఫైల్", "col_pillar": "సామర్థ్య స్తంభం", "col_rows": "వరుసలు",
        "col_size": "పరిమాణం", "col_quality": "గ్రేడ్", "col_id": "ID",
        "col_preview": "ప్రివ్యూ", "view_rows": "వరుసలను వీక్షించండి", "table_view": "టేబుల్ వీక్షణ",
        "protocol_view": "కార్డ్ వీక్షణ", "close_drawer": "మూసివేయండి"
    },
    "jury": {
        "title": "అడాప్షన్ AI 7-స్తంభాల సామర్థ్య సూట్ — జ్యూరీ ప్రూఫ్ హబ్",
        "subtitle": "ఏరోమెడ్ ఇండియా నిర్మాణంలో ఉపయోగించిన 7 ప్రధాన స్తంభాలకు సంబంధించిన ఆధారాలు.",
        "quality_grade_card": "నాణ్యత గ్రేడ్", "autoscientist_gain_card": "విజయాల రేటు",
        "predictive_fit_card": "ML ప్రిడిక్టివ్ ఫిట్", "credit_reserve_card": "SDK నిల్వ",
        "verified_proof": "ధృవీకరించబడిన రుజువు: 7 స్తంభాలు", "copy_id": "IDని కాపీ చేయండి",
        "copied": "కాపీ చేయబడింది!", "copy_command": "కమాండ్‌ను కాపీ చేయండి"
    }
}

# Urdu (ur)
ur_cities = cities_data["ur"]
ur = {
    "dir": "rtl",
    "cities": ur_cities,
    "chrome": {
        "brand_name": "ایرو میڈ", "brand_suffix": "انڈیا", "brand_sub": "طبی نگرانی",
        "active_metro": "فعال میٹرو", "search_metros": "12 ہندوستانی شہر تلاش کریں...",
        "select_language": "نگرانی کی زبان منتخب کریں", "indic_scripts_note": "13 ہندوستانی رسم الخط میں تصدیق شدہ طبی اصطلاحات",
        "more_languages": "+10 مزید", "export_advisory": "ایڈوائزری برآمد کریں", "bulletin": "بلیٹن",
        "render_connected": "رینڈر API منسلک ہے • R² = 0.988", "live_api": "لائیو API",
        "seed_mode": "فوری سیڈ موڈ (0ms)", "instant_seed": "سیڈ موڈ",
        "cpcb_caqm_grounding": "CPCB اور CAQM قانونی بنیاد", "live_projection": "لائیو 48 گھنٹے کی پیش گوئی"
    },
    "nav": {
        "workspaces": "طبی ورک اسپیس", "surveillance": "نگرانی کا جائزہ", "surveillance_sub": "بینٹو گرڈ اور ٹیلی میٹری",
        "simulator": "واٹ-اف سمیلیٹر", "simulator_sub": "ایم ایل لیب",
        "triage": "کلینیکل ٹریج کوپائلٹ", "triage_sub": "ویکٹر RAG گراؤنڈنگ",
        "datasets": "ڈیٹا سیٹ ایکسپلورر", "datasets_sub": "10 برآمد شدہ فائلیں",
        "jury": "اڈاپشن اے آئی 7-ستون ثبوت", "jury_sub": "ہیکاتھون ایوارڈ سوٹ",
        "precision_title": "ماڈل کی درستگی", "mae_label": "اوسط خرابی", "autoscientist_label": "آٹو سائنٹسٹ جیت",
        "autoscientist_win": "آٹو سائنٹسٹ جیت", "adaption_eval_label": "اڈاپشن تشخیص", "adaption_eval": "اڈاپشن تشخیص"
    },
    "overview": {
        "kpi_current_aqi": "ایئر کوالٹی انڈیکس (AQI)", "kpi_aqi": "براہ راست ہوا کا معیار",
        "kpi_aqi_sub": "اوپن میٹیو ملٹی اسٹیشن سینسرز", "kpi_pm25": "ماحولیاتی PM2.5 ارتکاز",
        "kpi_pm25_sub": "باریک ذرات کی مقدار (µg/m³)", "kpi_surge_risk": "48 گھنٹے ہسپتال میں داخلے کا خطرہ",
        "kpi_risk": "سانس کے داخلے کا خطرہ", "kpi_risk_sub": "ایم ایل پیش گوئی",
        "kpi_grap_stage": "قانونی گریپ (GRAP) مرحلہ", "kpi_dominant_trigger": "اہم محرک اور درجہ حرارت",
        "kpi_admissions": "متوقع ہسپتال داخلے", "kpi_admissions_sub": "48 گھنٹے ایمرجنسی گنجائش",
        "projected_admissions": "متوقع داخلے", "pts_day": "مریض/دن",
        "grap_sub": "گاڑیوں کی پابندیاں اور پرائمری اسکول کی وارننگ فعال ہے۔",
        "caqm_schedule": "CAQM قانونی شیڈول (17 صفحات)",
        "airway_penetration": "سانس کی نالی میں داخل ہونا:", "alveolar_deep": "ایلوولر (گہرا)",
        "capacity_strain": "گنجائش کا ہدف اور ہسپتال کا دباؤ", "capacity_sub": "48 گھنٹے متوقع آئی سی یو اور ہنگامی بستروں کی حد",
        "surge_score": "سرج سکور", "safe_capacity": "محفوظ گنجائش", "moderate_strain": "معتدل دباؤ",
        "high_surge_risk": "زیادہ اضافے کا خطرہ", "critical_surge_alert": "سنگین ہنگامی انتباہ",
        "high_surge": "زیادہ اضافہ", "severe": "شدید", "very_poor": "بہت خراب", "poor": "خراب",
        "moderate": "معتدل", "satisfactory": "تسلی بخش", "good": "اچھا",
        "localized_advisory": "مقامی کلینیکل ایڈوائزری", "rag_match": "RAG میچ", "vector_source": "ویکٹر ماخذ",
        "map_title": "پورے ہندوستان کا میٹرو جغرافیائی AQI نقشہ",
        "map_sub": "12 CPCB مراکز میں فضائی ٹیلی میٹری۔ تفصیلات کے لیے پن پر کلک کریں۔",
        "basemap_canvas": "کینوس لائٹ", "basemap_streets": "سڑکیں", "reset_view": "ری سیٹ کریں",
        "live_open_meteo_synced": "لائیو اوپن میٹیو ہم آہنگ", "cpcb_scale": "CPCB پیمانہ",
        "severity_ranking": "علاقائی شدت کی درجہ بندی (12 شہر)",
        "regional_severity_ranking": "12 شہروں کی علاقائی شدت کی درجہ بندی (لائیو)",
        "focus_dashboard": "ڈیش بورڈ پر فوکس کریں", "click_to_fly": "جانے کے لیے کلک کریں",
        "chart_title": "وبائی امراض کی نگرانی اور پیش گوئی ٹیلی میٹری",
        "tab_seasonal": "موسمی ٹیلی میٹری", "tab_cities": "12 شہروں کا موازنہ", "tab_weights": "ایم ایل اہمیت",
        "granularity_years": "سال (2015–2025)", "granularity_quarters": "سہ ماہی (Q1–Q4)",
        "granularity_months": "مہینے (جنوری–دسمبر)", "granularity_weeks": "ہفتے (W1–W4)", "granularity_7day": "7 دن لائیو",
        "all_years": "تمام سال", "all_years_range": "تمام سال (2015-2025)", "all_months": "تمام مہینے",
        "all_metros_avg": "تمام 12 شہروں کی اوسط", "drill_path": "راستہ", "drill_up": "↑ اوپر جائیں",
        "legend_aqi": "اوسط AQI", "legend_admissions": "روزانہ ہسپتال داخلے", "pm25_conc": "PM2.5 ارتکاز (µg/m³)",
        "click_to_drill": "💡 تفصیل دیکھنے کے لیے کسی بھی بار پر کلک کریں",
        "heatmap_title": "پیئرسن باہمی تعلق میٹرکس (8×8)",
        "heatmap_desc": "آلودگیوں، موسم اور داخلوں کے درمیان تعلق کے ضوابط (r)۔",
        "temp_label": "درجہ حرارت", "admissions_label": "داخلے", "key_epidemiological_finding": "اہم وبائی دریافت:",
        "dispatch_title": "لائیو ہسپتال ہنگامی روانگی کی قطار",
        "dispatch_desc": "ایم ایل کے خطرے اور گریپ مراحل کے تحت خودکار بستر اور آکسیجن وین کی تقسیم۔",
        "hospital_name": "ہسپتال کا نام", "metro": "میٹرو حب", "col_trigger": "ماحولیاتی محرک",
        "col_resource": "وسائل کی تقسیم", "col_grap": "CAQM GRAP مرحلہ", "col_eta": "پہنچنے کا وقت",
        "icu_strain": "آئی سی یو دباؤ", "priority": "ترجیح", "action": "کارروائی",
        "export_csv": "قطار کو CSV کے طور پر برآمد کریں"
    },
    "copilot": {
        "floating_button": "ایرو میڈ کوپائلٹ سے پوچھیں", "ai_triage": "اے آئی ٹریج", "rag_live": "RAG لائیو",
        "title": "ایرو میڈ کلینیکل کوپائلٹ", "ask_placeholder": "مراٹھی، ہندی، تمل یا انگریزی میں پوچھیں...", "send": "بھیجیں"
    },
    "simulator": {
        "title": "ماحولیاتی حساسیت اور ہسپتال سرج سمیلیٹر",
        "subtitle": "گریڈینٹ بوسٹنگ ریگریسر کے ذریعے تجزیہ۔ ایمرجنسی وارڈ میں داخلے کی پیش گوئی کریں۔",
        "active_city_baseline": "فعال شہر کی بنیاد", "presets_title": "شدید اسموگ اور موسم کے پیش سیٹ",
        "reset_defaults": "سلائیڈرز ری سیٹ کریں", "adjust_pollutants": "آلودگیوں اور موسم کو ایڈجسٹ کریں",
        "pm25_weight": "96.5% ایم ایل اہمیت", "hospital_surge_forecast": "ہسپتال سرج پیش گوئی",
        "predicted_daily_admissions": "متوقع روزانہ سانس کی ایمرجنسی داخلے", "projected_surge_delta": "متوقع اضافہ کا فرق",
        "critical_care_demands": "اہم دیکھ بھال اور طبی ضروریات", "icu_beds": "مطلوبہ آئی سی یو بیڈز",
        "nebulizers": "نیبولائزرز", "oxygen_cylinders": "ہنگامی آکسیجن سلنڈر", "statutory_grap_stage": "قانونی CAQM GRAP مرحلہ:"
    },
    "datasets": {
        "title": "آل انڈیا اڈاپشن لیبز برآمد شدہ کیٹلاگ",
        "subtitle": "اڈاپشن لیبز ایس ڈی کے کے ذریعے برآمد کردہ تمام ڈیٹا سیٹس کا آڈٹ۔",
        "total_synced": "کل ہم آہنگ", "datasets_label": "ڈیٹا سیٹس", "protocols_label": "پروٹوکولز",
        "search_placeholder": "تلاش کریں...", "filter_label": "فلٹر", "filter_all": "تمام",
        "col_name": "نام اور فائل", "col_pillar": "صلاحیت کا ستون", "col_rows": "قطاریں",
        "col_size": "سائز", "col_quality": "گریڈ", "col_id": "آئی ڈی",
        "col_preview": "پیش نظارہ", "view_rows": "قطاریں دیکھیں", "table_view": "ٹیبل ویو",
        "protocol_view": "کارڈ ویو", "close_drawer": "بند کریں"
    },
    "jury": {
        "title": "اڈاپشن اے آئی 7-ستون صلاحیت سوٹ — جیوری ثبوت مرکز",
        "subtitle": "ایرو میڈ انڈیا میں استعمال ہونے والے تمام 7 بنیادی ستونوں کا قابل تصدیق ثبوت۔",
        "quality_grade_card": "کوالٹی گریڈ", "autoscientist_gain_card": "جیت کی شرح",
        "predictive_fit_card": "ایم ایل پیش گوئی فٹ", "credit_reserve_card": "ایس ڈی کے کریڈٹ ریزرو",
        "verified_proof": "تصدیق شدہ ثبوت: 7 ستون", "copy_id": "آئی ڈی کاپی کریں",
        "copied": "کاپی ہو گیا!", "copy_command": "کمانڈ کاپی کریں"
    }
}

# Kannada (kn)
kn_cities = cities_data["kn"]
kn = {
    "dir": "ltr",
    "cities": kn_cities,
    "chrome": {
        "brand_name": "ಏರೋಮೆಡ್", "brand_suffix": "ಭಾರತ", "brand_sub": "ಕ್ಲಿನಿಕಲ್ ಕಣ್ಗಾವಲು",
        "active_metro": "ಸಕ್ರಿಯ ಮೆಟ್ರೋ", "search_metros": "12 ಭಾರತೀಯ ಮೆಟ್ರೋಗಳನ್ನು ಹುಡುಕಿ...",
        "select_language": "ಕಣ್ಗಾವಲು ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ", "indic_scripts_note": "13 ಭಾರತೀಯ ಲಿಪಿಗಳಲ್ಲಿ ಪರಿಶೀಲಿಸಿದ ವೈದ್ಯಕೀಯ ನಿಘಂಟು",
        "more_languages": "+10 ಹೆಚ್ಚು", "export_advisory": "ಸಲಹೆಯನ್ನು ರಫ್ತು ಮಾಡಿ", "bulletin": "ಬುಲೆಟಿನ್",
        "render_connected": "ರೆಂಡರ್ API ಸಂಪರ್ಕಗೊಂಡಿದೆ • R² = 0.988", "live_api": "ಲೈವ್ API",
        "seed_mode": "ತತ್ಕ್ಷಣದ ಸೀಡ್ ಮೋಡ್ (0ms)", "instant_seed": "ಸೀಡ್ ಮೋಡ್",
        "cpcb_caqm_grounding": "CPCB ಮತ್ತು CAQM ಶಾಸನಬದ್ಧ ಆಧಾರ", "live_projection": "ಲೈವ್ 48 ಗಂಟೆಗಳ ಮುನ್ಸೂಚನೆ"
    },
    "nav": {
        "workspaces": "ಕ್ಲಿನಿಕಲ್ ಕಾರ್ಯಕ್ಷೇತ್ರಗಳು", "surveillance": "ಕಣ್ಗಾವಲು ಅವಲೋಕನ", "surveillance_sub": "ಬೆಂಟೋ ಗ್ರಿಡ್ ಮತ್ತು ಟೆಲಿಮೆಟ್ರಿ",
        "simulator": "ವಾಟ್-ಇಫ್ ಸಿಮ್ಯುಲೇಟರ್", "simulator_sub": "ML ಸೂಕ್ಷ್ಮತೆಯ ಲ್ಯಾಬ್",
        "triage": "ಕ್ಲಿನಿಕಲ್ ಟ್ರಯಾಜ್ ಕೋಪೈಲಟ್", "triage_sub": "ವೆಕ್ಟರ್ RAG ಆಧಾರ",
        "datasets": "ಡೇಟಾಸೆಟ್ ಎಕ್ಸ್‌ಪ್ಲೋರರ್", "datasets_sub": "10 ಭೌತಿಕೀಕರಿಸಿದ CSV ಗಳು",
        "jury": "ಅಡಾಪ್ಟನ್ AI 7-ಸ್ತಂಭ ಪುರಾವೆ", "jury_sub": "ಹ್ಯಾಕಥಾನ್ ಪ್ರಶಸ್ತಿ ಸೂಟ್",
        "precision_title": "ಮಾದರಿ ನಿಖರತೆ", "mae_label": "ಸರಾಸರಿ ದೋಷ", "autoscientist_label": "ಆಟೋ ಸೈಂಟಿಸ್ಟ್ ಗೆಲುವು",
        "autoscientist_win": "ಆಟೋ ಸೈಂಟಿಸ್ಟ್ ಗೆಲುವು", "adaption_eval_label": "ಅಡಾಪ್ಟನ್ ಮೌಲ್ಯಮಾಪನ", "adaption_eval": "ಅಡಾಪ್ಟನ್ ಮೌಲ್ಯಮಾಪನ"
    },
    "overview": {
        "kpi_current_aqi": "ವಾಯು ಗುಣಮಟ್ಟ ಸೂಚ್ಯಂಕ (AQI)", "kpi_aqi": "ನೈಜ-ಸಮಯದ ವಾಯು ಗುಣಮಟ್ಟ",
        "kpi_aqi_sub": "ಓಪನ್-ಮೆಟಿಯೊ ಬಹು-ನಿಲ್ದಾಣ ಸಂವೇದಕಗಳು", "kpi_pm25": "ಪರಿಸರದ PM2.5 ಸಾಂದ್ರತೆ",
        "kpi_pm25_sub": "ಸೂಕ್ಷ್ಮ ಕಣಗಳ ವಸ್ತು (µg/m³)", "kpi_surge_risk": "48 ಗಂಟೆಗಳ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿ ಅಪಾಯ",
        "kpi_risk": "ಉಸಿರಾಟದ ದಾಖಲಾತಿ ಅಪಾಯ", "kpi_risk_sub": "ML ಮುನ್ಸೂಚನೆ",
        "kpi_grap_stage": "ಶಾಸನಬದ್ಧ GRAP ಹಂತ", "kpi_dominant_trigger": "ಪ್ರಮುಖ ಪ್ರಚೋದಕ ಮತ್ತು ತಾಪಮಾನ",
        "kpi_admissions": "ಅಂದಾಜು ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿಗಳು", "kpi_admissions_sub": "48 ಗಂಟೆ ತುರ್ತು ಸಾಮರ್ಥ್ಯ ವಿತರಣೆ",
        "projected_admissions": "ಅಂದಾಜು ದಾಖಲಾತಿಗಳು", "pts_day": "ರೋಗಿಗಳು/ದಿನ",
        "grap_sub": "ವಾಹನ ನಿರ್ಬಂಧಗಳು ಮತ್ತು ಪ್ರಾಥಮಿಕ ಶಾಲಾ ಎಚ್ಚರಿಕೆಗಳು ಸಕ್ರಿಯವಾಗಿವೆ.",
        "caqm_schedule": "CAQM ಶಾಸನಬದ್ಧ ವೇಳಾಪಟ್ಟಿ (17 ಪುಟಗಳು)",
        "airway_penetration": "ಉಸಿರಾಟದ ಮಾರ್ಗ ಪ್ರವೇಶ:", "alveolar_deep": "ಅಲ್ವಿಯೋಲಾರ್ (ಆಳವಾದ)",
        "capacity_strain": "ಸಾಮರ್ಥ್ಯ ಗುರಿ ಮತ್ತು ಆಸ್ಪತ್ರೆ ಒತ್ತಡ", "capacity_sub": "48 ಗಂಟೆಗಳ ಅಂದಾಜು ICU ಮತ್ತು ತುರ್ತು ಹಾಸಿಗೆ ಮಿತಿ",
        "surge_score": "ಏರಿಕೆ ಸ್ಕೋರ್", "safe_capacity": "ಸುರಕ್ಷಿತ ಸಾಮರ್ಥ್ಯ", "moderate_strain": "ಮಧ್ಯಮ ಒತ್ತಡ",
        "high_surge_risk": "ಹೆಚ್ಚಿನ ಏರಿಕೆ ಅಪಾಯ", "critical_surge_alert": "ತೀವ್ರ ತುರ್ತು ಎಚ್ಚರಿಕೆ",
        "high_surge": "ಹೆಚ್ಚಿನ ಏರಿಕೆ", "severe": "ತೀವ್ರ", "very_poor": "ಬಹಳ ಕಳಪೆ", "poor": "ಕಳಪೆ",
        "moderate": "ಮಧ್ಯಮ", "satisfactory": "ತೃಪ್ತಿದಾಯಕ", "good": "ಉತ್ತಮ",
        "localized_advisory": "ಸ್ಥಳೀಯ ಕ್ಲಿನಿಕಲ್ ಸಲಹೆ", "rag_match": "RAG ಹೊಂದಾಣಿಕೆ", "vector_source": "ವೆಕ್ಟರ್ ಮೂಲ",
        "map_title": "ಅಖಿಲ ಭಾರತ ಮೆಟ್ರೋ ಭೌಗೋಳಿಕ AQI ನಕ್ಷೆ",
        "map_sub": "12 CPCB ಕೇಂದ್ರಗಳ ವಾತಾವರಣದ ಟೆಲಿಮೆಟ್ರಿ. ವಿವರಗಳಿಗಾಗಿ ಪಿನ್ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.",
        "basemap_canvas": "ಕ್ಯಾನ್ವಾಸ್ ಲೈಟ್", "basemap_streets": "ಬೀದಿಗಳು", "reset_view": "ನಕ್ಷೆ ಮರುಹೊಂದಿಸಿ",
        "live_open_meteo_synced": "ಲೈವ್ ಓಪನ್-ಮೆಟಿಯೊ ಸಿಂಕ್ ಆಗಿದೆ", "cpcb_scale": "CPCB AQI ಪ್ರಮಾಣ",
        "severity_ranking": "ಪ್ರಾದೇಶಿಕ AQI ತೀವ್ರತೆ ಶ್ರೇಣಿ (12 ಮೆಟ್ರೋಗಳು)",
        "regional_severity_ranking": "12-ಮೆಟ್ರೋ ಪ್ರಾದೇಶಿಕ AQI ತೀವ್ರತೆ ಶ್ರೇಣಿ (ಲೈವ್)",
        "focus_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ಕೇಂದ್ರೀಕರಿಸಿ", "click_to_fly": "ನ್ಯಾವಿಗೇಟ್ ಮಾಡಲು ಕ್ಲಿಕ್ ಮಾಡಿ",
        "chart_title": "ಸಾಂಕ್ರಾಮಿಕ ರೋಗಶಾಸ್ತ್ರ ಕಣ್ಗಾವಲು ಮತ್ತು ಮುನ್ಸೂಚಕ ಟೆಲಿಮೆಟ್ರಿ",
        "tab_seasonal": "ಋತುಮಾನದ ಟೆಲಿಮೆಟ್ರಿ", "tab_cities": "12-ನಗರಗಳ ಹೋಲಿಕೆ", "tab_weights": "ML ಪ್ರಾಮುಖ್ಯತೆ",
        "granularity_years": "ವರ್ಷಗಳು (2015–2025)", "granularity_quarters": "ತ್ರೈಮಾಸಿಕಗಳು (Q1–Q4)",
        "granularity_months": "ತಿಂಗಳುಗಳು (ಜನವರಿ–ಡಿಸೆಂಬರ್)", "granularity_weeks": "ವಾರಗಳು (W1–W4)", "granularity_7day": "7-ದಿನ ಲೈವ್",
        "all_years": "ಎಲ್ಲಾ ವರ್ಷಗಳು", "all_years_range": "ಎಲ್ಲಾ ವರ್ಷಗಳು (2015-2025)", "all_months": "ಎಲ್ಲಾ ತಿಂಗಳುಗಳು",
        "all_metros_avg": "ಎಲ್ಲಾ 12 ಮೆಟ್ರೋಗಳ ಸರಾಸರಿ", "drill_path": "ಮಾರ್ಗ", "drill_up": "↑ ಮೇಲೆ ಹೋಗಿ",
        "legend_aqi": "ಸರಾಸರಿ AQI", "legend_admissions": "ದೈನಂದಿನ ದಾಖಲಾತಿಗಳು", "pm25_conc": "PM2.5 ಸಾಂದ್ರತೆ (µg/m³)",
        "click_to_drill": "💡 ವಿವರಗಳನ್ನು ನೋಡಲು ಯಾವುದೇ ಬಾರ್ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ",
        "heatmap_title": "ಪಿಯರ್ಸನ್ ಸಹಸಂಬಂಧ ಮ್ಯಾಟ್ರಿಕ್ಸ್ (8×8)",
        "heatmap_desc": "ಮಾಲಿನ್ಯಕಾರಕಗಳು, ಹವಾಮಾನ ಮತ್ತು ದಾಖಲಾತಿಗಳ ನಡುವಿನ ಸಹಸಂಬಂಧ ಗುಣಾಂಕಗಳು (r).",
        "temp_label": "ತಾಪಮಾನ", "admissions_label": "ದಾಖಲಾತಿಗಳು", "key_epidemiological_finding": "ಪ್ರಮುಖ ಸಾಂಕ್ರಾಮಿಕ ರೋಗಶಾಸ್ತ್ರೀಯ ಸಂಶೋಧನೆ:",
        "dispatch_title": "ಲೈವ್ ಆಸ್ಪತ್ರೆ ತುರ್ತು ರವಾನೆ ಸರದಿ",
        "dispatch_desc": "ನೈಜ-ಸಮಯದ ML ಅಪಾಯ ಮತ್ತು GRAP ಹಂತಗಳಿಂದ ಪ್ರಚೋದಿಸಲ್ಪಟ್ಟ ಹಾಸಿಗೆಗಳು ಮತ್ತು ಆಮ್ಲಜನಕ ವ್ಯಾನ್ ಹಂಚಿಕೆ.",
        "hospital_name": "ಆಸ್ಪತ್ರೆಯ ಹೆಸರು", "metro": "ಮೆಟ್ರೋ ಕೇಂದ್ರ", "col_trigger": "ವಾತಾವರಣದ ಪ್ರಚೋದಕ",
        "col_resource": "ಸಂಪನ್ಮೂಲ ಹಂಚಿಕೆ", "col_grap": "CAQM GRAP ಹಂತ", "col_eta": "ತಲುಪುವ ಸಮಯ",
        "icu_strain": "ICU ಒತ್ತಡ", "priority": "ಆದ್ಯತೆ", "action": "ಕ್ರಮ",
        "export_csv": "ಸರದಿಯನ್ನು CSV ಆಗಿ ರಫ್ತು ಮಾಡಿ"
    },
    "copilot": {
        "floating_button": "ಏರೋಮೆಡ್ ಕೋಪೈಲಟ್ ಅನ್ನು ಕೇಳಿ", "ai_triage": "AI ಟ್ರಯಾಜ್", "rag_live": "RAG ಲೈವ್",
        "title": "ಏರೋಮೆಡ್ ಕ್ಲಿನಿಕಲ್ ಕೋಪೈಲಟ್", "ask_placeholder": "ಮರಾಠಿ, ಹಿಂದಿ, ತಮಿಳು ಅಥವಾ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ಕೇಳಿ...", "send": "ಕಳುಹಿಸಿ"
    },
    "simulator": {
        "title": "ವಾತಾವರಣದ ಸೂಕ್ಷ್ಮತೆ ಮತ್ತು ಆಸ್ಪತ್ರೆ ಏರಿಕೆ ಸಿಮ್ಯುಲೇಟರ್",
        "subtitle": "ಗ್ರೇಡಿಯಂಟ್ ಬೂಸ್ಟಿಂಗ್ ರಿಗ್ರೆಸರ್‌ನಿಂದ ನಡೆಸಲ್ಪಡುವ ನೈಜ-ಸಮಯದ ವಿಶ್ಲೇಷಣೆ. ತುರ್ತು ವಾರ್ಡ್ ದಾಖಲಾತಿಗಳನ್ನು ಊಹಿಸಿ.",
        "active_city_baseline": "ಸಕ್ರಿಯ ನಗರ ಬೇಸ್‌ಲೈನ್", "presets_title": "ತೀವ್ರ ಹೊಗೆ ಮತ್ತು ಹವಾಮಾನ ಪೂರ್ವನಿಗದಿಗಳು",
        "reset_defaults": "ಸ್ಲೈಡರ್‌ಗಳನ್ನು ಮರುಹೊಂದಿಸಿ", "adjust_pollutants": "ಮಾಲಿನ್ಯಕಾರಕಗಳನ್ನು ಹೊಂದಿಸಿ",
        "pm25_weight": "96.5% ML ಪ್ರಾಮುಖ್ಯತೆ", "hospital_surge_forecast": "ಆಸ್ಪತ್ರೆ ಏರಿಕೆಯ ಮುನ್ಸೂಚನೆ",
        "predicted_daily_admissions": "ಅಂದಾಜು ದೈನಂದಿನ ಉಸಿರಾಟದ ತುರ್ತು ದಾಖಲಾತಿಗಳು", "projected_surge_delta": "ಅಂದಾಜು ವ್ಯತ್ಯಾಸ",
        "critical_care_demands": "ಕ್ರಿಟಿಕಲ್ ಕೇರ್ ಮತ್ತು ವೈದ್ಯಕೀಯ ಅಗತ್ಯಗಳು", "icu_beds": "ಅಗತ್ಯವಿರುವ ICU ಹಾಸಿಗೆಗಳು",
        "nebulizers": "ನೆಬ್ಯುಲೈಜರ್‌ಗಳು", "oxygen_cylinders": "ತುರ್ತು ಆಮ್ಲಜನಕ ಸಿಲಿಂಡರ್‌ಗಳು", "statutory_grap_stage": "ಶಾಸನಬದ್ಧ CAQM GRAP ಹಂತ:"
    },
    "datasets": {
        "title": "ಅಖಿಲ ಭಾರತ ಅಡಾಪ್ಟನ್ ಲ್ಯಾಬ್ಸ್ ರಫ್ತು ಕ್ಯಾಟಲಾಗ್",
        "subtitle": "ಅಡಾಪ್ಟನ್ ಲ್ಯಾಬ್ಸ್ SDK ಮೂಲಕ ಸಿಂಕ್ ಮಾಡಲಾದ ಡೇಟಾಸೆಟ್‌ಗಳ ಲೆಕ್ಕಪರಿಶೋಧನೆ.",
        "total_synced": "ಒಟ್ಟು ಸಿಂಕ್ ಮಾಡಲಾಗಿದೆ", "datasets_label": "ಡೇಟಾಸೆಟ್‌ಗಳು", "protocols_label": "ಪ್ರೋಟೋಕಾಲ್‌ಗಳು",
        "search_placeholder": "ಹುಡುಕಿ...", "filter_label": "ಫಿಲ್ಟರ್", "filter_all": "ಎಲ್ಲಾ",
        "col_name": "ಹೆಸರು ಮತ್ತು ಫೈಲ್", "col_pillar": "ಸಾಮರ್ಥ್ಯದ ಸ್ತಂಭ", "col_rows": "ಸಾಲುಗಳು",
        "col_size": "ಗಾತ್ರ", "col_quality": "ಗ್ರೇಡ್", "col_id": "ID",
        "col_preview": "ಮುನ್ನೋಟ", "view_rows": "ಸಾಲುಗಳನ್ನು ವೀಕ್ಷಿಸಿ", "table_view": "ಕೋಷ್ಟಕ ನೋಟ",
        "protocol_view": "ಕಾರ್ಡ್ ನೋಟ", "close_drawer": "ಮುಚ್ಚಿ"
    },
    "jury": {
        "title": "ಅಡಾಪ್ಟನ್ AI 7-ಸ್ತಂಭ ಸಾಮರ್ಥ್ಯ ಸೂಟ್ — ತೀರ್ಪುಗಾರರ ಪುರಾವೆ ಕೇಂದ್ರ",
        "subtitle": "ಏರೋಮೆಡ್ ಭಾರತವನ್ನು ನಿರ್ಮಿಸುವಲ್ಲಿ ಬಳಸಲಾದ ಎಲ್ಲಾ 7 ಪ್ರಮುಖ ಸ್ತಂಭಗಳ ಪುರಾವೆಗಳು.",
        "quality_grade_card": "ಗುಣಮಟ್ಟ ಗ್ರೇಡ್", "autoscientist_gain_card": "ಗೆಲುವಿನ ದರ",
        "predictive_fit_card": "ML ಮುನ್ಸೂಚಕ ಫಿಟ್", "credit_reserve_card": "SDK ಮೀಸಲು",
        "verified_proof": "ಪರಿಶೀಲಿಸಿದ ಪುರಾವೆ: 7 ಸ್ತಂಭಗಳು", "copy_id": "ID ನಕಲಿಸಿ",
        "copied": "ನಕಲಿಸಲಾಗಿದೆ!", "copy_command": "ಆಜ್ಞೆಯನ್ನು ನಕಲಿಸಿ"
    }
}

# Malayalam (ml)
ml_cities = cities_data["ml"]
ml = {
    "dir": "ltr",
    "cities": ml_cities,
    "chrome": {
        "brand_name": "എയറോമെഡ്", "brand_suffix": "ഇന്ത്യ", "brand_sub": "ക്ലിനിക്കൽ നിരീക്ഷണം",
        "active_metro": "സജീവ മെട്രോ", "search_metros": "12 ഇന്ത്യൻ മെട്രോകൾ തിരയുക...",
        "select_language": "നിരീക്ഷണ ഭാഷ തിരഞ്ഞെടുക്കുക", "indic_scripts_note": "13 ഇന്ത്യൻ ഭാഷകളിൽ പരിശോധിച്ചുറപ്പിച്ച മെഡിക്കൽ പദാവലി",
        "more_languages": "+10 കൂടുതൽ", "export_advisory": "ഉപദേശം എക്സ്പോർട്ട് ചെയ്യുക", "bulletin": "ബുള്ളറ്റിൻ",
        "render_connected": "റെൻഡർ API കണക്റ്റുചെയ്‌തു • R² = 0.988", "live_api": "തത്സമയ API",
        "seed_mode": "തൽക്ഷണ സീഡ് മോഡ് (0ms)", "instant_seed": "സീഡ് മോഡ്",
        "cpcb_caqm_grounding": "CPCB & CAQM നിയമപരമായ അടിത്തറ", "live_projection": "തത്സമയ 48 മണിക്കൂർ പ്രവചനം"
    },
    "nav": {
        "workspaces": "ക്ലിനിക്കൽ വർക്ക്‌സ്‌പേസുകൾ", "surveillance": "നിരീക്ഷണ അവലോകനം", "surveillance_sub": "ബെന്റോ ഗ്രിഡും ടെലിമെട്രിയും",
        "simulator": "വാട്ട്-ഇഫ് സിമുലേറ്റർ", "simulator_sub": "ML സെൻസിറ്റിവിറ്റി ലാബ്",
        "triage": "ക്ലിനിക്കൽ ട്രയേജ് കോപൈലറ്റ്", "triage_sub": "വെക്റ്റർ RAG അടിത്തറ",
        "datasets": "ഡാറ്റാസെറ്റ് എക്സ്പ്ലോറർ", "datasets_sub": "10 മെറ്റീരിയലൈസ്ഡ് CSV കൾ",
        "jury": "അഡാപ്ഷൻ AI 7-തൂൺ തെളിവ്", "jury_sub": "ഹാക്കത്തോൺ അവാർഡ് സ്യൂട്ട്",
        "precision_title": "മോഡൽ കൃത്യത", "mae_label": "ശരാശരി പിശക്", "autoscientist_label": "ഓട്ടോ സയന്റിസ്റ്റ് വിജയം",
        "autoscientist_win": "ഓട്ടോ സയന്റിസ്റ്റ് വിജയം", "adaption_eval_label": "അഡാപ്ഷൻ വിലയിരുത്തൽ", "adaption_eval": "അഡാപ്ഷൻ വിലയിരുത്തൽ"
    },
    "overview": {
        "kpi_current_aqi": "വായു ഗുണനിലവാര സൂചിക (AQI)", "kpi_aqi": "തത്സമയ വായു ഗുണനിലവാരം",
        "kpi_aqi_sub": "ഓപ്പൺ-മെറ്റിയോ സെൻസറുകൾ", "kpi_pm25": "അന്തരീക്ഷ PM2.5 സാന്ദ്രത",
        "kpi_pm25_sub": "സൂക്ഷ്മ കണികാ പദാർത്ഥം (µg/m³)", "kpi_surge_risk": "48 മണിക്കൂർ ആശുപത്രി പ്രവേശന സാധ്യത",
        "kpi_risk": "ശ്വസന പ്രവേശന സാധ്യത", "kpi_risk_sub": "ML പ്രവചനം",
        "kpi_grap_stage": "നിയമപരമായ GRAP ഘട്ടം", "kpi_dominant_trigger": "പ്രധാന ട്രിഗറും താപനിലയും",
        "kpi_admissions": "പ്രതീക്ഷിക്കുന്ന ആശുപത്രി പ്രവേശനങ്ങൾ", "kpi_admissions_sub": "48 മണിക്കൂർ അടിയന്തര ശേഷി വിതരണം",
        "projected_admissions": "പ്രതീക്ഷിക്കുന്ന പ്രവേശനങ്ങൾ", "pts_day": "രോഗികൾ/ദിവസം",
        "grap_sub": "വാഹന നിയന്ത്രണങ്ങളും പ്രൈമറി സ്കൂൾ മുന്നറിയിപ്പുകളും സജീവമാണ്.",
        "caqm_schedule": "CAQM നിയമപരമായ ഷെഡ്യൂൾ (17 പേജുകൾ)",
        "airway_penetration": "ശ്വാസനാളം തുളച്ചുകയറൽ:", "alveolar_deep": "അൽവിയോളാർ (ആഴത്തിലുള്ള)",
        "capacity_strain": "ശേഷി ലക്ഷ്യവും ആശുപത്രി സമ്മർദ്ദവും", "capacity_sub": "48 മണിക്കൂർ കണക്കാക്കിയ ICU, എമർജൻസി ബെഡ് പരിധി",
        "surge_score": "സർജ് സ്കോർ", "safe_capacity": "സുരക്ഷിത ശേഷി", "moderate_strain": "മിതമായ സമ്മർദ്ദം",
        "high_surge_risk": "ഉയർന്ന സർജ് സാധ്യത", "critical_surge_alert": "ഗുരുതരമായ അടിയന്തര മുന്നറിയിപ്പ്",
        "high_surge": "ഉയർന്ന വർദ്ധനവ്", "severe": "ഗുരുതരമായത്", "very_poor": "വളരെ മോശം", "poor": "മോശം",
        "moderate": "മിതമായത്", "satisfactory": "തൃപ്തികരമായത്", "good": "നല്ലത്",
        "localized_advisory": "പ്രാദേശിക ക്ലിനിക്കൽ നിർദ്ദേശം", "rag_match": "RAG പൊരുത്തം", "vector_source": "വെക്റ്റർ ഉറവിടം",
        "map_title": "പാൻ-ഇന്ത്യ മെട്രോ ഭൂമിശാസ്ത്രപരമായ AQI ഭൂപടം",
        "map_sub": "12 CPCB കേന്ദ്രങ്ങളിലെ അന്തരീക്ഷ ടെലിമെട്രി. ഫോക്കസ് ചെയ്യാൻ പിന്നിൽ ക്ലിക്ക് ചെയ്യുക.",
        "basemap_canvas": "കാൻവാസ് ലൈറ്റ്", "basemap_streets": "തെരുവുകൾ", "reset_view": "റീസെറ്റ് കാഴ്‌ച",
        "live_open_meteo_synced": "തത്സമയ ഓപ്പൺ-മെറ്റിയോ സമന്വയിപ്പിച്ചു", "cpcb_scale": "CPCB AQI സ്കെയിൽ",
        "severity_ranking": "മേഖലാ AQI തീവ്രത റാങ്കിംഗ് (12 മെട്രോകൾ)",
        "regional_severity_ranking": "12-മെട്രോ മേഖലാ AQI തീവ്രത റാങ്കിംഗ് (തത്സമയം)",
        "focus_dashboard": "ഡാഷ്‌ബോർഡ് ഫോക്കസ് ചെയ്യുക", "click_to_fly": "പോകാൻ ക്ലിക്ക് ചെയ്യുക",
        "chart_title": "എപ്പിഡെമിയോളജിക്കൽ നിരീക്ഷണവും പ്രവചന ടെലിമെട്രിയും",
        "tab_seasonal": "സീസണൽ ടെലിമെട്രി", "tab_cities": "12-നഗര താരതമ്യം", "tab_weights": "ML പ്രാധാന്യം",
        "granularity_years": "വർഷങ്ങൾ (2015–2025)", "granularity_quarters": "പാദങ്ങൾ (Q1–Q4)",
        "granularity_months": "മാസങ്ങൾ (ജനു–ഡിസം)", "granularity_weeks": "ആഴ്ചകൾ (W1–W4)", "granularity_7day": "7-ദിവസ തത്സമയം",
        "all_years": "എല്ലാ വർഷങ്ങളും", "all_years_range": "എല്ലാ വർഷങ്ങളും (2015-2025)", "all_months": "എല്ലാ മാസങ്ങളും",
        "all_metros_avg": "എല്ലാ 12 മെട്രോകളുടെയും ശരാശരി", "drill_path": "ഡ്രിൽ പാത്ത്", "drill_up": "↑ മുകളിലേക്ക്",
        "legend_aqi": "ശരാശരി AQI", "legend_admissions": "പ്രതിദിന പ്രവേശനങ്ങൾ", "pm25_conc": "PM2.5 സാന്ദ്രത (µg/m³)",
        "click_to_drill": "💡 കൂടുതൽ വിവരങ്ങൾക്ക് ഏതെങ്കിലും ബാറിൽ ക്ലിക്ക് ചെയ്യുക",
        "heatmap_title": "പിയേഴ്സൺ പരസ്പരബന്ധ മാട്രിക്സ് (8×8)",
        "heatmap_desc": "മലിനീകരണങ്ങൾ, കാലാവസ്ഥ, പ്രവേശനങ്ങൾ എന്നിവ തമ്മിലുള്ള പരസ്പരബന്ധ ഗുണകങ്ങൾ (r).",
        "temp_label": "താപനില", "admissions_label": "പ്രവേശനങ്ങൾ", "key_epidemiological_finding": "പ്രധാന കണ്ടെത്തൽ:",
        "dispatch_title": "തത്സമയ ആശുപത്രി എമർജൻസി വിതരണ ക്യൂ",
        "dispatch_desc": "തത്സമയ ML റിസ്കും GRAP ഘട്ടങ്ങളും അനുസരിച്ച് ഓട്ടോമേറ്റഡ് കിടക്കകളും ഓക്സിജൻ വാനും അനുവദിക്കൽ.",
        "hospital_name": "ആശുപത്രിയുടെ പേര്", "metro": "മെട്രോ ഹബ്", "col_trigger": "അന്തരീക്ഷ ഘടകം",
        "col_resource": "വിഭവ വിതരണം", "col_grap": "CAQM GRAP ഘട്ടം", "col_eta": "എത്തിച്ചേരുന്ന സമയം",
        "icu_strain": "ICU സമ്മർദ്ദം", "priority": "മുൻഗണന", "action": "നടപടി",
        "export_csv": "ക്യൂ CSV ആയി എക്സ്പോർട്ട് ചെയ്യുക"
    },
    "copilot": {
        "floating_button": "എയറോമെഡ് കോപൈലറ്റിനോട് ചോദിക്കുക", "ai_triage": "AI ട്രയേജ്", "rag_live": "RAG തത്സമയം",
        "title": "എയറോമെഡ് ക്ലിനിക്കൽ കോപൈലറ്റ്", "ask_placeholder": "മറാഠി, ഹിന്ദി, തമിഴ് അല്ലെങ്കിൽ ഇംഗ്ലീഷിൽ ചോദിക്കുക...", "send": "അയക്കുക"
    },
    "simulator": {
        "title": "അന്തരീക്ഷ സംവേദനക്ഷമതയും ആശുപത്രി സർജ് സിമുലേറ്ററും",
        "subtitle": "ഗ്രേഡിയന്റ് ബൂസ്റ്റിംഗ് റിഗ്രെസ്സർ ഉപയോഗിച്ചുള്ള തത്സമയ വിശകലനം. അത്യാഹിത വിഭാഗ പ്രവേശനം കണക്കാക്കുക.",
        "active_city_baseline": "സജീവ നഗര അടിസ്ഥാനം", "presets_title": "കടുത്ത പുകമഞ്ഞും കാലാവസ്ഥാ പ്രീസെറ്റുകളും",
        "reset_defaults": "റീസെറ്റ് ചെയ്യുക", "adjust_pollutants": "മലിനീകരണം ക്രമീകരിക്കുക",
        "pm25_weight": "96.5% ML പ്രാധാന്യം", "hospital_surge_forecast": "ആശുപത്രി സർജ് പ്രവചനം",
        "predicted_daily_admissions": "പ്രതീക്ഷിക്കുന്ന പ്രതിദിന ശ്വസന അത്യാഹിത പ്രവേശനങ്ങൾ", "projected_surge_delta": "കണക്കാക്കിയ വ്യത്യാസം",
        "critical_care_demands": "ക്രിട്ടിക്കൽ കെയർ ആവശ്യങ്ങൾ", "icu_beds": "ആവശ്യമായ ICU കിടക്കകൾ",
        "nebulizers": "നെബുലൈസറുകൾ", "oxygen_cylinders": "അടിയന്തര ഓക്സിജൻ സിലിണ്ടറുകൾ", "statutory_grap_stage": "നിയമപരമായ CAQM GRAP ഘട്ടം:"
    },
    "datasets": {
        "title": "പാൻ-ഇന്ത്യ അഡാപ്ഷൻ ലാബ്സ് എക്സ്പോർട്ട് കാറ്റലോഗ്",
        "subtitle": "അഡാപ്ഷൻ ലാബ്സ് SDK വഴി സമന്വയിപ്പിച്ച ഡാറ്റാസെറ്റുകളുടെ ഓഡിറ്റ്.",
        "total_synced": "ആകെ സമന്വയിപ്പിച്ചത്", "datasets_label": "ഡാറ്റാസെറ്റുകൾ", "protocols_label": "പ്രോട്ടോക്കോളുകൾ",
        "search_placeholder": "തിരയുക...", "filter_label": "ഫിൽട്ടർ", "filter_all": "എല്ലാം",
        "col_name": "പേരും ഫയലും", "col_pillar": "ശേഷി സ്തംഭം", "col_rows": "വരികൾ",
        "col_size": "വലുപ്പം", "col_quality": "ഗ്രേഡ്", "col_id": "ID",
        "col_preview": "പ്രിവ്യൂ", "view_rows": "വരികൾ കാണുക", "table_view": "പട്ടിക കാഴ്ച",
        "protocol_view": "കാർഡ് കാഴ്ച", "close_drawer": "അടയ്ക്കുക"
    },
    "jury": {
        "title": "അഡാപ്ഷൻ AI 7-സ്തംഭ ശേഷി സ്യൂട്ട് — ജൂറി തെളിവ് ഹബ്",
        "subtitle": "എയറോമെഡ് ഇന്ത്യ നിർമ്മിക്കുന്നതിൽ ഉപയോഗിച്ച എല്ലാ 7 പ്രധാന തൂണുകൾക്കുമുള്ള തെളിവുകൾ.",
        "quality_grade_card": "ഗുണനിലവാര ഗ്രേഡ്", "autoscientist_gain_card": "വിജയ നിരക്ക്",
        "predictive_fit_card": "ML പ്രവചന ഫിറ്റ്", "credit_reserve_card": "SDK കരുതൽ ധനം",
        "verified_proof": "പരിശോധിച്ച തെളിവ്: 7 തൂണുകൾ", "copy_id": "ID പകർപ്പുക",
        "copied": "പകർത്തി!", "copy_command": "കമാൻഡ് പകർപ്പുക"
    }
}

# Gujarati (gu)
gu_cities = cities_data["gu"]
gu = {
    "dir": "ltr",
    "cities": gu_cities,
    "chrome": {
        "brand_name": "એરોમેડ", "brand_suffix": "ઇન્ડિયા", "brand_sub": "ક્લિનિકલ સર્વેલન્સ",
        "active_metro": "સક્રિય મેટ્રો", "search_metros": "12 ભારતીય મેટ્રો શોધો...",
        "select_language": "સર્વેલન્સ ભાષા પસંદ કરો", "indic_scripts_note": "13 ભારતીય લિપિઓમાં ચકાસાયેલ તબીબી શબ્દભંડોળ",
        "more_languages": "+10 વધુ", "export_advisory": "સલાહ નિકાસ કરો", "bulletin": "બુલેટિન",
        "render_connected": "રેન્ડર API કનેક્ટેડ • R² = 0.988", "live_api": "લાઇવ API",
        "seed_mode": "ઝડપી સીડ મોડ (0ms)", "instant_seed": "સીડ મોડ",
        "cpcb_caqm_grounding": "CPCB અને CAQM કાનૂની આધાર", "live_projection": "લાઇવ 48 કલાકનું અનુમાન"
    },
    "nav": {
        "workspaces": "ક્લિનિકલ વર્કસ્પેસ", "surveillance": "સર્વેલન્સ ઝાંખી", "surveillance_sub": "બેન્ટો ગ્રીડ અને ટેલિમેટ્રી",
        "simulator": "વૉટ-ઇફ સિમ્યુલેટર", "simulator_sub": "ML સંવેદનશીલતા લેબ",
        "triage": "ક્લિનિકલ ટ્રાયજ કોપાયલટ", "triage_sub": "વેક્ટર RAG આધાર",
        "datasets": "ડેટાસેટ એક્સપ્લોરર", "datasets_sub": "10 સંકલિત CSV",
        "jury": "એડેપ્શન AI 7-સ્તંભ પુરાવો", "jury_sub": "હેકાથોન એવોર્ડ સ્યુટ",
        "precision_title": "મોડેલ ચોકસાઈ", "mae_label": "સરેરાશ ભૂલ", "autoscientist_label": "ઓટો સાયન્ટિસ્ટ વિજય",
        "autoscientist_win": "ઓટો સાયન્ટિસ્ટ વિજય", "adaption_eval_label": "એડેપ્શન મૂલ્યાંકન", "adaption_eval": "એડેપ્શન મૂલ્યાંકન"
    },
    "overview": {
        "kpi_current_aqi": "એર ક્વોલિટી ઇન્ડેક્સ (AQI)", "kpi_aqi": "રીઅલ-ટાઇમ હવાની ગુણવત્તા",
        "kpi_aqi_sub": "ઓપન-મેટિયો મલ્ટી-સ્ટેશન સેન્સર્સ", "kpi_pm25": "વાતાવરણીય PM2.5 સાંદ્રતા",
        "kpi_pm25_sub": "સુક્ષ્મ કણો (µg/m³)", "kpi_surge_risk": "48 કલાક હોસ્પિટલ એડમિશન જોખમ",
        "kpi_risk": "શ્વસન એડમિશન જોખમ", "kpi_risk_sub": "ML ગ્રેડિએન્ટ બૂસ્ટિંગ અનુમાન",
        "kpi_grap_stage": "કાનૂની GRAP તબક્કો", "kpi_dominant_trigger": "મુખ્ય ટ્રિગર અને તાપમાન",
        "kpi_admissions": "અંદાજિત હોસ્પિટલ એડમિશન", "kpi_admissions_sub": "48 કલાક ઇમરજન્સી ક્ષમતા",
        "projected_admissions": "અંદાજિત એડમિશન", "pts_day": "દર્દીઓ/દિવસ",
        "grap_sub": "વાહન પ્રતિબંધો અને પ્રાથમિક શાળા ચેતવણીઓ સક્રિય છે.",
        "caqm_schedule": "CAQM કાનૂની સમયપત્રક (17 પૃષ્ઠ)",
        "airway_penetration": "શ્વાસનળીમાં પ્રવેશ:", "alveolar_deep": "એલ્વિઓલર (ઊંડાણપૂર્વક)",
        "capacity_strain": "ક્ષમતા લક્ષ્ય અને હોસ્પિટલ તણાવ", "capacity_sub": "48 કલાક અંદાજિત ICU અને ઇમરજન્સી બેડ મર્યાદા",
        "surge_score": "સર્જ સ્કોર", "safe_capacity": "સુરક્ષિત ક્ષમતા", "moderate_strain": "મધ્યમ તણાવ",
        "high_surge_risk": "ઉચ્ચ સર્જ જોખમ", "critical_surge_alert": "ગંભીર ઇમરજન્સી ચેતવણી",
        "high_surge": "ઉચ્ચ વધારો", "severe": "ગંભીર", "very_poor": "ખૂબ ખરાબ", "poor": "ખરાબ",
        "moderate": "મધ્યમ", "satisfactory": "સંતોષકારક", "good": "સારું",
        "localized_advisory": "સ્થાનિક ક્લિનિકલ સલાહ", "rag_match": "RAG મેચ", "vector_source": "વેક્ટર સ્ત્રોત",
        "map_title": "અખિલ ભારતીય મેટ્રો ભૌગોલિક AQI નકશો",
        "map_sub": "12 CPCB કેન્દ્રો પર વાતાવરણીય ટેલિમેટ્રી. વિગતો માટે પિન પર ક્લિક કરો.",
        "basemap_canvas": "કેનવાસ લાઇટ", "basemap_streets": "શેરીઓ", "reset_view": "રીસેટ વ્યૂ",
        "live_open_meteo_synced": "લાઇવ ઓપન-મેટિયો સમન્વયિત", "cpcb_scale": "CPCB AQI સ્કેલ",
        "severity_ranking": "પ્રાદેશિક AQI તીવ્રતા રેન્કિંગ (12 મેટ્રો)",
        "regional_severity_ranking": "12-મેટ્રો પ્રાદેશિક AQI તીવ્રતા રેન્કિંગ (લાઇવ)",
        "focus_dashboard": "ડેશબોર્ડ ફોકસ કરો", "click_to_fly": "નેવિગેટ કરવા ક્લિક કરો",
        "chart_title": "રોગચાળા સંબંધી સર્વેલન્સ અને અનુમાનિત ટેલિમેટ્રી",
        "tab_seasonal": "મોસમી ટેલિમેટ્રી", "tab_cities": "12-શહેરોની સરખામણી", "tab_weights": "ML મહત્વ",
        "granularity_years": "વર્ષો (2015–2025)", "granularity_quarters": "ક્વાર્ટર્સ (Q1–Q4)",
        "granularity_months": "મહિનાઓ (જાન્યુ–ડિસેમ્બર)", "granularity_weeks": "અઠવાડિયા (W1–W4)", "granularity_7day": "7-દિવસ લાઇવ",
        "all_years": "બધા વર્ષો", "all_years_range": "બધા વર્ષો (2015-2025)", "all_months": "બધા મહિનાઓ",
        "all_metros_avg": "બધા 12 મેટ્રોની સરેરાશ", "drill_path": "ડ્રિલ પાથ", "drill_up": "↑ ઉપર જાઓ",
        "legend_aqi": "સરેરાશ AQI", "legend_admissions": "દૈનિક એડમિશન", "pm25_conc": "PM2.5 સાંદ્રતા (µg/m³)",
        "click_to_drill": "💡 વિગતો જોવા માટે કોઈપણ બાર પર ક્લિક કરો",
        "heatmap_title": "પિયર્સન સહસંબંધ મેટ્રિક્સ (8×8)",
        "heatmap_desc": "પ્રદૂષકો, હવામાન અને એડમિશન વચ્ચેના સહસંબંધ ગુણાંક (r).",
        "temp_label": "તાપમાન", "admissions_label": "એડમિશન", "key_epidemiological_finding": "મુખ્ય તારણ:",
        "dispatch_title": "લાઇવ હોસ્પિટલ ઇમરજન્સી ડિસ્પેચ કતાર",
        "dispatch_desc": "રીઅલ-ટાઇમ ML જોખમ અને GRAP તબક્કા દ્વારા બેડ અને ઓક્સિજન વાનની સ્વચાલિત ફાળવણી.",
        "hospital_name": "હોસ્પિટલનું નામ", "metro": "મેટ્રો હબ", "col_trigger": "વાતાવરણીય ટ્રિગર",
        "col_resource": "સંસાધન ફાળવણી", "col_grap": "CAQM GRAP તબક્કો", "col_eta": "પહોંચવાનો સમય",
        "icu_strain": "ICU તણાવ", "priority": "પ્રાથમિકતા", "action": "પગલાં",
        "export_csv": "કતાર CSV નિકાસ કરો"
    },
    "copilot": {
        "floating_button": "એરોમેડ કોપાયલટને પૂછો", "ai_triage": "AI ટ્રાયજ", "rag_live": "RAG લાઇવ",
        "title": "એરોમેડ ક્લિનિકલ કોપાયલટ", "ask_placeholder": "મરાઠી, હિન્દી, તમિલ અથવા અંગ્રેજીમાં પૂછો...", "send": "મોકલો"
    },
    "simulator": {
        "title": "વાતાવરણીય સંવેદનશીલતા અને હોસ્પિટલ સર્જ સિમ્યુલેટર",
        "subtitle": "ગ્રેડિએન્ટ બૂસ્ટિંગ રિગ્રેસર દ્વારા સંચાલિત વિશ્લેષણ. ઇમરજન્સી વોર્ડ એડમિશનનો અંદાજ લગાવો.",
        "active_city_baseline": "સક્રિય શહેર બેઝલાઇન", "presets_title": "તીવ્ર ધુમ્મસ અને હવામાન પ્રીસેટ્સ",
        "reset_defaults": "રીસેટ કરો", "adjust_pollutants": "પ્રદૂષકોને સમાયોજિત કરો",
        "pm25_weight": "96.5% ML મહત્વ", "hospital_surge_forecast": "હોસ્પિટલ સર્જ અનુમાન",
        "predicted_daily_admissions": "અંદાજિત દૈનિક શ્વસન ઇમરજન્સી એડમિશન", "projected_surge_delta": "અંદાજિત તફાવત",
        "critical_care_demands": "ક્રિટિકલ કેર અને તબીબી જરૂરિયાતો", "icu_beds": "જરૂરી ICU બેડ",
        "nebulizers": "નેબ્યુલાઇઝર્સ", "oxygen_cylinders": "ઇમરજન્સી ઓક્સિજન સિલિન્ડર્સ", "statutory_grap_stage": "કાનૂની CAQM GRAP તબક્કો:"
    },
    "datasets": {
        "title": "ઓલ ઇન્ડિયા એડેપ્શન લેબ્સ નિકાસ કેટલોગ",
        "subtitle": "એડેપ્શન લેબ્સ SDK દ્વારા સમન્વયિત ડેટાસેટ્સનું ઓડિટ.",
        "total_synced": "કુલ સમન્વયિત", "datasets_label": "ડેટાસેટ્સ", "protocols_label": "પ્રોટોકોલ્સ",
        "search_placeholder": "શોધો...", "filter_label": "ફિલ્ટર", "filter_all": "બધા",
        "col_name": "નામ અને ફાઇલ", "col_pillar": "ક્ષમતા સ્તંભ", "col_rows": "પંક્તિઓ",
        "col_size": "કદ", "col_quality": "ગ્રેડ", "col_id": "ID",
        "col_preview": "પૂર્વાવલોકન", "view_rows": "પંક્તિઓ જુઓ", "table_view": "ટેબલ વ્યૂ",
        "protocol_view": "કાર્ડ વ્યૂ", "close_drawer": "બંધ કરો"
    },
    "jury": {
        "title": "એડેપ્શન AI 7-સ્તંભ ક્ષમતા સ્યુટ — જ્યુરી પુરાવા કેન્દ્ર",
        "subtitle": "એરોમેડ ઇન્ડિયા બનાવવા માટે વપરાયેલા તમામ 7 મુખ્ય સ્તંભો માટેના પુરાવા.",
        "quality_grade_card": "ગુણવત્તા ગ્રેડ", "autoscientist_gain_card": "જીતનો દર",
        "predictive_fit_card": "ML પ્રિડિક્ટિવ ફિટ", "credit_reserve_card": "SDK અનામત",
        "verified_proof": "ચકાસાયેલ પુરાવો: 7 સ્તંભો", "copy_id": "ID કૉપિ કરો",
        "copied": "કૉપિ કર્યું!", "copy_command": "કમાન્ડ કૉપિ કરો"
    }
}

# Punjabi (pa)
pa_cities = cities_data["pa"]
pa = {
    "dir": "ltr",
    "cities": pa_cities,
    "chrome": {
        "brand_name": "ਐਰੋਮੈੱਡ", "brand_suffix": "ਇੰਡੀਆ", "brand_sub": "ਕਲੀਨਿਕਲ ਨਿਗਰਾਨੀ",
        "active_metro": "ਸਰਗਰਮ ਮੈਟਰੋ", "search_metros": "12 ਭਾਰਤੀ ਮੈਟਰੋ ਖੋਜੋ...",
        "select_language": "ਨਿਗਰਾਨੀ ਭਾਸ਼ਾ ਚੁਣੋ", "indic_scripts_note": "13 ਭਾਰਤੀ ਲਿਪੀਆਂ ਵਿੱਚ ਪ੍ਰਮਾਣਿਤ ਡਾਕਟਰੀ ਸ਼ਬਦਾਵਲੀ",
        "more_languages": "+10 ਹੋਰ", "export_advisory": "ਸਲਾਹ ਨਿਰਯਾਤ ਕਰੋ", "bulletin": "ਬੁਲੇਟਿਨ",
        "render_connected": "ਰੈਂਡਰ API ਕਨੈਕਟ ਕੀਤਾ گیا • R² = 0.988", "live_api": "ਲਾਈਵ API",
        "seed_mode": "ਤਤਕਾਲ ਸੀਡ ਮੋਡ (0ms)", "instant_seed": "ਸੀਡ ਮੋਡ",
        "cpcb_caqm_grounding": "CPCB ਅਤੇ CAQM ਕਾਨੂੰਨੀ ਆਧਾਰ", "live_projection": "ਲਾਈਵ 48 ਘੰਟੇ ਦਾ ਅਨੁਮਾਨ"
    },
    "nav": {
        "workspaces": "ਕਲੀਨਿਕਲ ਵਰਕਸਪੇਸ", "surveillance": "ਨਿਗਰਾਨੀ ਸੰਖੇਪ", "surveillance_sub": "ਬੈਂਟੋ ਗਰਿੱਡ ਅਤੇ ਟੈਲੀਮੈਟਰੀ",
        "simulator": "ਵੱਟ-ਇਫ ਸਿਮੂਲੇਟਰ", "simulator_sub": "ML ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਲੈਬ",
        "triage": "ਕਲੀਨਿਕਲ ਟ੍ਰਾਈਜ ਕੋਪਾਇਲਟ", "triage_sub": "ਵੈਕਟਰ RAG ਆਧਾਰ",
        "datasets": "ਡੇਟਾਸੈਟ ਐਕਸਪਲੋਰਰ", "datasets_sub": "10 ਸਮੱਗਰੀ ਵਾਲੀਆਂ CSVs",
        "jury": "ਅਡੈਪਸ਼ਨ AI 7-ਥੰਮ੍ਹ ਸਬੂਤ", "jury_sub": "ਹੈਕਾਥੌਨ ਅਵਾਰਡ ਸੂਟ",
        "precision_title": "ਮਾਡਲ ਸ਼ੁੱਧਤਾ", "mae_label": "ਔਸਤ ਗਲਤੀ", "autoscientist_label": "ਆਟੋ ਸਾਇੰਟਿਸਟ ਜਿੱਤ",
        "autoscientist_win": "ਆਟੋ ਸਾਇੰਟਿਸਟ ਜਿੱਤ", "adaption_eval_label": "ਅਡੈਪਸ਼ਨ ਮੁਲਾਂਕਣ", "adaption_eval": "ਅਡੈਪਸ਼ਨ ਮੁਲਾਂਕਣ"
    },
    "overview": {
        "kpi_current_aqi": "ਹਵਾ ਗੁਣਵੱਤਾ ਸੂਚਕਾਂਕ (AQI)", "kpi_aqi": "ਰੀਅਲ-ਟਾਈਮ ਹਵਾ ਗੁਣਵੱਤਾ",
        "kpi_aqi_sub": "ਓਪਨ-ਮੈਟੀਓ ਮਲਟੀ-ਸਟੇਸ਼ਨ ਸੈਂਸਰ", "kpi_pm25": "ਵਾਯੂਮੰਡਲੀ PM2.5 ਇਕਾਗਰਤਾ",
        "kpi_pm25_sub": "ਬਾਰੀਕ ਕਣਾਂ ਦੀ ਮਾਤਰਾ (µg/m³)", "kpi_surge_risk": "48 ਘੰਟੇ ਹਸਪਤਾਲ ਦਾਖਲਾ ਜੋਖਮ",
        "kpi_risk": "ਸਾਹ ਸੰਬੰਧੀ ਦਾਖਲਾ ਜੋਖਮ", "kpi_risk_sub": "ML ਗਰੇਡੀਐਂਟ ਬੂਸਟਿੰਗ ਭਵਿੱਖਬਾਣੀ",
        "kpi_grap_stage": "ਕਾਨੂੰਨੀ GRAP ਪੜਾਅ", "kpi_dominant_trigger": "ਮੁੱਖ ਕਾਰਕ ਅਤੇ ਤਾਪਮਾਨ",
        "kpi_admissions": "ਅਨੁਮਾਨਿਤ ਹਸਪਤਾਲ ਦਾਖਲੇ", "kpi_admissions_sub": "48 ਘੰਟੇ ਐਮਰਜੈਂਸੀ ਸਮਰੱਥਾ ਵੰਡ",
        "projected_admissions": "ਅਨੁਮਾਨਿਤ ਦਾਖਲੇ", "pts_day": "ਮਰੀਜ਼/ਦਿਨ",
        "grap_sub": "ਵਾਹਨਾਂ ਦੀਆਂ ਪਾਬੰਦੀਆਂ ਅਤੇ ਸਕੂਲ ਚੇਤਾਵਨੀਆਂ ਸਰਗਰਮ ਹਨ।",
        "caqm_schedule": "CAQM ਕਾਨੂੰਨੀ ਸਮਾਂ-ਸਾਰਣੀ (17 ਪੰਨੇ)",
        "airway_penetration": "ਸਾਹ ਨਾਲੀ ਵਿੱਚ ਦਾਖਲਾ:", "alveolar_deep": "ਐਲਵੀਓਲਰ (ਡੂੰਘਾ)",
        "capacity_strain": "ਸਮਰੱਥਾ ਟੀਚਾ ਅਤੇ ਹਸਪਤਾਲ ਦਾ ਦਬਾਅ", "capacity_sub": "48 ਘੰਟੇ ਅਨੁਮਾਨਿਤ ICU ਅਤੇ ਐਮਰਜੈਂਸੀ ਬੈੱਡ ਸੀਮਾ",
        "surge_score": "ਸਰਜ ਸਕੋਰ", "safe_capacity": "ਸੁਰੱਖਿਅਤ ਸਮਰੱਥਾ", "moderate_strain": "ਦਰਮਿਆਨਾ ਦਬਾਅ",
        "high_surge_risk": "ਉੱਚ ਵਾਧਾ ਜੋਖਮ", "critical_surge_alert": "ਗੰਭੀਰ ਐਮਰਜੈਂਸੀ ਚੇਤਾਵਨੀ",
        "high_surge": "ਉੱਚ ਵਾਧਾ", "severe": "ਗੰਭੀਰ", "very_poor": "ਬਹੁਤ ਮਾੜੀ", "poor": "ਮਾੜੀ",
        "moderate": "ਦਰਮਿਆਨੀ", "satisfactory": "ਤਸੱਲੀਬਖਸ਼", "good": "ਚੰਗੀ",
        "localized_advisory": "ਸਥਾਨਕ ਕਲੀਨਿਕਲ ਸਲਾਹ", "rag_match": "RAG ਮੇਲ", "vector_source": "ਵੈਕਟਰ ਸਰੋਤ",
        "map_title": "ਸਰਬ ਭਾਰਤੀ ਮੈਟਰੋ ਭੂਗੋਲਿਕ AQI ਨਕਸ਼ਾ",
        "map_sub": "12 CPCB ਕੇਂਦਰਾਂ ਵਿੱਚ ਵਾਯੂਮੰਡਲੀ ਟੈਲੀਮੈਟਰੀ। ਫੋਕਸ ਕਰਨ ਲਈ ਪਿੰਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।",
        "basemap_canvas": "ਕੈਨਵਸ ਲਾਈਟ", "basemap_streets": "ਗਲੀਆਂ", "reset_view": "ਰੀਸੈਟ ਵਿਊ",
        "live_open_meteo_synced": "ਲਾਈਵ ਓਪਨ-ਮੈਟੀਓ ਸਿੰਕ ਕੀਤਾ گیا", "cpcb_scale": "CPCB AQI ਪੈਮਾਨਾ",
        "severity_ranking": "ਖੇਤਰੀ AQI ਗੰਭੀਰਤਾ ਦਰਜਾਬੰਦੀ (12 ਮੈਟਰੋ)",
        "regional_severity_ranking": "12-ਮੈਟਰੋ ਖੇਤਰੀ AQI ਗੰਭੀਰਤਾ ਦਰਜਾਬੰਦੀ (ਲਾਈਵ)",
        "focus_dashboard": "ਡੈਸ਼ਬੋਰਡ 'ਤੇ ਫੋਕਸ ਕਰੋ", "click_to_fly": "ਜਾਣ ਲਈ ਕਲਿੱਕ ਕਰੋ",
        "chart_title": "ਮਹਾਂਮਾਰੀ ਵਿਗਿਆਨ ਨਿਗਰਾਨੀ ਅਤੇ ਭਵਿੱਖਬਾਣੀ ਟੈਲੀਮੈਟਰੀ",
        "tab_seasonal": "ਮੌਸਮੀ ਟੈਲੀਮੈਟਰੀ", "tab_cities": "12-ਸ਼ਹਿਰਾਂ ਦੀ ਤੁਲਨਾ", "tab_weights": "ML ਮਹੱਤਤਾ",
        "granularity_years": "ਸਾਲ (2015–2025)", "granularity_quarters": "ਤਿਮਾਹੀਆਂ (Q1–Q4)",
        "granularity_months": "ਮਹੀਨੇ (ਜਨਵਰੀ–ਦਸੰਬਰ)", "granularity_weeks": "ਹਫ਼ਤੇ (W1–W4)", "granularity_7day": "7-ਦਿਨ ਲਾਈਵ",
        "all_years": "ਸਾਰੇ ਸਾਲ", "all_years_range": "ਸਾਰੇ ਸਾਲ (2015-2025)", "all_months": "ਸਾਰੇ ਮਹੀਨੇ",
        "all_metros_avg": "ਸਾਰੇ 12 ਮੈਟਰੋਆਂ ਦੀ ਔਸਤ", "drill_path": "ਡ੍ਰਿਲ ਮਾਰਗ", "drill_up": "↑ ਉੱਪਰ ਜਾਓ",
        "legend_aqi": "ਔਸਤ AQI", "legend_admissions": "ਰੋਜ਼ਾਨਾ ਦਾਖਲੇ", "pm25_conc": "PM2.5 ਇਕਾਗਰਤਾ (µg/m³)",
        "click_to_drill": "💡 ਵੇਰਵੇ ਦੇਖਣ ਲਈ ਕਿਸੇ ਵੀ ਬਾਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ",
        "heatmap_title": "ਪੀਅਰਸਨ ਸਹਿਸੰਬੰਧ ਮੈਟ੍ਰਿਕਸ (8×8)",
        "heatmap_desc": "ਪ੍ਰਦੂਸ਼ਕਾਂ, ਮੌਸਮ ਅਤੇ ਦਾਖਲਿਆਂ ਵਿਚਕਾਰ ਸੰਬੰਧ ਗੁਣਾਂਕ (r)।",
        "temp_label": "ਤਾਪਮਾਨ", "admissions_label": "ਦਾਖਲੇ", "key_epidemiological_finding": "ਮੁੱਖ ਨਤੀਜਾ:",
        "dispatch_title": "ਲਾਈਵ ਹਸਪਤਾਲ ਐਮਰਜੈਂਸੀ ਵੰਡ ਕਤਾਰ",
        "dispatch_desc": "ਰੀਅਲ-ਟਾਈਮ ML ਜੋਖਮ ਅਤੇ GRAP ਪੜਾਵਾਂ ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ ਬੈੱਡ ਅਤੇ ਆਕਸੀਜਨ ਵੈਨ ਦੀ ਵੰਡ।",
        "hospital_name": "ਹਸਪਤਾਲ ਦਾ ਨਾਮ", "metro": "ਮੈਟਰੋ ਕੇਂਦਰ", "col_trigger": "ਵਾਯੂਮੰਡਲੀ ਕਾਰਕ",
        "col_resource": "ਸਰੋਤ ਵੰਡ", "col_grap": "CAQM GRAP ਪੜਾਅ", "col_eta": "ਪਹੁੰਚਣ ਦਾ ਸਮਾਂ",
        "icu_strain": "ICU ਦਬਾਅ", "priority": "ਤਰਜੀਹ", "action": "ਕਾਰਵਾਈ",
        "export_csv": "ਕਤਾਰ CSV ਨਿਰਯਾਤ ਕਰੋ"
    },
    "copilot": {
        "floating_button": "ਐਰੋਮੈੱਡ ਕੋਪਾਇਲਟ ਨੂੰ ਪੁੱਛੋ", "ai_triage": "AI ਟ੍ਰਾਈਜ", "rag_live": "RAG ਲਾਈਵ",
        "title": "ਐਰੋਮੈੱਡ ਕਲੀਨਿਕਲ ਕੋਪਾਇਲਟ", "ask_placeholder": "ਮਰਾਠੀ, ਹਿੰਦੀ, ਤਮਿਲ ਜਾਂ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਪੁੱਛੋ...", "send": "ਭੇਜੋ"
    },
    "simulator": {
        "title": "ਵਾਯੂਮੰਡਲੀ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਅਤੇ ਹਸਪਤਾਲ ਸਰਜ ਸਿਮੂਲੇਟਰ",
        "subtitle": "ਗਰੇਡੀਐਂਟ ਬੂਸਟਿੰਗ ਰਿਗ੍ਰੈਸਰ ਦੁਆਰਾ ਸੰਚਾਲਿਤ ਵਿਸ਼ਲੇਸ਼ਣ। ਐਮਰਜੈਂਸੀ ਵਾਰਡ ਦਾਖਲਿਆਂ ਦਾ ਅੰਦਾਜ਼ਾ ਲਗਾਓ।",
        "active_city_baseline": "ਸਰਗਰਮ ਸ਼ਹਿਰ ਬੇਸਲਾਈਨ", "presets_title": "ਤੀਬਰ ਧੂੰਏਂ ਅਤੇ ਮੌਸਮ ਦੇ ਪ੍ਰੀਸੈੱਟ",
        "reset_defaults": "ਸਲਾਈਡਰ ਰੀਸੈਟ ਕਰੋ", "adjust_pollutants": "ਪ੍ਰਦੂਸ਼ਕਾਂ ਨੂੰ ਵਿਵਸਥਿਤ ਕਰੋ",
        "pm25_weight": "96.5% ML ਮਹੱਤਤਾ", "hospital_surge_forecast": "ਹਸਪਤਾਲ ਸਰਜ ਪੂਰਵ ਅਨੁਮਾਨ",
        "predicted_daily_admissions": "ਅਨੁਮਾਨਿਤ ਰੋਜ਼ਾਨਾ ਸਾਹ ਸੰਬੰਧੀ ਐਮਰਜੈਂਸੀ ਦਾਖਲੇ", "projected_surge_delta": "ਅਨੁਮਾਨਿਤ ਅੰਤਰ",
        "critical_care_demands": "ਨਾਜ਼ੁਕ ਦੇਖਭਾਲ ਅਤੇ ਡਾਕਟਰੀ ਲੋੜਾਂ", "icu_beds": "ਲੋੜੀਂਦੇ ICU ਬੈੱਡ",
        "nebulizers": "ਨੈਬੂਲਾਈਜ਼ਰ", "oxygen_cylinders": "ਐਮਰਜੈਂਸੀ ਆਕਸੀਜਨ ਸਿਲੰਡਰ", "statutory_grap_stage": "ਕਾਨੂੰਨੀ CAQM GRAP ਪੜਾਅ:"
    },
    "datasets": {
        "title": "ਸਰਬ ਭਾਰਤੀ ਅਡੈਪਸ਼ਨ ਲੈਬਜ਼ ਨਿਰਯਾਤ ਕੈਟਾਲਾਗ",
        "subtitle": "ਅਡੈਪਸ਼ਨ ਲੈਬਜ਼ SDK ਦੁਆਰਾ ਸਿੰਕ ਕੀਤੇ ਡੇਟਾਸੈਟਾਂ ਦਾ ਆਡਿਟ।",
        "total_synced": "ਕੁੱਲ ਸਿੰਕ ਕੀਤਾ ਗਿਆ", "datasets_label": "ਡੇਟਾਸੈਟ", "protocols_label": "ਪ੍ਰੋਟੋਕੋਲ",
        "search_placeholder": "ਖੋਜੋ...", "filter_label": "ਫਿਲਟਰ", "filter_all": "ਸਾਰੇ",
        "col_name": "ਨਾਮ ਅਤੇ ਫਾਈਲ", "col_pillar": "ਸਮਰੱਥਾ ਥੰਮ੍ਹ", "col_rows": "ਕਤਾਰਾਂ",
        "col_size": "ਆਕਾਰ", "col_quality": "ਗ੍ਰੇਡ", "col_id": "ID",
        "col_preview": "ਪੂਰਵਦਰਸ਼ਨ", "view_rows": "ਕਤਾਰਾਂ ਦੇਖੋ", "table_view": "ਟੇਬਲ ਵਿਊ",
        "protocol_view": "ਕਾਰਡ ਵਿਊ", "close_drawer": "ਬੰਦ ਕਰੋ"
    },
    "jury": {
        "title": "ਅਡੈਪਸ਼ਨ AI 7-ਥੰਮ੍ਹ ਸਮਰੱਥਾ ਸੂਟ — ਜਿਊਰੀ ਸਬੂਤ ਕੇਂਦਰ",
        "subtitle": "ਐਰੋਮੈੱਡ ਇੰਡੀਆ ਬਣਾਉਣ ਵਿੱਚ ਵਰਤੇ ਗਏ ਸਾਰੇ 7 ਮੁੱਖ ਥੰਮ੍ਹਾਂ ਦੇ ਸਬੂਤ।",
        "quality_grade_card": "ਗੁਣਵੱਤਾ ਗ੍ਰੇਡ", "autoscientist_gain_card": "ਜਿੱਤ ਦਰ",
        "predictive_fit_card": "ML ਅਨੁਮਾਨਿਤ ਫਿੱਟ", "credit_reserve_card": "SDK ਰਿਜ਼ਰਵ",
        "verified_proof": "ਪ੍ਰਮਾਣਿਤ ਸਬੂਤ: 7 ਥੰਮ੍ਹ", "copy_id": "ID ਕਾਪੀ ਕਰੋ",
        "copied": "ਕਾਪੀ ਹੋ ਗਿਆ!", "copy_command": "ਕਮਾਂਡ ਕਾਪੀ ਕਰੋ"
    }
}

# Odia (or)
or_cities = cities_data["or"]
or_dict = {
    "dir": "ltr",
    "cities": or_cities,
    "chrome": {
        "brand_name": "ଏରୋମେଡ୍", "brand_suffix": "ଇଣ୍ଡିଆ", "brand_sub": "କ୍ଲିନିକାଲ୍ ନିରୀକ୍ଷଣ",
        "active_metro": "ସକ୍ରିୟ ମେଟ୍ରୋ", "search_metros": "୧୨ଟି ଭାରତୀୟ ମେଟ୍ରୋ ଖୋଜନ୍ତୁ...",
        "select_language": "ନିରୀକ୍ଷଣ ଭାଷା ଚୟନ କରନ୍ତୁ", "indic_scripts_note": "୧୩ଟି ଭାରତୀୟ ଭାଷାରେ ଯାଞ୍ଚ ହୋଇଥିବା ଡାକ୍ତରୀ ଶବ୍ଦକୋଷ",
        "more_languages": "+୧୦ ଅଧିକ", "export_advisory": "ପରାମର୍ଶ ରପ୍ତାନି କରନ୍ତୁ", "bulletin": "ବୁଲେଟିନ୍",
        "render_connected": "ରେଣ୍ଡର API ସଂଯୁକ୍ତ • R² = ୦.୯୮୮", "live_api": "ଲାଇଭ୍ API",
        "seed_mode": "ତତକ୍ଷଣାତ୍ ସିଡ୍ ମୋଡ୍ (0ms)", "instant_seed": "ସିଡ୍ ମୋଡ୍",
        "cpcb_caqm_grounding": "CPCB ଏବଂ CAQM ଆଇନଗତ ଆଧାର", "live_projection": "ଲାଇଭ୍ ୪୮ ଘଣ୍ଟାର ପୂର୍ବାନୁମାନ"
    },
    "nav": {
        "workspaces": "କ୍ଲିନିକାଲ୍ କାର୍ଯ୍ୟକ୍ଷେତ୍ର", "surveillance": "ନିରୀକ୍ଷଣ ସମୀକ୍ଷା", "surveillance_sub": "ବେଣ୍ଟୋ ଗ୍ରୀଡ୍ ଏବଂ ଟେଲିମେଟ୍ରି",
        "simulator": "ହ୍ୱାଟ୍-ଇଫ୍ ସିମୁଲେଟର", "simulator_sub": "ML ସମ୍ବେଦନଶୀଳତା ଲ୍ୟାବ୍",
        "triage": "କ୍ଲିନିକାଲ୍ ଟ୍ରାଏଜ୍ କୋପାଇଲଟ୍", "triage_sub": "ଭେକ୍ଟର RAG ଆଧାର",
        "datasets": "ଡାଟାସେଟ୍ ଏକ୍ସପ୍ଲୋରର୍", "datasets_sub": "୧୦ଟି ସଂକଳିତ CSV",
        "jury": "ଆଡାପ୍ସନ୍ AI ୭-ସ୍ତମ୍ଭ ପ୍ରମାଣ", "jury_sub": "ହ୍ୟାକାଥନ୍ ପୁରସ୍କାର ସୁଇଟ୍",
        "precision_title": "ମଡେଲ୍ ସଠିକତା", "mae_label": "ହାରାହାରି ତ୍ରୁଟି", "autoscientist_label": "ଅଟୋ ସାଇଣ୍ଟିଷ୍ଟ ବିଜୟ",
        "autoscientist_win": "ଅଟୋ ସାଇଣ୍ଟିଷ୍ଟ ବିଜୟ", "adaption_eval_label": "ଆଡାପ୍ସନ୍ ମୂଲ୍ୟାଙ୍କନ", "adaption_eval": "ଆଡାପ୍ସନ୍ ମୂଲ୍ୟାଙ୍କନ"
    },
    "overview": {
        "kpi_current_aqi": "ବାୟୁ ଗୁଣବତ୍ତା ସୂଚକାଙ୍କ (AQI)", "kpi_aqi": "ବାସ୍ତବ ସମୟ ବାୟୁ ଗୁଣବତ୍ତା",
        "kpi_aqi_sub": "ଓପନ୍-ମେଟିଓ ସେନ୍ସର୍", "kpi_pm25": "ପରିବେଶ PM2.5 ସାନ୍ଦ୍ରତା",
        "kpi_pm25_sub": "ସୂକ୍ଷ୍ମ କଣିକା (µg/m³)", "kpi_surge_risk": "୪୮ ଘଣ୍ଟା ହସ୍ପିଟାଲ୍ ଭର୍ତ୍ତି ବିପଦ",
        "kpi_risk": "ଶ୍ୱାସକ୍ରିୟା ଭର୍ତ୍ତି ବିପଦ", "kpi_risk_sub": "ML ପୂର୍ବାନୁମାନ",
        "kpi_grap_stage": "ଆଇନଗତ GRAP ପର୍ଯ୍ୟାୟ", "kpi_dominant_trigger": "ମୁଖ୍ୟ କାରକ ଏବଂ ତାପମାତ୍ରା",
        "kpi_admissions": "ଆନୁମାନିକ ହସ୍ପିଟାଲ୍ ଭର୍ତ୍ତି", "kpi_admissions_sub": "୪୮ ଘଣ୍ଟା ଜରୁରୀକାଳୀନ କ୍ଷମତା",
        "projected_admissions": "ଆନୁମାନିକ ଭର୍ତ୍ତି", "pts_day": "ରୋଗୀ/ଦିନ",
        "grap_sub": "ଯାନବାହନ କଟକଣା ଏବଂ ପ୍ରାଥମିକ ବିଦ୍ୟାଳୟ ଚେତାବନୀ ସକ୍ରିୟ ଅଛି।",
        "caqm_schedule": "CAQM ଆଇନଗତ କାର୍ଯ୍ୟସୂଚୀ (୧୭ ପୃଷ୍ଠା)",
        "airway_penetration": "ଶ୍ୱାସନଳୀ ପ୍ରବେଶ:", "alveolar_deep": "ଆଲଭିଓଲାର୍ (ଗଭୀର)",
        "capacity_strain": "କ୍ଷମତା ଲକ୍ଷ୍ୟ ଏବଂ ହସ୍ପିଟାଲ୍ ଚାପ", "capacity_sub": "୪୮ ଘଣ୍ଟାର ଆନୁମାନିକ ICU ଏବଂ ଜରୁରୀକାଳୀନ ବେଡ୍ ସୀମା",
        "surge_score": "ବୃଦ୍ଧି ସ୍କୋର", "safe_capacity": "ନିରାପଦ କ୍ଷମତା", "moderate_strain": "ମଧ୍ୟମ ଚାପ",
        "high_surge_risk": "ଉଚ୍ଚ ବୃଦ୍ଧି ବିପଦ", "critical_surge_alert": "ଗମ୍ଭୀର ଜରୁରୀକାଳୀନ ସତର୍କତା",
        "high_surge": "ଉଚ୍ଚ ବୃଦ୍ଧି", "severe": "ଗମ୍ଭୀର", "very_poor": "ବହୁତ ଖରାପ", "poor": "ଖରାପ",
        "moderate": "ମଧ୍ୟମ", "satisfactory": "ସନ୍ତୋଷଜନକ", "good": "ଭଲ",
        "localized_advisory": "ସ୍ଥାନୀୟ କ୍ଲିନିକାଲ୍ ପରାମର୍ଶ", "rag_match": "RAG ମେଳ", "vector_source": "ଭେକ୍ଟର ଉତ୍ସ",
        "map_title": "ସର୍ବଭାରତୀୟ ମେଟ୍ରୋ ଭୌଗୋଳିକ AQI ମାନଚିତ୍ର",
        "map_sub": "୧୨ଟି CPCB କେନ୍ଦ୍ରର ବାୟୁମଣ୍ଡଳୀୟ ଟେଲିମେଟ୍ରି। ବିବରଣୀ ପାଇଁ ପିନ୍ ଉପରେ କ୍ଲିକ୍ କରନ୍ତୁ।",
        "basemap_canvas": "କାନଭାସ୍ ଲାଇଟ୍", "basemap_streets": "ରାସ୍ତା", "reset_view": "ରିସେଟ୍ ଭ୍ୟୁ",
        "live_open_meteo_synced": "ଲାଇଭ୍ ଓପନ୍-ମେଟିଓ ସିଙ୍କ୍", "cpcb_scale": "CPCB AQI ମାପକାଠି",
        "severity_ranking": "ଆଞ୍ଚଳିକ AQI ତୀବ୍ରତା ମାନ୍ୟତା (୧୨ ମେଟ୍ରୋ)",
        "regional_severity_ranking": "୧୨-ମେଟ୍ରୋ ଆଞ୍ଚଳିକ AQI ତୀବ୍ରତା ମାନ୍ୟତା (ଲାଇଭ୍)",
        "focus_dashboard": "ଡ୍ୟାସବୋର୍ଡ ଫୋକସ୍ କରନ୍ତୁ", "click_to_fly": "ଯିବା ପାଇଁ କ୍ଲିକ୍ କରନ୍ତୁ",
        "chart_title": "ଏପିଡେମିଓଲୋଜିକାଲ୍ ନିରୀକ୍ଷଣ ଏବଂ ପୂର୍ବାନୁମାନ ଟେଲିମେଟ୍ରି",
        "tab_seasonal": "ଋତୁକାଳୀନ ଟେଲିମେଟ୍ରି", "tab_cities": "୧୨-ସହର ତୁଳନା", "tab_weights": "ML ଗୁରୁତ୍ୱ",
        "granularity_years": "ବର୍ଷ (୨୦୧୫–୨୦୨୫)", "granularity_quarters": "ତ୍ରୈମାସିକ (Q1–Q4)",
        "granularity_months": "ମାସ (ଜାନୁଆରୀ–ଡିସେମ୍ବର)", "granularity_weeks": "ସପ୍ତାହ (W1–W4)", "granularity_7day": "୭-ଦିନ ଲାଇଭ୍",
        "all_years": "ସମସ୍ତ ବର୍ଷ", "all_years_range": "ସମସ୍ତ ବର୍ଷ (୨୦୧୫-୨୦୨୫)", "all_months": "ସମସ୍ତ ମାସ",
        "all_metros_avg": "ସମସ୍ତ ୧୨ ମେଟ୍ରୋର ହାରାହାରି", "drill_path": "ମାର୍ଗ", "drill_up": "↑ ଉପରକୁ ଯାଆନ୍ତୁ",
        "legend_aqi": "ହାରାହାରି AQI", "legend_admissions": "ଦୈନିକ ଭର୍ତ୍ତି", "pm25_conc": "PM2.5 ସାନ୍ଦ୍ରତା (µg/m³)",
        "click_to_drill": "💡 ବିବରଣୀ ଦେଖିବାକୁ ଯେକୌଣସି ବାର୍ ଉପରେ କ୍ଲିକ୍ କରନ୍ତୁ",
        "heatmap_title": "ପିଅରସନ୍ ସହସମ୍ବନ୍ଧ ମ୍ୟାଟ୍ରିକ୍ସ (୮×୮)",
        "heatmap_desc": "ପ୍ରଦୂଷକ, ପାଣିପାଗ ଏବଂ ଭର୍ତ୍ତି ମଧ୍ୟରେ ସହସମ୍ବନ୍ଧ ଗୁଣାଙ୍କ (r)।",
        "temp_label": "ତାପମାତ୍ରା", "admissions_label": "ଭର୍ତ୍ତି", "key_epidemiological_finding": "ମୁଖ୍ୟ ନିରୀକ୍ଷଣ:",
        "dispatch_title": "ଲାଇଭ୍ ହସ୍ପିଟାଲ୍ ଜରୁରୀକାଳୀନ ବଣ୍ଟନ ଧାଡ଼ି",
        "dispatch_desc": "ML ବିପଦ ଏବଂ GRAP ପର୍ଯ୍ୟାୟ ଦ୍ୱାରା ବେଡ୍ ଏବଂ ଅକ୍ସିଜେନ୍ ଭ୍ୟାନ୍ ବଣ୍ଟନ।",
        "hospital_name": "ହସ୍ପିଟାଲ୍ ନାମ", "metro": "ମେଟ୍ରୋ କେନ୍ଦ୍ର", "col_trigger": "ବାୟୁମଣ୍ଡଳୀୟ କାରକ",
        "col_resource": "ସମ୍ବଳ ବଣ୍ଟନ", "col_grap": "CAQM GRAP ପର୍ଯ୍ୟାୟ", "col_eta": "ପହଞ୍ଚିବା ସମୟ",
        "icu_strain": "ICU ଚାପ", "priority": "ପ୍ରାଥମିକତା", "action": "ପଦକ୍ଷେପ",
        "export_csv": "ଧାଡ଼ି CSV ରପ୍ତାନି କରନ୍ତୁ"
    },
    "copilot": {
        "floating_button": "ଏରୋମେଡ୍ କୋପାଇଲଟ୍‌ଙ୍କୁ ପଚାରନ୍ତୁ", "ai_triage": "AI ଟ୍ରାଏଜ୍", "rag_live": "RAG ଲାଇଭ୍",
        "title": "ଏରୋମେଡ୍ କ୍ଲିନିକାଲ୍ କୋପାଇଲଟ୍", "ask_placeholder": "ମରାଠୀ, ହିନ୍ଦୀ, ତାମିଲ କିମ୍ବା ଇଂରାଜୀରେ ପଚାରନ୍ତୁ...", "send": "ପଠାନ୍ତୁ"
    },
    "simulator": {
        "title": "ବାୟୁମଣ୍ଡଳୀୟ ସମ୍ବେଦନଶୀଳତା ଏବଂ ହସ୍ପିଟାଲ୍ ସର୍ଜ୍ ସିମୁଲେଟର୍",
        "subtitle": "ଗ୍ରେଡିଏଣ୍ଟ ବୁଷ୍ଟିଂ ରିଗ୍ରେସର୍ ଦ୍ୱାରା ବିଶ୍ଳେଷଣ। ଜରୁରୀକାଳୀନ ୱାର୍ଡ ଭର୍ତ୍ତିର ପୂର୍ବାନୁମାନ କରନ୍ତୁ।",
        "active_city_baseline": "ସକ୍ରିୟ ସହର ବେସଲାଇନ୍", "presets_title": "ତୀବ୍ର ଧୂଆଁ ଏବଂ ପାଣିପାଗ ପ୍ରିସେଟ୍",
        "reset_defaults": "ସ୍ଲାଇଡର୍ ରିସେଟ୍ କରନ୍ତୁ", "adjust_pollutants": "ପ୍ରଦୂଷକ ସଜାଡ଼ନ୍ତୁ",
        "pm25_weight": "୯୬.୫% ML ଗୁରୁତ୍ୱ", "hospital_surge_forecast": "ହସ୍ପିଟାଲ୍ ସର୍ଜ୍ ପୂର୍ବାନୁମାନ",
        "predicted_daily_admissions": "ଆନୁମାନିକ ଦୈନିକ ଶ୍ୱାସକ୍ରିୟା ଜରୁରୀକାଳୀନ ଭର୍ତ୍ତି", "projected_surge_delta": "ଆନୁମାନିକ ପାର୍ଥକ୍ୟ",
        "critical_care_demands": "ଗୁରୁତର ଯତ୍ନ ଏବଂ ଚିକିତ୍ସା ଆବଶ୍ୟକତା", "icu_beds": "ଆବଶ୍ୟକ ICU ବେଡ୍",
        "nebulizers": "ନେବୁଲାଇଜର୍", "oxygen_cylinders": "ଜରୁରୀକାଳୀନ ଅକ୍ସିଜେନ୍ ସିଲିଣ୍ଡର୍", "statutory_grap_stage": "ଆଇନଗତ CAQM GRAP ପର୍ଯ୍ୟାୟ:"
    },
    "datasets": {
        "title": "ସର୍ବଭାରତୀୟ ଆଡାପ୍ସନ୍ ଲ୍ୟାବ୍ସ ରପ୍ତାନି କାଟାଲଗ୍",
        "subtitle": "ଆଡାପ୍ସନ୍ ଲ୍ୟାବ୍ସ SDK ମାଧ୍ୟମରେ ସିଙ୍କ୍ ହୋଇଥିବା ଡାଟାସେଟ୍‌ର ଅଡିଟ୍।",
        "total_synced": "ମୋଟ ସିଙ୍କ୍ ହୋଇଛି", "datasets_label": "ଡାଟାସେଟ୍", "protocols_label": "ପ୍ରୋଟୋକଲ୍",
        "search_placeholder": "ଖୋଜନ୍ତୁ...", "filter_label": "ଫିଲ୍ଟର୍", "filter_all": "ସମସ୍ତ",
        "col_name": "ନାମ ଏବଂ ଫାଇଲ୍", "col_pillar": "ସ୍ତମ୍ଭ", "col_rows": "ଧାଡ଼ି",
        "col_size": "ଆକାର", "col_quality": "ଗ୍ରେଡ୍", "col_id": "ID",
        "col_preview": "ପୂର୍ବାବଲୋକନ", "view_rows": "ଧାଡ଼ି ଦେଖନ୍ତୁ", "table_view": "ଟେବୁଲ୍ ଭ୍ୟୁ",
        "protocol_view": "କାର୍ଡ ଭ୍ୟୁ", "close_drawer": "ବନ୍ଦ କରନ୍ତୁ"
    },
    "jury": {
        "title": "ଆଡାପ୍ସନ୍ AI ୭-ସ୍ତମ୍ଭ ସୁଇଟ୍ — ଜୁରୀ ପ୍ରମାଣ କେନ୍ଦ୍ର",
        "subtitle": "ଏରୋମେଡ୍ ଇଣ୍ଡିଆ ନିର୍ମାଣରେ ବ୍ୟବହୃତ ସମସ୍ତ ୭ଟି ମୁଖ୍ୟ ସ୍ତମ୍ଭର ପ୍ରମାଣ।",
        "quality_grade_card": "ଗୁଣବତ୍ତା ଗ୍ରେଡ୍", "autoscientist_gain_card": "ବିଜୟ ହାର",
        "predictive_fit_card": "ML ପୂର୍ବାନୁମାନ ଫିଟ୍", "credit_reserve_card": "SDK ରିଜର୍ଭ",
        "verified_proof": "ଯାଞ୍ଚ ହୋଇଥିବା ପ୍ରମାଣ: ୭ ସ୍ତମ୍ଭ", "copy_id": "ID କପି କରନ୍ତୁ",
        "copied": "କପି ହୋଇଛି!", "copy_command": "କମାଣ୍ଡ କପି କରନ୍ତୁ"
    }
}

# Assamese (as)
as_cities = cities_data["as"]
as_dict = {
    "dir": "ltr",
    "cities": as_cities,
    "chrome": {
        "brand_name": "এৰোমেড", "brand_suffix": "ইণ্ডিয়া", "brand_sub": "ক্লিনিকেল নিৰীক্ষণ",
        "active_metro": "সক্ৰিয় মেট্ৰ'", "search_metros": "১২খন ভাৰতীয় মেট্ৰ' সন্ধান কৰক...",
        "select_language": "নিৰীক্ষণ ভাষা বাছক", "indic_scripts_note": "১৩টা ভাৰতীয় লিপিত পৰীক্ষিত চিকিৎসা শব্দকোষ",
        "more_languages": "+১০ অধিক", "export_advisory": "পৰামৰ্শ ৰপ্তানি কৰক", "bulletin": "বুলেটিন",
        "render_connected": "ৰেণ্ডাৰ API সংযোগ হ'ল • R² = ০.৯৮৮", "live_api": "লাইভ API",
        "seed_mode": "তাত্ক্ষণিক সীড ম'ড (0ms)", "instant_seed": "সীড ম'ড",
        "cpcb_caqm_grounding": "CPCB আৰু CAQM আইনী ভিত্তি", "live_projection": "লাইভ ৪৮ ঘণ্টাৰ পূৰ্বাভাস"
    },
    "nav": {
        "workspaces": "ক্লিনিকেল কৰ্মক্ষেত্ৰ", "surveillance": "নিৰীক্ষণ পৰ্যালোচনা", "surveillance_sub": "বেণ্টো গ্ৰিড আৰু টেলিমেট্ৰী",
        "simulator": "হোৱাট-ইফ চিমুলেটৰ", "simulator_sub": "ML সংবেদনশীলতা লেব",
        "triage": "ক্লিনিকেল ট্ৰায়াজ ক'পাইলট", "triage_sub": "ভেক্টৰ RAG ভিত্তি",
        "datasets": "ডাটাছেট এক্সপ্ল'ৰাৰ", "datasets_sub": "১০টা সংকলিত CSV",
        "jury": "এডাপশ্যন AI ৭-স্তম্ভ প্ৰমাণ", "jury_sub": "হেকাথন বঁটা সংহতি",
        "precision_title": "মডেলৰ নিখুঁততা", "mae_label": "গড় ভুল", "autoscientist_label": "অট' ছায়েন্টিষ্ট জয়",
        "autoscientist_win": "অট' ছায়েন্টিষ্ট জয়", "adaption_eval_label": "এডাপশ্যন মূল্যায়ন", "adaption_eval": "এডাপশ্যন মূল্যায়ন"
    },
    "overview": {
        "kpi_current_aqi": "বায়ু মান সূচকাংক (AQI)", "kpi_aqi": "প্ৰকৃত সময়ৰ বায়ু মান",
        "kpi_aqi_sub": "অ'পেন-মেটিঅ' মাল্টি-ষ্টেচন চেন্সৰ", "kpi_pm25": "বায়ুমণ্ডলীয় PM2.5 ঘনত্ব",
        "kpi_pm25_sub": "সূক্ষ্ম কণিকা (µg/m³)", "kpi_surge_risk": "৪৮ ঘণ্টা চিকিৎসালয় ভৰ্তিৰ বিপদ",
        "kpi_risk": "শ্বাসতন্ত্ৰ ভৰ্তিৰ বিপদ", "kpi_risk_sub": "ML ভৱিষ্যদ্বাণী",
        "kpi_grap_stage": "আইনী GRAP পৰ্যায়", "kpi_dominant_trigger": "প্ৰধান কাৰক আৰু উষ্ণতা",
        "kpi_admissions": "আনুমানিক চিকিৎসালয় ভৰ্তি", "kpi_admissions_sub": "৪৮ ঘণ্টা জৰুৰীকালীন ক্ষমতা",
        "projected_admissions": "আনুমানিক ভৰ্তি", "pts_day": "ৰোগী/দিন",
        "grap_sub": "যান-বাহন নিষেধাজ্ঞা আৰু প্ৰাথমিক বিদ্যালয় সতৰ্কবাণী সক্ৰিয় আছে।",
        "caqm_schedule": "CAQM আইনী সময়সূচী (১৭ পৃষ্ঠা)",
        "airway_penetration": "শ্বাসনলী প্ৰৱেশ:", "alveolar_deep": "এলভিঅ'লাৰ (গভীৰ)",
        "capacity_strain": "ক্ষমতা লক্ষ্য আৰু চিকিৎসালয়ৰ চাপ", "capacity_sub": "৪৮ ঘণ্টাৰ আনুমানিক ICU আৰু জৰুৰীকালীন বিছনা সীমা",
        "surge_score": "বৃদ্ধি স্ক'ৰ", "safe_capacity": "সুৰক্ষিত ক্ষমতা", "moderate_strain": "মধ্যমীয়া চাপ",
        "high_surge_risk": "উচ্চ বৃদ্ধিৰ বিপদ", "critical_surge_alert": "গুৰুতৰ জৰুৰীকালীন সতৰ্কবাণী",
        "high_surge": "উচ্চ বৃদ্ধি", "severe": "গুৰুতৰ", "very_poor": "অতি বেয়া", "poor": "বেয়া",
        "moderate": "মধ্যমীয়া", "satisfactory": "সন্তোষজনক", "good": "ভাল",
        "localized_advisory": "স্থানীয় ক্লিনিকেল পৰামৰ্শ", "rag_match": "RAG মিল", "vector_source": "ভেক্টৰ উৎস",
        "map_title": "সৰ্বভাৰতীয় মেট্ৰ' ভৌগোলিক AQI মানচিত্ৰ",
        "map_sub": "১২টা CPCB কেন্দ্ৰৰ বায়ুমণ্ডলীয় টেলিমেট্ৰী। ফ'কাচ কৰিবলৈ পিনত ক্লিক কৰক।",
        "basemap_canvas": "কেনভাছ লাইট", "basemap_streets": "ৰাস্তা", "reset_view": "ৰিচেট ভিউ",
        "live_open_meteo_synced": "লাইভ অ'পেন-মেটিঅ' সমলয় কৰা হ'ল", "cpcb_scale": "CPCB AQI স্কেল",
        "severity_ranking": "আঞ্চলিক AQI তীব্ৰতা ৰেংকিং (১২ মেট্ৰ')",
        "regional_severity_ranking": "১২-মেট্ৰ' আঞ্চলিক AQI তীব্ৰতা ৰেংকিং (লাইভ)",
        "focus_dashboard": "ডেশ্বব'ৰ্ড ফ'কাচ কৰক", "click_to_fly": "যাবলৈ ক্লিক কৰক",
        "chart_title": "মহামাৰী বিজ্ঞান নিৰীক্ষণ আৰু ভৱিষ্যদ্বাণী টেলিমেট্ৰী",
        "tab_seasonal": "ঋতুকালীন টেলিমেট্ৰী", "tab_cities": "১২-খন চহৰৰ তুলনা", "tab_weights": "ML গুৰুত্ব",
        "granularity_years": "বছৰ (২০১৫–২০২৫)", "granularity_quarters": "ত্ৰৈমাসিক (Q1–Q4)",
        "granularity_months": "মাহ (জানুৱাৰী–ডিচেম্বৰ)", "granularity_weeks": "সপ্তাহ (W1–W4)", "granularity_7day": "৭-দিন লাইভ",
        "all_years": "সকলো বছৰ", "all_years_range": "সকলো বছৰ (২০১৫-২০২৫)", "all_months": "সকলো মাহ",
        "all_metros_avg": "সকলো ১২ মেট্ৰ'ৰ গড়", "drill_path": "পথ", "drill_up": "↑ ওপৰলৈ যাওক",
        "legend_aqi": "গড় AQI", "legend_admissions": "দৈনিক ভৰ্তি", "pm25_conc": "PM2.5 ঘনত্ব (µg/m³)",
        "click_to_drill": "💡 বিৱৰণ চাবলৈ যিকোনো বাৰত ক্লিক কৰক",
        "heatmap_title": "পিয়াৰচন সহসম্বন্ধ মেট্ৰিক্স (৮×৮)",
        "heatmap_desc": "প্ৰদূষক, বতৰ আৰু ভৰ্তিৰ মাজৰ সহসম্বন্ধ গুণাংক (r)।",
        "temp_label": "উষ্ণতা", "admissions_label": "ভৰ্তি", "key_epidemiological_finding": "মুখ্য ফলাফল:",
        "dispatch_title": "লাইভ চিকিৎসালয় জৰুৰীকালীন বিতৰণ শাৰী",
        "dispatch_desc": "ML বিপদ আৰু GRAP পৰ্যায় অনুসৰি বিছনা আৰু অক্সিজেন ভ্যান স্বয়ংক্ৰিয় বিতৰণ।",
        "hospital_name": "চিকিৎসালয়ৰ নাম", "metro": "মেট্ৰ' কেন্দ্ৰ", "col_trigger": "বায়ুমণ্ডলীয় কাৰক",
        "col_resource": "সম্পদ বিতৰণ", "col_grap": "CAQM GRAP পৰ্যায়", "col_eta": "উপস্থিতি সময়",
        "icu_strain": "ICU চাপ", "priority": "প্ৰাথমিকতা", "action": "পদক্ষেপ",
        "export_csv": "শাৰী CSV ৰপ্তানি কৰক"
    },
    "copilot": {
        "floating_button": "এৰোমেড ক'পাইলটক সোধক", "ai_triage": "AI ট্ৰায়াজ", "rag_live": "RAG লাইভ",
        "title": "এৰোমেড ক্লিনিকেল ক'পাইলট", "ask_placeholder": "মাৰাঠী, হিন্দী, তামিল বা ইংৰাজীত সোধক...", "send": "প্ৰেৰণ কৰক"
    },
    "simulator": {
        "title": "বায়ুমণ্ডলীয় সংবেদনশীলতা আৰু চিকিৎসালয় বৃদ্ধি চিমুলেটৰ",
        "subtitle": "গ্ৰেডিয়েণ্ট বুষ্টিং ৰিগ্ৰেচৰ দ্বাৰা বিশ্লেষণ। জৰুৰীকালীন ভৰ্তিৰ পূৰ্বানুমান কৰক।",
        "active_city_baseline": "সক্ৰিয় চহৰ বেচলাইন", "presets_title": "তীব্ৰ ধোঁৱাশা আৰু বতৰ প্ৰিছেট",
        "reset_defaults": "ৰিচেট কৰক", "adjust_pollutants": "প্ৰদূষক সামঞ্জস্য কৰক",
        "pm25_weight": "৯৬.৫% ML গুৰুত্ব", "hospital_surge_forecast": "চিকিৎসালয় বৃদ্ধি পূৰ্বাভাস",
        "predicted_daily_admissions": "আনুমানিক দৈনিক শ্বাসতন্ত্ৰ জৰুৰীকালীন ভৰ্তি", "projected_surge_delta": "আনুমানিক পাৰ্থক্য",
        "critical_care_demands": "জৰুৰীকালীন যত্ন আৰু চিকিৎসা প্ৰয়োজন", "icu_beds": "প্ৰয়োজনীয় ICU বিছনা",
        "nebulizers": "নেবুলাইজাৰ", "oxygen_cylinders": "জৰুਰীকালীন অক্সিজেন চিলিণ্ডাৰ", "statutory_grap_stage": "আইনী CAQM GRAP পৰ্যায়:"
    },
    "datasets": {
        "title": "সৰ্বভাৰতীয় এডাপশ্যন লেব্ছ ৰপ্তানি ক্যাটালগ",
        "subtitle": "এডাপশ্যন লেব্ছ SDK দ্বাৰা সমন্বিত ডাটাছেটৰ অডিট।",
        "total_synced": "মুঠ সমন্বিত", "datasets_label": "ডাটাছেট", "protocols_label": "প্ৰট'কল",
        "search_placeholder": "সন্ধান কৰক...", "filter_label": "ফিল্টাৰ", "filter_all": "সকলো",
        "col_name": "নাম আৰু ফাইল", "col_pillar": "স্তম্ভ", "col_rows": "শাৰী",
        "col_size": "আকাৰ", "col_quality": "গ্ৰেড", "col_id": "ID",
        "col_preview": "পূৰ্বদৰ্শন", "view_rows": "শাৰী চাওক", "table_view": "টেবুল ভিউ",
        "protocol_view": "কাৰ্ড ভিউ", "close_drawer": "বন্ধ কৰক"
    },
    "jury": {
        "title": "এডাপশ্যন AI ৭-স্তম্ভ সংহতি — জুৰী প্ৰমাণ কেন্দ্ৰ",
        "subtitle": "এৰোমেড ইণ্ডিয়া নিৰ্মাণত ব্যৱহাৰ কৰা সকলো ৭টা মূল স্তম্ভৰ প্ৰমাণ।",
        "quality_grade_card": "গুণমান গ্ৰেড", "autoscientist_gain_card": "জয়ৰ হাৰ",
        "predictive_fit_card": "ML পূৰ্বানুমান ফিট", "credit_reserve_card": "SDK সংৰক্ষণ",
        "verified_proof": "পৰীক্ষিত প্ৰমাণ: ৭টা স্তম্ভ", "copy_id": "ID কপি কৰক",
        "copied": "কপি কৰা হ'ল!", "copy_command": "কমাণ্ড কপি কৰক"
    }
}

all_translations = {
    "en": en,
    "hi": hi,
    "mr": mr,
    "bn": bn,
    "ta": ta,
    "te": te,
    "ur": ur,
    "kn": kn,
    "ml": ml,
    "gu": gu,
    "pa": pa,
    "or": or_dict,
    "as": as_dict
}

output_path = "/home/suyash/Projects/aeromed-india/frontend/src/i18n/translations.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("/**\n")
    f.write(" * AeroMed India - Comprehensive 13-Language Translation Dictionary\n")
    f.write(" * Supports: en, hi, mr, bn, ta, te, ur, kn, ml, gu, pa, or, as\n")
    f.write(" * 100% full coverage of all workspaces, telemetry controls, map legends, and clinical modals.\n")
    f.write(" */\n\n")
    f.write("export const translations = ")
    f.write(json.dumps(all_translations, ensure_ascii=False, indent=2))
    f.write(";\n")

print(f"Successfully generated {output_path} with all 13 languages!")
