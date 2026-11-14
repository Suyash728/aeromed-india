# -*- coding: utf-8 -*-
"""
AeroMed India - Translation Enricher
Enriches frontend/src/i18n/translations.js with 100% comprehensive dictionary keys
for chrome, overview, simulator, copilot, datasets, and jury across all 13 languages.
"""

import json

ENRICHMENTS = {
    "en": {
        "chrome": {
            "footer_desc": "Clinical Air Quality & Respiratory Disease Surveillance Monorepo",
            "footer_adaption": "Adaption Labs Grounded",
            "rules_count": "8,188 Rules",
            "live_model_calc": "Live Model Calculation"
        },
        "overview": {
            "insight_years": "10-Year Decadal Trend: PM2.5 exposure shows compound annual +4.2% increase across urban corridors.",
            "insight_quarters": "Seasonal Quarterly Analysis: Q4 (Winter Smog) records 3.4x higher particulate levels than Q3 (Monsoon).",
            "insight_months": "Winter Inversion Peak: Nov–Jan admissions spike +240% across Indo-Gangetic Plain.",
            "insight_weeks": "Weekly Micro-Surge: Post-crop burning weeks show acute ICU respiratory admissions.",
            "insight_live": "Live 7-Day Rolling Horizon: Real-time correlation with CPCB monitoring stations.",
            "r2_precision": "ML R² = 0.9879",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 Concentration (Fine Respirable Smog)",
            "pm10_title": "PM10 (Coarse Inhalable Dust)",
            "no2_title": "NO2 (Vehicular Combustion)",
            "so2_title": "SO2 (Industrial Emissions)",
            "temperature_title": "Ambient Temperature",
            "humidity_title": "Relative Humidity",
            "live_calc": "Live Model Calculation",
            "temp_hint": "Cold air traps winter surface inversion",
            "humidity_hint": "High moisture condenses dense smog haze",
            "vs_baseline": "vs Baseline"
        },
        "copilot": {
            "rag_title": "TF-IDF Vector RAG Evidence Grounding",
            "sub_ms": "Sub-ms Retrieval",
            "retrieved_source": "Retrieved Knowledge Source",
            "matched_excerpt": "Exact Matched Clinical Rule Excerpt",
            "guardrails_verified": "Adaption Blueprint Medical Guardrails Verified",
            "rule_1": "Rule 1: CPCB AQI Standard Compliance (0-500)",
            "rule_2": "Rule 2: Statutory CAQM GRAP Directives (Stage I-IV)",
            "rule_3": "Rule 3: Zero Pharmaceutical Rx Hallucination",
            "rule_4": "Rule 4: Mandatory Triage Trigger (SpO2 < 92%)",
            "rule_5": "Rule 5: Certified N95 & HEPA Filtration Mandate",
            "er_warning": "SpO2 < 92%: Immediate Emergency ER Transport Required!",
            "pulse_spo2": "Pulse SpO2:",
            "context_label": "Context:",
            "rule_count": "8,188 Rules",
            "profile_pediatric": "Pediatric Asthma (Age 4–12)",
            "profile_geriatric": "Geriatric COPD (Age 60+)",
            "profile_worker": "Outdoor Gig/Delivery Worker",
            "profile_maternal": "Maternal & Prenatal Care",
            "profile_general": "General Population"
        },
        "datasets": {
            "filter_grade_a": "Grade A (9.4+)",
            "filter_invented": "Synthetic Invent",
            "filter_forge": "Forge Extracted",
            "table_view": "Table View",
            "protocol_view": "Protocol Card View",
            "close_drawer": "Close Drawer",
            "samples_header": "Synthesized & Extracted Ground-Truth Rows",
            "prompt_context": "Meteorological / Clinical Prompt Context:",
            "protocol_truth": "Clinical Response Protocol / Ground Truth:",
            "copy_id_title": "Copy full Adaption Dataset ID"
        },
        "jury": {
            "quality_grade_card": "Adaption Quality Grade",
            "autoscientist_gain_card": "AutoScientist Win Rate",
            "predictive_fit_card": "ML Predictive Fit",
            "credit_reserve_card": "SDK Credit Reserve",
            "top_percentile": "Top 33rd Percentile Globally",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (3 Iterations)",
            "mae_subtitle": "MAE ±1.88 daily admissions",
            "buffer_retained": "Verified >400 Buffer Retained",
            "verification_command_title": "Direct Adaption SDK Verification One-Liner for Jury",
            "copy_command": "Copy Command"
        }
    },

    "hi": {
        "chrome": {
            "footer_desc": "चिकित्सीय वायु गुणवत्ता एवं श्वसन रोग निगरानी मोनोरेपो",
            "footer_adaption": "अडैप्शन लैब्स द्वारा समर्थित",
            "rules_count": "८,१८८ नियम",
            "live_model_calc": "लाइव मॉडल गणना"
        },
        "overview": {
            "insight_years": "१०-वर्षीय प्रवृत्ति: शहरी क्षेत्रों में PM2.5 में +४.२% वार्षिक वृद्धि।",
            "insight_quarters": "मौसमी त्रैमासिक विश्लेषण: Q4 (सर्दियों का स्मॉग) मानसून की तुलना में ३.४ गुना अधिक।",
            "insight_months": "शीतकालीन इनवर्जन चरम: नवंबर-जनवरी में भारत-गंगा मैदान में प्रवेश में +२४०% की वृद्धि।",
            "insight_weeks": "साप्ताहिक वृद्धि: पराली जलने के बाद के हफ्तों में आईसीयू श्वसन आपातकाल में तेज वृद्धि।",
            "insight_live": "लाइव ७-दिवसीय चक्र: सीपीसीबी निगरानी स्टेशनों के साथ वास्तविक समय सहसंबंध।",
            "r2_precision": "एमएल R² = ०.९८७९",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 सांद्रता (सूक्ष्म श्वसनीय स्मॉग)",
            "pm10_title": "PM10 (स्थूल इनहेलेबल धूल)",
            "no2_title": "NO2 (वाहन दहन)",
            "so2_title": "SO2 (औद्योगिक उत्सर्जन)",
            "temperature_title": "परिवेशी तापमान",
            "humidity_title": "सापेक्ष आर्द्रता",
            "live_calc": "लाइव मॉडल गणना",
            "temp_hint": "ठंडी हवा सर्दियों में सतह पर प्रदूषण को रोकती है",
            "humidity_hint": "अधिक नमी से घना स्मॉग और धुंध बनती है",
            "vs_baseline": "बनाम आधारभूत"
        },
        "copilot": {
            "rag_title": "TF-IDF वेक्टर RAG साक्ष्य आधार",
            "sub_ms": "उप-मिलीसेकंड पुनर्प्राप्ति",
            "retrieved_source": "पुनर्प्राप्त ज्ञान स्रोत",
            "matched_excerpt": "सटीक मिलान किया गया चिकित्सीय नियम उद्धरण",
            "guardrails_verified": "अडैप्शन ब्लूप्रिंट मेडिकल सुरक्षा उपाय सत्यापित",
            "rule_1": "नियम १: सीपीसीबी एक्यूआई मानक अनुपालन (०-५००)",
            "rule_2": "नियम २: वैधानिक सीएक्यूएम ग्रैप निर्देश (चरण I-IV)",
            "rule_3": "नियम ३: शून्य अनधिकृत दवा निर्माण",
            "rule_4": "नियम ४: अनिवार्य आपातकालीन ट्रिगर (SpO2 < ९२%)",
            "rule_5": "नियम ५: प्रमाणित N95 और HEPA निस्पंदन अनिवार्यता",
            "er_warning": "SpO2 < ९२%: तत्काल आपातकालीन अस्पताल परिवहन आवश्यक!",
            "pulse_spo2": "पल्स SpO2:",
            "context_label": "संदर्भ:",
            "rule_count": "८,१८८ नियम",
            "profile_pediatric": "बाल अस्थमा (आयु ४–१२)",
            "profile_geriatric": "वृद्ध सीओपीडी (आयु ६०+)",
            "profile_worker": "आउटडोर गिग/डिलीवरी कार्यकर्ता",
            "profile_maternal": "मातृ एवं प्रसवपूर्व देखभाल",
            "profile_general": "सामान्य जनसंख्या"
        },
        "datasets": {
            "filter_grade_a": "ग्रेड ए (९.४+)",
            "filter_invented": "सिंथेटिक इन्वेंट",
            "filter_forge": "फोर्ज निष्कर्षित",
            "table_view": "तालिका दृश्य",
            "protocol_view": "प्रोटोकॉल कार्ड दृश्य",
            "close_drawer": "दराज बंद करें",
            "samples_header": "संश्लेषित और निष्कर्षित वास्तविक पंक्तियाँ",
            "prompt_context": "मौसम विज्ञान / नैदानिक संदर्भ:",
            "protocol_truth": "नैदानिक प्रतिक्रिया प्रोटोकॉल / वास्तविक साक्ष्य:",
            "copy_id_title": "पूर्ण अडैप्शन डेटासेट आईडी कॉपी करें"
        },
        "jury": {
            "quality_grade_card": "अडैप्शन गुणवत्ता ग्रेड",
            "autoscientist_gain_card": "ऑटो-साइंटिस्ट जीत दर",
            "predictive_fit_card": "एमएल पूर्वानुमान सटीकता",
            "credit_reserve_card": "एसडीके क्रेडिट रिज़र्व",
            "top_percentile": "वैश्विक स्तर पर शीर्ष ३३वां प्रतिशतक",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (३ पुनरावृत्तियां)",
            "mae_subtitle": "औसत त्रुटि ±१.८८ दैनिक प्रवेश",
            "buffer_retained": "सत्यापित >४०० क्रेडिट बफर सुरक्षित",
            "verification_command_title": "जूरी के लिए प्रत्यक्ष अडैप्शन एसडीके सत्यापन कमांड",
            "copy_command": "कमांड कॉपी करें"
        }
    },

    "mr": {
        "chrome": {
            "footer_desc": "क्लिनिकल हवा गुणवत्ता व श्वसन रोग पाळत मोनोरेपो",
            "footer_adaption": "अडॅप्शन लॅब्स प्रमाणित",
            "rules_count": "८,१८८ नियम",
            "live_model_calc": "थेट मॉडेल गणना"
        },
        "overview": {
            "insight_years": "१०-वार्षिक कल: शहरी पट्ट्यात PM2.5 मध्ये दरवर्षी +४.२% वाढ.",
            "insight_quarters": "हंगामी त्रैमासिक विश्लेषण: Q4 (हिवाळी धुरके) मान्सूनपेक्षा ३.४ पट जास्त.",
            "insight_months": "हिवाळी इनव्हर्जन उच्चांक: नोव्हेंबर-जानेवारीत रुग्णालयात भरतीत +२४०% वाढ.",
            "insight_weeks": "साप्ताहिक वाढ: शेतातील धुरानंतरच्या आठवड्यात आयसीयू प्रवेशात वाढ.",
            "insight_live": "थेट ७-दिवसीय चक्र: सीपीसीबी केंद्रांशी थेट सहसंबंध.",
            "r2_precision": "एमएल R² = ०.९८७९",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 एकाग्रता (सूक्ष्म श्वसनीय धूर)",
            "pm10_title": "PM10 (स्थूल इनहेलेबल धूळ)",
            "no2_title": "NO2 (वाहनांचे ज्वलन)",
            "so2_title": "SO2 (औद्योगिक उत्सर्जन)",
            "temperature_title": "सभोवतालचे तापमान",
            "humidity_title": "सापेक्ष आर्द्रता",
            "live_calc": "थेट मॉडेल गणना",
            "temp_hint": "थंड हवा हिवाळ्यात पृष्ठभागावर प्रदूषण अडकवून ठेवते",
            "humidity_hint": "जास्त आर्द्रतेमुळे दाट धुके आणि धूर तयार होतो",
            "vs_baseline": "तुलनेत मूळ प्रमाण"
        },
        "copilot": {
            "rag_title": "TF-IDF व्हेक्टर RAG पुरावा आधार",
            "sub_ms": "उप-मिलीसेकंद पुनर्प्राप्ती",
            "retrieved_source": "पुनर्प्राप्त ज्ञान स्रोत",
            "matched_excerpt": "अचूक जुळलेला वैद्यकीय नियम उतारा",
            "guardrails_verified": "अडॅप्शन ब्लूप्रिंट वैद्यकीय सुरक्षा नियम प्रमाणित",
            "rule_1": "नियम १: सीपीसीबी एक्यूआय मानक अनुपालन (०-५००)",
            "rule_2": "नियम २: वैधानिक सीएक्यूएम ग्रॅप निर्देश (टप्पा I-IV)",
            "rule_3": "नियम ३: शून्य औषधोपचार कल्पितता",
            "rule_4": "नियम ४: अनिवार्य आणीबाणी ट्रिगर (SpO2 < ९२%)",
            "rule_5": "नियम ५: प्रमाणित N95 व HEPA फिल्टर वापरणे अनिवार्य",
            "er_warning": "SpO2 < ९२%: त्वरित आपत्कालीन रुग्णालय ट्रान्सपोर्ट आवश्यक!",
            "pulse_spo2": "पल्स SpO2:",
            "context_label": "संदर्भ:",
            "rule_count": "८,१८८ नियम",
            "profile_pediatric": "बाल दमा (वय ४–१२)",
            "profile_geriatric": "ज्येष्ठ सीओपीडी (वय ६०+)",
            "profile_worker": "आउटडोअर गिग/डिलिव्हरी कामगार",
            "profile_maternal": "मातृ आणि प्रसूतीपूर्व काळजी",
            "profile_general": "सामान्य लोकसंख्या"
        },
        "datasets": {
            "filter_grade_a": "ग्रेड ए (९.४+)",
            "filter_invented": "सिंथेटिक इन्व्हेंट",
            "filter_forge": "फोर्ज काढलेले",
            "table_view": "तक्ता दृश्य",
            "protocol_view": "प्रोटोकॉल कार्ड दृश्य",
            "close_drawer": "बंद करा",
            "samples_header": "संश्लेषित आणि काढलेल्या मूळ ओळी",
            "prompt_context": "हवामान / क्लिनिकल संदर्भ:",
            "protocol_truth": "क्लिनिकल प्रतिसाद प्रोटोकॉल / मूळ सत्य:",
            "copy_id_title": "पूर्ण अडॅप्शन डेटासेट आयडी कॉपी करा"
        },
        "jury": {
            "quality_grade_card": "अडॅप्शन गुणवत्ता ग्रेड",
            "autoscientist_gain_card": "ऑटो-सायंटिस्ट विजय दर",
            "predictive_fit_card": "एमएल अंदाज तंदुरुस्ती",
            "credit_reserve_card": "एसडीके क्रेडिट राखीव",
            "top_percentile": "जागतिक स्तरावर शीर्ष ३३ वे पर्सेंटाइल",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (३ पुनरावृत्ती)",
            "mae_subtitle": "सरासरी त्रुटी ±१.८८ दैनिक प्रवेश",
            "buffer_retained": "प्रमाणित >४०० क्रेडिट राखीव",
            "verification_command_title": "ज्युरीसाठी थेट अडॅप्शन एसडीके पडताळणी आज्ञा",
            "copy_command": "कमांड कॉपी करा"
        }
    },

    "bn": {
        "chrome": {
            "footer_desc": "ক্লিনিক্যাল বায়ু মান ও শ্বাসযন্ত্রের রোগ নজরদারি মনোরেপো",
            "footer_adaption": "অ্যাডাপশন ল্যাবস দ্বারা সমর্থিত",
            "rules_count": "৮,১৮৮ নিয়ম",
            "live_model_calc": "লাইভ মডেল গণনা"
        },
        "overview": {
            "insight_years": "১০ বছরের প্রবণতা: শহরাঞ্চলে PM2.5 প্রতি বছর +৪.২% বৃদ্ধি।",
            "insight_quarters": "ত্রৈমাসিক বিশ্লেষণ: Q4 (শীতকালীন ধোঁয়াশা) বর্ষার তুলনায় ৩.৪ গুণ বেশি।",
            "insight_months": "শীতকালীন ইনভার্সন শীর্ষ: নভেম্বর-জানুয়ারিতে হাসপাতালে ভর্তির সংখ্যা +২৪০% বৃদ্ধি।",
            "insight_weeks": "সাপ্তাহিক স্পাইক: খড় পোড়ানোর পরের সপ্তাহগুলিতে আইসিইউ ভর্তি বৃদ্ধি পায়।",
            "insight_live": "লাইভ ৭-দিনের চক্র: সিপিসিবি স্টেশনের সাথে রিয়েল-টাইম সম্পর্ক।",
            "r2_precision": "এমএল R² = ০.৯৮৭৯",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 ঘনত্ব (সূক্ষ্ম শ্বাসযোগ্য ধোঁয়াশা)",
            "pm10_title": "PM10 (স্থূল শ্বাসযোগ্য ধূলিকণা)",
            "no2_title": "NO2 (যানবাহন নির্গমন)",
            "so2_title": "SO2 (শিল্প নির্গমন)",
            "temperature_title": "পরিবেষ্টনকারী তাপমাত্রা",
            "humidity_title": "আপেক্ষিক আর্দ্রতা",
            "live_calc": "লাইভ মডেল গণনা",
            "temp_hint": "ঠান্ডা বাতাস শীতকালে ভূপৃষ্ঠের দূষণ আটকে রাখে",
            "humidity_hint": "উচ্চ আর্দ্রতায় ঘন ধোঁয়াশা তৈরি হয়",
            "vs_baseline": "বনাম বেসলাইন"
        },
        "copilot": {
            "rag_title": "TF-IDF ভেক্টর RAG প্রমাণ ভিত্তি",
            "sub_ms": "সাব-মিলিসেকেন্ড পুনরুদ্ধার",
            "retrieved_source": "পুনরুদ্ধার করা জ্ঞান উৎস",
            "matched_excerpt": "সঠিক মিলে যাওয়া ক্লিনিক্যাল নিয়ম উদ্ধৃতি",
            "guardrails_verified": "অ্যাডাপশন ব্লুপ্রিন্ট চিকিৎসা সুরক্ষা নিয়ম যাচাইকৃত",
            "rule_1": "নিয়ম ১: সিপিসিবি AQI মানদণ্ড মেনে চলা (০-৫০০)",
            "rule_2": "নিয়ম ২: সংবিধিবদ্ধ সিএকিউএম GRAP নির্দেশিকা (পর্যায় I-IV)",
            "rule_3": "নিয়ম ৩: শূন্য কাল্পনিক প্রেসক্রিপশন",
            "rule_4": "নিয়ম ৪: বাধ্যতামূলক জরুরি ট্রিপ (SpO2 < ৯২%)",
            "rule_5": "নিয়ম ৫: প্রত্যয়িত N95 এবং HEPA ফিল্টারিং বাধ্যতামূলক",
            "er_warning": "SpO2 < ৯২%: অবিলম্বে জরুরি হাসপাতালে স্থানান্তর প্রয়োজন!",
            "pulse_spo2": "পালস SpO2:",
            "context_label": "প্রসঙ্গ:",
            "rule_count": "৮,১৮৮ নিয়ম",
            "profile_pediatric": "শিশুদের হাঁপানি (বয়স ৪–১২)",
            "profile_geriatric": "বয়স্ক সিওপিডি (বয়স ৬০+)",
            "profile_worker": "আউটডোর গিগ/ডেলিভারি কর্মী",
            "profile_maternal": "মাতৃ ও প্রসবপূর্ব যত্ন",
            "profile_general": "সাধারণ জনসংখ্যা"
        },
        "datasets": {
            "filter_grade_a": "গ্রেড এ (৯.৪+)",
            "filter_invented": "সিন্থেটিক ইনভেন্ট",
            "filter_forge": "ফোর্জ নিষ্কাশিত",
            "table_view": "টেবিল ভিউ",
            "protocol_view": "প্রোটোকল কার্ড ভিউ",
            "close_drawer": "বন্ধ করুন",
            "samples_header": "সংশ্লেষিত এবং নিষ্কাশিত সত্য সারি",
            "prompt_context": "আবহাওয়া / ক্লিনিক্যাল প্রেক্ষাপট:",
            "protocol_truth": "ক্লিনিক্যাল প্রতিক্রিয়া প্রোটোকল / আসল প্রমাণ:",
            "copy_id_title": "সম্পূর্ণ অ্যাডাপশন ডেটাসেট আইডি কপি করুন"
        },
        "jury": {
            "quality_grade_card": "অ্যাডাপশন কোয়ালিটি গ্রেড",
            "autoscientist_gain_card": "অটো-সায়েন্টিস্ট জয়ের হার",
            "predictive_fit_card": "এমএল পূর্বাভাসের যথার্থতা",
            "credit_reserve_card": "এসডিকে ক্রেডিট রিজার্ভ",
            "top_percentile": "বিশ্বব্যাপী শীর্ষ ৩৩তম পার্সেন্টাইল",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (৩টি পুনরাবৃত্তি)",
            "mae_subtitle": "গড় ত্রুটি ±১.৮৮ দৈনিক ভর্তি",
            "buffer_retained": "যাচাইকৃত >৪০০ ক্রেডিট সংরক্ষিত",
            "verification_command_title": "জুরির জন্য সরাসরি অ্যাডাপশন এসডিকে যাচাই কমান্ড",
            "copy_command": "কমান্ড কপি করুন"
        }
    },

    "ta": {
        "chrome": {
            "footer_desc": "மருத்துவக் காற்றுத் தரம் மற்றும் சுவாச நோய் கண்காணிப்பு களஞ்சியம்",
            "footer_adaption": "அடாப்ஷன் லேப்ஸ் ஆதரவுடன்",
            "rules_count": "8,188 விதிகள்",
            "live_model_calc": "நேரலை மாதிரி கணக்கீடு"
        },
        "overview": {
            "insight_years": "10 ஆண்டு போக்கு: நகர்ப்புறங்களில் PM2.5 ஆண்டுக்கு +4.2% கூட்டு வளர்ச்சி.",
            "insight_quarters": "பருவகால காலாண்டு பகுப்பாய்வு: Q4 (குளிர்கால புகைப்பனி) பருவமழையை விட 3.4 மடங்கு அதிகம்.",
            "insight_months": "குளிர்கால தலைகீழ் உச்சம்: நவம்பர்-ஜனவரியில் மருத்துவமனை சேர்க்கை +240% அதிகரிக்கிறது.",
            "insight_weeks": "வாராந்திர எழுச்சி: பயிர் எரிப்புக்குப் பிந்தைய வாரங்களில் தீவிர சுவாச அவசரநிலைகள்.",
            "insight_live": "நேரலை 7-நாள் சுழற்சி: CPCB நிலையங்களுடன் நிகழ்நேர தொடர்பு.",
            "r2_precision": "ML R² = 0.9879",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 செறிவு (நுண்ணிய சுவாச புகைப்பனி)",
            "pm10_title": "PM10 (சுவாசிக்கக்கூடிய தூசி)",
            "no2_title": "NO2 (வாகன எரிப்பு)",
            "so2_title": "SO2 (தொழில்துறை உமிழ்வு)",
            "temperature_title": "சுற்றுப்புற வெப்பநிலை",
            "humidity_title": "ஒப்பீட்டு ஈரப்பதம்",
            "live_calc": "நேரலை மாதிரி கணக்கீடு",
            "temp_hint": "குளிர்ந்த காற்று குளிர்காலத்தில் மாசுபாட்டைத் தரைமட்டத்தில் பிடித்து வைக்கிறது",
            "humidity_hint": "அதிக ஈரப்பதம் அடர்த்தியான புகைமூட்டத்தை உருவாக்குகிறது",
            "vs_baseline": "அடிப்படையுடன் ஒப்பிடுகையில்"
        },
        "copilot": {
            "rag_title": "TF-IDF வெக்டர் RAG ஆதார அடிப்படை",
            "sub_ms": "மில்லிசெகண்டுக்கும் குறைவான மீட்டெடுப்பு",
            "retrieved_source": "மீட்டெடுக்கப்பட்ட அறிவு மூலம்",
            "matched_excerpt": "துல்லியமாக பொருந்தும் மருத்துவ விதி பகுதி",
            "guardrails_verified": "அடாப்ஷன் வரைபட மருத்துவ பாதுகாப்பு விதிகள் சரிபார்க்கப்பட்டன",
            "rule_1": "விதி 1: CPCB AQI தரநிலை இணக்கம் (0-500)",
            "rule_2": "விதி 2: சட்டப்பூர்வ CAQM GRAP வழிகாட்டுதல்கள் (நிலை I-IV)",
            "rule_3": "விதி 3: போலியான மருந்துக் குறிப்புகள் முற்றிலும் இல்லை",
            "rule_4": "விதி 4: கட்டாய அவசர சிகிச்சை தூண்டுதல் (SpO2 < 92%)",
            "rule_5": "விதி 5: சான்றளிக்கப்பட்ட N95 மற்றும் HEPA வடிகட்டுதல் கட்டாயம்",
            "er_warning": "SpO2 < 92%: உடனடி அவசர சிகிச்சை மருத்துவமனை போக்குவரத்து தேவை!",
            "pulse_spo2": "துடிப்பு SpO2:",
            "context_label": "சூழல்:",
            "rule_count": "8,188 விதிகள்",
            "profile_pediatric": "குழந்தைகள் ஆஸ்துமா (வயது 4–12)",
            "profile_geriatric": "முதியோர் சிஓபிடி (வயது 60+)",
            "profile_worker": "வெளிப்புற டெலிவரி தொழிலாளர்கள்",
            "profile_maternal": "தாய்மை மற்றும் மகப்பேறுக்கு முந்தைய பராமரிப்பு",
            "profile_general": "பொது மக்கள்"
        },
        "datasets": {
            "filter_grade_a": "தரம் A (9.4+)",
            "filter_invented": "செயற்கை உருவாக்கம்",
            "filter_forge": "ஃபோர்ஜ் பிரித்தெடுக்கப்பட்டது",
            "table_view": "அட்டவணை காட்சி",
            "protocol_view": "நெறிமுறை அட்டை காட்சி",
            "close_drawer": "மூடு",
            "samples_header": "உருவாக்கப்பட்ட மற்றும் பிரித்தெடுக்கப்பட்ட உண்மை வரிசைகள்",
            "prompt_context": "வானிலை / மருத்துவ சூழல்:",
            "protocol_truth": "மருத்துவ பதில் நெறிமுறை / உண்மை ஆதாரம்:",
            "copy_id_title": "முழு அடாப்ஷன் தரவுத்தொகுப்பு ஐடியை நகலெடுக்கவும்"
        },
        "jury": {
            "quality_grade_card": "அடாப்ஷன் தர மதிப்பீடு",
            "autoscientist_gain_card": "ஆட்டோ-சயின்டிஸ்ட் வெற்றி விகிதம்",
            "predictive_fit_card": "ML முன்கணிப்பு துல்லியம்",
            "credit_reserve_card": "SDK கிரெடிட் இருப்பு",
            "top_percentile": "உலகளவில் முதல் 33வது சதவீதம்",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (3 சுற்றுகள்)",
            "mae_subtitle": "சராசரி பிழை ±1.88 தினசரி சேர்க்கைகள்",
            "buffer_retained": "சரிபார்க்கப்பட்டது: >400 கிரெடிட்கள் கையிருப்பில்",
            "verification_command_title": "நடுவர்களுக்கான நேரடி அடாப்ஷன் SDK சரிபார்ப்பு கட்டளை",
            "copy_command": "கட்டளையை நகலெடு"
        }
    },

    "te": {
        "chrome": {
            "footer_desc": "క్లినికల్ గాలి నాణ్యత మరియు శ్వాసకోశ వ్యాధుల నిఘా మోనోరెపో",
            "footer_adaption": "అడాప్షన్ ల్యాబ్స్ ద్వారా ఆధారితం",
            "rules_count": "8,188 నియమాలు",
            "live_model_calc": "లైవ్ మోడల్ లెక్కింపు"
        },
        "overview": {
            "insight_years": "10 సంవత్సరాల ధోరణి: నగరాల్లో PM2.5 ఏటా +4.2% పెరుగుతోంది.",
            "insight_quarters": "త్రైమాసిక విశ్లేషణ: Q4 (శీతాకాల పొగమంచు) వర్షాకాలం కంటే 3.4 రెట్లు ఎక్కువ.",
            "insight_months": "శీతాకాల ఇన్వర్షన్ గరిష్టం: నవంబర్-జనవరిలో ఆసుపత్రి చేరికలు +240% పెరుగుతాయి.",
            "insight_weeks": "వారపు పెరుగుదల: పంట వ్యర్థాల దహనం తర్వాత ఐసీయూ శ్వాసకోశ చేరికలు తీవ్రమవుతాయి.",
            "insight_live": "లైవ్ 7-రోజుల చక్రం: CPCB కేంద్రాలతో నిజ-సమయ సహసంబంధం.",
            "r2_precision": "ML R² = 0.9879",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 సాంద్రత (సూక్ష్మ శ్వాసకోశ పొగమంచు)",
            "pm10_title": "PM10 (పీల్చదగిన ధూళి)",
            "no2_title": "NO2 (వాహనాల దహనం)",
            "so2_title": "SO2 (పారిశ్రామిక ఉద్గారాలు)",
            "temperature_title": "పరిసర ఉష్ణోగ్రత",
            "humidity_title": "సాపేక్ష ఆర్ద్రత",
            "live_calc": "లైవ్ మోడల్ లెక్కింపు",
            "temp_hint": "చల్లని గాలి శీతాకాలంలో కాలుష్యాన్ని భూమిపైనే బంధిస్తుంది",
            "humidity_hint": "ఎక్కువ తేమ దట్టమైన పొగమంచును ఏర్పరుస్తుంది",
            "vs_baseline": "బేస్లైన్తో పోలిస్తే"
        },
        "copilot": {
            "rag_title": "TF-IDF వెక్టర్ RAG ఆధార బలం",
            "sub_ms": "సబ్-మిల్లీసెకన్ శోధన",
            "retrieved_source": "సేకరించిన జ్ఞాన మూలం",
            "matched_excerpt": "సరిపోలిన ఖచ్చితమైన క్లినికల్ నియమ సారాంశం",
            "guardrails_verified": "అడాప్షన్ బ్లూప్రింట్ వైద్య రక్షణ నియమాలు ధృవీకరించబడ్డాయి",
            "rule_1": "నియమం 1: CPCB AQI ప్రమాణాల పాటించటం (0-500)",
            "rule_2": "నియమం 2: చట్టబద్ధమైన CAQM GRAP ఆదేశాలు (దశ I-IV)",
            "rule_3": "నియమం 3: ఊహాత్మక ప్రిస్క్రిప్షన్లు సున్నా",
            "rule_4": "నియమం 4: తప్పనిసరి అత్యవసర ట్రిగ్గర్ (SpO2 < 92%)",
            "rule_5": "నియమం 5: సర్టిఫైడ్ N95 మరియు HEPA ఫిల్టరింగ్ తప్పనిసరి",
            "er_warning": "SpO2 < 92%: తక్షణ అత్యవసర ఆసుపత్రి రవాణా అవసరం!",
            "pulse_spo2": "పల్స్ SpO2:",
            "context_label": "సందర్భం:",
            "rule_count": "8,188 నియమాలు",
            "profile_pediatric": "పిల్లల ఆస్తమా (వయస్సు 4–12)",
            "profile_geriatric": "వృద్ధుల సిఓపిడి (వయస్సు 60+)",
            "profile_worker": "బహిరంగ డెలివరీ కార్మికులు",
            "profile_maternal": "మాతృ మరియు ప్రసవపూర్వ సంరక్షణ",
            "profile_general": "సాధారణ జనాభా"
        },
        "datasets": {
            "filter_grade_a": "గ్రేడ్ A (9.4+)",
            "filter_invented": "సింథటిక్ ఇన్వెంట్",
            "filter_forge": "ఫోర్జ్ ఎక్స్ట్రాక్ట్",
            "table_view": "టేబుల్ వీక్షణ",
            "protocol_view": "ప్రోటోకాల్ కార్డ్ వీక్షణ",
            "close_drawer": "మూసివేయి",
            "samples_header": "సంశ్లేషణ చేయబడిన మరియు సేకరించబడిన వాస్తవ వరుసలు",
            "prompt_context": "వాతావరణ / క్లినికల్ సందర్భం:",
            "protocol_truth": "క్లినికల్ ప్రతిస్పందన ప్రోటోకాల్ / వాస్తవ ఆధారం:",
            "copy_id_title": "పూర్తి అడాప్షన్ డేటాసెట్ ఐడీని కాపీ చేయండి"
        },
        "jury": {
            "quality_grade_card": "అడాప్షన్ నాణ్యత గ్రేడ్",
            "autoscientist_gain_card": "ఆటో-సైంటిస్ట్ గెలుపు రేటు",
            "predictive_fit_card": "ML అంచనా ఖచ్చితత్వం",
            "credit_reserve_card": "SDK క్రెడిట్ రిజర్వ్",
            "top_percentile": "ప్రపంచవ్యాప్తంగా టాప్ 33వ పర్సంటైల్",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (3 పునరావృత్తులు)",
            "mae_subtitle": "సగటు లోపం ±1.88 రోజువారీ చేరికలు",
            "buffer_retained": "ధృవీకరించబడింది: >400 క్రెడిట్ల రిజర్వ్ భద్రం",
            "verification_command_title": "జ్యూరీ కోసం ప్రత్యక్ష అడాప్షన్ SDK ధృవీకరణ ఆదేశం",
            "copy_command": "కమాండ్ కాపీ చేయండి"
        }
    },

    "ur": {
        "chrome": {
            "footer_desc": "کلینیکل ہوا کے معیار اور تنفسی امراض کی نگرانی مونو ریپو",
            "footer_adaption": "اڈاپشن لیبز کے زیرِ اہتمام",
            "rules_count": "۸،۱۸۸ قواعد",
            "live_model_calc": "لائیو ماڈل کیلکولیشن"
        },
        "overview": {
            "insight_years": "۱۰ سالہ رجحان: شہری راہداریوں میں PM2.5 سالانہ +۴.۲٪ بڑھ رہا ہے۔",
            "insight_quarters": "موسمی سہ ماہی تجزیہ: Q4 (موسم سرما کا سموگ) مانسون سے ۳.۴ گنا زیادہ ہے۔",
            "insight_months": "موسم سرما میں الٹ پلٹ کا عروج: نومبر تا جنوری ہسپتال میں داخلوں میں +۲۴۰٪ اضافہ۔",
            "insight_weeks": "ہفتہ وار اضافہ: فصلوں کی باقیات جلانے کے بعد آئی سی یو تنفسی داخلوں میں شدت۔",
            "insight_live": "لائیو ۷ روزہ چکر: سی پی سی بی اسٹیشنوں کے ساتھ حقیقی وقت کا تعلق۔",
            "r2_precision": "ایم ایل R² = ۰.۹۸۷۹",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 ارتکاز (باریک سانس لینے کے قابل سموگ)",
            "pm10_title": "PM10 (موٹی سانس کے ذریعے اندر جانے والی دھول)",
            "no2_title": "NO2 (گاڑیوں کا دھواں)",
            "so2_title": "SO2 (صنعتی اخراج)",
            "temperature_title": "محیط درجہ حرارت",
            "humidity_title": "اضافی نمی",
            "live_calc": "لائیو ماڈل کیلکولیشن",
            "temp_hint": "سرد ہوا موسم سرما میں آلودگی کو زمین کے قریب قید رکھتی ہے",
            "humidity_hint": "زیادہ نمی گھنے سموگ کا باعث بنتی ہے",
            "vs_baseline": "بمقابلہ بنیادی شرح"
        },
        "copilot": {
            "rag_title": "TF-IDF ویکٹر RAG ثبوتی بنیاد",
            "sub_ms": "سب ملی سیکنڈ بازیافت",
            "retrieved_source": "حاصل کردہ علمی ذریعہ",
            "matched_excerpt": "ہوبہو مطابقت پذیر کلینیکل اصول کا اقتباس",
            "guardrails_verified": "اڈاپشن بلیو پرنٹ طبی حفاظتی اقدامات کی تصدیق شدہ",
            "rule_1": "قاعدہ ۱: سی پی سی بی AQI معیارات کی تعمیل (۰-۵۰۰)",
            "rule_2": "قاعدہ ۲: قانونی CAQM GRAP ہدایات (مرحلہ I-IV)",
            "rule_3": "قاعدہ ۳: ادویات کے خود ساختہ نسخوں کی مکمل ممانعت",
            "rule_4": "قاعدہ ۴: لازمی ہنگامی انتباہ (SpO2 < ۹۲٪)",
            "rule_5": "قاعدہ ۵: تصدیق شدہ N95 اور HEPA فلٹریشن لازمی",
            "er_warning": "SpO2 < ۹۲٪: فوری طور پر ہنگامی ہسپتال منتقلی درکار ہے!",
            "pulse_spo2": "نبض SpO2:",
            "context_label": "سیاق و سباق:",
            "rule_count": "۸،۱۸۸ قواعد",
            "profile_pediatric": "بچوں کا دمہ (عمر ۴–۱۲)",
            "profile_geriatric": "بزرگ سی او پی ڈی (عمر ۶۰+)",
            "profile_worker": "بیرونی ڈیلیوری ورکرز",
            "profile_maternal": "زچگی اور قبل از پیدائش دیکھ بھال",
            "profile_general": "عام آبادی"
        },
        "datasets": {
            "filter_grade_a": "گریڈ اے (۹.۴+)",
            "filter_invented": "مصنوعی تخلیق",
            "filter_forge": "فوج سے نکالا گیا",
            "table_view": "ٹیبل ویو",
            "protocol_view": "پروٹوکول کارڈ ویو",
            "close_drawer": "بند کریں",
            "samples_header": "ترکیب شدہ اور نکالی گئی حقیقی قطاریں",
            "prompt_context": "موسمیاتی / کلینیکل سیاق و سباق:",
            "protocol_truth": "کلینیکل رسپانس پروٹوکول / اصل حقائق:",
            "copy_id_title": "مکمل اڈاپشن ڈیٹا سیٹ آئی ڈی کاپی کریں"
        },
        "jury": {
            "quality_grade_card": "اڈاپشن کوالٹی گریڈ",
            "autoscientist_gain_card": "آٹو سائنٹسٹ جیت کی شرح",
            "predictive_fit_card": "ایم ایل پیشین گوئی کی درستگی",
            "credit_reserve_card": "ایس ڈی کے کریڈٹ ریزرو",
            "top_percentile": "عالمی سطح پر ٹاپ ۳۳واں پرسنٹائل",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (۳ تکرار)",
            "mae_subtitle": "اوسط غلطی ±۱.۸۸ روزانہ داخلے",
            "buffer_retained": "تصدیق شدہ: >۴۰۰ کریڈٹ بفر محفوظ",
            "verification_command_title": "جیوری کے لیے براہ راست اڈاپشن SDK تصدیقی کمانڈ",
            "copy_command": "کمانڈ کاپی کریں"
        }
    },

    "kn": {
        "chrome": {
            "footer_desc": "ಕ್ಲಿನಿಕಲ್ ವಾಯು ಗುಣಮಟ್ಟ ಮತ್ತು ಉಸಿರಾಟದ ಕಾಯಿಲೆಗಳ ಕಣ್ಗಾವಲು ಮೊನೊರೆಪೋ",
            "footer_adaption": "ಅಡಾಪ್ಟನ್ ಲ್ಯಾಬ್ಸ್ ಆಧಾರಿತ",
            "rules_count": "೮,೧೮೮ ನಿಯಮಗಳು",
            "live_model_calc": "ಲೈವ್ ಮಾದರಿ ಲೆಕ್ಕಾಚಾರ"
        },
        "overview": {
            "insight_years": "೧೦-ವರ್ಷಗಳ ಪ್ರವೃತ್ತಿ: ನಗರಗಳಲ್ಲಿ PM2.5 ವಾರ್ಷಿಕ +೪.೨% ಹೆಚ್ಚಳ.",
            "insight_quarters": "ತ್ರೈಮಾಸಿಕ ವಿಶ್ಲೇಷಣೆ: Q4 (ಚಳಿಗಾಲದ ಹೊಗೆ) ಮಾನ್ಸೂನ್‌ಗಿಂತ ೩.೪ ಪಟ್ಟು ಹೆಚ್ಚು.",
            "insight_months": "ಚಳಿಗಾಲದ ಇನ್ವರ್ಶನ್ ಗರಿಷ್ಠ: ನವೆಂಬರ್-ಜನವರಿಯಲ್ಲಿ ಆಸ್ಪತ್ರೆ ದಾಖಲಾತಿ +೨೪೦% ಏರಿಕೆ.",
            "insight_weeks": "ವಾರದ ಏರಿಕೆ: ಬೆಳೆ ಸುಡುವ ನಂತರದ ವಾರಗಳಲ್ಲಿ ತೀವ್ರ ಐಸಿಯು ದಾಖಲಾತಿ.",
            "insight_live": "ಲೈವ್ ೭-ದಿನಗಳ ಚಕ್ರ: CPCB ಕೇಂದ್ರಗಳೊಂದಿಗೆ ನೈಜ-ಸಮಯದ ಪರಸ್ಪರ ಸಂಬಂಧ.",
            "r2_precision": "ML R² = ೦.೯೮೭೯",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 ಸಾಂದ್ರತೆ (ಸೂಕ್ಷ್ಮ ಉಸಿರಾಟದ ಹೊಗೆ)",
            "pm10_title": "PM10 (ಉಸಿರಾಡಬಹುದಾದ ಧೂಳು)",
            "no2_title": "NO2 (ವಾಹನ ದಹನ)",
            "so2_title": "SO2 (ಕೈಗಾರಿಕಾ ಹೊರಸೂಸುವಿಕೆ)",
            "temperature_title": "ಪರಿಸರದ ತಾಪಮಾನ",
            "humidity_title": "ಸಾಪೇಕ್ಷ ಆರ್ದ್ರತೆ",
            "live_calc": "ಲೈವ್ ಮಾದರಿ ಲೆಕ್ಕಾಚಾರ",
            "temp_hint": "ತಂಪಾದ ಗಾಳಿ ಚಳಿಗಾಲದಲ್ಲಿ ಮಾಲಿನ್ಯವನ್ನು ನೆಲದ ಹತ್ತಿರವೇ ಹಿಡಿದಿಡುತ್ತದೆ",
            "humidity_hint": "ಹೆಚ್ಚಿನ ತೇವಾಂಶವು ದಟ್ಟವಾದ ಹೊಗೆಮಂಜನ್ನು ಉಂಟುಮಾಡುತ್ತದೆ",
            "vs_baseline": "ಮೂಲಕ್ಕೆ ಹೋಲಿಸಿದರೆ"
        },
        "copilot": {
            "rag_title": "TF-IDF ವೆಕ್ಟರ್ RAG ಪುರಾವೆ ಆಧಾರ",
            "sub_ms": "ಉಪ-ಮಿಲಿಸೆಕೆಂಡ್ ಮರುಪಡೆಯುವಿಕೆ",
            "retrieved_source": "ಮರುಪಡೆಯಲಾದ ಜ್ಞಾನ ಮೂಲ",
            "matched_excerpt": "ನಿಖರವಾಗಿ ಹೊಂದಾಣಿಕೆಯಾದ ಕ್ಲಿನಿಕಲ್ ನಿಯಮದ ಸಾರಾಂಶ",
            "guardrails_verified": "ಅಡಾಪ್ಟನ್ ವೈದ್ಯಕೀಯ ರಕ್ಷಣಾ ನಿಯಮಗಳನ್ನು ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "rule_1": "ನಿಯಮ ೧: CPCB AQI ಮಾನದಂಡ ಪಾಲನೆ (೦-೫೦೦)",
            "rule_2": "ನಿಯಮ ೨: ಶಾಸನಬದ್ಧ CAQM GRAP ನಿರ್ದೇಶನಗಳು (ಹಂತ I-IV)",
            "rule_3": "ನಿಯಮ ೩: ಯಾವುದೇ ಔಷಧಿ ಕಲ್ಪಿತ ಬರವಣಿಗೆ ಇಲ್ಲ",
            "rule_4": "ನಿಯಮ ೪: ಕಡ್ಡಾಯ ತುರ್ತು ಎಚ್ಚರಿಕೆ (SpO2 < ೯೨%)",
            "rule_5": "ನಿಯಮ ೫: ಪ್ರಮಾಣೀಕೃತ N95 ಮತ್ತು HEPA ಶೋಧನೆ ಕಡ್ಡಾಯ",
            "er_warning": "SpO2 < ೯೨%: ತಕ್ಷಣದ ತುರ್ತು ಆಸ್ಪತ್ರೆ ಸಾಗಣೆ ಅಗತ್ಯವಿದೆ!",
            "pulse_spo2": "ನಾಡಿ SpO2:",
            "context_label": "ಸಂದರ್ಭ:",
            "rule_count": "೮,೧೮೮ ನಿಯಮಗಳು",
            "profile_pediatric": "ಮಕ್ಕಳ ಆಸ್ತಮಾ (ವಯಸ್ಸು ೪–೧೨)",
            "profile_geriatric": "ಹಿರಿಯ ಸಿಒಪಿಡಿ (ವಯಸ್ಸು ೬೦+)",
            "profile_worker": "ಹೊರಾಂಗಣ ಡೆಲಿವರಿ ಕಾರ್ಮಿಕರು",
            "profile_maternal": "ತಾಯಂದಿರ ಮತ್ತು ಹೆರಿಗೆ ಪೂರ್ವ ಆರೈಕೆ",
            "profile_general": "ಸಾಮಾನ್ಯ ಜನಸಂಖ್ಯೆ"
        },
        "datasets": {
            "filter_grade_a": "ಗ್ರೇಡ್ ಎ (೯.೪+)",
            "filter_invented": "ಸಿಂಥೆಟಿಕ್ ಇನ್ವೆಂಟ್",
            "filter_forge": "ಫೋರ್ಜ್ ಹೊರತೆಗೆದ",
            "table_view": "ಕೋಷ್ಟಕ ವೀಕ್ಷಣೆ",
            "protocol_view": "ಪ್ರೋಟೋಕಾಲ್ ಕಾರ್ಡ್ ವೀಕ್ಷಣೆ",
            "close_drawer": "ಮುಚ್ಚಿ",
            "samples_header": "ಸಂಶ್ಲೇಷಿತ ಮತ್ತು ಹೊರತೆಗೆಯಲಾದ ನೈಜ ಸಾಲುಗಳು",
            "prompt_context": "ಹವಾಮಾನ / ಕ್ಲಿನಿಕಲ್ ಸಂದರ್ಭ:",
            "protocol_truth": "ಕ್ಲಿನಿಕಲ್ ಪ್ರತಿಕ್ರಿಯೆ ಪ್ರೋಟೋಕಾಲ್ / ನೈಜ ಪುರಾವೆ:",
            "copy_id_title": "ಸಂಪೂರ್ಣ ಅಡಾಪ್ಟನ್ ಡೇಟಾಸೆಟ್ ಐಡಿ ನಕಲಿಸಿ"
        },
        "jury": {
            "quality_grade_card": "ಅಡಾಪ್ಟನ್ ಗುಣಮಟ್ಟ ಗ್ರೇಡ್",
            "autoscientist_gain_card": "ಆಟೋ-ಸೈಂಟಿಸ್ಟ್ ಗೆಲುವಿನ ದರ",
            "predictive_fit_card": "ML ಮುನ್ಸೂಚನೆ ನಿಖರತೆ",
            "credit_reserve_card": "SDK ಕ್ರೆಡಿಟ್ ಮೀಸಲು",
            "top_percentile": "ಜಾಗತಿಕವಾಗಿ ಅಗ್ರ ೩೩ನೇ ಪರ್ಸೆಂಟೈಲ್",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (೩ ಪುನರಾವರ್ತನೆಗಳು)",
            "mae_subtitle": "ಸರಾಸರಿ ದೋಷ ±೧.೮೮ ದೈನಂದಿನ ದಾಖಲಾತಿಗಳು",
            "buffer_retained": "ಪರಿಶೀಲಿಸಲಾಗಿದೆ: >೪೦೦ ಕ್ರೆಡಿಟ್‌ಗಳು ಸುರಕ್ಷಿತವಾಗಿವೆ",
            "verification_command_title": "ಜ್ಯೂರಿಗಾಗಿ ನೇರ ಅಡಾಪ್ಟನ್ SDK ಪರಿಶೀಲನಾ ಆಜ್ಞೆ",
            "copy_command": "ಆಜ್ಞೆಯನ್ನು ನಕಲಿಸಿ"
        }
    },

    "ml": {
        "chrome": {
            "footer_desc": "ക്ലിനിക്കൽ വായു നിലവാരവും ശ്വാസകോശ രോഗ നിരീക്ഷണ കേന്ദ്രവും",
            "footer_adaption": "അഡാപ്ഷൻ ലാബ്സ് പിന്തുണയോടെ",
            "rules_count": "8,188 നിയമങ്ങൾ",
            "live_model_calc": "തത്സമയ മോഡൽ കണക്കുകൂട്ടൽ"
        },
        "overview": {
            "insight_years": "10 വർഷത്തെ പ്രവണത: നഗരങ്ങളിൽ PM2.5 വർഷം തോറും +4.2% വർദ്ധിക്കുന്നു.",
            "insight_quarters": "ത്രൈമാസ വിശകലനം: Q4 (ശൈത്യകാല പുകമഞ്ഞ്) മൺസൂണിനേക്കാൾ 3.4 മടങ്ങ് കൂടുതൽ.",
            "insight_months": "ശൈത്യകാല ഇൻവേർഷൻ പീക്ക്: നവംബർ-ജനുവരിയിൽ ആശുപത്രി പ്രവേശനം +240% വർദ്ധിക്കുന്നു.",
            "insight_weeks": "വാരാന്ത്യ സ്പൈക്ക്: കൃഷി അവശിഷ്ടങ്ങൾ കത്തിച്ചതിനു ശേഷമുള്ള ആഴ്ചകളിൽ ഐസിയു അഡ്മിഷൻ വർദ്ധനവ്.",
            "insight_live": "തത്സമയ 7-ദിവസ സൈക്കിൾ: CPCB സ്റ്റേഷനുകളുമായി തത്സമയ പരസ്പരബന്ധം.",
            "r2_precision": "ML R² = 0.9879",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 സാന്ദ്രത (ശ്വസനയോഗ്യമായ പുകമഞ്ഞ്)",
            "pm10_title": "PM10 (ശ്വസിക്കാവുന്ന പൊടിപടലങ്ങൾ)",
            "no2_title": "NO2 (വാഹന പുക)",
            "so2_title": "SO2 (വ്യാവസായിക ഉദ്വമനം)",
            "temperature_title": "അന്തരീക്ഷ താപനില",
            "humidity_title": "ആപേക്ഷിക ആർദ്രത",
            "live_calc": "തത്സമയ മോഡൽ കണക്കുകൂട്ടൽ",
            "temp_hint": "തണുത്ത വായു ശൈത്യകാലത്ത് മലിനീകരണത്തെ നിലത്തുതന്നെ തടഞ്ഞുനിർത്തുന്നു",
            "humidity_hint": "കൂടുതൽ ഈർപ്പം കട്ടിയുള്ള പുകമഞ്ഞിന് കാരണമാകുന്നു",
            "vs_baseline": "ബേസ്‌ലൈനുമായി താരതമ്യം ചെയ്യുമ്പോൾ"
        },
        "copilot": {
            "rag_title": "TF-IDF വെക്റ്റർ RAG തെളിവ് അടിത്തറ",
            "sub_ms": "സബ്-മില്ലിസെക്കൻഡ് വീണ്ടെടുക്കൽ",
            "retrieved_source": "വീണ്ടെടുത്ത വിജ്ഞാന ഉറവിടം",
            "matched_excerpt": "കൃത്യമായി പൊരുത്തപ്പെടുന്ന ക്ലിനിക്കൽ നിയമ ഉദ്ധരണി",
            "guardrails_verified": "അഡാപ്ഷൻ ബ്ലൂപ്രിന്റ് മെഡിക്കൽ സുരക്ഷാ നിയമങ്ങൾ പരിശോധിച്ചു",
            "rule_1": "നിയമം 1: CPCB AQI മാനദണ്ഡങ്ങൾ പാലിക്കൽ (0-500)",
            "rule_2": "നിയമം 2: നിയമാനുസൃത CAQM GRAP നിർദ്ദേശങ്ങൾ (ഘട്ടം I-IV)",
            "rule_3": "നിയമം 3: വ്യാജ കുറിപ്പടികൾ പൂർണ്ണമായി ഒഴിവാക്കൽ",
            "rule_4": "നിയമം 4: അടിയന്തിര ഹോസ്പിറ്റൽ ട്രിഗർ (SpO2 < 92%)",
            "rule_5": "നിയമം 5: സാക്ഷ്യപ്പെടുത്തിയ N95, HEPA ഫിൽട്ടറുകൾ നിർബന്ധം",
            "er_warning": "SpO2 < 92%: അടിയന്തിരമായി ആശുപത്രിയിലേക്ക് മാറ്റേണ്ടതുണ്ട്!",
            "pulse_spo2": "പൾസ് SpO2:",
            "context_label": "സന്ദർഭം:",
            "rule_count": "8,188 നിയമങ്ങൾ",
            "profile_pediatric": "കുട്ടികളിലെ ആസ്ത്മ (പ്രായം 4–12)",
            "profile_geriatric": "മുതിർന്നവരിലെ സിഒപിഡി (പ്രായം 60+)",
            "profile_worker": "ഡെലിവറി തൊഴിലാളികൾ",
            "profile_maternal": "മാതൃ-പ്രസവപൂർവ പരിചരണം",
            "profile_general": "സാധാരണ ജനങ്ങൾ"
        },
        "datasets": {
            "filter_grade_a": "ഗ്രേഡ് എ (9.4+)",
            "filter_invented": "സിന്തറ്റിക് ഇൻവെന്റ്",
            "filter_forge": "ഫോർജ് എക്‌സ്ട്രാക്റ്റുചെയ്‌തത്",
            "table_view": "പട്ടിക കാഴ്ച",
            "protocol_view": "പ്രോട്ടോക്കോൾ കാർഡ് കാഴ്ച",
            "close_drawer": "അടയ്ക്കുക",
            "samples_header": "സമാഹരിച്ചതും വേർതിരിച്ചതുമായ യഥാർത്ഥ വരികൾ",
            "prompt_context": "കാലാവസ്ഥ / ക്ലിനിക്കൽ പശ്ചാത്തലം:",
            "protocol_truth": "ക്ലിനിക്കൽ പ്രതികരണ പ്രോട്ടോക്കോൾ / യഥാർത്ഥ തെളിവ്:",
            "copy_id_title": "പൂർണ്ണ അഡാപ്ഷൻ ഡാറ്റാസെറ്റ് ഐഡി പകർത്തുക"
        },
        "jury": {
            "quality_grade_card": "അഡാപ്ഷൻ ഗുണനിലവാര ഗ്രേഡ്",
            "autoscientist_gain_card": "ഓട്ടോ-സയന്റിസ്റ്റ് വിജയ നിരക്ക്",
            "predictive_fit_card": "ML പ്രവചന കൃത്യത",
            "credit_reserve_card": "SDK ക്രെഡിറ്റ് കരുതൽ ധനം",
            "top_percentile": "ആഗോളതലത്തിൽ മികച്ച 33-ാം പെർസെന്റൈൽ",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (3 ആവർത്തനങ്ങൾ)",
            "mae_subtitle": "ശരാശരി പിശക് ±1.88 പ്രതിദിന അഡ്മിഷനുകൾ",
            "buffer_retained": "സ്ഥിരീകരിച്ചത്: >400 ക്രെഡിറ്റുകൾ കരുതൽ ശേഖരത്തിൽ",
            "verification_command_title": "ജൂറിക്കായുള്ള നേരിട്ടുള്ള അഡാപ്ഷൻ SDK സ്ഥിരീകരണ കമാൻഡ്",
            "copy_command": "കമാൻഡ് പകർത്തുക"
        }
    },

    "gu": {
        "chrome": {
            "footer_desc": "ક્લિનિકલ હવા ગુણવત્તા અને શ્વસન રોગ સર્વેલન્સ મોનોરેપો",
            "footer_adaption": "અડેપ્શન લેબ્સ આધારિત",
            "rules_count": "૮,૧૮૮ નિયમો",
            "live_model_calc": "લાઇવ મોડેલ ગણતરી"
        },
        "overview": {
            "insight_years": "૧૦-વર્ષનો ટ્રેન્ડ: શહેરી વિસ્તારોમાં PM2.5 માં વાર્ષિક +૪.૨% વધારો.",
            "insight_quarters": "મોસમી ત્રિમાસિક વિશ્લેષણ: Q4 (શિયાળુ સ્મોગ) ચોમાસા કરતાં ૩.૪ ગણું વધારે.",
            "insight_months": "શિયાળુ ઇન્વર્ઝન ટોચ: નવેમ્બર-જાન્યુઆરીમાં હોસ્પિટલ પ્રવેશમાં +૨૪૦% વધારો.",
            "insight_weeks": "સાપ્તાહિક વધારો: પરાળી સળગાવ્યા પછીના અઠવાડિયામાં આઈસીયુ શ્વસન કટોકટી.",
            "insight_live": "લાઇવ ૭-દિવસીય ચક્ર: સીપીસીબી સ્ટેશનો સાથે રીઅલ-ટાઇમ સંબંધ.",
            "r2_precision": "ML R² = ૦.૯૮૭૯",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 સાંદ્રતા (ઝીણો શ્વાસમાં જતો સ્મોગ)",
            "pm10_title": "PM10 (શ્વાસમાં જતી ધૂળ)",
            "no2_title": "NO2 (વાહનોનું ઉત્સર્જન)",
            "so2_title": "SO2 (ઔદ્યોગિક ઉત્સર્જન)",
            "temperature_title": "વાતાવરણનું તાપમાન",
            "humidity_title": "સાપેક્ષ ભેજ",
            "live_calc": "લાઇવ મોડેલ ગણતરી",
            "temp_hint": "ઠંડી હવા શિયાળામાં પ્રદૂષણને જમીન નજીક રોકી રાખે છે",
            "humidity_hint": "વધુ ભેજથી ગાઢ ધુમ્મસ અને સ્મોગ બને છે",
            "vs_baseline": "બેઝલાઇનની સરખામણીમાં"
        },
        "copilot": {
            "rag_title": "TF-IDF વેક્ટર RAG પુરાવા આધાર",
            "sub_ms": "સબ-મિલિસેકન્ડ પુનઃપ્રાપ્તિ",
            "retrieved_source": "પુનઃપ્રાપ્ત જ્ઞાન સ્ત્રોત",
            "matched_excerpt": "ચોક્કસ મેળ ખાતો ક્લિનિકલ નિયમનો અંશ",
            "guardrails_verified": "અડેપ્શન બ્લૂપ્રિન્ટ મેડિકલ સુરક્ષા નિયમો ચકાસાયેલ",
            "rule_1": "નિયમ ૧: સીપીસીબી AQI ધોરણોનું પાલન (૦-૫૦૦)",
            "rule_2": "નિયમ ૨: કાનૂની CAQM GRAP નિર્દેશો (તબક્કો I-IV)",
            "rule_3": "નિયમ ૩: કાલ્પનિક દવાઓ લખવાની સંપૂર્ણ મનાઈ",
            "rule_4": "નિયમ ૪: ફરજિયાત કટોકટી ચેતવણી (SpO2 < ૯૨%)",
            "rule_5": "નિયમ ૫: પ્રમાણિત N95 અને HEPA ફિલ્ટરેશન ફરજિયાત",
            "er_warning": "SpO2 < ૯૨%: તાત્કાલિક ઇમરજન્સી હોસ્પિટલ પરિવહન જરૂરી!",
            "pulse_spo2": "પલ્સ SpO2:",
            "context_label": "સંદર્ભ:",
            "rule_count": "૮,૧૮૮ નિયમો",
            "profile_pediatric": "બાળ અસ્થમા (ઉંમર ૪–૧૨)",
            "profile_geriatric": "વૃદ્ધ સીઓપીડી (ઉંમર ૬૦+)",
            "profile_worker": "આઉટડોર ડિલિવરી વર્કર્સ",
            "profile_maternal": "માતૃત્વ અને પૂર્વપ્રસૂતિ સંભાળ",
            "profile_general": "સામાન્ય વસ્તી"
        },
        "datasets": {
            "filter_grade_a": "ગ્રેડ એ (૯.૪+)",
            "filter_invented": "સિન્થેટિક ઇન્વેન્ટ",
            "filter_forge": "ફોર્જ નિષ્કર્ષિત",
            "table_view": "કોષ્ટક દૃશ્ય",
            "protocol_view": "પ્રોટોકોલ કાર્ડ દૃશ્ય",
            "close_drawer": "બંધ કરો",
            "samples_header": "સંશ્લેષિત અને કાઢવામાં આવેલી સત્ય પંક્તિઓ",
            "prompt_context": "હવામાન / ક્લિનિકલ સંદર્ભ:",
            "protocol_truth": "ક્લિનિકલ પ્રતિસાદ પ્રોટોકોલ / વાસ્તવિક પુરાવો:",
            "copy_id_title": "સંપૂર્ણ અડેપ્શન ડેટાસેટ આઈડી કોપી કરો"
        },
        "jury": {
            "quality_grade_card": "અડેપ્શન ગુણવત્તા ગ્રેડ",
            "autoscientist_gain_card": "ઓટો-સાયન્ટિસ્ટ જીતનો દર",
            "predictive_fit_card": "ML આગાહી ચોકસાઈ",
            "credit_reserve_card": "SDK ક્રેડિટ અનામત",
            "top_percentile": "વૈશ્વિક સ્તરે ટોચના ૩૩મા પર્સેન્ટાઇલ",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (૩ પુનરાવર્તનો)",
            "mae_subtitle": "સરેરાશ ભૂલ ±૧.૮૮ દૈનિક પ્રવેશ",
            "buffer_retained": "ચકાસાયેલ: >૪૦૦ ક્રેડિટ્સ અનામત સુરક્ષિત",
            "verification_command_title": "જ્યુરી માટે સીધો અડેપ્શન SDK ચકાસણી આદેશ",
            "copy_command": "આદેશ કોપી કરો"
        }
    },

    "pa": {
        "chrome": {
            "footer_desc": "ਕਲੀਨਿਕਲ ਹਵਾ ਗੁਣਵੱਤਾ ਅਤੇ ਸਾਹ ਦੀਆਂ ਬਿਮਾਰੀਆਂ ਦੀ ਨਿਗਰਾਨੀ ਮੋਨੋਰੇਪੋ",
            "footer_adaption": "ਅਡੈਪਸ਼ਨ ਲੈਬਜ਼ ਦੁਆਰਾ ਸੰਚਾਲਿਤ",
            "rules_count": "੮,੧੮੮ ਨਿਯਮ",
            "live_model_calc": "ਲਾਈਵ ਮਾਡਲ ਗਣਨਾ"
        },
        "overview": {
            "insight_years": "੧੦-ਸਾਲਾ ਰੁਝਾਨ: ਸ਼ਹਿਰੀ ਖੇਤਰਾਂ ਵਿੱਚ PM2.5 ਵਿੱਚ ਸਾਲਾਨਾ +੪.੨% ਵਾਧਾ।",
            "insight_quarters": "ਤਿਮਾਹੀ ਵਿਸ਼ਲੇਸ਼ਣ: Q4 (ਸਰਦੀਆਂ ਦਾ ਸਮੋਗ) ਮਾਨਸੂਨ ਨਾਲੋਂ ੩.੪ ਗੁਣਾ ਵੱਧ ਹੈ।",
            "insight_months": "ਸਰਦੀਆਂ ਦਾ ਸਿਖਰ: ਨਵੰਬਰ-ਜਨਵਰੀ ਵਿੱਚ ਹਸਪਤਾਲ ਦਾਖਲਿਆਂ ਵਿੱਚ +੨੪੦% ਵਾਧਾ।",
            "insight_weeks": "ਹਫ਼ਤਾਵਾਰੀ ਵਾਧਾ: ਪਰਾਲੀ ਸਾੜਨ ਤੋਂ ਬਾਅਦ ਦੇ ਹਫ਼ਤਿਆਂ ਵਿੱਚ ਆਈਸੀਯੂ ਸਾਹ ਸੰਕਟ।",
            "insight_live": "ਲਾਈਵ ੭-ਦਿਨਾਂ ਚੱਕਰ: ਸੀਪੀਸੀਬੀ ਸਟੇਸ਼ਨਾਂ ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਸਬੰਧ।",
            "r2_precision": "ML R² = ੦.੯੮੭੯",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 ਗਾੜ੍ਹਾਪਣ (ਬਰੀਕ ਸਾਹ ਲੈਣ ਯੋਗ ਸਮੋਗ)",
            "pm10_title": "PM10 (ਸਾਹ ਰਾਹੀਂ ਅੰਦਰ ਜਾਣ ਵਾਲੀ ਧੂੜ)",
            "no2_title": "NO2 (ਵਾਹਨਾਂ ਦਾ ਧੂੰਆਂ)",
            "so2_title": "SO2 (ਉਦਯੋਗਿਕ ਨਿਕਾਸ)",
            "temperature_title": "ਆਲੇ ਦੁਆਲੇ ਦਾ ਤਾਪਮਾਨ",
            "humidity_title": "ਨਮੀ ਦੀ ਦਰ",
            "live_calc": "ਲਾਈਵ ਮਾਡਲ ਗਣਨਾ",
            "temp_hint": "ਠੰਡੀ ਹਵਾ ਸਰਦੀਆਂ ਵਿੱਚ ਪ੍ਰਦੂਸ਼ਣ ਨੂੰ ਜ਼ਮੀਨ ਨੇੜੇ ਰੋਕਦੀ ਹੈ",
            "humidity_hint": "ਵੱਧ ਨਮੀ ਸੰਘਣਾ ਧੂੰਆਂ ਅਤੇ ਧੁੰਦ ਬਣਾਉਂਦੀ ਹੈ",
            "vs_baseline": "ਬੇਸਲਾਈਨ ਦੇ ਮੁਕਾਬਲੇ"
        },
        "copilot": {
            "rag_title": "TF-IDF ਵੈਕਟਰ RAG ਸਬੂਤ ਆਧਾਰ",
            "sub_ms": "ਸਬ-ਮਿਲੀਸਕਿੰਟ ਪ੍ਰਾਪਤੀ",
            "retrieved_source": "ਪ੍ਰਾਪਤ ਕੀਤਾ ਗਿਆ ਗਿਆਨ ਸਰੋਤ",
            "matched_excerpt": "ਸਹੀ ਮੇਲ ਖਾਂਦਾ ਕਲੀਨਿਕਲ ਨਿਯਮ",
            "guardrails_verified": "ਅਡੈਪਸ਼ਨ ਮੈਡੀਕਲ ਸੁਰੱਖਿਆ ਨਿਯਮ ਪ੍ਰਮਾਣਿਤ",
            "rule_1": "ਨਿਯਮ ੧: ਸੀਪੀਸੀਬੀ AQI ਮਾਪਦੰਡਾਂ ਦੀ ਪਾਲਣਾ (੦-੫੦੦)",
            "rule_2": "ਨਿਯਮ ੨: ਕਾਨੂੰਨੀ CAQM GRAP ਨਿਰਦੇਸ਼ (ਪੜਾਅ I-IV)",
            "rule_3": "ਨਿਯਮ ੩: ਮਨਘੜਤ ਦਵਾਈਆਂ ਲਿਖਣ ਦੀ ਪੂਰੀ ਮਨਾਹੀ",
            "rule_4": "ਨਿਯਮ ੪: ਲਾਜ਼ਮੀ ਐਮਰਜੈਂਸੀ ਚੇਤਾਵਨੀ (SpO2 < ੯੨%)",
            "rule_5": "ਨਿਯਮ ੫: ਪ੍ਰਮਾਣਿਤ N95 ਅਤੇ HEPA ਫਿਲਟਰ ਲਾਜ਼ਮੀ",
            "er_warning": "SpO2 < ੯੨%: ਤੁਰੰਤ ਐਮਰਜੈਂਸੀ ਹਸਪਤਾਲ ਲਿਜਾਣ ਦੀ ਲੋੜ ਹੈ!",
            "pulse_spo2": "ਪਲਸ SpO2:",
            "context_label": "ਸੰਦਰਭ:",
            "rule_count": "੮,੧੮੮ ਨਿਯਮ",
            "profile_pediatric": "ਬੱਚਿਆਂ ਦਾ ਦਮਾ (ਉਮਰ ੪–੧੨)",
            "profile_geriatric": "ਬਜ਼ੁਰਗ ਸੀਓਪੀਡੀ (ਉਮਰ ੬੦+)",
            "profile_worker": "ਬਾਹਰੀ ਡਿਲੀਵਰੀ ਵਰਕਰ",
            "profile_maternal": "ਮਾਵਾਂ ਅਤੇ ਜਣੇਪੇ ਤੋਂ ਪਹਿਲਾਂ ਦੀ ਦੇਖਭਾਲ",
            "profile_general": "ਆਮ ਆਬਾਦੀ"
        },
        "datasets": {
            "filter_grade_a": "ਗ੍ਰੇਡ ਏ (੯.੪+)",
            "filter_invented": "ਸਿੰਥੈਟਿਕ ਇਨਵੈਂਟ",
            "filter_forge": "ਫੋਰਜ ਤੋਂ ਕੱਢਿਆ ਗਿਆ",
            "table_view": "ਸਾਰਣੀ ਦ੍ਰਿਸ਼",
            "protocol_view": "ਪ੍ਰੋਟੋਕੋਲ ਕਾਰਡ ਦ੍ਰਿਸ਼",
            "close_drawer": "ਬੰਦ ਕਰੋ",
            "samples_header": "ਸੰਸ਼ਲੇਸ਼ਿਤ ਅਤੇ ਕੱਢੀਆਂ ਗਈਆਂ ਸੱਚੀਆਂ ਕਤਾਰਾਂ",
            "prompt_context": "ਮੌਸਮ / ਕਲੀਨਿਕਲ ਸੰਦਰਭ:",
            "protocol_truth": "ਕਲੀਨਿਕਲ ਜਵਾਬ ਪ੍ਰੋਟੋਕੋਲ / ਅਸਲ ਸਬੂਤ:",
            "copy_id_title": "ਪੂਰੀ ਅਡੈਪਸ਼ਨ ਡਾਟਾਸੈੱਟ ਆਈਡੀ ਕਾਪੀ ਕਰੋ"
        },
        "jury": {
            "quality_grade_card": "ਅਡੈਪਸ਼ਨ ਗੁਣਵੱਤਾ ਗ੍ਰੇਡ",
            "autoscientist_gain_card": "ਆਟੋ-ਸਾਇੰਟਿਸਟ ਜਿੱਤ ਦਰ",
            "predictive_fit_card": "ML ਭਵਿੱਖਬਾਣੀ ਸ਼ੁੱਧਤਾ",
            "credit_reserve_card": "SDK ਕ੍ਰੈਡਿਟ ਰਿਜ਼ਰਵ",
            "top_percentile": "ਵਿਸ਼ਵ ਪੱਧਰ 'ਤੇ ਚੋਟੀ ਦੇ ੩੩ਵੇਂ ਪ੍ਰਤੀਸ਼ਤ ਵਿੱਚ",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (੩ ਦੁਹਰਾਓ)",
            "mae_subtitle": "ਔਸਤ ਗਲਤੀ ±੧.੮੮ ਰੋਜ਼ਾਨਾ ਦਾਖਲੇ",
            "buffer_retained": "ਪ੍ਰਮਾਣਿਤ: >੪੦੦ ਕ੍ਰੈਡਿਟ ਬਫਰ ਸੁਰੱਖਿਅਤ",
            "verification_command_title": "ਜਿਊਰੀ ਲਈ ਸਿੱਧੀ ਅਡੈਪਸ਼ਨ SDK ਪੁਸ਼ਟੀਕਰਨ ਕਮਾਂਡ",
            "copy_command": "ਕਮਾਂਡ ਕਾਪੀ ਕਰੋ"
        }
    },

    "or": {
        "chrome": {
            "footer_desc": "କ୍ଲିନିକାଲ୍ ବାୟୁ ଗୁଣବତ୍ତା ଏବଂ ଶ୍ୱାସରୋଗ ନିରୀକ୍ଷଣ ମୋନୋରେପୋ",
            "footer_adaption": "ଆଡାପ୍ସନ୍ ଲ୍ୟାବ୍ସ ଦ୍ୱାରା ପରିଚାଳିତ",
            "rules_count": "୮,୧୮୮ ନିୟମ",
            "live_model_calc": "ଲାଇଭ୍ ମଡେଲ୍ ଗଣନା"
        },
        "overview": {
            "insight_years": "୧୦-ବର୍ଷର ଧାରା: ସହରାଞ୍ଚଳରେ PM2.5 ବାର୍ଷିକ +୪.୨% ବୃଦ୍ଧି ପାଉଛି।",
            "insight_quarters": "ଋତୁକାଳୀନ ବିଶ୍ଳେଷଣ: Q4 (ଶୀତକାଳୀନ ଧୂଆଁ) ମୌସୁମୀ ତୁଳନାରେ ୩.୪ ଗୁଣ ଅଧିକ।",
            "insight_months": "ଶୀତକାଳୀନ ଇନଭର୍ସନ୍ ଶୀର୍ଷ: ନଭେମ୍ବର-ଜାନୁଆରୀରେ ଡାକ୍ତରଖାନା ଭର୍ତ୍ତି +୨୪୦% ବୃଦ୍ଧି।",
            "insight_weeks": "ସାପ୍ତାହିକ ବୃଦ୍ଧି: ନଡ଼ା ପୋଡ଼ିବା ପରେ ଆଇସିୟୁ ଶ୍ୱାସରୋଗ ଭର୍ତ୍ତି ବୃଦ୍ଧି।",
            "insight_live": "ଲାଇଭ୍ ୭-ଦିନିଆ ଚକ୍ର: ସିପିସିବି କେନ୍ଦ୍ରଗୁଡ଼ିକ ସହିତ ବାସ୍ତବ ସମ୍ପର୍କ।",
            "r2_precision": "ML R² = ୦.୯୮୭୯",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 ସାନ୍ଦ୍ରତା (ସୂକ୍ଷ୍ମ ଶ୍ୱାସକ୍ରିୟା ଧୂଆଁ)",
            "pm10_title": "PM10 (ଶ୍ୱାସକ୍ରିୟା ଧୂଳିକଣା)",
            "no2_title": "NO2 (ଯାନବାହାନ ନିର୍ଗମନ)",
            "so2_title": "SO2 (ଶିଳ୍ପ ନିର୍ଗମନ)",
            "temperature_title": "ପରିବେଶ ତାପମାତ୍ରା",
            "humidity_title": "ଆପେକ୍ଷିକ ଆର୍ଦ୍ରତା",
            "live_calc": "ଲାଇଭ୍ ମଡେଲ୍ ଗଣନା",
            "temp_hint": "ଥଣ୍ଡା ପବନ ଶୀତଦିନେ ପ୍ରଦୂଷଣକୁ ଭୂମି ନିକଟରେ ଧରି ରଖେ",
            "humidity_hint": "ଅଧିକ ଆର୍ଦ୍ରତା ଘନ ଧୂଆଁ ସୃଷ୍ଟି କରେ",
            "vs_baseline": "ବେସଲାଇନ୍ ତୁଳନାରେ"
        },
        "copilot": {
            "rag_title": "TF-IDF ଭେକ୍ଟର RAG ପ୍ରମାଣ ଆଧାର",
            "sub_ms": "ସବ୍-ମିଲିସେକେଣ୍ଡ୍ ପ୍ରାପ୍ତି",
            "retrieved_source": "ପ୍ରାପ୍ତ ଜ୍ଞାନ ଉତ୍ସ",
            "matched_excerpt": "ସଠିକ୍ ମେଳ ଖାଉଥିବା କ୍ଲିନିକାଲ୍ ନିୟମ",
            "guardrails_verified": "ଆଡାପ୍ସନ୍ ବ୍ଲୁପ୍ରିଣ୍ଟ୍ ମେଡିକାଲ୍ ସୁରକ୍ଷା ନିୟମ ଯାଞ୍ଚ ହୋଇଛି",
            "rule_1": "ନିୟମ ୧: ସିପିସିବି AQI ମାନକ ପାଳନ (୦-୫୦୦)",
            "rule_2": "ନିୟମ ୨: ଆଇନଗତ CAQM GRAP ନିର୍ଦ୍ଦେଶାବଳୀ (ପର୍ଯ୍ୟାୟ I-IV)",
            "rule_3": "ନିୟମ ୩: କାଳ୍ପନିକ ଔଷଧ ସମ୍ପୂର୍ଣ୍ଣ ନିଷେଧ",
            "rule_4": "ନିୟମ ୪: ବାଧ୍ୟତାମୂଳକ ଜରୁରୀକାଳୀନ ସତର୍କତା (SpO2 < ୯୨%)",
            "rule_5": "ନିୟମ ୫: ପ୍ରମାଣିତ N95 ଏବଂ HEPA ଫିଲ୍ଟରେସନ୍ ବାଧ୍ୟତାମୂଳକ",
            "er_warning": "SpO2 < ୯୨%: ତୁରନ୍ତ ଜରୁରୀକାଳୀନ ଡାକ୍ତରଖାନା ସ୍ଥାନାନ୍ତର ଆବଶ୍ୟକ!",
            "pulse_spo2": "ପଲ୍ସ SpO2:",
            "context_label": "ପ୍ରସଙ୍ଗ:",
            "rule_count": "୮,୧୮୮ ନିୟମ",
            "profile_pediatric": "ଶିଶୁ ଆଜ୍‌ମା (ବୟସ ୪–୧୨)",
            "profile_geriatric": "ବୃଦ୍ଧ ସିଓପିଡି (ବୟସ ୬୦+)",
            "profile_worker": "ବାହ୍ୟ ଡେଲିଭରି କର୍ମଚାରୀ",
            "profile_maternal": "ମାତୃତ୍ୱ ଏବଂ ପ୍ରସବପୂର୍ବ ଯତ୍ନ",
            "profile_general": "ସାଧାରଣ ଜନସଂଖ୍ୟା"
        },
        "datasets": {
            "filter_grade_a": "ଗ୍ରେଡ୍ ଏ (୯.୪+)",
            "filter_invented": "ସିନ୍ଥେଟିକ୍ ଉଦ୍ଭାବନ",
            "filter_forge": "ଫୋର୍ଜ୍ ପ୍ରାପ୍ତ",
            "table_view": "ଟେବୁଲ୍ ଦୃଶ୍ୟ",
            "protocol_view": "ପ୍ରୋଟୋକଲ୍ କାର୍ଡ ଦୃଶ୍ୟ",
            "close_drawer": "ବନ୍ଦ କରନ୍ତୁ",
            "samples_header": "ସଂଶ୍ଳେଷିତ ଏବଂ ପ୍ରାପ୍ତ ପ୍ରକୃତ ଧାଡ଼ି",
            "prompt_context": "ପାଣିପାଗ / କ୍ଲିନିକାଲ୍ ପ୍ରସଙ୍ଗ:",
            "protocol_truth": "କ୍ଲିନିକାଲ୍ ପ୍ରତିକ୍ରିୟା ପ୍ରୋଟୋକଲ୍ / ପ୍ରକୃତ ପ୍ରମାଣ:",
            "copy_id_title": "ସମ୍ପୂର୍ଣ୍ଣ ଆଡାପ୍ସନ୍ ଡାଟାସେଟ୍ ଆଇଡି କପି କରନ୍ତୁ"
        },
        "jury": {
            "quality_grade_card": "ଆଡାପ୍ସନ୍ ଗୁଣବତ୍ତା ଗ୍ରେଡ୍",
            "autoscientist_gain_card": "ଅଟୋ-ସାଇଣ୍ଟିଷ୍ଟ ବିଜୟ ହାର",
            "predictive_fit_card": "ML ପୂର୍ବାନୁମାନ ସଠିକତା",
            "credit_reserve_card": "SDK କ୍ରେଡିଟ୍ ସଂରକ୍ଷଣ",
            "top_percentile": "ବିଶ୍ୱସ୍ତରରେ ଶୀର୍ଷ ୩୩ତମ ପରସେଣ୍ଟାଇଲ୍",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (୩ଟି ପୁନରାବୃତ୍ତି)",
            "mae_subtitle": "ହାରାହାରି ତ୍ରୁଟି ±୧.୮୮ ଦୈନିକ ଭର୍ତ୍ତି",
            "buffer_retained": "ଯାଞ୍ଚ ହୋଇଛି: >୪୦୦ କ୍ରେଡିଟ୍ ସୁରକ୍ଷିତ",
            "verification_command_title": "ଜୁରୀଙ୍କ ପାଇଁ ପ୍ରତ୍ୟକ୍ଷ ଆଡାପ୍ସନ୍ SDK ଯାଞ୍ଚ ନିର୍ଦ୍ଦେଶ",
            "copy_command": "ନିର୍ଦ୍ଦେଶ କପି କରନ୍ତୁ"
        }
    },

    "as": {
        "chrome": {
            "footer_desc": "ক্লিনিকেল বায়ু মান আৰু শ্বাসতন্ত্ৰ ৰোগ নিৰীক্ষণ মনোকেন্দ্ৰ",
            "footer_adaption": "এডাপশ্যন লেব্ছ দ্বাৰা চালিত",
            "rules_count": "৮,১৮৮ নিয়ম",
            "live_model_calc": "লাইভ মডেল গণনা"
        },
        "overview": {
            "insight_years": "১০-বছৰীয়া ধাৰা: নগৰাঞ্চলত PM2.5 বাৰ্ষিক +৪.২% হাৰত বৃদ্ধি পাইছে।",
            "insight_quarters": "ঋতুকালীন বিশ্লেষণ: Q4 (শীতকালীন ধোঁৱাশা) বাৰিষাতকৈ ৩.৪ গুণ অধিক।",
            "insight_months": "শীতকালীন ইনভাৰ্চন শিখৰ: নৱেম্বৰ-জানুৱাৰীত চিকিৎসালয়ত ভৰ্তি +২৪০% বৃদ্ধি।",
            "insight_weeks": "সাপ্তাহিক বৃদ্ধি: খেতিৰ নৰা পোৰাৰ পিছৰ সপ্তাহবোৰত আইচিইউ শ্বাসতন্ত্ৰ সংকট।",
            "insight_live": "লাইভ ৭-দিনীয়া চক্ৰ: চিপিচিবি কেন্দ্ৰসমূহৰ সৈতে লাইভ সম্পৰ্ক।",
            "r2_precision": "ML R² = ০.৯৮৭৯",
            "pm25_conc": "PM2.5 (µg/m³)"
        },
        "simulator": {
            "pm25_title": "PM2.5 ঘনত্ব (সূক্ষ্ম শ্বাসযোগ্য ধোঁৱাশা)",
            "pm10_title": "PM10 (স্থূল শ্বাসযোগ্য ধূলিকণা)",
            "no2_title": "NO2 (যান-বাহনৰ ধোঁৱা)",
            "so2_title": "SO2 (ঔদ্যোগিক নিৰ্গমন)",
            "temperature_title": "পৰিৱেশৰ উষ্ণতা",
            "humidity_title": "আপেক্ষিক আৰ্দ্ৰতা",
            "live_calc": "লাইভ মডেল গণনা",
            "temp_hint": "শীতকালত ঠাণ্ডা বতাহে প্ৰদূষণক মাটিৰ ওচৰতে আবদ্ধ কৰি ৰাখে",
            "humidity_hint": "অধিক আৰ্দ্ৰতাই ঘন কুঁৱলী আৰু ধোঁৱাশা সৃষ্টি কৰে",
            "vs_baseline": "বেচলাইনৰ তুলনাত"
        },
        "copilot": {
            "rag_title": "TF-IDF ভেক্টৰ RAG প্ৰমাণ ভিত্তি",
            "sub_ms": "উপ-মিলিছেকেণ্ড উদ্ধাৰ",
            "retrieved_source": "উদ্ধাৰ কৰা জ্ঞানৰ উৎস",
            "matched_excerpt": "সঠিক মিল থকা ক্লিনিকেল নিয়মৰ অংশ",
            "guardrails_verified": "এডাপশ্যন ব্লুপ্ৰিণ্ট চিকিৎসা সুৰক্ষা নিয়ম পৰীক্ষিত",
            "rule_1": "নিয়ম ১: চিপিচিবি AQI মানদণ্ড মানি চলা (০-৫০০)",
            "rule_2": "নিয়ম ২: আইনী CAQM GRAP নিৰ্দেশনা (পৰ্যায় I-IV)",
            "rule_3": "নিয়ম ৩: কাল্পনিক ঔষধ সম্পূৰ্ণ নিষিদ্ধ",
            "rule_4": "নিয়ম ৪: বাধ্যতামূলক জৰুৰীকালীন সতৰ্কতা (SpO2 < ৯২%)",
            "rule_5": "নিয়ম ৫: প্ৰমাণিত N95 আৰু HEPA ফিল্টাৰ বাধ্যতামূলক",
            "er_warning": "SpO2 < ৯২%: তাৎক্ষণিকভাৱে জৰুৰীকালীন চিকিৎসালয় স্থানান্তৰ প্ৰয়োজন!",
            "pulse_spo2": "পালছ SpO2:",
            "context_label": "প্ৰসংগ:",
            "rule_count": "৮,১৮৮ নিয়ম",
            "profile_pediatric": "শিশু হাঁপানি (বয়স ৪–১২)",
            "profile_geriatric": "বয়োজ্যেষ্ঠ চিঅ'পিডি (বয়স ৬০+)",
            "profile_worker": "বাহিৰৰ ডেলিভাৰী কৰ্মী",
            "profile_maternal": "মাতৃত্ব আৰু প্ৰসৱপূৰ্ব যত্ন",
            "profile_general": "সাধাৰণ জনসংখ্যা"
        },
        "datasets": {
            "filter_grade_a": "গ্ৰেড এ (৯.৪+)",
            "filter_invented": "সিন্থেটিক উদ্ভাৱন",
            "filter_forge": "ফৰ্জ নিষ্কাশিত",
            "table_view": "টেবুল ভিউ",
            "protocol_view": "প্ৰট'কল কাৰ্ড ভিউ",
            "close_drawer": "বন্ধ কৰক",
            "samples_header": "সংশ্লেষিত আৰু নিষ্কাশিত প্ৰকৃত শাৰী",
            "prompt_context": "বতৰ / ক্লিনিকেল প্ৰসংগ:",
            "protocol_truth": "ক্লিনিকেল প্ৰতিক্ৰিয়া প্ৰট'কল / প্ৰকৃত প্ৰমাণ:",
            "copy_id_title": "সম্পূৰ্ণ এডাপশ্যন ডাটাছেট আইডি কপি কৰক"
        },
        "jury": {
            "quality_grade_card": "এডাপশ্যন গুণমান গ্ৰেড",
            "autoscientist_gain_card": "অট'-বিজ্ঞানী জয়ৰ হাৰ",
            "predictive_fit_card": "ML ভৱিষ্যদ্বাণীৰ নিখুঁততা",
            "credit_reserve_card": "SDK ক্ৰেডিট সংৰক্ষণ",
            "top_percentile": "বিশ্বজুৰি শীৰ্ষ ৩৩তম শতাংশত",
            "qwen_lora": "Qwen/Qwen3.5-2B LoRA (৩টা পুনৰাবৃত্তি)",
            "mae_subtitle": "গড় ত্ৰুটি ±১.৮৮ দৈনিক ভৰ্তি",
            "buffer_retained": "পৰীক্ষিত: >৪০০ ক্ৰেডিট সুৰক্ষিত",
            "verification_command_title": "জুৰীৰ বাবে প্ৰত্যক্ষ এডাপশ্যন SDK পৰীক্ষণ আদেশ",
            "copy_command": "আদেশ কপি কৰক"
        }
    }
}

def main():
    translations_file = "/home/suyash/Projects/aeromed-india/frontend/src/i18n/translations.js"
    with open(translations_file, "r", encoding="utf-8") as f:
        text = f.read()

    prefix = "export const translations = "
    idx = text.find(prefix)
    json_str = text[idx + len(prefix):].strip()
    if json_str.endswith(";"):
        json_str = json_str[:-1]

    data = json.loads(json_str)

    # Apply enrichments
    for lang, categories in ENRICHMENTS.items():
        if lang not in data:
            continue
        for cat, items in categories.items():
            if cat not in data[lang]:
                data[lang][cat] = {}
            data[lang][cat].update(items)

    with open(translations_file, "w", encoding="utf-8") as f:
        f.write("/**\n")
        f.write(" * AeroMed India - Comprehensive 13-Language Translation Dictionary\n")
        f.write(" * Supports: en, hi, mr, bn, ta, te, ur, kn, ml, gu, pa, or, as\n")
        f.write(" * 100% full coverage of all workspaces, telemetry controls, map legends, and clinical modals.\n")
        f.write(" */\n\n")
        f.write("export const translations = ")
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
        f.write(";\n")

    print(f"Successfully enriched {translations_file} across all 13 languages!")

if __name__ == "__main__":
    main()
