import React, { useState } from 'react';

const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

// Mock monthly data for India respiratory surge trends
const DATA_SETS = {
  overview: {
    title: 'Seasonal Respiratory Surge Correlation (AQI vs Admissions)',
    line1: [180, 190, 170, 160, 160, 175, 165, 170, 200, 210, 240, 235], // PM2.5 / AQI Index
    line2: [40, 30, 50, 40, 55, 40, 70, 100, 110, 120, 150, 140],     // ICU Admissions / 100k
    label1: 'Average PM2.5 Index',
    label2: 'Patient Admissions',
  },
  pm25: {
    title: '12-Month Regional PM2.5 Concentration Trend',
    line1: [220, 250, 190, 140, 110, 90, 85, 95, 160, 280, 350, 340],
    line2: [180, 190, 170, 160, 160, 175, 165, 170, 200, 210, 240, 235],
    label1: 'Peak PM2.5',
    label2: 'Baseline AQI',
  },
  admissions: {
    title: 'Monthly Hospital Emergency Ward Admissions',
    line1: [80, 95, 70, 60, 50, 45, 60, 90, 130, 190, 240, 220],
    line2: [40, 30, 50, 40, 55, 40, 70, 100, 110, 120, 150, 140],
    label1: 'ICU Surge',
    label2: 'Normal Ward',
  }
};

export default function SurgeStatisticsChart() {
  const [activeTab, setActiveTab] = useState('overview');
  const currentData = DATA_SETS[activeTab];

  return (
    <div className="panel" style={{ marginTop: '24px' }}>
      {/* Header & Tabs */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px', marginBottom: '20px' }}>
        <div>
          <h2 style={{ fontSize: '16px', fontWeight: '700', color: '#f9fafb' }}>
            📊 {currentData.title}
          </h2>
          <p style={{ fontSize: '12px', color: '#9ca3af', marginTop: '2px' }}>
            Comparative historical analytics powered by Adaption AI regression pipeline.
          </p>
        </div>

        <div style={{ display: 'flex', background: 'var(--main-bg)', padding: '4px', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
          <button 
            onClick={() => setActiveTab('overview')}
            style={{ padding: '6px 12px', fontSize: '11px', fontWeight: '600', borderRadius: '6px', border: 'none', background: activeTab === 'overview' ? '#3b82f6' : 'transparent', color: activeTab === 'overview' ? '#fff' : '#9ca3af', cursor: 'pointer' }}
          >
            Overview
          </button>
          <button 
            onClick={() => setActiveTab('pm25')}
            style={{ padding: '6px 12px', fontSize: '11px', fontWeight: '600', borderRadius: '6px', border: 'none', background: activeTab === 'pm25' ? '#3b82f6' : 'transparent', color: activeTab === 'pm25' ? '#fff' : '#9ca3af', cursor: 'pointer' }}
          >
            PM2.5 Index
          </button>
          <button 
            onClick={() => setActiveTab('admissions')}
            style={{ padding: '6px 12px', fontSize: '11px', fontWeight: '600', borderRadius: '6px', border: 'none', background: activeTab === 'admissions' ? '#3b82f6' : 'transparent', color: activeTab === 'admissions' ? '#fff' : '#9ca3af', cursor: 'pointer' }}
          >
            Admissions
          </button>
        </div>
      </div>

      {/* SVG Smooth Line & Area Graph */}
      <div style={{ background: 'var(--main-bg)', border: '1px solid var(--border-color)', borderRadius: '12px', padding: '20px', position: 'relative' }}>
        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '16px', fontSize: '11px', marginBottom: '10px' }}>
          <span style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#3b82f6' }}>
            <span style={{ width: '10px', height: '10px', background: '#3b82f6', borderRadius: '50%' }}></span> {currentData.label1}
          </span>
          <span style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#06b6d4' }}>
            <span style={{ width: '10px', height: '10px', background: '#06b6d4', borderRadius: '50%' }}></span> {currentData.label2}
          </span>
        </div>

        <svg viewBox="0 0 800 220" style={{ width: '100%', height: '190px', overflow: 'visible' }}>
          {/* Grid lines */}
          <line x1="0" y1="40" x2="800" y2="40" stroke="#374151" strokeDasharray="4 4" strokeWidth="0.8" />
          <line x1="0" y1="100" x2="800" y2="100" stroke="#374151" strokeDasharray="4 4" strokeWidth="0.8" />
          <line x1="0" y1="160" x2="800" y2="160" stroke="#374151" strokeDasharray="4 4" strokeWidth="0.8" />

          {/* Line 2 (Cyan) */}
          <path
            d={`M ${currentData.line2.map((val, idx) => `${(idx / 11) * 780 + 10},${200 - (val / 380) * 180}`).join(' L ')}`}
            fill="none"
            stroke="#06b6d4"
            strokeWidth="3"
            strokeLinecap="round"
          />

          {/* Line 1 (Blue) */}
          <path
            d={`M ${currentData.line1.map((val, idx) => `${(idx / 11) * 780 + 10},${200 - (val / 380) * 180}`).join(' L ')}`}
            fill="none"
            stroke="#3b82f6"
            strokeWidth="3"
            strokeLinecap="round"
          />
        </svg>

        {/* X-Axis Months */}
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px', padding: '0 4px', color: '#9ca3af', fontSize: '11px', fontWeight: '600' }}>
          {MONTHS.map((m) => (
            <span key={m}>{m}</span>
          ))}
        </div>
      </div>
    </div>
  );
}