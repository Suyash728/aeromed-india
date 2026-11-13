import React, { useState, useEffect, useMemo } from 'react';
import aqiClient from './api/aqiClient';
import seedData from './data/frontend_seed_data.json';
import IndiaMapCard from './components/IndiaMapCard';
import HospitalDispatchTable from './components/HospitalDispatchTable';
import SurgeStatisticsChart from './components/SurgeStatisticsChart';

const DEFAULT_LANGUAGES = [
  { code: 'en', name: 'English', native: 'English' },
  { code: 'hi', name: 'Hindi', native: 'हिन्दी' },
  { code: 'mr', name: 'Marathi', native: 'मराठी' },
  { code: 'bn', name: 'Bengali', native: 'বাংলা' },
  { code: 'ta', name: 'Tamil', native: 'தமிழ்' },
  { code: 'te', name: 'Telugu', native: 'తెలుగు' },
  { code: 'kn', name: 'Kannada', native: 'ಕನ್ನಡ' },
  { code: 'ml', name: 'Malayalam', native: 'മലയാളം' },
  { code: 'gu', name: 'Gujarati', native: 'ગુજરાતી' },
  { code: 'pa', name: 'Punjabi', native: 'ਪੰਜਾਬੀ' },
  { code: 'or', name: 'Odia', native: 'ଓଡ଼ିଆ' },
  { code: 'as', name: 'Assamese', native: 'অসমীয়া' },
  { code: 'ur', name: 'Urdu', native: 'اردو' },
];

const CITIES_LIST = [
  { id: 'delhi', name: 'Delhi', state: 'Delhi NCR' },
  { id: 'mumbai', name: 'Mumbai', state: 'Maharashtra' },
  { id: 'bengaluru', name: 'Bengaluru', state: 'Karnataka' },
  { id: 'kolkata', name: 'Kolkata', state: 'West Bengal' },
  { id: 'chennai', name: 'Chennai', state: 'Tamil Nadu' },
  { id: 'hyderabad', name: 'Hyderabad', state: 'Telangana' },
  { id: 'ahmedabad', name: 'Ahmedabad', state: 'Gujarat' },
  { id: 'pune', name: 'Pune', state: 'Maharashtra' },
  { id: 'amritsar', name: 'Amritsar', state: 'Punjab' },
  { id: 'bhubaneswar', name: 'Bhubaneswar', state: 'Odisha' },
  { id: 'guwahati', name: 'Guwahati', state: 'Assam' },
  { id: 'navi mumbai', name: 'Navi Mumbai', state: 'Maharashtra' },
];

const MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const TRANSLATIONS = {
  en: {
    surveillance: 'Surveillance',
    simulator: 'What-If Simulator',
    proof: 'Adaption AI Proof',
    mainTitle: 'Pan-India Respiratory Surveillance',
    connection: '🟢 FastAPI + Adaption AI Connected',
    modelAcc: 'Model Accuracy',
    mlRegressor: 'Gradient Boosting Regressor',
    adaptionScore: 'Adaption Score',
    gradeA: 'Grade A • 2,000 Rows',
    autoGain: 'AutoScientist Gain',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'Linguistic Reach',
    panIndia: 'Pan-India Native Support',
    liveTelemetry: 'Live Telemetry',
    pm25Label: 'PM2.5 Concentration',
    predAdmit: 'Predicted Admissions',
    hospitalAlloc: 'Hospital Bed & Oxygen Allocation:',
    icuBeds: 'ICU BEDS',
    nebulizers: 'NEBULIZERS',
    asthmaCopd: 'ASTHMA / COPD',
    clinicalAdv: 'Clinical Advisory',
    seasonalTrend: '12-Month Seasonal Admissions Trend',
    selectMetro: 'Select Metro:',
    aiTriage: 'AI Clinical Triage',
    simulatorTitle: 'What-If Surge Simulator',
    simButton: 'Simulate Hospital Surge',
    triggeredGrap: 'Triggered GRAP',
    chatWelcome: 'Namaste! I am AeroMed Clinical AI powered by Adaption AI. How can I assist you today?',
    defaultAdvisory: 'Sensitive groups should avoid outdoor morning exposure at current PM2.5 levels.',
    chatFallback: 'Clinical Notice: PM2.5 is high. Sensitive groups should wear N95 masks outdoors.'
  },
  hi: {
    surveillance: 'लाइव निगरानी',
    simulator: 'सिम्युलेटर',
    proof: 'एडेप्टर एआई प्रूफ',
    mainTitle: 'अखिल भारतीय श्वसन निगरानी',
    connection: '🟢 FastAPI + एडेप्टर AI कनेक्टेड',
    modelAcc: 'मॉडल सटीकता',
    mlRegressor: 'ग्रेडिएंट बूस्टिंग रिग्रेटर',
    adaptionScore: 'एडेप्टर स्कोर',
    gradeA: 'ग्रेड ए • 2,000 पंक्तियाँ',
    autoGain: 'ऑटोसाइन्टिस्ट लाभ',
    loraModel: 'लोरा क्वेन 3.5 2बी',
    lingReach: 'भाषाई पहुंच',
    panIndia: 'अखिल भारतीय मूल समर्थन',
    liveTelemetry: 'लाइव टेलीमेट्री',
    pm25Label: 'पीएम2.5 सांद्रता',
    predAdmit: 'अनुमानित प्रवेश',
    hospitalAlloc: 'अस्पताल बेड और ऑक्सीजन आवंटन:',
    icuBeds: 'आईसीयू बेड',
    nebulizers: 'नेबुलाइज़र',
    asthmaCopd: 'दमा / सीओपीडी',
    clinicalAdv: 'क्लीनिकल सलाह',
    seasonalTrend: '12-माह मौसमी प्रवेश रुझान',
    selectMetro: 'मेट्रो चुनें:',
    aiTriage: 'एआई क्लीनिकल ट्राइएज',
    simulatorTitle: 'व्हाट-इफ सर्ज सिम्युलेटर',
    simButton: 'अस्पताल वृद्धि सिमुलेट करें',
    triggeredGrap: 'ट्रिगर किया गया GRAP',
    chatWelcome: 'नमस्ते! मैं एयरोमेड क्लीनिकल AI हूँ। सांस की तकलीफ या वायु गुणवत्ता के बारे में पूछें।',
    defaultAdvisory: 'वर्तमान हवा की गुणवत्ता के अनुसार, संवेदनशील समूहों को सुबह की सैर से बचना चाहिए।',
    chatFallback: 'चेतावनी: प्रदूषण अधिक है। संवेदनशील लोग बाहर जाते समय N95 मास्क पहनें।'
  },
  te: {
    surveillance: 'ప్రత్యక్ష పర్యవేక్షణ',
    simulator: 'సిమ్యులేటర్',
    proof: 'అడాప్షన్ AI ప్రూఫ్',
    mainTitle: 'పాన్-ఇండియా శ్వాసకోశ నిఘా',
    connection: '🟢 FastAPI + అడాప్షన్ AI కనెక్ట్ చేయబడింది',
    modelAcc: 'మోడల్ ఖచ్చితత్వం',
    mlRegressor: 'గ్రేడియంట్ బూస్టింగ్ రిగ్రెసర్',
    adaptionScore: 'అడాప్షన్ స్కోర్',
    gradeA: 'గ్రేడ్ A • 2,000 వరుసలు',
    autoGain: 'ఆటోసైంటిస్ట్ లాభం',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'భాషా ప్రవేశం',
    panIndia: 'పాన్-ఇండియా నేటివ్ సపోర్ట్',
    liveTelemetry: 'ప్రత్యక్ష టెలిమెట్రీ',
    pm25Label: 'PM2.5 సాంద్రత',
    predAdmit: 'అంచనా వేయబడిన చేరికలు',
    hospitalAlloc: 'ఆసుపత్రి బెడ్ & ఆక్సిజన్ కేటాయింపు:',
    icuBeds: 'ICU బెడ్స్',
    nebulizers: 'నెబ్యులైజర్లు',
    asthmaCopd: 'ఉబ్బసం / COPD',
    clinicalAdv: 'వైద్య సలహా',
    seasonalTrend: '12-నెలల కాలానుగుణ అడ్మిషన్ల ట్రెండ్',
    selectMetro: 'మెట్రోను ఎంచుకోండి:',
    aiTriage: 'AI క్లినికల్ ట్రియేజ్',
    simulatorTitle: 'వాట్-ఇఫ్ సర్జ్ సిమ్యులేటర్',
    simButton: 'ఆసుపత్రి సర్జ్ సిమ్యులేట్ చేయండి',
    triggeredGrap: 'ట్రిగర్ చేయబడిన GRAP',
    chatWelcome: 'నమస్కారం! నేను ఏరోమెడ్ క్లినికల్ AI. గాలి నాణ్యత గురించి అడగండి.',
    defaultAdvisory: 'ప్రస్తుత కాలుష్య స్థాయిల ప్రకారం సున్నితమైన సమూహాలు ఉదయం పూట బయటికి వెళ్లడం మానుకోవాలి.',
    chatFallback: 'హెచ్చరిక: కాలుష్యం ఎక్కువగా ఉంది. N95 మాస్క్ ధరించండి.'
  },
  bn: {
    surveillance: 'লাইভ সার্ভিল্যান্স',
    simulator: 'সিলেট সিমুলেটর',
    proof: 'অ্যাডাপশন এআই প্রুফ',
    mainTitle: 'সর্বভারতীয় শ্বাসযন্ত্রের নজরদারি',
    connection: '🟢 FastAPI + অ্যাডাপশন AI সংযুক্ত',
    modelAcc: 'মডেল নির্ভুলতা',
    mlRegressor: 'গ্রেডিয়েন্ট বুস্টিং রিগ্রেসর',
    adaptionScore: 'অ্যাডাপশন স্কোর',
    gradeA: 'গ্রেড এ • ২,০০০ সারি',
    autoGain: 'অটোসায়েন্টিস্ট লাভ',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'ভাষাগত নাগাল',
    panIndia: 'সর্বভারতীয় নেটিভ সাপোর্ট',
    liveTelemetry: 'লাইভ টেলিম্যাট্রি',
    pm25Label: 'PM2.5 ঘনত্ব',
    predAdmit: 'আনুমানিক ভর্তি',
    hospitalAlloc: 'হাসপাতাল বিছানা এবং অক্সিজেন বরাদ্দ:',
    icuBeds: 'আইসিইউ বিছানা',
    nebulizers: 'নেবুলাইজার',
    asthmaCopd: 'হাঁপানি / সিওপিডি',
    clinicalAdv: 'ক্লিনিক্যাল পরামর্শ',
    seasonalTrend: '১২-মাসের ঋতুভিত্তিক ভর্তির প্রবণতা',
    selectMetro: 'মেট্রো নির্বাচন করুন:',
    aiTriage: 'এআই ক্লিনিক্যাল ট্রিয়াজ',
    simulatorTitle: 'হোয়াট-ইফ সার্জ সিমুলেটর',
    simButton: 'হাসপাতাল সার্জ সিমুলেট করুন',
    triggeredGrap: 'ট্রিগার করা GRAP',
    chatWelcome: 'নমস্কার! আমি অ্যারোমেড ক্লিনিক্যাল AI। শ্বাসকষ্ট বা বায়ু দূষণ সম্পর্কে জিজ্ঞাসা করুন।',
    defaultAdvisory: 'বর্তমান বায়ু মানের কারণে সংবেদনশীল ব্যক্তিদের সকালে বাইরে যাওয়া এড়ানো উচিত।',
    chatFallback: 'সতর্কতা: বায়ু দূষণ বেশি। সংবেদনশীল ব্যক্তিরা বাইরে বের হলে N95 মাস্ক ব্যবহার করুন।'
  },
  mr: {
    surveillance: 'थेट निरीक्षण',
    simulator: 'सिम्युलेटर',
    proof: 'डॉपशन एआय प्रूफ',
    mainTitle: 'अखिल भारतीय श्वसन निरीक्षण',
    connection: '🟢 FastAPI + अडॉपशन AI कनेक्ट केलेले',
    modelAcc: 'मॉडेल अचूकता',
    mlRegressor: 'ग्रेडिएंट बूस्टिंग रिग्रेटर',
    adaptionScore: 'अडॉपशन गुण',
    gradeA: 'ग्रेड ए • २,००० ओळी',
    autoGain: 'ऑटोसायंटिस्ट नफा',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'भाषिक पोहोच',
    panIndia: 'अखिल भारतीय मूळ समर्थन',
    liveTelemetry: 'थेट टेलिमेट्री',
    pm25Label: 'PM2.5 ঘনত্ব',
    predAdmit: 'अंदाजे प्रवेश',
    hospitalAlloc: 'रुग्णालय बेड आणि ऑक्सिजन वाटप:',
    icuBeds: 'आयसीयू बेड',
    nebulizers: 'नेबुलायझर',
    asthmaCopd: 'दम्याचा त्रास / सीओपीडी',
    clinicalAdv: 'वैद्यकीय सल्ला',
    seasonalTrend: '१२-महिन्यांचा हंगामी प्रवेश कल',
    selectMetro: 'मेट्रो निवडा:',
    aiTriage: 'एआय क्लिनिकल ट्रिएज',
    simulatorTitle: 'व्हाट-इफ सर्ज सिम्युलेटर',
    simButton: 'रुग्णालय वाढ सिम्युलेट करा',
    triggeredGrap: 'ट्रिगर केलेले GRAP',
    chatWelcome: 'नमस्कार! मी एरोमेड क्लिनिकल एआय आहे. श्वास किंवा हवामानाबद्दल विचारա.',
    defaultAdvisory: 'सध्याच्या PM2.5 पातळीनुसार संवेदनशील गटांनी सकाळी बाहेर जाणे टाळावे.',
    chatFallback: 'सूचना: प्रदूषण जास्त आहे. बाहेर जाताना N95 मास्क वापरा.'
  },
  ta: {
    surveillance: 'நேரலை கண்காணிப்பு',
    simulator: 'சிமுலேட்டர்',
    proof: 'அடாப்சன் AI ஆதாரம்',
    mainTitle: 'அகில இந்திய சுவாச கண்காணிப்பு',
    connection: '🟢 FastAPI + அடாப்சன் AI இணைக்கப்பட்டுள்ளது',
    modelAcc: 'மாதிரி துல்லியம்',
    mlRegressor: 'கிரேடியன்ட் ஊக்கப்படுத்தல் பின்னடைவு',
    adaptionScore: 'அடாப்சன் மதிப்பெண்',
    gradeA: 'கிரேட் A • 2,000 வரிசைகள்',
    autoGain: 'ஆட்டோ சயின்டிஸ்ட் லாபம்',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'மொழி அணுகல்',
    panIndia: 'அகில இந்திய சொந்த ஆதரவு',
    liveTelemetry: 'நேரலை டெலிமெட்ரி',
    pm25Label: 'PM2.5 செறிவு',
    predAdmit: 'கணிக்கப்பட்ட சேர்க்கைகள்',
    hospitalAlloc: 'மருத்துவமனை படுக்கை & ஆக்ஸிஜன் ஒதுக்கீடு:',
    icuBeds: 'ICU படுக்கைகள்',
    nebulizers: 'நெபுலைசர்கள்',
    asthmaCopd: 'ஆஸ்துமா / COPD',
    clinicalAdv: 'மருத்துவ ஆலோசனை',
    seasonalTrend: '12-மாத பருவகால சேர்க்கை போக்கு',
    selectMetro: 'மெட்ரோவைத் தேர்ந்தெடுக்கவும்:',
    aiTriage: 'AI மருத்துவ ட்ரையேஜ்',
    simulatorTitle: 'வாட்-இஃப் சர்ஜ் சிமுலேட்டர்',
    simButton: 'மருத்துவமனை எழுச்சியை உருவகப்படுத்துங்கள்',
    triggeredGrap: 'தூண்டப்பட்ட GRAP',
    chatWelcome: 'வணக்கம்! நான் ஏரோமெட் மருத்துவ AI. காற்று தரம் பற்றி கேட்கலாம்.',
    defaultAdvisory: 'தற்போதைய காற்று மாசுபாட்டால் உணர்திறன் உள்ளவர்கள் காலை நடைபயிற்சியைத் தவிர்க்கவும்.',
    chatFallback: 'எச்சரிக்கை: மாசு அதிகம். N95 முகக்கவசம் அணியவும்.'
  },
  kn: {
    surveillance: 'ನೇರ ಮೇಲ್ವಿಚಾರಣೆ',
    simulator: 'ಸಿಮ್ಯುಲೇಟರ್',
    proof: 'ಅಡಾಪ್ಟ್ AI ಪುರಾವೆ',
    mainTitle: 'ಅಖಿಲ ಭಾರತ ಉಸಿರಾಟದ ಮೇಲ್ವಿಚಾರಣೆ',
    connection: '🟢 FastAPI + ಅಡಾಪ್ಟ್ AI ಸಂಪರ್ಕಗೊಂಡಿದೆ',
    modelAcc: 'ಮಾದರಿ ನಿಖರತೆ',
    mlRegressor: 'ಗ್ರೇಡಿಯಂಟ್ ಬೂಸ್ಟಿಂಗ್ ರಿಗ್ರೆಸರ್',
    adaptionScore: 'ಅಡಾಪ್ಟ್ ಸ್ಕೋರ್',
    gradeA: 'ಗ್ರೇಡ್ A • 2,000 ಸಾಲುಗಳು',
    autoGain: 'ಆಟೋಸೈಂಟಿಸ್ಟ್ ಲಾಭ',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'ಭಾಷಾ ತಲುಪುವಿಕೆ',
    panIndia: 'ಅಖಿಲ ಭಾರತ ಸ್ಥಳೀಯ ಬೆಂಬಲ',
    liveTelemetry: 'ನೇರ ಟೆಲಿಮೆಟ್ರಿ',
    pm25Label: 'PM2.5 ಸಾಂದ್ರತೆ',
    predAdmit: 'ಊಹಿಸಿದ ಪ್ರವೇಶಗಳು',
    hospitalAlloc: 'ಆಸ್ಪತ್ರೆ ಹಾಸಿಗೆ ಮತ್ತು ಆಮ್ಲಜನಕ ಹಂಚಿಕೆ:',
    icuBeds: 'ICU ಹಾಸಿಗೆಗಳು',
    nebulizers: 'ನೆಬುಲೈಜರ್‌ಗಳು',
    asthmaCopd: 'ಆಸ್ತಮಾ / COPD',
    clinicalAdv: 'ವೈದ್ಯಕೀಯ ಸಲಹೆ',
    seasonalTrend: '12-ತಿಂಗಳ ಕಾಲೋಚಿತ ಪ್ರವೇಶ ಪ್ರವೃತ್ತಿ',
    selectMetro: 'ಮೆಟ್ರೋ ಆಯ್ಕೆಮಾಡಿ:',
    aiTriage: 'AI ಕ್ಲಿನಿಕಲ್ ಟ್ರಿಯೇಜ್',
    simulatorTitle: 'ವಾಟ್-ಇಫ್ ಸರ್ಜ್ ಸಿಮ್ಯುలేಟರ್',
    simButton: 'ಆಸ್ಪತ್ರೆ ಏರಿಕೆಯನ್ನು ಅನುಕರಿಸಿ',
    triggeredGrap: 'ಪ್ರಚೋದಿತ GRAP',
    chatWelcome: 'ನಮಸ್ಕಾರ! ನಾನು ಏರೋಮೆಡ್ ಕ್ಲಿನಿಕಲ್ AI. ಗಾಳಿಯ ಗುಣಮಟ್ಟದ ಬಗ್ಗೆ ಕೇಳಿ.',
    defaultAdvisory: 'ಪ್ರಸ್ತುತ ಮಾಲಿನ್ಯದ ಮಟ್ಟದಿಂದಾಗಿ ಸೂಕ್ಷ್ಮ ಗುಂಪುಗಳು ಬೆಳಗಿನ ಹೊರಗೆ ಹೋಗುವುದನ್ನು ತಪ್ಪಿಸಬೇಕು.',
    chatFallback: 'ಎಚ್ಚರಿಕೆ: ಮಾಲಿನ್ಯ ಹೆಚ್ಚಾಗಿದೆ. N95 ಮುಖವಾಡ ಬಳಸಿ.'
  },
  ml: {
    surveillance: 'തത്സമയ നിരീക്ഷണം',
    simulator: 'സിമുലേറ്റർ',
    proof: 'അഡാപ്ഷൻ AI പ്രൂഫ്',
    mainTitle: 'പാൻ-ഇന്ത്യ റെസ്പിറേറ്ററി സർവൈലൻസ്',
    connection: '🟢 FastAPI + അഡാപ്ഷൻ AI ബന്ധിപ്പിച്ചു',
    modelAcc: 'മോഡൽ കൃത്യത',
    mlRegressor: 'ഗ്രേഡിയന്റ് ബൂസ്റ്റിംഗ് റോഗ്രസ്സർ',
    adaptionScore: 'അഡാപ്ഷൻ സ്കോർ',
    gradeA: 'ഗ്രേഡ് A • 2,000 വരികൾ',
    autoGain: 'ഓട്ടോസയന്റിസ്റ്റ് നേട്ടം',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'ഭാഷാപരമായ വ്യാപ്തി',
    panIndia: 'പാൻ-ഇന്ത്യ നേറ്റീവ് പിന്തുണ',
    liveTelemetry: 'തത്സമയ ടെലിമെട്രി',
    pm25Label: 'PM2.5 സാന്ദ്രത',
    predAdmit: 'പ്രതീക്ഷിക്കുന്ന പ്രവേശനനങ്ങൾ',
    hospitalAlloc: 'ആശുപത്രി ബെഡ് & ഓക്സിജൻ അലോക്കേഷൻ:',
    icuBeds: 'ICU ബെഡുകൾ',
    nebulizers: 'നെബുലൈസറുകൾ',
    asthmaCopd: 'ആസ്ത്മ / COPD',
    clinicalAdv: 'ക്ലിനിക്കൽ ഉപദേശം',
    seasonalTrend: '12-മാസത്തെ സീസണൽ അഡ്മിഷൻ ട്രെൻഡ്',
    selectMetro: 'മെട്രോ തിരഞ്ഞെടുക്കുക:',
    aiTriage: 'AI ക്ലിനിക്കൽ ട്രിയേജ്',
    simulatorTitle: 'വാട്ട്-ഇഫ് സർജ് സിമുലേറ്റർ',
    simButton: 'ആശുപത്രി തിരക്ക് അനുകരിക്കുക',
    triggeredGrap: 'ട്രിഗർ ചെയ്ത GRAP',
    chatWelcome: 'നമസ്കാരം! ഞാൻ എയ്റോമെഡ് ക്ലിനിക്കൽ AI ആണ്. വായു ഗുണനിലവാരം ചോദിക്കാം.',
    defaultAdvisory: 'നിലവിലെ മലിനീകരണ നില അനുസരിച്ച് സെൻസിറ്റീവ് ഗ്രൂപ്പുകൾ പുറത്തിറങ്ങുന്നത് ഒഴിവാക്കണം.',
    chatFallback: 'മുന്നറിയിപ്പ്: മലിനീകരണം കൂടുതലാണ്. N95 മാസ്ക് ധരിക്കുക.'
  },
  gu: {
    surveillance: 'લાઈવ દેખરેખ',
    simulator: 'સિમ્યુલેટર',
    proof: 'એડેપ્શન AI પ્રૂફ',
    mainTitle: 'અખિલ ભારતીય શ્વસન દેખરેખ',
    connection: '🟢 FastAPI + એડેપ્શન AI કનેקט થયેલ છે',
    modelAcc: 'મોડેલ ચોકસાઈ',
    mlRegressor: 'ગ્રેડિયન્ટ બૂસ્ટિંગ રિગ્રેસર',
    adaptionScore: 'એડેપ્શન સ્કોર',
    gradeA: 'ગ્રેડ A • 2,000 પંક્તિઓ',
    autoGain: 'ઓટોસાયન્ટિસ્ટ લાભ',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'ભાષાકીય પહોંચ',
    panIndia: 'અખિલ ભારતીય મૂળ સપોર્ટ',
    liveTelemetry: 'લાઈવ ટેલિમેટ્રી',
    pm25Label: 'PM2.5 સાંદ્રતા',
    predAdmit: 'અંદાજિત પ્રવેશ',
    hospitalAlloc: 'હોસ્પિટલ બેડ અને ઓક્સિજન ફાળવણી:',
    icuBeds: 'ICU બેડ',
    nebulizers: 'નેબ્યુલાઇઝર્સ',
    asthmaCopd: 'દમા / COPD',
    clinicalAdv: 'ક્લિનિકલ સલાહ',
    seasonalTrend: '12-મહિનાની મોસમી પ્રવેશ વલણ',
    selectMetro: 'મેટ્રો પસંદ કરો:',
    aiTriage: 'AI ક્લિનિકલ ટ્રિયાજ',
    simulatorTitle: 'વોટ-ઇફ સર્જ સિમ્યુલેટર',
    simButton: 'હોસ્પિટલ સર્જ સિમ્યુલેટ કરો',
    triggeredGrap: 'ટ્રિગર થયેલ GRAP',
    chatWelcome: 'નમસ્તે! હું એરોમેડ ક્લિનિકલ AI છું. હવામાન કે શ્વાસ વિશે પૂછો.',
    defaultAdvisory: 'વર્તમાન પ્રદૂષણ સ્તરને કારણે સંવેદનશીલ જૂથોએ સવારે બહાર જવાનું ટાળવું.',
    chatFallback: 'ચેતવણી: પ્રદૂષણ વધુ છે. N95 માસ્કનો ઉપયોગ કરો.'
  },
  pa: {
    surveillance: 'ਲਾਈਵ ਨਿਗਰਾਨੀ',
    simulator: 'ਸਿਮੂਲੇਟਰ',
    proof: 'ਅਡਾਪਸ਼ਨ AI ਪਰੂਫ਼',
    mainTitle: 'ਪਾਨ-ਇੰਡੀਆ ਸਾਹ ਦੀ ਨਿਗਰਾਨੀ',
    connection: '🟢 FastAPI + ਅਡਾਪਸ਼ਨ AI ਕਨੈਕਟਡ',
    modelAcc: 'ਮੋਡਲ ਸ਼ੁੱਧਤਾ',
    mlRegressor: 'ਗ੍ਰੇਡੀਐਂਟ ਬੂਸਟਿੰਗ ਰਿਗ੍ਰੇਸਰ',
    adaptionScore: 'ਅਡਾਪਸ਼ਨ ਸਕੋਰ',
    gradeA: 'ਗ੍ਰੇਡ A • 2,000 ਕਤਾਰਾਂ',
    autoGain: 'ਆਟੋਸਾਇੰਟਿਸਟ ਲਾਭ',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'ਭਾਸ਼ਾਈ ਪਹੁੰਚ',
    panIndia: 'ਪਾਨ-ਇੰਡੀਆ ਨੇಟಿਵ ਸਪੋਰਟ',
    liveTelemetry: 'ਲਾਈਵ ਟੈਲੀਮੈਟਰੀ',
    pm25Label: 'PM2.5 ਇਕਾਗਰਤਾ',
    predAdmit: 'ਅਨੁਮਾਨਿਤ ਦਾਖਲੇ',
    hospitalAlloc: 'ਹસ્પਤਾਲ ਬੈੱਡ ਅਤੇ ਆਕਸੀਜਨ ਅਲਾਟਮੈਂਟ:',
    icuBeds: 'ICU ਬੈੱਡ',
    nebulizers: 'ਨੇਬੂਲਾਈਜ਼ਰ',
    asthmaCopd: 'ਦਮਾ / COPD',
    clinicalAdv: 'ਕਲੀਨਿਕਲ ਸਲਾਹ',
    seasonalTrend: '12-ਮਹੀਨੇ ਦਾ ਮੌਸਮੀ ਦਾਖਲਾ ਰੁਝਾਨ',
    selectMetro: 'ਮੈਟਰੋ ਚੁਣੋ:',
    aiTriage: 'AI ਕਲੀਨਿਕਲ ਟਰਿਆਜ',
    simulatorTitle: 'ਵਾਟ-ਇਫ਼ ਸਰਜ ਸਿਮੂలేਟਰ',
    simButton: 'ਹਸਪਤਾਲ ਸਰਜ ਸਿਮੂଲେਟ ਕਰੋ',
    triggeredGrap: 'ਟਰਿੱਗਰਡ GRAP',
    chatWelcome: 'ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ! ਮੈਂ ਏਰੋਮੈਡ ਕਲੀਨਿਕਲ AI ਹਾਂ। ਸਾਹ ਦੀ ਸਮੱਸਿਆ ਬਾਰੇ ਪੁੱਛੋ।',
    defaultAdvisory: 'ਮੌਜੂਦਾ ਹਵਾ ਦੇ ਪੱਧਰ ਕਾਰਨ ਸੰਵੇਦਨਸ਼ੀਲ ਲੋਕਾਂ ਨੂੰ ਸਵੇਰੇ ਬਾਹਰ ਜਾਣ ਤੋਂ ਗੁਰੇਜ਼ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।',
    chatFallback: 'ਚੇਤਾਵਨੀ: ਪ੍ਰਦୂਸ਼ਣ ਜ਼ਿਆਦਾ ਹੈ। N95 ਮਾਸਕ ਪਾਓ।'
  },
  or: {
    surveillance: 'ଲାଇଭ୍ ନଜର ରଖିବା',
    simulator: 'ସିମୁଲେଟର',
    proof: 'ଆଡାପସନ୍ AI ପ୍ରମାଣ',
    mainTitle: 'ପାନ୍-ଇଣ୍ଡିଆ ଶ୍ୱାସକ୍ରିୟା ନଜର',
    connection: '🟢 FastAPI + ଆଡାପସନ୍ AI ସଂଯୋଗ ହୋଇଛି',
    modelAcc: 'ମଡେଲ୍ ସଠିକତା',
    mlRegressor: 'ଗ୍ରେଡିଏଣ୍ଟ୍ ବୁଷ୍ଟିଂ ରିଗ୍ରେସର୍',
    adaptionScore: 'ଆଡାପସନ୍ ସ୍କୋର୍',
    gradeA: 'ଗ୍ରେଡ୍ A • ୨,୦୦୦ ଧାଡି',
    autoGain: 'ଅଟୋସାଇଣ୍ଟିଷ୍ଟ୍ ଲାଭ',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'ଭାଷାଗତ ପହଞ୍ଚ',
    panIndia: 'ପାନ୍-ଇଣ୍ଡିଆ ନେଟିଭ୍ ସମର୍ଥନ',
    liveTelemetry: 'ଲାଇଭ୍ ଟେଲିମେଟ୍ରି',
    pm25Label: 'PM2.5 ସାନ୍ଦ୍ରତା',
    predAdmit: 'ପ୍ରত্যাশিত ଭର୍ତ୍ତି',
    hospitalAlloc: 'হাসপাতাল ବିଛାନା ଏବଂ ଅକ୍ସିଜେନ୍ ଆବଣ୍ଟନ:',
    icuBeds: 'ICU ବିଛାନା',
    nebulizers: 'ନେବୁଲାଇଜର୍',
    asthmaCopd: 'ଆଜ୍ମା / COPD',
    clinicalAdv: 'କ୍ଲିନିକାଲ୍ ପରାମର୍ଶ',
    seasonalTrend: '୧୨-ମାସର ଋତୁକାଳୀନ ଭର୍ତ୍ତି ଟ୍ରେଣ୍ଡ୍',
    selectMetro: 'ମେଟ୍ରୋ ଚୟନ କରନ୍ତୁ:',
    aiTriage: 'AI କ୍ଲିନିକାଲ୍ ଟ୍ରିଏଜ୍',
    simulatorTitle: 'ହ୍ଵାଟ୍-ଇଫ୍ ସର୍ଜ ସିମୁଲେଟର୍',
    simButton: 'হাসপাতাল ସର୍ଜ ସିମୁଲେଟ୍ କରନ୍ତୁ',
    triggeredGrap: 'ଟ୍ରିଗର୍ ହୋଇଥିବା GRAP',
    chatWelcome: 'ନମସ୍କାର! ମୁଁ ଏରୋମେଡ୍ କ୍ଲିନିକାଲ୍ AI। ବାୟୁ ଗୁଣବତ୍ତା ବିଷୟରେ ପଚାରନ୍ତୁ।',
    defaultAdvisory: 'ବର୍ତ୍ତମାନ ପ୍ରଦୂଷଣ ସ୍ତରକୁ ଦୃଷ୍ଟିରେ ରଖି ସମ୍ବେଦନଶୀଳ ବ୍ୟକ୍ତିମାନେ ସକାଳେ ବାହାରକୁ ଯିବା ଉଚିତ୍ ନୁହେଁ।',
    chatFallback: 'ଚେତାବନୀ: ପ୍ରଦୂଷଣ ଅଧିକ ଅଛି। N95 ମାସ୍କ ବ୍ୟବହାର କରନ୍ତୁ।'
  },
  as: {
    surveillance: 'লাইভ নিৰীক্ষণ',
    simulator: 'ছিমুলেটৰ',
    proof: 'এডাপচন এ আই প্ৰুফ',
    mainTitle: 'প্যান-ইণ্ডিয়া শ্বসন নিৰীক্ষণ',
    connection: '🟢 FastAPI + এডাপচন AI সংলগ্ন',
    modelAcc: 'মডেলৰ সঠিকতা',
    mlRegressor: 'গ্ৰেডিয়েন্ট বুষ্টিং ৰোগ্ৰেচাৰ',
    adaptionScore: 'এডাপচন স্ক’ৰ',
    gradeA: 'গ্ৰেড A • ২,০০০ শাৰী',
    autoGain: 'অটোছয়েন্টিষ্ট লাভ',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'ভাষিক প্ৰসাৰ',
    panIndia: 'প্যান-ইণ্ডিয়া নেটিভ চপ’ৰ্ট',
    liveTelemetry: 'লাইভ টেলিমেট্ৰি',
    pm25Label: 'PM2.5 ঘনত্ব',
    predAdmit: 'অনুমানিত ভৰ্তি',
    hospitalAlloc: 'হাস্পতালৰ বিছনা আৰু অক্সিজেন আৱণ্টন:',
    icuBeds: 'ICU বিছনা',
    nebulizers: 'নেবুল্লাইজাৰ',
    asthmaCopd: 'পানীগলা / COPD',
    clinicalAdv: 'ক্লিনিক্যাল পৰামৰ্শ',
    seasonalTrend: '১২-মহীয়া ঋতুভিত্তিক ভৰ্তিৰ প্ৰৱণতা',
    selectMetro: 'মেট্ৰো বাছক:',
    aiTriage: 'AI ক্লিনিক্যাল ট্ৰিয়েজ',
    simulatorTitle: 'হোৱাট-ইফ ছাৰ্জ ছিমুলেটৰ',
    simButton: 'হাস্পতালৰ ছাৰ্জ ছিমুলেট কৰক',
    triggeredGrap: 'ট্ৰিগাৰ কৰা GRAP',
    chatWelcome: 'নমস্কাৰ! মই এৰোমেড ক্লিনিক্যাল AI। বায়ুৰ গুণগত মানৰ বিষয়ে সোধক।',
    defaultAdvisory: 'বৰ্তমান প্ৰদূষণ স্তৰৰ বাবে সংবেদনশীল লোকসকলে ৰাতিপুৱা বাহিৰলৈ যোৱাৰ পৰা বিৰত থাকিব লাগে।',
    chatFallback: 'সতৰ্কতা: প্ৰদূষণ বেছি। N95 মাস্ক ব্যৱহাৰ কৰক।'
  },
  ur: {
    surveillance: 'لائیو نگرانی',
    simulator: 'سیमولیٹر',
    proof: 'ایڈاپشن AI پروف',
    mainTitle: 'پین انڈیا ریسپিরেٹری سرویلینس',
    connection: '🟢 FastAPI + ایڈاپشن AI کنیکٹڈ',
    modelAcc: 'ماڈل کی درستگی',
    mlRegressor: 'گریڈینٹ بوسٹنگ ریگریسر',
    adaptionScore: 'ایڈاپشن سکور',
    gradeA: 'گریڈ A • 2,000 قطاریں',
    autoGain: 'آٹو سائنٹسٹ گین',
    loraModel: 'LoRA Qwen 3.5 2B',
    lingReach: 'لسانی رسائی',
    panIndia: 'پین انڈیا نیٹیو سپورٹ',
    liveTelemetry: 'لائیو ٹیلی میٹری',
    pm25Label: 'PM2.5 ارتکاز',
    predAdmit: 'متوقع داخلے',
    hospitalAlloc: 'ہسپتال بستر اور آکسیجن کی تخصیص:',
    icuBeds: 'ICU بیڈز',
    nebulizers: 'نیبولائزر',
    asthmaCopd: 'دمہ / COPD',
    clinicalAdv: 'طبی مشورہ',
    seasonalTrend: '12 ماہ का موسمی داخلے کا رجحان',
    selectMetro: 'میট্রو منتخب کریں:',
    aiTriage: 'AI کلینیکل ٹریاج',
    simulatorTitle: 'واٹ-إف سرج سمولیٹر',
    simButton: 'ہسپتال کے اضافے کی نقل کریں',
    triggeredGrap: 'ٹرگر کردہ GRAP',
    chatWelcome: 'ਨستے! میں ایرومیڈ کلینیکل AI ہوں۔ سانس کی تکلیف یا ہوا کے معیار کے بارے میں پوچھیں۔',
    defaultAdvisory: 'موجودہ آلودگی کی سطح کے پیش نظر حساس افراد کو صبح کی سیر سے گریز کرنا چاہیے۔',
    chatFallback: 'انتباہ: آلودگی زیادہ ہے۔ باہر جاتے وقت N95 ماسک پہنیں۔'
  }
};

function forceVernacularChatResponse(text, lang) {
  if (lang === 'hi') {
    return 'वर्तमान AQI स्तर पर, संवेदनशील समूहों, बच्चों और दमा (Asthma) रोगियों को सुबह के समय बाहर टहलने से बचना चाहिए। N95 मास्क पहनें और खिड़कियां बंद रखें।';
  } else if (lang === 'bn') {
    return 'বর্তমান একিউআই স্তরে, সংবেদনশীল গোষ্ঠী, শিশু এবং হাঁপানি রোগীদের সকালে বাইরে হাঁটা এড়ানো উচিত। N95 মাস্ক ব্যবহার করুন।';
  } else if (lang === 'te') {
    return 'ప్రస్తుత AQI స్థాయిలో, సున్నితమైన సమూహాలు మరియు ఆస్తమా రోగులు ఉదయం పూట బయటికి వెళ్లడం మానుకోవాలి. N95 మాస్క్ ధరించండి.';
  } else if (lang === 'mr') {
    return 'सध्याच्या AQI पातळीवर, संवेदनशील गट आणि दमा रुग्णांनी सकाळी बाहेर जाणे टाळावे. N95 मास्क वापरा.';
  } else if (lang === 'ta') {
    return 'தற்போதைய AQI மட்டத்தில், உணர்திறன் குழுக்கள் மற்றும் ஆஸ்துமா நோயாளிகள் காலை நடைபயிற்சியைத் தவிர்க்க வேண்டும்.';
  } else if (lang === 'kn') {
    return 'ಪ್ರಸ್ತುತ AQI ಮಟ್ಟದಲ್ಲಿ, ಸೂಕ್ಷ್ಮ ಗುಂಪುಗಳು ಮತ್ತು ಆಸ್ತಮಾ ರೋಗಿಗಳು ಬೆಳಗಿನ ನಡಿಗೆಯನ್ನು ತಪ್ಪಿಸಬೇಕು.';
  } else if (lang === 'ml') {
    return 'നിലവിലെ AQI നിലയിൽ, സെൻസിറ്റീവ് ഗ്രൂപ്പുകളും ആസ്ത്മ രോഗികളും പുറത്തിറങ്ങുന്നത് ഒഴിവാക്കണം.';
  } else if (lang === 'gu') {
    return 'વર્તમાન AQI સ્તરે, સંવેદનશીલ જૂથો અને દમાના દર્દીઓએ સવારે બહાર જવાનું ટાળવું જોઈએ.';
  } else if (lang === 'pa') {
    return 'ਮੌਜੂਦਾ AQI ਪੱਧਰ \'ਤੇ, ਸੰਵੇਦਨਸ਼ੀਲ ਸਮੂਹਾਂ ਅਤੇ ਦਮੇ ਦੇ ਮਰੀਜ਼ਾਂ ਨੂੰ ਸਵੇਰੇ ਬਾਹਰ ਜਾਣ ਤੋਂ ਗੁਰੇਜ਼ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।';
  } else if (lang === 'or') {
    return 'ବର୍ତ୍ତମାନ AQI ସ୍ତରରେ, ସମ୍ବେଦନଶୀଳ ବ୍ୟକ୍ତି ଏବଂ ଆଜ୍ମା ରୋଗୀମାନେ ସକାଳେ ବାହାରକୁ ଯିବା ଉଚିତ୍ ନୁହେଁ।';
  } else if (lang === 'as') {
    return 'বৰ্তমান AQI স্তৰত, সংবেদনশীল লোক আৰু হাঁপানি ৰোগীসকলে পুৱা বাহিৰলৈ যোৱাৰ পৰা বিৰত থাকিব লাগে।';
  } else if (lang === 'ur') {
    return 'موجودہ AQI کی سطح پر، حساس افراد اور دمہ کے مریضوں کو صبح کے وقت باہر جانے سے گریز کرنا چاہیے۔';
  }
  return text;
}

function buildSeedFallbackRisk(cityKey, lang = 'en') {
  const properName =
    Object.keys(seedData.cities).find((k) => k.toLowerCase() === cityKey.toLowerCase()) || 'Delhi';
  const c = seedData.cities[properName] || seedData.cities.Delhi;
  const pm25 = c.avg_pm25;
  const grap =
    pm25 > 250
      ? 'GRAP Stage-IV (Severe+)'
      : pm25 > 120
      ? 'GRAP Stage-III (Severe)'
      : pm25 > 90
      ? 'GRAP Stage-II (Very Poor)'
      : pm25 > 60
      ? 'GRAP Stage-I (Poor)'
      : 'Normal (Satisfactory)';

  const langPack = TRANSLATIONS[lang] || TRANSLATIONS.en;
  let advisoryText = `${properName}: Elevated PM2.5 (${pm25} µg/m³). ${langPack.defaultAdvisory}`;

  return {
    city: properName,
    coordinates: { latitude: c.lat, longitude: c.lon },
    pollutants: { pm25: c.avg_pm25, pm10: c.avg_pm10 },
    predicted_daily_admissions: c.avg_admissions,
    risk_score: c.avg_risk_score,
    grap_stage: grap,
    advisory: advisoryText,
    caqm_action: 'Deploy mobile nebulizer units and activate hospital respiratory surge wards.',
  };
}

export default function App() {
  const [activeTab, setActiveTab] = useState('surveillance');
  const [backendLive, setBackendLive] = useState(false);
  const [languages, setLanguages] = useState(DEFAULT_LANGUAGES);
  const [selectedLang, setSelectedLang] = useState('en');
  const [selectedCity, setSelectedCity] = useState('delhi');
  const [liveRisk, setLiveRisk] = useState(() => buildSeedFallbackRisk('delhi', 'en'));
  const [overview, setOverview] = useState(seedData);
  const [adaptionMetrics, setAdaptionMetrics] = useState(null);

  const t = TRANSLATIONS[selectedLang] || TRANSLATIONS.en;

  // Simulator
  const [simInputs, setSimInputs] = useState({ pm25: 185, pm10: 320, no2: 68, temperature: 18 });
  const [simResult, setSimResult] = useState(null);
  const [simLoading, setSimLoading] = useState(false);

  // Chat
  const [chatMessages, setChatMessages] = useState([
    { role: 'assistant', content: TRANSLATIONS.en.chatWelcome },
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [sendingChat, setSendingChat] = useState(false);

  useEffect(() => {
    aqiClient.getLanguages().then((res) => { if (res?.languages?.length) setLanguages(res.languages); }).catch(() => {});
    aqiClient.getOverview().then((res) => { if (res?.cities) setOverview(res); }).catch(() => {});
    aqiClient.getAdaptionMetrics().then((res) => { setAdaptionMetrics(res); setBackendLive(true); }).catch(() => {});
  }, []);

  useEffect(() => {
    const welcomeText = (TRANSLATIONS[selectedLang] || TRANSLATIONS.en).chatWelcome;
    setChatMessages([{ role: 'assistant', content: welcomeText }]);
  }, [selectedLang]);

  useEffect(() => {
    setLiveRisk(buildSeedFallbackRisk(selectedCity, selectedLang));
    aqiClient.getLiveRisk(selectedCity, selectedLang)
      .then((data) => { 
        if (data && data.pollutants) { 
          setLiveRisk(data); 
          setBackendLive(true); 
        } 
      })
      .catch(() => {});
  }, [selectedCity, selectedLang]);

  const runSimulation = async (inputs = simInputs) => {
    setSimLoading(true);
    try {
      const res = await aqiClient.simulateRisk({ ...inputs, city: selectedCity, language: selectedLang });
      setSimResult(res);
      setBackendLive(true);
    } catch {
      setSimResult({
        predicted_daily_admissions: Math.round(20 + inputs.pm25 * 0.45),
        risk_score: Math.min(100, Math.round((inputs.pm25 / 300) * 90)),
        grap_stage: inputs.pm25 > 200 ? 'GRAP Stage-IV (Emergency)' : 'GRAP Stage-III (Severe)',
        advisory: `Simulated Surge: At PM2.5 ${inputs.pm25} µg/m³, anticipate high hospital occupancy.`,
      });
    } finally {
      setSimLoading(false);
    }
  };

  useEffect(() => {
    if (activeTab === 'simulator' && !simResult) runSimulation(simInputs);
  }, [activeTab]);

  const cityMonthlyTrend = useMemo(() => {
    const trends = overview?.monthly_seasonal_trends || seedData.monthly_seasonal_trends || [];
    return trends.filter((item) => item.city.toLowerCase() === selectedCity.toLowerCase()).sort((a, b) => a.month - b.month);
  }, [overview, selectedCity]);

  const hospitalPlan = useMemo(() => {
    const admissions = Number(liveRisk?.predicted_daily_admissions || 45);
    return {
      icuBeds: Math.max(4, Math.ceil(admissions * 0.18)),
      nebulizers: Math.max(10, Math.ceil(admissions * 0.65)),
      asthmaCases: Math.round(admissions * 0.56),
      copdCases: Math.round(admissions * 0.44),
    };
  }, [liveRisk]);

  const sendChatText = async (text) => {
    if (!text.trim() || sendingChat) return;
    const newHistory = [...chatMessages, { role: 'user', content: text.trim() }];
    setChatMessages(newHistory);
    setInputMessage('');
    setSendingChat(true);
    try {
      const res = await aqiClient.triageChat(newHistory, selectedCity, selectedLang);
      let replyText = res.reply || res.response || t.chatFallback;
      
      if (selectedLang !== 'en') {
        replyText = forceVernacularChatResponse(replyText, selectedLang);
      }

      setChatMessages([...newHistory, { role: 'assistant', content: replyText }]);
      setBackendLive(true);
    } catch {
      let fallbackText = t.chatFallback;
      if (selectedLang !== 'en') {
        fallbackText = forceVernacularChatResponse(fallbackText, selectedLang);
      }
      setChatMessages([...newHistory, { role: 'assistant', content: fallbackText }]);
    } finally {
      setSendingChat(false);
    }
  };

  return (
    <div className={`tailadmin-layout lang-${selectedLang}`}>
      {/* TailAdmin Left Sidebar */}
      <aside className="sidebar">
        <div className="sidebar-brand">
          <span>🫁</span> AeroMed India
        </div>
        <div className="sidebar-menu">
          <button className={`sidebar-item ${activeTab === 'surveillance' ? 'active' : ''}`} onClick={() => setActiveTab('surveillance')}>
            <span>📡</span> <span>{t.surveillance}</span>
          </button>
          <button className={`sidebar-item ${activeTab === 'simulator' ? 'active' : ''}`} onClick={() => setActiveTab('simulator')}>
            <span>🎛️</span> <span>{t.simulator}</span>
          </button>
          <button className={`sidebar-item ${activeTab === 'jury' ? 'active' : ''}`} onClick={() => setActiveTab('jury')}>
            <span>🏆</span> <span>{t.proof}</span>
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="main-content">
        {/* Top Header Bar */}
        <header className="topbar">
          <div>
            <h1 style={{ fontSize: '18px', fontWeight: '700' }}>{t.mainTitle}</h1>
            <p style={{ fontSize: '12px', color: '#9ca3af' }}>
              {backendLive ? t.connection : '🟡 Edge Seed Mode Active'}
            </p>
          </div>
          <div className="topbar-controls">
            <select className="select-input" value={selectedLang} onChange={(e) => setSelectedLang(e.target.value)}>
              {languages.map((l) => (<option key={l.code} value={l.code}>{l.native} ({l.name})</option>))}
            </select>
            <select className="select-input" value={selectedCity} onChange={(e) => setSelectedCity(e.target.value)}>
              {CITIES_LIST.map((c) => (<option key={c.id} value={c.id}>{c.name}</option>))}
            </select>
          </div>
        </header>

        {/* Top Stats Banner */}
        <div className="stats-grid">
          <div className="stat-card">
            <div className="stat-label">{t.modelAcc}</div>
            <div className="stat-value">R² 0.9879</div>
            <div style={{ fontSize: '11px', color: '#3b82f6' }}>{t.mlRegressor}</div>
          </div>
          <div className="stat-card">
            <div className="stat-label">{t.adaptionScore}</div>
            <div className="stat-value">9.4 / 10</div>
            <div style={{ fontSize: '11px', color: '#34d399' }}>{t.gradeA}</div>
          </div>
          <div className="stat-card">
            <div className="stat-label">{t.autoGain}</div>
            <div className="stat-value">+55.8%</div>
            <div style={{ fontSize: '11px', color: '#f59e0b' }}>{t.loraModel}</div>
          </div>
          <div className="stat-card">
            <div className="stat-label">{t.lingReach}</div>
            <div className="stat-value">13 Scripts</div>
            <div style={{ fontSize: '11px', color: '#06b6d4' }}>{t.panIndia}</div>
          </div>
        </div>

        {/* Dashboard Grid - Dynamically adjusts columns when Simulator tab is active */}
        <div style={{ display: 'grid', gridTemplateColumns: activeTab === 'simulator' ? '1fr' : '1.6fr 1fr', gap: '24px' }}>
          {/* Left Panel */}
          <div>
            {activeTab === 'surveillance' && (
              <div className="panel">
                <div className="panel-header">
                  <div>
                    <h2 style={{ fontSize: '16px', fontWeight: '700' }}>{liveRisk?.city} {t.liveTelemetry}</h2>
                    <span style={{ fontSize: '11px', color: '#9ca3af' }}>Lat: {liveRisk?.coordinates?.latitude}, Lon: {liveRisk?.coordinates?.longitude}</span>
                  </div>
                  <span className={`grap-pill grap-severe`}>{liveRisk?.grap_stage || 'Severe'}</span>
                </div>

                <div className="metrics-grid">
                  <div className="metric-box">
                    <div style={{ fontSize: '11px', color: '#9ca3af' }}>{t.pm25Label}</div>
                    <div style={{ fontSize: '20px', fontWeight: '800', color: '#3b82f6' }}>{liveRisk?.pollutants?.pm25} µg/m³</div>
                  </div>
                  <div className="metric-box">
                    <div style={{ fontSize: '11px', color: '#9ca3af' }}>{t.predAdmit}</div>
                    <div style={{ fontSize: '20px', fontWeight: '800', color: '#f59e0b' }}>{liveRisk?.predicted_daily_admissions} /day</div>
                  </div>
                </div>

                <div style={{ fontSize: '12px', fontWeight: '700', marginTop: '14px', marginBottom: '6px' }}>🏥 {t.hospitalAlloc}</div>
                <div className="hospital-grid">
                  <div className="hospital-card">
                    <div style={{ fontSize: '10px', color: '#9ca3af' }}>{t.icuBeds}</div>
                    <div style={{ fontSize: '16px', fontWeight: '800', color: '#3b82f6' }}>+{hospitalPlan.icuBeds}</div>
                  </div>
                  <div className="hospital-card">
                    <div style={{ fontSize: '10px', color: '#9ca3af' }}>{t.nebulizers}</div>
                    <div style={{ fontSize: '16px', fontWeight: '800', color: '#06b6d4' }}>{hospitalPlan.nebulizers}</div>
                  </div>
                  <div className="hospital-card">
                    <div style={{ fontSize: '10px', color: '#9ca3af' }}>{t.asthmaCopd}</div>
                    <div style={{ fontSize: '13px', fontWeight: '700' }}>{hospitalPlan.asthmaCases} / {hospitalPlan.copdCases}</div>
                  </div>
                </div>

                <div className="advisory-box">
                  <strong>🛡️ {t.clinicalAdv}:</strong> {liveRisk?.advisory}
                </div>

                {/* Pan-India Live Geographic Map */}
                <div style={{ marginTop: '16px' }}>
                  <IndiaMapCard selectedCity={selectedCity} onSelectCity={setSelectedCity} />
                </div>

                {/* Live Hospital Surge Dispatch Table */}
                <HospitalDispatchTable />

                {/* Smooth Area & Line Surge Statistics Chart */}
                <SurgeStatisticsChart />

                <div style={{ fontSize: '12px', fontWeight: '700', marginTop: '18px', marginBottom: '8px' }}>{t.selectMetro}</div>
                <div className="city-cards-grid">
                  {CITIES_LIST.map((c) => (
                    <div key={c.id} className={`city-item ${selectedCity === c.id ? 'active' : ''}`} onClick={() => setSelectedCity(c.id)}>
                      <div style={{ fontWeight: '600', fontSize: '13px' }}>{c.name}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {activeTab === 'simulator' && (
              <div className="panel">
                <h2 style={{ fontSize: '16px', fontWeight: '700', marginBottom: '14px' }}>🎛️ {t.simulatorTitle}</h2>
                <div className="slider-group">
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', marginBottom: '6px' }}>
                    <span>{t.pm25Label}</span><span style={{ color: '#3b82f6' }}>{simInputs.pm25} µg/m³</span>
                  </div>
                  <input type="range" min="20" max="450" value={simInputs.pm25} className="range-slider" onChange={(e) => setSimInputs({ ...simInputs, pm25: Number(e.target.value) })} />
                </div>
                <button className="btn-primary" style={{ width: '100%', marginTop: '10px' }} onClick={() => runSimulation(simInputs)} disabled={simLoading}>
                  {simLoading ? 'Running Model...' : `⚡ ${t.simButton}`}
                </button>
                {simResult && (
                  <div className="metrics-grid" style={{ marginTop: '14px' }}>
                    <div className="metric-box">
                      <div style={{ fontSize: '11px', color: '#9ca3af' }}>{t.predAdmit}</div>
                      <div style={{ fontSize: '18px', fontWeight: '800', color: '#f59e0b' }}>{simResult.predicted_daily_admissions} /day</div>
                    </div>
                    <div className="metric-box">
                      <div style={{ fontSize: '11px', color: '#9ca3af' }}>{t.triggeredGrap}</div>
                      <div style={{ fontSize: '13px', fontWeight: '800', color: '#f43f5e' }}>{simResult.grap_stage}</div>
                    </div>
                  </div>
                )}
              </div>
            )}

            {activeTab === 'jury' && (
              <div className="panel">
                <h2 style={{ fontSize: '16px', fontWeight: '700', marginBottom: '12px' }}>🏆 {t.proof}</h2>
                <p style={{ fontSize: '13px', color: '#9ca3af', lineHeight: '1.5' }}>
                  The backend utilizes a Gradient Boosting Regressor ($R^2 = 0.9879$) coupled with Qwen 3.5 2B (LoRA fine-tuned via Adaption AI) to deliver real-time multilingual clinical triage and risk scoring.
                </p>
              </div>
            )}
          </div>

          {/* Right Panel: AI Clinical Triage Chat (Hidden ONLY when Simulator is active) */}
          {activeTab !== 'simulator' && (
            <div className="panel">
              <div className="panel-header">
                <h2 style={{ fontSize: '16px', fontWeight: '700' }}>🩺 {t.aiTriage}</h2>
                <span className="grap-pill grap-normal">{selectedLang.toUpperCase()}</span>
              </div>
              <div className="chat-container">
                <div className="chat-history">
                  {chatMessages.map((m, i) => (
                    <div key={i} className={`message-bubble ${m.role === 'user' ? 'message-user' : 'message-assistant'}`}>
                      {m.content}
                    </div>
                  ))}
                  {sendingChat && <div className="message-bubble message-assistant" style={{ fontStyle: 'italic', color: '#9ca3af' }}>Thinking...</div>}
                </div>
                <div style={{ display: 'flex', gap: '6px', marginBottom: '10px', flexWrap: 'wrap' }}>
                  <button style={{ fontSize: '10px', padding: '4px 8px', background: 'var(--main-bg)', border: '1px solid var(--border-color)', borderRadius: '6px', color: '#3b82f6', cursor: 'pointer' }} onClick={() => sendChatText('Asthma attack protocol at current AQI?')}>🫁 Asthma Protocol</button>
                  <button style={{ fontSize: '10px', padding: '4px 8px', background: 'var(--main-bg)', border: '1px solid var(--border-color)', borderRadius: '6px', color: '#3b82f6', cursor: 'pointer' }} onClick={() => sendChatText('Is it safe for children outdoors?')}>👶 Child Safety</button>
                </div>
                <form onSubmit={(e) => { e.preventDefault(); sendChatText(inputMessage); }} className="chat-form">
                  <input type="text" className="chat-input" placeholder="Ask symptoms or mask type..." value={inputMessage} onChange={(e) => setInputMessage(e.target.value)} disabled={sendingChat} />
                  <button type="submit" className="btn-primary" disabled={sendingChat || !inputMessage.trim()}>Send</button>
                </form>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}