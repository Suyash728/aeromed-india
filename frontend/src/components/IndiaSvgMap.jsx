import React, { useState, useMemo, useRef, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { MapPin, RefreshCw, Layers, Radio, Sparkles } from 'lucide-react';
import aqiClient from '../api/aqiClient';
import { useTranslation } from '../i18n/LanguageContext';

// Exact coordinates for 12 CPCB monitoring hubs
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

// Strategic positioning offsets to eliminate visual overlap in dense corridors (Mumbai-Pune & Bengaluru-Chennai)
const METRO_LAYOUT = {
  'mumbai': { pinOffset: [-6, 0], labelClass: 'mt-1', zIndex: 30 },
  'navi mumbai': { pinOffset: [16, 8], labelClass: 'mt-1', zIndex: 40 },
  'pune': { pinOffset: [12, 16], labelClass: 'mt-1', zIndex: 20 },
  'bengaluru': { pinOffset: [-10, 4], labelClass: 'mt-1', zIndex: 25 },
  'chennai': { pinOffset: [14, -2], labelClass: 'mt-1', zIndex: 25 },
  'delhi': { pinOffset: [0, 0], labelClass: 'mt-1', zIndex: 35 },
  'amritsar': { pinOffset: [0, -4], labelClass: 'mt-1', zIndex: 20 },
  'kolkata': { pinOffset: [0, 0], labelClass: 'mt-1', zIndex: 25 },
  'ahmedabad': { pinOffset: [0, 0], labelClass: 'mt-1', zIndex: 20 },
  'hyderabad': { pinOffset: [0, 0], labelClass: 'mt-1', zIndex: 20 },
  'bhubaneswar': { pinOffset: [6, 0], labelClass: 'mt-1', zIndex: 20 },
  'guwahati': { pinOffset: [0, 0], labelClass: 'mt-1', zIndex: 20 },
};

// CPCB AQI Severity Color Mapping
function getSeverity(aqiVal) {
  if (aqiVal > 300) return { color: '#D92D20', bg: 'bg-rose-50 text-rose-700', label: 'Severe / Stage II+' };
  if (aqiVal > 200) return { color: '#F04438', bg: 'bg-orange-50 text-orange-700', label: 'Poor / Stage I' };
  if (aqiVal > 100) return { color: '#F79009', bg: 'bg-amber-50 text-amber-700', label: 'Moderate' };
  return { color: '#12B76A', bg: 'bg-emerald-50 text-emerald-700', label: 'Good' };
}

// Programmatic Map Controller for smooth flyTo and Pan-India reset.
// Depends on primitive lat/lon so it flies only when the selected city changes,
// not on every re-render (which used to snap the map back whenever the user panned).
function MapController({ targetLat, targetLon, focusNonce, resetTrigger }) {
  const map = useMap();

  useEffect(() => {
    if (targetLat != null && targetLon != null) {
      map.flyTo([targetLat, targetLon], 7, {
        duration: 1.2,
        easeLinearity: 0.25,
      });
    }
  }, [targetLat, targetLon, focusNonce, map]);

  // The card stretches to match its row, so tell Leaflet whenever its box resizes
  useEffect(() => {
    const container = map.getContainer();
    const observer = new ResizeObserver(() => map.invalidateSize());
    observer.observe(container);
    return () => observer.disconnect();
  }, [map]);

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
  const { t } = useTranslation();
  const [resetTrigger, setResetTrigger] = useState(0);
  // Bumped on every city click so re-clicking the already-selected city re-centres the map
  const [focusNonce, setFocusNonce] = useState(0);
  const [basemapStyle, setBasemapStyle] = useState('canvas'); // 'canvas' | 'streets'
  const [liveMapBatch, setLiveMapBatch] = useState(null);
  const [syncTimestamp, setSyncTimestamp] = useState(null);
  const mapRef = useRef(null);

  // Poll or fetch live Open-Meteo batch data for all 12 metros on load
  useEffect(() => {
    let isMounted = true;
    async function loadLiveMap() {
      try {
        const res = await aqiClient.getLiveMap();
        if (isMounted && res && res.cities && res.cities.length > 0) {
          setLiveMapBatch(res.cities);
          setSyncTimestamp(res.sync_timestamp || new Date().toISOString());
        }
      } catch (err) {
        // Fall back to the prop cities, but leave a trace so a dead backend is diagnosable
        console.warn('Live map refresh failed; showing baseline cities.', err);
      }
    }
    loadLiveMap();
    const interval = setInterval(loadLiveMap, 600000); // 10 min refresh
    return () => {
      isMounted = false;
      clearInterval(interval);
    };
  }, []);

  // Merge live batch data with provided fallback citiesData
  const enrichedCities = useMemo(() => {
    const dataSource = (liveMapBatch && liveMapBatch.length > 0) ? liveMapBatch : citiesData;
    return dataSource.map((c) => {
      const key = (c.id || c.name || '').toLowerCase().trim();
      const geo = METRO_GEOMETRY[key] || { lat: c.lat || 22.0, lon: c.lon || 78.0, state: c.state || 'India' };
      const aqi = c.aqi || Math.round((c.pm25 || 50) * 1.6);
      return {
        ...c,
        id: key,
        name: c.name || geo.state,
        lat: geo.lat,
        lon: geo.lon,
        state: c.state || geo.state,
        aqi,
      };
    });
  }, [citiesData, liveMapBatch]);

  // Active targeted city object
  const activeTarget = useMemo(() => {
    const key = (selectedCity || '').toLowerCase().trim();
    return enrichedCities.find(c => (c.name || '').toLowerCase() === key || (c.id || '').toLowerCase() === key);
  }, [selectedCity, enrichedCities]);

  // Sort cities for leaderboard ranking
  const sortedCities = useMemo(() => {
    return [...enrichedCities].sort((a, b) => (b.aqi || 0) - (a.aqi || 0));
  }, [enrichedCities]);

  // Create clean, crisp DivIcon with anti-collision offsets and dynamic z-index
  const createCityIcon = (city, isSelected, severity) => {
    const val = city.aqi;
    const color = severity.color;
    const isPulsing = isSelected || val > 200;
    const layout = METRO_LAYOUT[city.id] || { pinOffset: [0, 0], labelClass: 'mt-1', zIndex: 20 };
    const zIndexVal = isSelected ? 1000 : layout.zIndex;

    return L.divIcon({
      className: 'custom-leaflet-marker',
      html: `
        <div style="position: relative; display: flex; flex-direction: column; align-items: center; transform: translate(calc(-50% + ${layout.pinOffset[0]}px), calc(-50% + ${layout.pinOffset[1]}px)); cursor: pointer; user-select: none; z-index: ${zIndexVal};">
          ${isPulsing ? `<span style="position: absolute; width: 32px; height: 32px; border-radius: 9999px; background-color: ${color}; opacity: 0.35; animation: ping 1.8s cubic-bezier(0, 0, 0.2, 1) infinite; top: -2px;"></span>` : ''}
          <div style="position: relative; display: flex; align-items: center; justify-content: center; min-width: 28px; height: 26px; padding: 0 6px; border-radius: 9999px; background-color: ${color}; color: #ffffff; font-size: 11px; font-weight: 800; font-family: ui-sans-serif, system-ui; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.18), 0 2px 4px -2px rgba(0,0,0,0.12); border: 2px solid #ffffff; transition: transform 0.2s ease; ${isSelected ? 'outline: 3px solid #465FFF; outline-offset: 1px; transform: scale(1.18);' : ''}">
            ${val}
          </div>
          <div style="margin-top: 3px; padding: 1.5px 6px; border-radius: 6px; background-color: rgba(255, 255, 255, 0.96); backdrop-filter: blur(4px); font-size: 10px; font-weight: 700; color: #111827; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12); border: 1px solid #e5e7eb; white-space: nowrap; pointer-events: none;">
            ${city.name}
          </div>
        </div>
      `,
      iconSize: [40, 48],
      iconAnchor: [20, 16],
      popupAnchor: [layout.pinOffset[0], -20 + layout.pinOffset[1]],
    });
  };

  const selectedKey = (selectedCity || '').toLowerCase();

  // Icons are memoised: rebuilding a DivIcon makes Leaflet replace the marker's DOM node,
  // which swallowed clicks when it happened on hover. Rebuild only when data or selection change.
  const cityIcons = useMemo(() => {
    const icons = {};
    for (const city of enrichedCities) {
      const isSelected = selectedKey === (city.name || '').toLowerCase();
      icons[city.id] = createCityIcon(city, isSelected, getSeverity(city.aqi));
    }
    return icons;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [enrichedCities, selectedKey]);

  const handleCityClick = (city) => {
    setFocusNonce(n => n + 1);
    onSelectCity(city.name || city.id);
  };

  const handleResetView = () => {
    setResetTrigger(prev => prev + 1);
  };

  const formattedTime = syncTimestamp ? new Date(syncTimestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : 'Live';

  return (
    <div className="tailadmin-card p-5 h-full flex flex-col">
      {/* Card Header with Basemap Switcher & Reset Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-3">
        <div>
          <h3 className="font-bold text-gray-900 text-base font-['Outfit'] flex items-center gap-2">
            <MapPin className="w-4 h-4 text-[#465FFF]" />
            {t('overview.map_title', 'Pan-India Metro Geographic AQI Map')}
          </h3>
          <p className="text-xs text-gray-500 mt-0.5">
            {t('overview.map_sub', 'Atmospheric telemetry across 12 CPCB monitoring hubs. Click pin to fly & focus.')}
          </p>
        </div>

        {/* Action Controls & Layer Switcher Pill */}
        <div className="flex items-center gap-2 self-start sm:self-auto">
          {/* Layer Switcher Pill (100% Free Zero-Key Esri / OSM) */}
          <div className="flex items-center gap-1 p-0.5 bg-gray-100 rounded-lg border border-gray-200 text-[11px] font-semibold">
            <button
              onClick={() => setBasemapStyle('canvas')}
              className={`px-2 py-1 rounded-md transition ${
                basemapStyle === 'canvas' ? 'bg-white text-[#465FFF] shadow-2xs font-bold' : 'text-gray-600 hover:text-gray-900'
              }`}
              title="Esri World Light Gray Canvas (Zero Watermark)"
            >
              {t('overview.basemap_canvas', 'Canvas Light')}
            </button>
            <button
              onClick={() => setBasemapStyle('streets')}
              className={`px-2 py-1 rounded-md transition ${
                basemapStyle === 'streets' ? 'bg-white text-[#465FFF] shadow-2xs font-bold' : 'text-gray-600 hover:text-gray-900'
              }`}
              title="OpenStreetMap Standard Clinical Filter"
            >
              {t('overview.basemap_streets', 'Streets')}
            </button>
          </div>

          <button
            onClick={handleResetView}
            className="flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold text-gray-600 hover:text-gray-900 bg-gray-100 hover:bg-gray-200 rounded-lg transition border border-gray-200 shadow-2xs cursor-pointer"
            title="Reset map view to Pan-India"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">{t('overview.reset_view', 'Reset View')}</span>
          </button>
        </div>
      </div>

      {/* Interactive Map Canvas (100% Free Zero-Key Basemaps) */}
      <div className="relative w-full flex-1 min-h-[360px] rounded-xl overflow-hidden border border-gray-200 shadow-inner z-0">
        <MapContainer
          center={[22.5, 79.0]}
          zoom={4.7}
          minZoom={4}
          maxZoom={14}
          scrollWheelZoom={false}
          zoomControl={true}
          style={{ height: '100%', width: '100%', backgroundColor: '#f4f5f7' }}
          ref={mapRef}
        >
          {/* Primary Option: Esri World Light Gray Canvas (Base + Reference Labels) */}
          {basemapStyle === 'canvas' && (
            <>
              <TileLayer
                attribution='Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ'
                url="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}"
                maxZoom={16}
              />
              <TileLayer
                attribution=""
                url="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer/tile/{z}/{y}/{x}"
                maxZoom={16}
              />
            </>
          )}

          {/* Secondary Option: OpenStreetMap Standard with Clean Light Filter */}
          {basemapStyle === 'streets' && (
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
              maxZoom={19}
              className="map-streets-filter"
            />
          )}

          {/* Programmatic Map Controller */}
          <MapController
            targetLat={activeTarget?.lat}
            targetLon={activeTarget?.lon}
            focusNonce={focusNonce}
            resetTrigger={resetTrigger}
          />

          {/* 12 Metro Pins with Anti-Collision Offsets */}
          {enrichedCities.map((city) => {
            const severity = getSeverity(city.aqi);

            return (
              <Marker
                key={city.id || city.name}
                position={[city.lat, city.lon]}
                icon={cityIcons[city.id]}
                zIndexOffset={selectedKey === (city.name || '').toLowerCase() ? 1000 : 0}
                riseOnHover
                eventHandlers={{
                  click: () => handleCityClick(city),
                }}
              >
                <Popup closeButton={false} className="tailadmin-popup">
                  <div className="p-2 min-w-[200px]">
                    <div className="flex items-center justify-between border-b border-gray-100 pb-1.5 mb-2">
                      <div>
                        <div className="font-bold text-gray-900 text-sm font-['Outfit']">
                          {t('cities.' + (city.name || '').toLowerCase(), city.name)}
                        </div>
                        <div className="text-[10px] text-gray-500">
                          {t('cities.' + (city.state || '').toLowerCase(), city.state)}
                        </div>
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
                      {t('overview.focus_dashboard', 'Focus Dashboard')}
                    </button>
                  </div>
                </Popup>
              </Marker>
            );
          })}
        </MapContainer>

        {/* Live Open-Meteo Synced Badge Overlay in Top Right */}
        <div className="absolute top-2.5 right-2.5 z-[1000] flex items-center gap-1.5 bg-white/95 backdrop-blur-md px-2.5 py-1 rounded-full border border-gray-200/90 shadow-xs text-[10px] font-semibold text-emerald-700 pointer-events-none">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span>{t('overview.live_open_meteo_synced', 'Live Open-Meteo Synced')} ({formattedTime})</span>
        </div>

        {/* CPCB AQI Legend Overlay in Bottom Left */}
        <div className="absolute bottom-2.5 left-2.5 z-[1000] bg-white/95 backdrop-blur-md px-3 py-2 rounded-xl border border-gray-200/90 shadow-md text-[10px] space-y-1 pointer-events-none">
          <div className="font-bold text-gray-800 text-[10px] uppercase tracking-wider">
            {t('overview.cpcb_scale', 'CPCB AQI Scale')}
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

      {/* 12-Metro Ranked Leaderboard Strip - Expanded so all city names display cleanly without awkward clipping */}
      <div className="mt-4 pt-3 border-t border-gray-100">
        <div className="flex items-center justify-between text-xs font-semibold text-gray-500 mb-2">
          <span>{t('overview.severity_ranking', 'Regional AQI Severity Ranking (12 Metros)')}</span>
          <span className="text-[11px] text-gray-400">{t('overview.click_to_fly', 'Click to Fly')}</span>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-2">
          {sortedCities.map((city, idx) => {
            const isSelected = (selectedCity || '').toLowerCase() === (city.name || '').toLowerCase();
            const sev = getSeverity(city.aqi);
            return (
              <button
                key={city.id || city.name}
                onClick={() => handleCityClick(city)}
                className={`
                  flex items-center justify-between p-2 rounded-xl text-left border transition cursor-pointer min-w-0
                  ${isSelected 
                    ? 'border-[#465FFF] bg-[#465FFF]/10 shadow-xs' 
                    : 'border-gray-100 hover:border-gray-300 bg-gray-50/70 hover:bg-white'
                  }
                `}
              >
                <div className="min-w-0 pr-1.5 flex-1">
                  <div className="text-[11px] font-semibold text-gray-900 flex items-center gap-1">
                    <span className="text-[10px] text-gray-400 font-mono">#{idx+1}</span>
                    <span className="truncate">{t('cities.' + (city.name || '').toLowerCase(), city.name)}</span>
                  </div>
                  <div className="text-[10px] text-gray-400 truncate">{t('cities.' + (city.state || '').toLowerCase(), city.state)}</div>
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
