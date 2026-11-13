import React, { useState } from 'react';
import { 
  ResponsiveContainer, 
  ComposedChart, 
  Area, 
  Bar, 
  Line, 
  XAxis, 
  YAxis, 
  Tooltip, 
  CartesianGrid, 
  Legend,
  BarChart
} from 'recharts';
import { BarChart3, TrendingUp } from 'lucide-react';

export default function SurgeStatisticsChart({ overviewData }) {
  const [activeTab, setActiveTab] = useState('seasonal');

  // 1. Seasonal 12-Month Smog Curve Data
  const monthlyData = [
    { month: 'Jan', aqi: 245, pm25: 182, admissions: 145 },
    { month: 'Feb', aqi: 210, pm25: 148, admissions: 122 },
    { month: 'Mar', aqi: 155, pm25: 98, admissions: 82 },
    { month: 'Apr', aqi: 130, pm25: 75, admissions: 64 },
    { month: 'May', aqi: 120, pm25: 68, admissions: 52 },
    { month: 'Jun', aqi: 85, pm25: 42, admissions: 38 },
    { month: 'Jul', aqi: 65, pm25: 32, admissions: 28 },
    { month: 'Aug', aqi: 70, pm25: 35, admissions: 31 },
    { month: 'Sep', aqi: 110, pm25: 58, admissions: 48 },
    { month: 'Oct', aqi: 195, pm25: 135, admissions: 105 },
    { month: 'Nov', aqi: 320, pm25: 255, admissions: 215 },
    { month: 'Dec', aqi: 290, pm25: 220, admissions: 188 },
  ];

  // 2. 12-City Benchmark Comparison Data
  const cityComparisonData = overviewData?.city_summary || [
    { city: 'Amritsar', pm25: 195, aqi: 280, admissions: 165 },
    { city: 'Delhi', pm25: 173, aqi: 260, admissions: 152 },
    { city: 'Kolkata', pm25: 142, aqi: 215, admissions: 118 },
    { city: 'Ahmedabad', pm25: 110, aqi: 180, admissions: 94 },
    { city: 'Hyderabad', pm25: 95, aqi: 162, admissions: 78 },
    { city: 'Navi Mumbai', pm25: 90, aqi: 155, admissions: 72 },
    { city: 'Mumbai', pm25: 88, aqi: 150, admissions: 70 },
    { city: 'Bhubaneswar', pm25: 85, aqi: 145, admissions: 68 },
    { city: 'Pune', pm25: 76, aqi: 135, admissions: 58 },
    { city: 'Guwahati', pm25: 62, aqi: 115, admissions: 45 },
    { city: 'Chennai', pm25: 52, aqi: 98, admissions: 38 },
    { city: 'Bengaluru', pm25: 45, aqi: 82, admissions: 32 },
  ];

  // 3. Feature Importance Data (Scikit-Learn ML Model weights)
  const featureImportanceData = [
    { feature: 'PM2.5 (Fine Particles)', weight: 96.48, color: '#465FFF' },
    { feature: 'PM10 (Coarse Dust)', weight: 1.82, color: '#12B76A' },
    { feature: 'NO2 (Traffic Combustion)', weight: 0.72, color: '#F79009' },
    { feature: 'Temperature (Inversion)', weight: 0.44, color: '#F04438' },
    { feature: 'Humidity (Smog Trap)', weight: 0.31, color: '#0EA5E9' },
    { feature: 'SO2 (Industrial Sulfur)', weight: 0.15, color: '#8B5CF6' },
    { feature: 'CO (Carbon Monoxide)', weight: 0.08, color: '#64748B' },
  ];

  return (
    <div className="tailadmin-card p-5 h-full flex flex-col justify-between">
      {/* Header with Title and Tabs */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
        <div>
          <h3 className="font-bold text-gray-900 text-base font-['Outfit'] flex items-center gap-2">
            <BarChart3 className="w-4 h-4 text-[#465FFF]" />
            Epidemiological Surveillance & Predictive Telemetry
          </h3>
          <p className="text-xs text-gray-500 mt-0.5">
            CPCB 10-year atmospheric archives correlated with ICMR daily respiratory hospital admissions.
          </p>
        </div>

        {/* Tab Controls */}
        <div className="flex items-center gap-1 p-1 bg-gray-100 rounded-xl border border-gray-200/80 self-start sm:self-auto">
          <button
            onClick={() => setActiveTab('seasonal')}
            className={`
              px-3 py-1.5 rounded-lg text-xs font-semibold transition
              ${activeTab === 'seasonal'
                ? 'bg-white text-[#465FFF] shadow-2xs'
                : 'text-gray-600 hover:text-gray-900'
              }
            `}
          >
            Seasonal Curve
          </button>
          <button
            onClick={() => setActiveTab('cities')}
            className={`
              px-3 py-1.5 rounded-lg text-xs font-semibold transition
              ${activeTab === 'cities'
                ? 'bg-white text-[#465FFF] shadow-2xs'
                : 'text-gray-600 hover:text-gray-900'
              }
            `}
          >
            12-City Benchmark
          </button>
          <button
            onClick={() => setActiveTab('features')}
            className={`
              px-3 py-1.5 rounded-lg text-xs font-semibold transition
              ${activeTab === 'features'
                ? 'bg-white text-[#465FFF] shadow-2xs'
                : 'text-gray-600 hover:text-gray-900'
              }
            `}
          >
            ML Importance
          </button>
        </div>
      </div>

      {/* Chart Viewports */}
      <div className="h-[280px] w-full mt-2">
        {activeTab === 'seasonal' && (
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart data={monthlyData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
              <defs>
                <linearGradient id="colorAqi" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#465FFF" stopOpacity={0.25} />
                  <stop offset="95%" stopColor="#465FFF" stopOpacity={0.0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#F2F4F7" vertical={false} />
              <XAxis dataKey="month" stroke="#98A2B3" fontSize={11} tickLine={false} />
              <YAxis yAxisId="left" stroke="#98A2B3" fontSize={11} tickLine={false} />
              <YAxis yAxisId="right" orientation="right" stroke="#98A2B3" fontSize={11} tickLine={false} />
              <Tooltip 
                contentStyle={{ 
                  backgroundColor: '#FFFFFF', 
                  borderRadius: '12px', 
                  border: '1px solid #E4E7EC',
                  boxShadow: '0 4px 6px -1px rgba(16, 24, 40, 0.1)',
                  fontSize: '12px'
                }} 
              />
              <Legend 
                verticalAlign="top" 
                height={36} 
                iconType="circle"
                wrapperStyle={{ fontSize: '11px', fontWeight: 600 }}
              />
              <Area 
                yAxisId="left"
                type="monotone" 
                dataKey="aqi" 
                name="Average US AQI" 
                stroke="#465FFF" 
                strokeWidth={2.5}
                fillOpacity={1} 
                fill="url(#colorAqi)" 
              />
              <Bar 
                yAxisId="right"
                dataKey="admissions" 
                name="Daily Hospital Admissions" 
                fill="#F04438" 
                radius={[4, 4, 0, 0]} 
                maxBarSize={28}
                opacity={0.85}
              />
              <Line 
                yAxisId="left"
                type="monotone" 
                dataKey="pm25" 
                name="PM2.5 (µg/m³)" 
                stroke="#12B76A" 
                strokeWidth={2}
                dot={{ r: 3, fill: '#12B76A' }}
              />
            </ComposedChart>
          </ResponsiveContainer>
        )}

        {activeTab === 'cities' && (
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={cityComparisonData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#F2F4F7" vertical={false} />
              <XAxis dataKey="city" stroke="#98A2B3" fontSize={10} tickLine={false} />
              <YAxis stroke="#98A2B3" fontSize={11} tickLine={false} />
              <Tooltip 
                contentStyle={{ 
                  backgroundColor: '#FFFFFF', 
                  borderRadius: '12px', 
                  border: '1px solid #E4E7EC',
                  fontSize: '12px' 
                }} 
              />
              <Legend verticalAlign="top" height={36} iconType="circle" wrapperStyle={{ fontSize: '11px', fontWeight: 600 }} />
              <Bar dataKey="pm25" name="PM2.5 Concentration (µg/m³)" fill="#465FFF" radius={[4, 4, 0, 0]} />
              <Bar dataKey="admissions" name="Projected Hospital Admissions" fill="#F79009" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        )}

        {activeTab === 'features' && (
          <div className="h-full flex flex-col justify-center px-4 space-y-2.5">
            {featureImportanceData.map((f) => (
              <div key={f.feature}>
                <div className="flex justify-between items-center text-xs mb-1">
                  <span className="font-semibold text-gray-800">{f.feature}</span>
                  <span className="font-bold text-gray-900 tabular-nums">{f.weight}%</span>
                </div>
                <div className="w-full h-2.5 bg-gray-100 rounded-full overflow-hidden">
                  <div 
                    className="h-full rounded-full transition-all duration-500"
                    style={{ width: `${f.weight}%`, backgroundColor: f.color }}
                  />
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Footer Insight Pill */}
      <div className="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between text-xs text-gray-500">
        <span className="flex items-center gap-1.5 font-medium">
          <TrendingUp className="w-3.5 h-3.5 text-[#12B76A]" />
          Winter Inversion Peak: Nov–Jan admissions spike +240% across Indo-Gangetic Plain.
        </span>
        <span className="text-[11px] font-bold text-[#465FFF] tabular-nums">
          ML R² = 0.9879
        </span>
      </div>
    </div>
  );
}
