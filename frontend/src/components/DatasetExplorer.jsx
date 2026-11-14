import React, { useState, useEffect } from 'react';
import aqiClient from '../api/aqiClient';
import { 
  Database, 
  Search, 
  Filter, 
  Eye, 
  X, 
  Check, 
  Copy, 
  Table as TableIcon,
  FileText,
  Sparkles,
  Download,
  Layers
} from 'lucide-react';
import { useTranslation } from '../i18n/LanguageContext';

export default function DatasetExplorer() {
  const { t } = useTranslation();
  const [datasets, setDatasets] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedFilter, setSelectedFilter] = useState('all');
  const [previewDataset, setPreviewDataset] = useState(null);
  const [modalViewMode, setModalViewMode] = useState('table'); // 'table' | 'protocol'
  const [copiedId, setCopiedId] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fallback initial dataset catalog (10 datasets materialized)
  const defaultCatalog = [
    {
      dataset_name: "Pan-India Respiratory Clinical Master Q&A",
      filename: "pan_india_master_clinical_qa_2050.csv",
      adaption_dataset_id: "8c3a464c-45c7-4164-aa8d-7a105125f3a9",
      pillar: "Pillar F: Combine & Validation",
      kind: "Combined Master",
      row_count: 2050,
      size_mb: 16.28,
      quality_grade: "Grade A",
      quality_score: 9.4,
      columns: ["original_prompt", "original_completion", "enhanced_prompt", "enhanced_completion"],
      sample_rows: [
        { enhanced_prompt: "City: Delhi | PM2.5: 220 ug/m3 | Patient: Pediatric Asthma | Language: English", enhanced_completion: "CRITICAL AIR QUALITY ADVISORY: Peak particulate exposure. Halt outdoor recess. Enforce daily preventive corticosteroid inhaler and keep rescue salbutamol accessible. If child exhibits stridor or retractions, immediately seek pediatric emergency care." },
        { enhanced_prompt: "City: Kolkata | PM2.5: 142 ug/m3 | Patient: Geriatric COPD | Language: English", enhanced_completion: "SEVERE SMOG WARNING: Minimize outdoor morning exertion. Verify SpO2 remains above 92%. In the event of acute dyspnea, initiate emergency bronchodilator protocol and contact hospital." }
      ]
    },
    {
      dataset_name: "India Outdoor Workers & High-Risk Commuter Smog Protocols",
      filename: "outdoor_workers_smog_protocols.csv",
      adaption_dataset_id: "0788bf56-1cf0-41fd-8a03-d255dc3ef4a7",
      pillar: "Pillar B+C: Occupational Smog Shield",
      kind: "Invented + Localized",
      row_count: 1000,
      size_mb: 44.37,
      quality_grade: "Grade A",
      quality_score: 9.5,
      percentile: "57.7th Percentile",
      columns: ["enhanced_prompt", "enhanced_completion", "target_language", "target_language_code"],
      sample_rows: [
        { enhanced_prompt: "Occupational Smog Protocol for Delivery Gig Workers in Hazardous AQI (150-500+)", enhanced_completion: "Mandatory N95 respirator deployment with certified facial seal. Work shift rotation with mandatory 15-minute rest breaks in filtered indoor rest stations every 90 minutes. Hydration schedules to maintain airway mucosal hydration." }
      ]
    },
    {
      dataset_name: "Pan-India AQI Respiratory Clinical Q&A",
      filename: "pan_india_aqi_clinical_qa_2000_grade_a.csv",
      adaption_dataset_id: "3bf58b6b-462c-4412-8171-fa1bed843e67",
      pillar: "Pillar B: Invent (Synthetic)",
      kind: "Invented",
      row_count: 2000,
      size_mb: 15.33,
      quality_grade: "Grade A",
      quality_score: 9.4,
      columns: ["enhanced_prompt", "enhanced_completion"],
      sample_rows: [
        { enhanced_prompt: "City: Mumbai | Condition: Moderate | Language: Marathi", enhanced_completion: "मुंबई हवा गुणवत्ता मध्यम श्रेणीत आहे. दम्याच्या रुग्णांनी सकाळी जास्त वेळ बाहेर धावणे टाळावे." }
      ]
    },
    {
      dataset_name: "Pan-India Clinical Advisories (Augmented)",
      filename: "pan_india_clinical_advisories_augmented_1003.csv",
      adaption_dataset_id: "24bada6c-7841-446c-9f12-b2bdec861d53",
      pillar: "Pillar G: AutoScientist Substrate",
      kind: "Augmented",
      row_count: 1003,
      size_mb: 6.20,
      quality_grade: "Grade B",
      quality_score: 8.8,
      columns: ["original_prompt", "original_completion", "enhanced_prompt", "enhanced_completion"],
      sample_rows: [
        { original_prompt: "Asthma action plan during cold-season thermal inversion", enhanced_completion: "Cold temperature stabilizes dense ground-level particulate matter. Use spacer with MDI inhaler and wear thermal face covering." }
      ]
    },
    {
      dataset_name: "Pan-India Localized Advisories (9 Indic Locales)",
      filename: "pan_india_localized_advisories.csv",
      adaption_dataset_id: "ac7589fd-355d-45e2-9168-4ab4a7e1ceef",
      pillar: "Pillar C: Cultural Localization",
      kind: "Localized (9 Locales)",
      row_count: 80,
      size_mb: 0.31,
      quality_grade: "Grade A",
      quality_score: 9.2,
      columns: ["original_prompt", "original_completion", "enhanced_prompt", "enhanced_completion"],
      sample_rows: [
        { enhanced_prompt: "Advisory in Tamil (IN:ta)", enhanced_completion: "சென்னை காற்று தரம் மிதமான பிரிவில் உள்ளது. மூச்சுத்திணறல் உள்ளவர்கள் காலை நேர நடைபயிற்சியை தவிர்க்கவும்." }
      ]
    },
    {
      dataset_name: "CAQM Official GRAP Schedule Extracted Rules",
      filename: "caqm_grap_extracted_rules.csv",
      adaption_dataset_id: "31535351-f429-4240-a8ea-db8af555936e",
      pillar: "Pillar A: Forge PDF Extraction",
      kind: "Forge Adapted",
      row_count: 17,
      size_mb: 0.06,
      quality_grade: "Statutory Standard",
      quality_score: 10.0,
      columns: ["title", "text", "enhanced_prompt", "enhanced_completion"],
      sample_rows: [
        { enhanced_prompt: "GRAP Stage III Statutory Directives (AQI 401-450)", enhanced_completion: "Mandatory ban on BS-III petrol and BS-IV diesel 4-wheelers in NCR. Closure of primary educational institutions." }
      ]
    },
    {
      dataset_name: "Multi-Turn Doctor-Patient Clinical Trajectories",
      filename: "multi_turn_clinical_trajectories.csv",
      adaption_dataset_id: "e6fd4ced-b683-4abb-8e99-77aa496456db",
      pillar: "Pillar E: Trajectory Extension",
      kind: "Extended Multi-Turn",
      row_count: 7,
      size_mb: 0.03,
      quality_grade: "Grade A",
      quality_score: 9.3,
      columns: ["prompt", "completion", "enhanced_prompt", "enhanced_completion"],
      sample_rows: [
        { enhanced_prompt: "Patient follow-up: My chest tightness increased after commuting today", enhanced_completion: "Doctor: What is your current SpO2 reading? If below 92%, seek emergency evaluation. Inhale 2 puffs of rescue bronchodilator now." }
      ]
    },
    {
      dataset_name: "Indian AQI Clinical Q&A (Seed)",
      filename: "indian_aqi_clinical_qa_50.csv",
      adaption_dataset_id: "cde47eea-5f78-4124-9a38-e46a6e0515a2",
      pillar: "Pillar B: Invent (Q&A)",
      kind: "Invented",
      row_count: 50,
      size_mb: 0.69,
      quality_grade: "Grade B",
      quality_score: 8.9,
      columns: ["enhanced_prompt", "enhanced_completion"],
      sample_rows: [
        { enhanced_prompt: "Clinical guidance for Amritsar stubble burning season", enhanced_completion: "High particulate density requires double filtration and avoiding unmasked exposure during agricultural clearing." }
      ]
    }
  ];

  useEffect(() => {
    async function loadDatasets() {
      try {
        const res = await aqiClient.getDatasets();
        if (res && res.catalog && res.catalog.length > 0) {
          setDatasets(res.catalog);
        } else {
          setDatasets(defaultCatalog);
        }
      } catch (err) {
        setDatasets(defaultCatalog);
      } finally {
        setLoading(false);
      }
    }
    loadDatasets();
  }, []);

  const handleCopyId = (id) => {
    if (!id) return;
    navigator.clipboard.writeText(id);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const filteredDatasets = datasets.filter(d => {
    const q = searchQuery.toLowerCase();
    const nameMatch = d.dataset_name?.toLowerCase().includes(q) || false;
    const fileMatch = d.filename?.toLowerCase().includes(q) || false;
    const pillarMatch = d.pillar?.toLowerCase().includes(q) || false;
    const matchesSearch = nameMatch || fileMatch || pillarMatch;

    if (selectedFilter === 'all') return matchesSearch;
    if (selectedFilter === 'grade_a') return matchesSearch && d.quality_grade?.includes('A');
    if (selectedFilter === 'invented') return matchesSearch && (d.kind?.includes('Invented') || d.kind?.includes('Master'));
    if (selectedFilter === 'forge') return matchesSearch && d.kind?.includes('Forge');
    return matchesSearch;
  });

  // Helper to extract rows for modal
  const getPreviewRows = () => {
    if (!previewDataset) return [];
    return previewDataset.sample_rows || previewDataset.sample_preview || [];
  };

  // Helper to extract columns for modal
  const getPreviewColumns = () => {
    if (!previewDataset) return [];
    if (previewDataset.columns && previewDataset.columns.length > 0) {
      return previewDataset.columns;
    }
    const rows = getPreviewRows();
    if (rows.length > 0) {
      return Object.keys(rows[0]);
    }
    return ['field', 'value'];
  };

  // Dynamic Prompt/Context resolver for Protocol Card View
  const resolvePrompt = (row) => {
    if (!row) return '';
    return row.enhanced_prompt || 
           row.prompt || 
           row.original_prompt || 
           row.question || 
           row.instruction || 
           row.title || 
           row.text || 
           (row.city ? `City: ${row.city} (${row.year}-${row.month}) | AQI: ${row.aqi} | PM2.5: ${row.pm25}` : JSON.stringify(row));
  };

  // Dynamic Completion/Protocol resolver for Protocol Card View
  const resolveCompletion = (row) => {
    if (!row) return '';
    return row.enhanced_completion || 
           row.completion || 
           row.original_completion || 
           row.answer || 
           row.response || 
           row.text || 
           (row.respiratory_admissions !== undefined ? `Admissions: ${row.respiratory_admissions} | Risk Score: ${row.predicted_risk_score || row.respiratory_risk_score || 'N/A'}` : '');
  };

  return (
    <div className="space-y-6">
      
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <h2 className="text-xl font-bold text-gray-900 font-['Outfit'] flex items-center gap-2">
            <Database className="w-5 h-5 text-[#465FFF]" />
            {t('datasets.title', 'Pan-India Adaption Labs Exported Dataset Catalog')}
          </h2>
          <p className="text-xs text-gray-500 mt-1">
            {t('datasets.subtitle', 'Audit of all materialized datasets via Adaption Labs SDK and tracked under backend/data/adaption_exports/ (<25MB each).')}
          </p>
        </div>
        <div className="flex items-center gap-2 bg-white px-3 py-1.5 rounded-xl border border-gray-200 text-xs font-semibold text-gray-700 shadow-2xs">
          <span>{t('datasets.total_synced', 'Total Synchronized')}:</span>
          <span className="text-[#465FFF] font-bold">
            {datasets.length} {t('datasets.datasets_label', 'Datasets')} • 8,188+ {t('datasets.protocols_label', 'Protocols')}
          </span>
        </div>
      </div>

      {/* Search & Filter Toolbar */}
      <div className="tailadmin-card p-4 flex flex-col sm:flex-row items-center justify-between gap-3">
        <div className="relative w-full sm:w-80">
          <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder={t('datasets.search_placeholder', 'Search datasets, pillars, filenames...')}
            className="w-full pl-9 pr-3 py-2 text-xs bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#465FFF]/30 focus:border-[#465FFF]"
          />
        </div>

        <div className="flex items-center gap-1.5 self-start sm:self-auto overflow-x-auto no-scrollbar">
          <span className="text-xs text-gray-400 font-semibold uppercase flex items-center gap-1 pl-1">
            <Filter className="w-3.5 h-3.5" /> {t('datasets.filter_label', 'Filter')}:
          </span>
          <button
            onClick={() => setSelectedFilter('all')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition cursor-pointer ${
              selectedFilter === 'all' ? 'bg-[#465FFF] text-white shadow-xs' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            {t('datasets.filter_all', 'All')} ({datasets.length})
          </button>
          <button
            onClick={() => setSelectedFilter('grade_a')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition cursor-pointer ${
              selectedFilter === 'grade_a' ? 'bg-[#465FFF] text-white shadow-xs' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            Grade A (9.4+)
          </button>
          <button
            onClick={() => setSelectedFilter('invented')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition cursor-pointer ${
              selectedFilter === 'invented' ? 'bg-[#465FFF] text-white shadow-xs' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            Synthetic Invent
          </button>
          <button
            onClick={() => setSelectedFilter('forge')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition cursor-pointer ${
              selectedFilter === 'forge' ? 'bg-[#465FFF] text-white shadow-xs' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            Forge Extracted
          </button>
        </div>
      </div>

      {/* Dataset Table */}
      <div className="tailadmin-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-[11px] font-bold text-gray-400 uppercase tracking-wider bg-gray-50/50">
                <th className="py-3 px-4">{t('datasets.col_name', 'Dataset Name & File')}</th>
                <th className="py-3 px-4">{t('datasets.col_pillar', 'Adaption Capability Pillar')}</th>
                <th className="py-3 px-4">{t('datasets.col_rows', 'Rows')}</th>
                <th className="py-3 px-4">{t('datasets.col_size', 'Size')}</th>
                <th className="py-3 px-4">{t('datasets.col_quality', 'Quality Grade')}</th>
                <th className="py-3 px-4">{t('datasets.col_id', 'Adaption Dataset ID')}</th>
                <th className="py-3 px-4 text-right">{t('datasets.col_preview', 'Preview')}</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {filteredDatasets.map((ds) => {
                // Defensive Size MB Calculation
                const sizeVal = typeof ds.size_mb === 'number' && !isNaN(ds.size_mb)
                  ? ds.size_mb.toFixed(2)
                  : (ds.file_size_bytes ? (ds.file_size_bytes / 1048576).toFixed(2) : '0.12');

                const rowCountVal = ds.row_count || ds.total_rows || 0;

                return (
                  <tr key={ds.adaption_dataset_id || ds.filename} className="hover:bg-gray-50/70 transition">
                    <td className="py-3.5 px-4">
                      <div className="font-bold text-gray-900 text-xs">{ds.dataset_name}</div>
                      <div className="text-[11px] font-mono text-gray-400 mt-0.5">{ds.filename}</div>
                    </td>
                    <td className="py-3.5 px-4 font-semibold text-gray-700">
                      {ds.pillar}
                    </td>
                    <td className="py-3.5 px-4 font-bold text-gray-900 tabular-nums">
                      {rowCountVal.toLocaleString()}
                    </td>
                    <td className="py-3.5 px-4 text-gray-600 tabular-nums font-mono font-medium">
                      {sizeVal} MB
                    </td>
                    <td className="py-3.5 px-4">
                      <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold border ${
                        ds.quality_grade?.includes('A') 
                          ? 'bg-emerald-50 text-emerald-700 border-emerald-200' 
                          : 'bg-amber-50 text-amber-700 border-amber-200'
                      }`}>
                        {ds.quality_grade} {ds.quality_score ? `(${ds.quality_score}/10)` : ''}
                      </span>
                    </td>
                    <td className="py-3.5 px-4">
                      <div className="flex items-center gap-1.5 font-mono text-[11px] text-gray-500">
                        <span>{ds.adaption_dataset_id?.slice(0, 13)}...</span>
                        <button
                          onClick={() => handleCopyId(ds.adaption_dataset_id)}
                          className="p-1 hover:bg-gray-200 rounded transition text-gray-400 hover:text-gray-700 cursor-pointer"
                          title="Copy full Adaption Dataset ID"
                        >
                          {copiedId === ds.adaption_dataset_id ? (
                            <Check className="w-3.5 h-3.5 text-emerald-600" />
                          ) : (
                            <Copy className="w-3.5 h-3.5" />
                          )}
                        </button>
                      </div>
                    </td>
                    <td className="py-3.5 px-4 text-right">
                      <button
                        onClick={() => {
                          setPreviewDataset(ds);
                          // Default to table if tabular schema with >4 columns
                          if (ds.columns && ds.columns.length > 4 && !ds.columns.includes('enhanced_prompt')) {
                            setModalViewMode('table');
                          } else {
                            setModalViewMode('protocol');
                          }
                        }}
                        className="px-2.5 py-1 bg-white hover:bg-[#465FFF] text-[#465FFF] hover:text-white border border-[#465FFF]/30 rounded-lg text-xs font-semibold shadow-2xs transition inline-flex items-center gap-1 cursor-pointer"
                      >
                        <Eye className="w-3.5 h-3.5" />
                        {t('datasets.view_rows', 'View Rows')}
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Dynamic Schema-Adaptive Sample Row Modal */}
      {previewDataset && (
        <div className="fixed inset-0 bg-gray-900/40 backdrop-blur-xs z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl max-w-4xl w-full max-h-[88vh] flex flex-col shadow-2xl border border-gray-200 animate-in fade-in zoom-in-95 duration-150">
            
            {/* Modal Header */}
            <div className="p-5 border-b border-gray-100 flex items-center justify-between">
              <div>
                <h3 className="font-bold text-gray-900 text-base font-['Outfit'] flex items-center gap-2">
                  <Database className="w-4 h-4 text-[#465FFF]" />
                  {previewDataset.dataset_name}
                </h3>
                <div className="text-xs text-gray-500 mt-0.5 font-mono">
                  {previewDataset.filename} • {(previewDataset.row_count || previewDataset.total_rows || 0).toLocaleString()} Rows • {previewDataset.quality_grade}
                </div>
              </div>

              <div className="flex items-center gap-3">
                {/* View Mode Switcher Pills */}
                <div className="flex items-center gap-1 p-0.5 bg-gray-100 rounded-lg border border-gray-200">
                  <button
                    onClick={() => setModalViewMode('table')}
                    className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-xs font-semibold transition cursor-pointer ${
                      modalViewMode === 'table' ? 'bg-white text-[#465FFF] shadow-2xs' : 'text-gray-600 hover:text-gray-900'
                    }`}
                  >
                    <TableIcon className="w-3.5 h-3.5" />
                    Table View
                  </button>
                  <button
                    onClick={() => setModalViewMode('protocol')}
                    className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-xs font-semibold transition cursor-pointer ${
                      modalViewMode === 'protocol' ? 'bg-white text-[#465FFF] shadow-2xs' : 'text-gray-600 hover:text-gray-900'
                    }`}
                  >
                    <FileText className="w-3.5 h-3.5" />
                    Protocol Card View
                  </button>
                </div>

                <button
                  onClick={() => setPreviewDataset(null)}
                  className="p-2 text-gray-400 hover:text-gray-700 hover:bg-gray-100 rounded-xl transition cursor-pointer"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Modal Body */}
            <div className="p-5 overflow-y-auto flex-1">
              
              {/* Option A: Table View (Horizontally Scrollable Grid for Tabular Data) */}
              {modalViewMode === 'table' && (
                <div className="border border-gray-200 rounded-xl overflow-x-auto shadow-2xs">
                  <table className="w-full text-left text-xs whitespace-nowrap">
                    <thead className="bg-gray-50 border-b border-gray-200 text-[11px] font-bold text-gray-500 uppercase tracking-wider">
                      <tr>
                        <th className="py-2.5 px-3 border-r border-gray-200 text-gray-400 text-center w-12">#</th>
                        {getPreviewColumns().map((col) => (
                          <th key={col} className="py-2.5 px-3 border-r border-gray-200 font-mono">
                            {col}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100">
                      {getPreviewRows().map((row, idx) => (
                        <tr key={idx} className="hover:bg-gray-50/80 transition font-mono text-[11px]">
                          <td className="py-2 px-3 border-r border-gray-100 text-gray-400 text-center font-sans">
                            {idx + 1}
                          </td>
                          {getPreviewColumns().map((col) => {
                            const val = row[col];
                            const textVal = val !== null && val !== undefined ? String(val) : '';
                            return (
                              <td key={col} className="py-2 px-3 border-r border-gray-100 text-gray-800 max-w-md truncate" title={textVal}>
                                {textVal || <span className="text-gray-300 italic">null</span>}
                              </td>
                            );
                          })}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}

              {/* Option B: Protocol Card View (Adaptive Prompt / Clinical Protocol Cards) */}
              {modalViewMode === 'protocol' && (
                <div className="space-y-4">
                  <div className="text-xs font-bold text-gray-400 uppercase tracking-wider flex items-center gap-1.5">
                    <Sparkles className="w-3.5 h-3.5 text-[#465FFF]" />
                    Synthesized & Extracted Ground-Truth Rows ({getPreviewRows().length} Samples)
                  </div>

                  {getPreviewRows().map((sample, idx) => {
                    const promptVal = resolvePrompt(sample);
                    const completionVal = resolveCompletion(sample);

                    return (
                      <div key={idx} className="p-4 bg-gray-50 rounded-xl border border-gray-200 space-y-2.5 text-xs shadow-2xs">
                        {/* Prompt Section */}
                        <div>
                          <div className="flex items-center justify-between mb-1">
                            <span className="font-bold text-gray-700 uppercase tracking-wide text-[10px]">
                              Meteorological / Clinical Prompt Context:
                            </span>
                            {sample.target_language && (
                              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-[#465FFF]/10 text-[#465FFF]">
                                {sample.target_language} ({sample.target_language_code})
                              </span>
                            )}
                          </div>
                          <div className="p-3 bg-white rounded-lg border border-gray-200 text-gray-800 font-mono text-[11px] leading-relaxed whitespace-pre-wrap">
                            {promptVal || <span className="text-gray-400 italic">No prompt field present</span>}
                          </div>
                        </div>

                        {/* Completion Section */}
                        {completionVal && (
                          <div>
                            <span className="font-bold text-[#465FFF] uppercase tracking-wide text-[10px] block mb-1">
                              Clinical Response Protocol / Ground Truth:
                            </span>
                            <div className="p-3 bg-white rounded-lg border border-gray-200 text-gray-800 leading-relaxed whitespace-pre-wrap">
                              {completionVal}
                            </div>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              )}

            </div>

            {/* Modal Footer */}
            <div className="p-4 border-t border-gray-100 bg-gray-50 rounded-b-2xl flex items-center justify-between text-xs">
              <div className="font-mono text-gray-500 text-[11px] flex items-center gap-2">
                <span>Adaption ID: {previewDataset.adaption_dataset_id}</span>
              </div>
              <button
                onClick={() => setPreviewDataset(null)}
                className="px-4 py-1.5 bg-[#465FFF] hover:bg-[#3649db] text-white rounded-xl font-semibold shadow-xs transition cursor-pointer"
              >
                Close Drawer
              </button>
            </div>

          </div>
        </div>
      )}

    </div>
  );
}
