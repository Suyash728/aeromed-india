import React, { useState, useMemo, useRef, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { MapPin, RefreshCw, ZoomIn, ZoomOut, Layers, AlertCircle, ArrowUpRight } from 'lucide-react';

// Exact coordinates and metadata for 12 CPCB monitoring metros
const CARTO_API_KEY = import.meta.env.VITE_CARTO_API_KEY || 'cb1_58o3_1_a2fd168e29e816562973384e';

const METRO_GEOMETRY = {
  'delhi': { lat: 28.6139, lon: 77.2090, state: 'Delhi NCR' },
  'mumbai': { lat: 19.0760, lon: 72.8777, state: 'Maharashtra' },
  'navi mumbai': { lat: 19.0330, lon: 73.0297, state: 'Maharashtra' },
  'bengaluru': { lat: 12.9716, lon: 77.5946, state: 'Karnataka' },
  'kolkata': { lat: 22.5726, lon: 88.3639, state: 'West Bengal' },
  'chennai': { lat: 13.0827, lon: 80.2707, state: 'Tamil Nadu' },
  'hyderabad': { lat: 17.3850, lon: 78.4867, state: 'Telangana' },
  'ahmedabad': { lat: 23.0225, lon: 72.5714, state: 'Gujarat' },
  'pune': { lat: 18.5204, lon: 73.8567, state: 'Maharashtra' },
  'amritsar': { lat: 31.6340, lon: 74.8723, state: 'Punjab' },
  'bhubaneswar': { lat: 20.2961, lon: 85.8245, state: 'Odisha' },
  'guwahati': { lat: 26.1445, lon: 91.7362, state: 'Assam' },
};

// CPCB AQI Severity Color Mapping
function getSeverity(aqiVal) {
  if (aqiVal > 300) return { color: '#D92D20', bg: 'bg-rose-50 text-rose-700', label: 'Severe / Stage II+' };
  if (aqiVal > 200) return { color: '#F04438', bg: 'bg-orange-50 text-orange-700', label: 'Poor / Stage I' };
  if (aqiVal > 100) return { color: '#F79009', bg: 'bg-amber-50 text-amber-700', label: 'Moderate' };
  return { color: '#12B76A', bg: 'bg-emerald-50 text-emerald-700', label: 'Good' };
}

// Custom Map Controller for programmatic flyTo and reset
function MapController({ targetCoords, resetTrigger }) {
  const map = useMap();

  useEffect(() => {
    if (targetCoords) {
      map.flyTo([targetCoords.lat, targetCoords.lon], 7, {
        duration: 1.2,
        easeLinearity: 0.25,
      });
    }
  }, [targetCoords, map]);

  useEffect(() => {
    if (resetTrigger > 0) {
      map.flyTo([22.5, 79.0], 4.7, {
        duration: 1.0,
      });
    }
  }, [resetTrigger, map]);

  return null;
}

export default function IndiaSvgMap({ citiesData = [], selectedCity, onSelectCity }) {
  const [hoveredCity, setHoveredCity] = useState(null);
  const [resetTrigger, setResetTrigger] = useState(0);
  const mapRef = useRef(null);

  // Normalize cities data with coordinates
  const enrichedCities = useMemo(() => {
    return citiesData.map((c) => {
      const key = (c.id || c.name || '').toLowerCase().trim();
      const geo = METRO_GEOMETRY[key] || { lat: c.lat || 22.0, lon: c.lon || 78.0, state: c.state || 'India' };
      const aqi = c.aqi || Math.round((c.pm25 || 50) * 1.6);
      return {
        ...c,
        lat: geo.lat,
        lon: geo.lon,
        state: c.state || geo.state,
        aqi,
      };
    });
  }, [citiesData]);

  // Selected city object
  const activeTarget = useMemo(() => {
    const key = (selectedCity || '').toLowerCase().trim();
    return enrichedCities.find(c => (c.name || '').toLowerCase() === key || (c.id || '').toLowerCase() === key);
  }, [selectedCity, enrichedCities]);

  // Sort cities for leaderboard
  const sortedCities = useMemo(() => {
    return [...enrichedCities].sort((a, b) => (b.aqi || 0) - (a.aqi || 0));
  }, [enrichedCities]);

  // Create custom DivIcon for Leaflet
  const createCityIcon = (city, isSelected, severity) => {
    const val = city.aqi;
    const color = severity.color;
    const isPulsing = isSelected || val > 200;

    return L.divIcon({
      className: 'custom-leaflet-marker',
      html: `
        <div style="position: relative; display: flex; flex-direction: column; align-items: center; transform: translate(-50%, -50%); cursor: pointer; user-select: none;">
          ${isPulsing ? `<span style="position: absolute; width: 32px; height: 32px; border-radius: 9999px; background-color: ${color}; opacity: 0.35; animation: ping 1.8s cubic-bezier(0, 0, 0.2, 1) infinite; top: -2px;"></span>` : ''}
          <div style="position: relative; display: flex; align-items: center; justify-content: center; min-width: 28px; height: 26px; padding: 0 6px; border-radius: 9999px; background-color: ${color}; color: #ffffff; font-size: 11px; font-weight: 800; font-family: ui-sans-serif, system-ui; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.18), 0 2px 4px -2px rgba(0,0,0,0.12); border: 2px solid #ffffff; transition: transform 0.2s ease; ${isSelected ? 'outline: 3px solid #465FFF; outline-offset: 1px; transform: scale(1.18); z-index: 50;' : ''}">
            ${val}
          </div>
          <div style="margin-top: 3px; padding: 1px 6px; border-radius: 6px; background-color: rgba(255, 255, 255, 0.95); backdrop-filter: blur(4px); font-size: 10px; font-weight: 700; color: #1f2937; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1); border: 1px solid #e5e7eb; white-space: nowrap; pointer-events: none;">
            ${city.name}
          </div>
        </div>
      `,
      iconSize: [40, 48],
      iconAnchor: [20, 16],
      popupAnchor: [0, -18],
    });
  };

  const handleCityClick = (city) => {
    onSelectCity(city.name || city.id);
  };

  const handleResetView = () => {
    setResetTrigger(prev => prev + 1);
  };

  return (
    <div className="tailadmin-card p-5 h-full flex flex-col justify-between">
      {/* Card Header with Reset & Action Controls */}
      <div className="flex items-center justify-between mb-3">
        <div>
          <h3 className="font-bold text-gray-900 text-base font-['Outfit'] flex items-center gap-2">
            <MapPin className="w-4 h-4 text-[#465FFF]" />
            Pan-India Metro Geographic AQI Map
          </h3>
          <p className="text-xs text-gray-500 mt-0.5">
            Real-time CartoDB atmospheric surveillance across 12 CPCB monitoring hubs. Click pin to fly & focus.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={handleResetView}
            className="flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold text-gray-600 hover:text-gray-900 bg-gray-100 hover:bg-gray-200 rounded-lg transition border border-gray-200 shadow-2xs"
            title="Reset map view to Pan-India"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Reset View</span>
          </button>
          <span className="text-[11px] font-semibold text-[#465FFF] bg-[#465FFF]/10 border border-[#465FFF]/20 px-2.5 py-1 rounded-full">
            12 Hubs Live
          </span>
        </div>
      </div>

      {/* Interactive Leaflet Map Canvas */}
      <div className="relative w-full h-[360px] rounded-xl overflow-hidden border border-gray-200 shadow-inner z-0">
        <MapContainer
          center={[22.5, 79.0]}
          zoom={4.7}
          minZoom={4}
          maxZoom={12}
          scrollWheelZoom={false}
          zoomControl={true}
          style={{ height: '100%', width: '100%', backgroundColor: '#f8fafc' }}
          ref={mapRef}
        >
          {/* CartoDB Voyager Light Tiles with authenticated API key */}
          <TileLayer
            attribution='&copy; <a href="https://carto.com/">CARTO</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            url={`https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png${CARTO_API_KEY ? `?api_key=${CARTO_API_KEY}` : ''}`}
            subdomains="abcd"
            maxZoom={19}
          />

          {/* Programmatic Map Controller */}
          <MapController
            targetCoords={activeTarget ? { lat: activeTarget.lat, lon: activeTarget.lon } : null}
            resetTrigger={resetTrigger}
          />

          {/* 12 Metro Pins */}
          {enrichedCities.map((city) => {
            const isSelected = (selectedCity || '').toLowerCase() === (city.name || '').toLowerCase();
            const severity = getSeverity(city.aqi);
            const icon = createCityIcon(city, isSelected, severity);

            return (
              <Marker
                key={city.id || city.name}
                position={[city.lat, city.lon]}
                icon={icon}
                eventHandlers={{
                  click: () => handleCityClick(city),
                  mouseover: () => setHoveredCity(city),
                  mouseout: () => setHoveredCity(null),
                }}
              >
                <Popup closeButton={false} className="tailadmin-popup">
                  <div className="p-2 min-w-[190px]">
                    <div className="flex items-center justify-between border-b border-gray-100 pb-1.5 mb-2">
                      <div>
                        <div className="font-bold text-gray-900 text-sm font-['Outfit']">{city.name}</div>
                        <div className="text-[10px] text-gray-500">{city.state}</div>
                      </div>
                      <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${severity.bg}`}>
                        {severity.label}
                      </span>
                    </div>

                    <div className="space-y-1 text-xs">
                      <div className="flex items-center justify-between">
                        <span className="text-gray-500">Live AQI:</span>
                        <span className="font-extrabold text-gray-900 tabular-nums">{city.aqi}</span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-gray-500">PM2.5:</span>
                        <span className="font-semibold text-gray-800 tabular-nums">{city.pm25 || 65} µg/m³</span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-gray-500">48h Surge Risk:</span>
                        <span className="font-bold text-[#465FFF] tabular-nums">{city.predicted_risk_score || 55}/100</span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-gray-500">CAQM GRAP:</span>
                        <span className="font-bold text-rose-600">
                          {city.aqi > 400 ? 'Stage III/IV' : city.aqi > 300 ? 'Stage II' : city.aqi > 200 ? 'Stage I' : 'Normal'}
                        </span>
                      </div>
                    </div>

                    <button
                      onClick={() => handleCityClick(city)}
                      className="mt-2.5 w-full py-1.5 bg-[#465FFF] hover:bg-[#3649db] text-white text-[11px] font-bold rounded-lg transition text-center shadow-xs cursor-pointer"
                    >
                      Focus Dashboard
                    </button>
                  </div>
                </Popup>
              </Marker>
            );
          })}
        </MapContainer>

        {/* CPCB AQI Legend Overlay in Bottom Left */}
        <div className="absolute bottom-2.5 left-2.5 z-[1000] bg-white/95 backdrop-blur-md px-3 py-2 rounded-xl border border-gray-200/90 shadow-md text-[10px] space-y-1 pointer-events-none">
          <div className="font-bold text-gray-800 text-[10px] uppercase tracking-wider">
            CPCB AQI Scale
          </div>
          <div className="flex items-center gap-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500" />
            <span className="text-gray-600">&lt;100 Good</span>
            <span className="w-2.5 h-2.5 rounded-full bg-amber-500 ml-1" />
            <span className="text-gray-600">101-200 Mod</span>
            <span className="w-2.5 h-2.5 rounded-full bg-orange-500 ml-1" />
            <span className="text-gray-600">201-300 Poor</span>
            <span className="w-2.5 h-2.5 rounded-full bg-rose-600 ml-1" />
            <span className="text-gray-600">300+ Severe</span>
          </div>
        </div>
      </div>

      {/* 12-Metro Ranked Leaderboard Strip */}
      <div className="mt-4 pt-3 border-t border-gray-100">
        <div className="flex items-center justify-between text-xs font-semibold text-gray-500 mb-2">
          <span>Regional AQI Severity Ranking (12 Metros)</span>
          <span className="text-[11px] text-gray-400">Click to Fly</span>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
          {sortedCities.slice(0, 6).map((city, idx) => {
            const isSelected = (selectedCity || '').toLowerCase() === (city.name || '').toLowerCase();
            const sev = getSeverity(city.aqi);
            return (
              <button
                key={city.id || city.name}
                onClick={() => handleCityClick(city)}
                className={`
                  flex items-center justify-between p-2 rounded-xl text-left border transition cursor-pointer
                  ${isSelected 
                    ? 'border-[#465FFF] bg-[#465FFF]/10 shadow-xs' 
                    : 'border-gray-100 hover:border-gray-300 bg-gray-50/70 hover:bg-white'
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
                  {city.aqi}
                </span>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
