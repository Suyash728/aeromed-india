import React from 'react';
import { useTranslation } from '../i18n/LanguageContext';

export default function RadialGauge({ value = 78, max = 100, label }) {
  const { t } = useTranslation();
  const percentage = Math.min(Math.max(value / max, 0), 1);
  const strokeWidth = 14;
  const radius = 80;
  const circumference = Math.PI * radius; // Semi-circle circumference
  const strokeDashoffset = circumference - (percentage * circumference);

  // Determine severity color & translated status
  let color = '#12B76A'; // Safe
  let statusText = t('overview.safe_capacity', 'Safe Capacity');
  let badgeBg = 'bg-emerald-50 text-emerald-700 border-emerald-200';

  if (value > 80) {
    color = '#D92D20'; // Critical Emergency
    statusText = t('overview.critical_surge_alert', 'Critical Surge Alert');
    badgeBg = 'bg-rose-50 text-rose-700 border-rose-200';
  } else if (value > 60) {
    color = '#F04438'; // Severe
    statusText = t('overview.high_surge_risk', 'High Surge Risk');
    badgeBg = 'bg-orange-50 text-orange-700 border-orange-200';
  } else if (value > 35) {
    color = '#F79009'; // Moderate
    statusText = t('overview.moderate_strain', 'Moderate Strain');
    badgeBg = 'bg-amber-50 text-amber-700 border-amber-200';
  }

  return (
    <div className="flex flex-col items-center justify-center p-2">
      <div className="relative w-48 h-28 flex items-center justify-center">
        <svg 
          viewBox="0 0 200 120" 
          className="w-full h-full overflow-visible"
        >
          {/* Background Arc */}
          <path
            d="M 20 100 A 80 80 0 0 1 180 100"
            fill="none"
            stroke="#F2F4F7"
            strokeWidth={strokeWidth}
            strokeLinecap="round"
          />
          {/* Colored Value Arc */}
          <path
            d="M 20 100 A 80 80 0 0 1 180 100"
            fill="none"
            stroke={color}
            strokeWidth={strokeWidth}
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            strokeLinecap="round"
            style={{ transition: 'stroke-dashoffset 0.8s ease-out, stroke 0.4s ease' }}
          />
        </svg>

        {/* Center Number & Label */}
        <div className="absolute bottom-1 flex flex-col items-center justify-center">
          <div className="text-3xl font-extrabold text-gray-900 tracking-tight tabular-nums font-['Outfit']">
            {value}
            <span className="text-sm font-semibold text-gray-400">/{max}</span>
          </div>
          <div className="text-[11px] font-semibold text-gray-500 uppercase tracking-wider">
            {t('overview.surge_score', 'Surge Score')}
          </div>
        </div>
      </div>

      {/* Status Pill */}
      <div className={`mt-2 px-3 py-1 rounded-full text-xs font-bold border ${badgeBg} tracking-wide`}>
        {statusText}
      </div>
    </div>
  );
}
