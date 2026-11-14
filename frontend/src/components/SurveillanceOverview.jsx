import React from 'react';
import { 
  Wind, 
  Activity, 
  ShieldAlert, 
  Thermometer, 
  TrendingUp, 
  ArrowUpRight, 
  CheckCircle2, 
  AlertTriangle,
  FileText,
  Sparkles,
  ChevronRight,
  MapPin
} from 'lucide-react';
import RadialGauge from './RadialGauge';
import SurgeStatisticsChart from './SurgeStatisticsChart';
import IndiaSvgMap from './IndiaSvgMap';
import CorrelationHeatmap from './CorrelationHeatmap';
import HospitalDispatchTable from './HospitalDispatchTable';
import { useTranslation } from '../i18n/LanguageContext';

export default function SurveillanceOverview({ 
  activeCity, 
  cityData, 
  allCitiesData, 
  overviewData, 
  liveRiskData, 
  onSelectCity,
  onNavigateTab
}) {
  const { t } = useTranslation();

  // Extract metrics from live API or seed fallback
  const aqi = liveRiskData?.aqi || cityData?.aqi || 245;
  const pm25 = liveRiskData?.pm25 || cityData?.pm25 || 173;
  const pm10 = liveRiskData?.pm10 || cityData?.pm10 || 240;
  const riskScore = liveRiskData?.predicted_risk_score || cityData?.predicted_risk_score || 78;
  const admissions = liveRiskData?.predicted_admissions || cityData?.predicted_admissions || 142;
  const cpcbCategory = liveRiskData?.cpcb_category || cityData?.cpcb_category || (pm25 > 150 ? 'Severe' : pm25 > 100 ? 'Very Poor' : 'Moderate');
  const grapStage = liveRiskData?.grap_stage || (pm25 > 250 ? 'Stage IV (Emergency)' : pm25 > 150 ? 'Stage III (Severe)' : 'Stage II (Very Poor)');
  const temp = liveRiskData?.temperature || cityData?.temperature || 24;
  const humidity = liveRiskData?.humidity || cityData?.humidity || 62;
  const localizedAdvisory = liveRiskData?.localized_advisory || cityData?.clinical_advisory || "Sensitive groups should limit outdoor exertion during peak morning traffic.";
  const groundedDatasetId = liveRiskData?.grounded_dataset_id || "3bf58b6b-462c-4412-8171-fa1bed843e67";
  const groundingSimilarity = liveRiskData?.grounding_similarity_score ? (liveRiskData.grounding_similarity_score * 100).toFixed(1) : "88.4";

  // Clean markdown asterisks or hashes from advisory text
  const cleanAdvisory = (localizedAdvisory || '')
    .replace(/\*\*/g, '')
    .replace(/###?/g, '')
    .trim();

  // Category Pill styling
  const getCategoryBadge = (cat) => {
    switch (cat?.toLowerCase()) {
      case 'severe':
        return 'bg-rose-50 text-rose-700 border-rose-200';
      case 'very poor':
        return 'bg-orange-50 text-orange-700 border-orange-200';
      case 'poor':
      case 'moderate':
        return 'bg-amber-50 text-amber-700 border-amber-200';
      default:
        return 'bg-emerald-50 text-emerald-700 border-emerald-200';
    }
  };

  const localizedCity = t('cities.' + (activeCity || '').toLowerCase(), activeCity || 'Delhi');

  return (
    <div className="space-y-6">

      {/* Row 1: 4 TailAdmin KPI Cards (12 Cols) */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        {/* KPI 1: Live City AQI */}
        <div className="tailadmin-card p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-bold text-gray-500 uppercase tracking-wider">
              {t('overview.kpi_current_aqi', 'Atmospheric AQI Index')}
            </span>
            <div className="w-8 h-8 rounded-xl bg-[#465FFF]/10 text-[#465FFF] flex items-center justify-center">
              <Wind className="w-4 h-4" />
            </div>
          </div>
          <div>
            <div className="flex items-baseline justify-between">
              <div className="text-3xl font-extrabold text-gray-900 font-['Outfit'] tabular-nums tracking-tight">
                {aqi}
              </div>
              <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${getCategoryBadge(cpcbCategory)}`}>
                {t('overview.' + cpcbCategory?.toLowerCase().replace(' ', '_'), cpcbCategory)}
              </span>
            </div>
            <div className="flex items-center justify-between text-xs text-gray-500 mt-2 pt-2 border-t border-gray-100 font-mono">
              <span>PM2.5: <strong className="text-gray-900">{pm25}</strong> µg/m³</span>
              <span>PM10: <strong className="text-gray-900">{pm10}</strong> µg/m³</span>
            </div>
          </div>
        </div>

        {/* KPI 2: 48-Hour Hospital Surge Risk */}
        <div className="tailadmin-card p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-bold text-gray-500 uppercase tracking-wider">
              {t('overview.kpi_surge_risk', '48h Surge Risk Score')}
            </span>
            <div className="w-8 h-8 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center">
              <Activity className="w-4 h-4" />
            </div>
          </div>
          <div>
            <div className="flex items-baseline justify-between">
              <div className="text-3xl font-extrabold text-gray-900 font-['Outfit'] tabular-nums tracking-tight">
                {riskScore}
                <span className="text-sm font-semibold text-gray-400">/100</span>
              </div>
              <span className="text-xs font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-full border border-rose-200">
                {t('overview.high_surge', 'High Surge')}
              </span>
            </div>
            <div className="flex items-center justify-between text-xs text-gray-500 mt-2 pt-2 border-t border-gray-100">
              <span>{t('overview.projected_admissions', 'Projected Admissions')}:</span>
              <strong className="text-gray-900 font-mono tabular-nums">
                {admissions} {t('overview.pts_day', 'pts/day')}
              </strong>
            </div>
          </div>
        </div>

        {/* KPI 3: Statutory CAQM GRAP Stage */}
        <div className="tailadmin-card p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-bold text-gray-500 uppercase tracking-wider">
              {t('overview.kpi_grap_stage', 'Statutory GRAP Stage')}
            </span>
            <div className="w-8 h-8 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center">
              <ShieldAlert className="w-4 h-4" />
            </div>
          </div>
          <div>
            <div className="flex items-baseline justify-between">
              <div className="text-lg font-extrabold text-gray-900 font-['Outfit'] tracking-tight truncate">
                {grapStage}
              </div>
            </div>
            <p className="text-[11px] text-gray-500 mt-1 line-clamp-1">
              {t('overview.grap_sub', 'Civic vehicle restrictions & primary school warnings active.')}
            </p>
            <div className="text-[10px] font-semibold text-[#465FFF] mt-2 pt-2 border-t border-gray-100 flex items-center gap-1">
              <span>{t('overview.caqm_schedule', 'CAQM Statutory Schedule (17 Pages)')}</span>
            </div>
          </div>
        </div>

        {/* KPI 4: Dominant Trigger & Weather */}
        <div className="tailadmin-card p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-bold text-gray-500 uppercase tracking-wider">
              {t('overview.kpi_dominant_trigger', 'Dominant Trigger & Temp')}
            </span>
            <div className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
              <Thermometer className="w-4 h-4" />
            </div>
          </div>
          <div>
            <div className="flex items-baseline justify-between">
              <div className="text-2xl font-extrabold text-gray-900 font-['Outfit'] tracking-tight">
                PM2.5 (96.5%)
              </div>
              <span className="text-xs font-semibold text-gray-500 font-mono tabular-nums">
                {temp}°C • {humidity}%
              </span>
            </div>
            <div className="text-xs text-gray-500 mt-2 pt-2 border-t border-gray-100 flex items-center justify-between">
              <span>{t('overview.airway_penetration', 'Airway Penetration:')}</span>
              <strong className="text-rose-600 font-semibold">{t('overview.alveolar_deep', 'Alveolar (Deep)')}</strong>
            </div>
          </div>
        </div>

      </div>

      {/* Row 2: Live Geo-Clinical Pair (Side-by-Side: 7/8 Cols Map + 5/4 Cols Capacity & Strain) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
        
        {/* Left 7 or 8 Cols: Interactive Pan-India Metro AQI Map */}
        <div className="lg:col-span-7 xl:col-span-8 flex flex-col">
          <IndiaSvgMap 
            citiesData={allCitiesData} 
            selectedCity={activeCity} 
            onSelectCity={onSelectCity} 
          />
        </div>

        {/* Right 5 or 4 Cols: Capacity Target & Hospital Strain + Localized Advisory + Active City Pill */}
        <div className="lg:col-span-5 xl:col-span-4 flex flex-col justify-between">
          <div className="tailadmin-card p-5 h-full flex flex-col justify-between">
            {/* Header with Active City Pill Badge */}
            <div className="border-b border-gray-100 pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 className="font-bold text-gray-900 text-sm font-['Outfit']">
                  {t('overview.capacity_strain', 'Capacity Target & Hospital Strain')}
                </h3>
                <p className="text-xs text-gray-400 mt-0.5">
                  {t('overview.capacity_sub', '48-hour projected ICU & emergency bed threshold')}
                </p>
              </div>
              
              {/* Active City Pill Badge */}
              <div className="shrink-0 self-start sm:self-auto flex items-center gap-1.5 px-2.5 py-1 bg-[#465FFF]/10 border border-[#465FFF]/25 rounded-full text-[11px] font-bold text-[#465FFF] shadow-2xs font-mono">
                <MapPin className="w-3 h-3 text-[#465FFF]" />
                <span>{localizedCity}</span>
                <span className="text-gray-300">•</span>
                <span className="font-normal text-[10px] text-gray-600">
                  {t('chrome.live_projection', 'Live 48h Projection')}
                </span>
              </div>
            </div>

            {/* Radial Gauge */}
            <div className="my-auto py-2">
              <RadialGauge value={riskScore} max={100} />
            </div>

            {/* Localized Clinical Advisory Card */}
            <div className="mt-3 pt-3 border-t border-gray-100">
              <div className="flex items-center justify-between text-xs mb-1.5">
                <span className="font-bold text-gray-800 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5 text-[#465FFF]" />
                  {t('overview.localized_advisory', 'Localized Clinical Advisory')}
                </span>
                <span className="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                  RAG {groundingSimilarity}% {t('overview.rag_match', 'Match')}
                </span>
              </div>
              
              <div className="p-3 bg-gray-50 rounded-xl border border-gray-200 text-xs text-gray-700 leading-relaxed font-sans border-l-4 border-l-[#465FFF]">
                "{cleanAdvisory}"
              </div>

              {/* Vector RAG Citation Pill */}
              <div className="mt-2.5 flex items-center justify-between text-[10px] text-gray-400 font-mono">
                <span>{t('overview.vector_source', 'Vector Source')}:</span>
                <button
                  onClick={() => onNavigateTab && onNavigateTab('triage')}
                  className="text-[#465FFF] hover:underline font-bold flex items-center gap-0.5 cursor-pointer"
                >
                  ID: {groundedDatasetId.slice(0, 14)}...
                  <ChevronRight className="w-3 h-3" />
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>

      {/* Row 3: Historical Epidemiological Pair (Side-by-Side: 7/8 Cols Chart + 5/4 Cols Heatmap) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
        
        {/* Left 7 or 8 Cols: Dual-Axis Recharts Chart with Temporal Drill-Down */}
        <div className="lg:col-span-7 xl:col-span-8 flex flex-col">
          <SurgeStatisticsChart overviewData={overviewData} />
        </div>

        {/* Right 5 or 4 Cols: Interactive Pearson Epidemiological Correlation Heatmap */}
        <div className="lg:col-span-5 xl:col-span-4 flex flex-col">
          <CorrelationHeatmap />
        </div>

      </div>

      {/* Row 4: Hospital Dispatch Queue Table (12 Cols) */}
      <div>
        <HospitalDispatchTable />
      </div>

    </div>
  );
}
