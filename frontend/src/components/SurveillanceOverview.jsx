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
  ChevronRight
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

  return (
    <div className="space-y-6">

      {/* Row 1: 4 TailAdmin KPI Cards */}
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
                {cpcbCategory}
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
                High Surge
              </span>
            </div>
            <div className="flex items-center justify-between text-xs text-gray-500 mt-2 pt-2 border-t border-gray-100">
              <span>{t('overview.projected_admissions', 'Projected Admissions')}:</span>
              <strong className="text-gray-900 font-mono tabular-nums">{admissions} pts/day</strong>
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
              Civic vehicle restrictions & primary school warnings active.
            </p>
            <div className="text-[10px] font-semibold text-[#465FFF] mt-2 pt-2 border-t border-gray-100 flex items-center gap-1">
              <span>CAQM Statutory Schedule (17 Pages)</span>
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
              <span>Airway Penetration:</span>
              <strong className="text-rose-600 font-semibold">Alveolar (Deep)</strong>
            </div>
          </div>
        </div>

      </div>

      {/* Row 2: 8-Col + 4-Col Bento Split */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        {/* Left 8 Cols: Dual-Axis Recharts Chart with Temporal Drill-Down */}
        <div className="lg:col-span-8">
          <SurgeStatisticsChart overviewData={overviewData} />
        </div>

        {/* Right 4 Cols: Radial Gauge + Localized Advisory + RAG Badge */}
        <div className="lg:col-span-4 space-y-4">
          <div className="tailadmin-card p-5 flex flex-col justify-between">
            <div className="border-b border-gray-100 pb-3">
              <h3 className="font-bold text-gray-900 text-sm font-['Outfit']">
                {t('overview.capacity_strain', 'Capacity Target & Hospital Strain')}
              </h3>
              <p className="text-xs text-gray-400 mt-0.5">
                48-hour projected ICU & emergency bed threshold
              </p>
            </div>

            {/* Radial Gauge */}
            <RadialGauge value={riskScore} max={100} />

            {/* Localized Clinical Advisory Card */}
            <div className="mt-4 pt-3 border-t border-gray-100">
              <div className="flex items-center justify-between text-xs mb-1.5">
                <span className="font-bold text-gray-800 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5 text-[#465FFF]" />
                  {t('overview.localized_advisory', 'Localized Clinical Advisory')}
                </span>
                <span className="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                  RAG {groundingSimilarity}% Match
                </span>
              </div>
              <div className="p-3 bg-gray-50 rounded-xl border border-gray-200 text-xs text-gray-700 leading-relaxed font-sans border-l-4 border-l-[#465FFF]">
                "{localizedAdvisory}"
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

      {/* Row 3: 6-Col + 6-Col Bento Split */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        {/* Left 6 Cols: Interactive Esri Light Canvas Map of India with 12 Metros & Leaderboard */}
        <div className="lg:col-span-6">
          <IndiaSvgMap 
            citiesData={allCitiesData} 
            selectedCity={activeCity} 
            onSelectCity={onSelectCity} 
          />
        </div>

        {/* Right 6 Cols: Interactive Pearson Epidemiological Correlation Heatmap */}
        <div className="lg:col-span-6">
          <CorrelationHeatmap />
        </div>

      </div>

      {/* Row 4: Hospital Dispatch Queue Table */}
      <div>
        <HospitalDispatchTable />
      </div>

    </div>
  );
}
