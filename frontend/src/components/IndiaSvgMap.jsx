import React, { useState } from 'react';
import { MapPin, AlertCircle, ArrowUpRight } from 'lucide-react';

export default function IndiaSvgMap({ citiesData = [], selectedCity, onSelectCity }) {
  const [hoveredCity, setHoveredCity] = useState(null);

  // Exact projected coordinates on 600x650 viewport
  const metroCoordinates = {
    'amritsar': { x: 161, y: 146, labelAnchor: 'end', dx: -12, dy: -6 },
    'delhi': { x: 201, y: 205, labelAnchor: 'start', dx: 14, dy: -4 },
    'ahmedabad': { x: 122, y: 315, labelAnchor: 'end', dx: -12, dy: 4 },
    'kolkata': { x: 390, y: 324, labelAnchor: 'start', dx: 14, dy: 4 },
    'guwahati': { x: 452, y: 254, labelAnchor: 'start', dx: 12, dy: -6 },
    'mumbai': { x: 128, y: 392, labelAnchor: 'end', dx: -14, dy: -4 },
    'navi mumbai': { x: 140, y: 405, labelAnchor: 'start', dx: 14, dy: 10 },
    'pune': { x: 154, y: 418, labelAnchor: 'end', dx: -12, dy: 10 },
    'bhubaneswar': { x: 347, y: 368, labelAnchor: 'start', dx: 12, dy: 6 },
    'hyderabad': { x: 223, y: 425, labelAnchor: 'start', dx: 14, dy: 4 },
    'chennai': { x: 253, y: 510, labelAnchor: 'start', dx: 14, dy: 4 },
    'bengaluru': { x: 208, y: 512, labelAnchor: 'end', dx: -14, dy: 4 },
  };

  // Helper for color coding based on AQI / PM2.5
  const getSeverity = (pm) => {
    if (pm > 150) return { color: '#D92D20', bg: 'bg-rose-50 text-rose-700', label: 'Severe' };
    if (pm > 100) return { color: '#F04438', bg: 'bg-orange-50 text-orange-700', label: 'Poor' };
    if (pm > 60) return { color: '#F79009', bg: 'bg-amber-50 text-amber-700', label: 'Moderate' };
    return { color: '#12B76A', bg: 'bg-emerald-50 text-emerald-700', label: 'Good' };
  };

  // Sort cities for leaderboard
  const sortedCities = [...citiesData].sort((a, b) => (b.pm25 || b.pm || 0) - (a.pm25 || a.pm || 0));

  return (
    <div className="tailadmin-card p-5 h-full flex flex-col justify-between">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="font-bold text-gray-900 text-base font-['Outfit'] flex items-center gap-2">
            <MapPin className="w-4 h-4 text-[#465FFF]" />
            Pan-India Metro AQI Surveillance Map
          </h3>
          <p className="text-xs text-gray-500 mt-0.5">
            Geographic atmospheric surveillance across 12 CPCB monitoring hubs. Click to focus metro.
          </p>
        </div>
        <span className="text-[11px] font-semibold text-gray-400 bg-gray-100 px-2.5 py-1 rounded-full">
          12 Hubs Active
        </span>
      </div>

      {/* SVG Map Canvas */}
      <div className="relative w-full h-[340px] bg-gray-50/50 rounded-xl border border-gray-100 p-2 flex items-center justify-center overflow-hidden">
        <svg 
          viewBox="0 0 540 600" 
          className="w-full h-full max-h-[320px] select-none"
        >
          {/* India Landmass Vector Contour */}
          <path
            d="
              M 160,110 
              C 165,90 190,80 200,95 
              C 215,100 230,120 235,145 
              C 250,150 270,165 290,175 
              C 330,175 365,185 410,210 
              C 440,210 470,225 480,245 
              C 485,265 470,285 445,285 
              C 425,285 405,275 390,290 
              C 380,310 395,335 390,360 
              C 380,380 350,400 330,425 
              C 300,460 275,505 250,555 
              C 240,565 230,570 220,550 
              C 205,510 180,470 160,430 
              C 140,390 120,350 115,310 
              C 110,270 100,240 125,200 
              C 140,170 150,135 160,110 Z
            "
            fill="#FFFFFF"
            stroke="#D0D5DD"
            strokeWidth="1.8"
            strokeDasharray="none"
            className="drop-shadow-xs"
          />

          {/* Internal Regional Ribs */}
          <path
            d="M 125,200 Q 220,250 390,290"
            fill="none"
            stroke="#EAECF0"
            strokeWidth="1.2"
            strokeDasharray="4 4"
          />
          <path
            d="M 140,390 Q 240,400 330,425"
            fill="none"
            stroke="#EAECF0"
            strokeWidth="1.2"
            strokeDasharray="4 4"
          />

          {/* Metro Nodes */}
          {citiesData.map((city) => {
            const key = city.id?.toLowerCase();
            const coords = metroCoordinates[key] || { x: 260, y: 300, labelAnchor: 'start', dx: 10, dy: 0 };
            const isSelected = selectedCity?.toLowerCase() === key;
            const pmVal = city.pm25 || city.pm || 75;
            const severity = getSeverity(pmVal);

            return (
              <g 
                key={city.id} 
                className="cursor-pointer group"
                onClick={() => onSelectCity(city.id)}
                onMouseEnter={() => setHoveredCity(city)}
                onMouseLeave={() => setHoveredCity(null)}
              >
                {/* Outer Pulsing Ring if Selected or High AQI */}
                {(isSelected || pmVal > 140) && (
                  <circle
                    cx={coords.x}
                    cy={coords.y}
                    r={isSelected ? 18 : 12}
                    fill={severity.color}
                    opacity="0.25"
                    className="pulsing-ring"
                  />
                )}

                {/* Core Dot */}
                <circle
                  cx={coords.x}
                  cy={coords.y}
                  r={isSelected ? 7 : 5}
                  fill={severity.color}
                  stroke="#FFFFFF"
                  strokeWidth={isSelected ? 2.5 : 1.5}
                  className="transition-all duration-200 group-hover:scale-125"
                />

                {/* City Label */}
                <text
                  x={coords.x + coords.dx}
                  y={coords.y + coords.dy}
                  textAnchor={coords.labelAnchor}
                  className={`
                    text-[11px] select-none transition-colors
                    ${isSelected 
                      ? 'fill-[#465FFF] font-extrabold text-[12px]' 
                      : 'fill-gray-600 font-medium group-hover:fill-gray-900'
                    }
                  `}
                >
                  {city.name}
                </text>
              </g>
            );
          })}
        </svg>

        {/* Floating Tooltip Card */}
        {hoveredCity && (
          <div className="absolute bottom-3 right-3 bg-white/95 backdrop-blur-md border border-gray-200 rounded-xl p-3 shadow-lg text-xs pointer-events-none animate-in fade-in duration-100 z-10 w-48">
            <div className="font-bold text-gray-900 flex items-center justify-between">
              <span>{hoveredCity.name}</span>
              <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${getSeverity(hoveredCity.pm25 || hoveredCity.pm).bg}`}>
                {getSeverity(hoveredCity.pm25 || hoveredCity.pm).label}
              </span>
            </div>
            <div className="text-[11px] text-gray-500 mb-1.5">{hoveredCity.state}</div>
            <div className="flex items-center justify-between border-t border-gray-100 pt-1.5">
              <span className="text-gray-500">PM2.5 Level</span>
              <span className="font-bold text-gray-900 tabular-nums">
                {hoveredCity.pm25 || hoveredCity.pm} µg/m³
              </span>
            </div>
            <div className="flex items-center justify-between text-gray-500 pt-0.5">
              <span>Predicted Risk</span>
              <span className="font-bold text-[#465FFF] tabular-nums">
                {hoveredCity.predicted_risk_score || 64}/100
              </span>
            </div>
          </div>
        )}
      </div>

      {/* 12-Metro Ranked Leaderboard Strip */}
      <div className="mt-4 pt-3 border-t border-gray-100">
        <div className="flex items-center justify-between text-xs font-semibold text-gray-500 mb-2">
          <span>Regional AQI Severity Ranking</span>
          <span className="text-[11px] text-gray-400">CPCB Metric</span>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
          {sortedCities.slice(0, 6).map((city, idx) => {
            const isSelected = selectedCity?.toLowerCase() === city.id?.toLowerCase();
            const pm = city.pm25 || city.pm || 0;
            const sev = getSeverity(pm);
            return (
              <button
                key={city.id}
                onClick={() => onSelectCity(city.id)}
                className={`
                  flex items-center justify-between p-2 rounded-xl text-left border transition
                  ${isSelected 
                    ? 'border-[#465FFF] bg-[#465FFF]/5 shadow-2xs' 
                    : 'border-gray-100 hover:border-gray-200 bg-gray-50/50'
                  }
                `}
              >
                <div className="truncate pr-1">
                  <div className="text-[11px] font-semibold text-gray-800 truncate flex items-center gap-1">
                    <span className="text-[10px] text-gray-400 font-mono">#{idx+1}</span>
                    {city.name}
                  </div>
                  <div className="text-[10px] text-gray-400 truncate">{city.state}</div>
                </div>
                <span className={`text-[11px] font-bold px-1.5 py-0.5 rounded ${sev.bg} tabular-nums shrink-0`}>
                  {pm}
                </span>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
