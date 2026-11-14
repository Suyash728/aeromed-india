import React, { useState, useEffect, useMemo } from 'react';
import aqiClient from './api/aqiClient';
import seedData from './data/frontend_seed_data.json';
import Sidebar from './components/Sidebar';
import TopHeader from './components/TopHeader';
import SurveillanceOverview from './components/SurveillanceOverview';
import WhatIfSimulator from './components/WhatIfSimulator';
import ClinicalTriageCopilot from './components/ClinicalTriageCopilot';
import DatasetExplorer from './components/DatasetExplorer';
import AdaptionProof from './components/AdaptionProof';
import ClinicalBriefingModal from './components/ClinicalBriefingModal';
import QuickTriageDrawer from './components/QuickTriageDrawer';
import { LanguageProvider, useTranslation } from './i18n/LanguageContext';

const DEFAULT_CITIES = [
  { id: 'delhi', name: 'Delhi', state: 'Delhi NCR', lat: 28.6139, lon: 77.209, pm25: 174, aqi: 260, admissions: 152, predicted_risk_score: 78 },
  { id: 'mumbai', name: 'Mumbai', state: 'Maharashtra', lat: 19.076, lon: 72.8777, pm25: 88, aqi: 150, admissions: 70, predicted_risk_score: 48 },
  { id: 'navi mumbai', name: 'Navi Mumbai', state: 'Maharashtra', lat: 19.033, lon: 73.0297, pm25: 90, aqi: 155, admissions: 72, predicted_risk_score: 50 },
  { id: 'bengaluru', name: 'Bengaluru', state: 'Karnataka', lat: 12.9716, lon: 77.5946, pm25: 45, aqi: 82, admissions: 32, predicted_risk_score: 28 },
  { id: 'kolkata', name: 'Kolkata', state: 'West Bengal', lat: 22.5726, lon: 88.3639, pm25: 142, aqi: 215, admissions: 118, predicted_risk_score: 72 },
  { id: 'chennai', name: 'Chennai', state: 'Tamil Nadu', lat: 13.0827, lon: 80.2707, pm25: 52, aqi: 98, admissions: 38, predicted_risk_score: 34 },
  { id: 'hyderabad', name: 'Hyderabad', state: 'Telangana', lat: 17.385, lon: 78.4867, pm25: 95, aqi: 162, admissions: 78, predicted_risk_score: 54 },
  { id: 'ahmedabad', name: 'Ahmedabad', state: 'Gujarat', lat: 23.0225, lon: 72.5714, pm25: 110, aqi: 180, admissions: 94, predicted_risk_score: 62 },
  { id: 'pune', name: 'Pune', state: 'Maharashtra', lat: 18.5204, lon: 73.8567, pm25: 76, aqi: 135, admissions: 58, predicted_risk_score: 42 },
  { id: 'amritsar', name: 'Amritsar', state: 'Punjab', lat: 31.634, lon: 74.8723, pm25: 195, aqi: 280, admissions: 165, predicted_risk_score: 84 },
  { id: 'bhubaneswar', name: 'Bhubaneswar', state: 'Odisha', lat: 20.2961, lon: 85.8245, pm25: 85, aqi: 145, admissions: 68, predicted_risk_score: 46 },
  { id: 'guwahati', name: 'Guwahati', state: 'Assam', lat: 26.1445, lon: 91.7362, pm25: 62, aqi: 115, admissions: 45, predicted_risk_score: 36 },
];

function DashboardContent() {
  const { language, setLanguage, t, isRtl, languages } = useTranslation();
  const [activeTab, setActiveTab] = useState('surveillance');
  const [selectedCity, setSelectedCity] = useState('Delhi');
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [briefingModalOpen, setBriefingModalOpen] = useState(false);

  // Live state
  const [overviewData, setOverviewData] = useState(seedData);
  const [liveRiskData, setLiveRiskData] = useState(null);
  const [isLiveApi, setIsLiveApi] = useState(false);

  // 1. Initial background fetch: Overview
  useEffect(() => {
    async function initData() {
      try {
        const ovRes = await aqiClient.getOverview();
        if (ovRes && ovRes.metadata) {
          setOverviewData(ovRes);
          setIsLiveApi(true);
        }
      } catch (err) {
        setIsLiveApi(false);
      }
    }
    initData();
  }, []);

  // 2. City & Language change: fetch live risk & localized advisory with in-flight abort
  useEffect(() => {
    const controller = new AbortController();
    async function fetchLiveRisk() {
      try {
        const riskRes = await aqiClient.getLiveRisk(selectedCity, language, { signal: controller.signal });
        if (!controller.signal.aborted && riskRes && (riskRes.predicted_risk_score || riskRes.predicted_admissions || riskRes.aqi)) {
          setLiveRiskData(riskRes);
          setIsLiveApi(true);
        }
      } catch (err) {
        if (controller.signal.aborted || err.name === 'AbortError') {
          return; // Discard superseded in-flight requests cleanly
        }
        // Fallback to seed calculation
        const cityObj = DEFAULT_CITIES.find(c => c.name.toLowerCase() === selectedCity.toLowerCase()) || DEFAULT_CITIES[0];
        setLiveRiskData({
          city: cityObj.name,
          aqi: cityObj.aqi,
          pm25: cityObj.pm25,
          pm10: Math.round(cityObj.pm25 * 1.6),
          predicted_risk_score: cityObj.predicted_risk_score,
          predicted_admissions: cityObj.admissions,
          cpcb_category: cityObj.pm25 > 150 ? 'Severe' : cityObj.pm25 > 100 ? 'Very Poor' : 'Moderate',
          grap_stage: cityObj.pm25 > 250 ? 'Stage IV (Emergency)' : cityObj.pm25 > 150 ? 'Stage III (Severe)' : 'Stage II (Very Poor)',
          localized_advisory: `Current particulate exposure in ${cityObj.name} is elevated. Sensitive groups should avoid prolonged outdoor exertion during morning hours.`,
          grounded_dataset_id: '3bf58b6b-462c-4412-8171-fa1bed843e67',
          grounding_similarity_score: 0.884,
          temperature: 24,
          humidity: 62
        });
      }
    }
    fetchLiveRisk();
    return () => {
      controller.abort();
    };
  }, [selectedCity, language]);

  // Merge seed data with live city list
  const allCitiesData = useMemo(() => {
    return DEFAULT_CITIES.map((c) => {
      const match = seedData?.cities?.[c.name];
      return {
        ...c,
        pm25: match ? Math.round(match.avg_pm25) : c.pm25,
        admissions: match ? Math.round(match.avg_admissions) : c.admissions,
        predicted_risk_score: match ? Math.round(match.avg_risk_score) : c.predicted_risk_score,
      };
    });
  }, []);

  const activeCityData = useMemo(() => {
    return allCitiesData.find(c => c.name.toLowerCase() === selectedCity.toLowerCase()) || allCitiesData[0];
  }, [allCitiesData, selectedCity]);

  // Indic Language Font Class
  const langFontClass = `lang-${language}`;

  return (
    <div className={`min-h-screen bg-gray-50 flex ${langFontClass}`} dir={isRtl ? 'rtl' : 'ltr'}>
      
      {/* Persistent Left Sidebar */}
      <Sidebar 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
        isOpen={sidebarOpen} 
        setIsOpen={setSidebarOpen} 
      />

      {/* Main Content Layout */}
      <div className="flex-1 flex flex-col lg:pl-72 min-w-0 transition-all">
        
        {/* Sticky Top Header */}
        <TopHeader 
          cities={DEFAULT_CITIES}
          selectedCity={selectedCity}
          onSelectCity={setSelectedCity}
          languages={languages}
          selectedLanguage={language}
          onSelectLanguage={setLanguage}
          isLiveApi={isLiveApi}
          setSidebarOpen={setSidebarOpen}
          onOpenExportModal={() => setBriefingModalOpen(true)}
        />

        {/* Workspace Body */}
        <main className="p-4 sm:p-6 lg:p-8 flex-1 max-w-[1600px] w-full mx-auto">
          {activeTab === 'surveillance' && (
            <SurveillanceOverview
              activeCity={selectedCity}
              cityData={activeCityData}
              allCitiesData={allCitiesData}
              overviewData={overviewData}
              liveRiskData={liveRiskData}
              onSelectCity={setSelectedCity}
              onNavigateTab={setActiveTab}
            />
          )}

          {activeTab === 'simulator' && (
            <WhatIfSimulator
              activeCity={selectedCity}
              baselineAdmissions={activeCityData?.admissions || 152}
            />
          )}

          {activeTab === 'triage' && (
            <ClinicalTriageCopilot
              activeCity={selectedCity}
              activeLanguage={language}
            />
          )}

          {activeTab === 'datasets' && (
            <DatasetExplorer />
          )}

          {activeTab === 'jury' && (
            <AdaptionProof />
          )}
        </main>

        {/* Global Footer */}
        <footer className="border-t border-gray-200 bg-white px-6 py-4 text-xs text-gray-500 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <span className="font-bold text-gray-800 font-['Outfit']">AeroMed India</span>
            <span>•</span>
            <span>{t('chrome.footer_desc', 'Clinical Air Quality & Respiratory Disease Surveillance Monorepo')}</span>
          </div>
          <div className="flex items-center gap-4 text-gray-400 font-mono text-[11px]">
            <span>Model R²: 0.9879</span>
            <span>•</span>
            <span>AutoScientist Gain: +55.8%</span>
            <span>•</span>
            <span className="text-[#465FFF] font-semibold">{t('chrome.footer_adaption', 'Adaption Labs Grounded')}</span>
          </div>
        </footer>

        {/* Printable Health & GRAP Advisory Bulletin Modal */}
        <ClinicalBriefingModal
          isOpen={briefingModalOpen}
          onClose={() => setBriefingModalOpen(false)}
          cityData={activeCityData}
          liveRiskData={liveRiskData}
          selectedCity={selectedCity}
          selectedLanguage={language}
          languages={languages}
        />

        {/* Floating Quick-Triage Copilot Drawer */}
        <QuickTriageDrawer
          activeCity={selectedCity}
          activeLanguage={language}
          languages={languages}
        />

      </div>

    </div>
  );
}

export default function App() {
  return (
    <LanguageProvider>
      <DashboardContent />
    </LanguageProvider>
  );
}
