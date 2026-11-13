import React, { useEffect } from 'react';

const CITIES_DATA = [
  { id: 'delhi', name: 'Delhi', lat: 28.6139, lon: 77.209, pm: 173, status: 'Severe' },
  { id: 'mumbai', name: 'Mumbai', lat: 19.076, lon: 72.8777, pm: 88, status: 'Moderate' },
  { id: 'bengaluru', name: 'Bengaluru', lat: 12.9716, lon: 77.5946, pm: 45, status: 'Normal' },
  { id: 'kolkata', name: 'Kolkata', lat: 22.5726, lon: 88.3639, pm: 142, status: 'Severe' },
  { id: 'chennai', name: 'Chennai', lat: 13.0827, lon: 80.2707, pm: 52, status: 'Moderate' },
  { id: 'hyderabad', name: 'Hyderabad', lat: 17.385, lon: 78.4867, pm: 95, status: 'Poor' },
  { id: 'ahmedabad', name: 'Ahmedabad', lat: 23.0225, lon: 72.5714, pm: 110, status: 'Poor' },
  { id: 'pune', name: 'Pune', lat: 18.5204, lon: 73.8567, pm: 76, status: 'Moderate' },
  { id: 'amritsar', name: 'Amritsar', lat: 31.634, lon: 74.8723, pm: 195, status: 'Severe' },
  { id: 'bhubaneswar', name: 'Bhubaneswar', lat: 20.2961, lon: 85.8245, pm: 85, status: 'Moderate' },
  { id: 'guwahati', name: 'Guwahati', lat: 26.1445, lon: 91.7362, pm: 62, status: 'Moderate' },
  { id: 'navi mumbai', name: 'Navi Mumbai', lat: 19.033, lon: 73.0297, pm: 90, status: 'Moderate' },
];

export default function IndiaMapCard({ selectedCity, onSelectCity }) {
  useEffect(() => {
    if (!document.getElementById('leaflet-css')) {
      const link = document.createElement('link');
      link.id = 'leaflet-css';
      link.rel = 'stylesheet';
      link.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
      document.head.appendChild(link);
    }

    if (!document.getElementById('leaflet-js')) {
      const script = document.createElement('script');
      script.id = 'leaflet-js';
      script.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
      script.async = true;
      script.onload = initMap;
      document.body.appendChild(script);
    } else {
      initMap();
    }
  }, [selectedCity]);

  function initMap() {
    const L = window.L;
    if (!L) return;

    const container = document.getElementById('real-india-map');
    if (!container) return;

    if (container._leaflet_id) {
      container._leaflet_id = null;
      container.innerHTML = '';
    }

    // Strict India geographical bounding box coordinates
    const indiaBounds = L.latLngBounds(
      [6.5, 68.7], 
      [35.5, 97.4]  
    );

    const map = L.map(container, {
      zoomControl: true,
      attributionControl: false,
      maxBounds: indiaBounds,
      maxBoundsViscosity: 1.0,
      minZoom: 6, // Strict zoom constraint so user stays within India region
      maxZoom: 10
    }).setView([22.5937, 78.9629], 5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
    }).addTo(map);

    CITIES_DATA.forEach((c) => {
      const isSelected = selectedCity.toLowerCase() === c.id.toLowerCase();
      const color = c.pm > 120 ? '#f43f5e' : c.pm > 90 ? '#f59e0b' : '#34d399';

      const customIcon = L.divIcon({
        className: 'custom-map-pin',
        html: `
          <div style="
            background: ${color};
            width: ${isSelected ? '18px' : '12px'};
            height: ${isSelected ? '18px' : '12px'};
            border: 2px solid #ffffff;
            border-radius: 50%;
            box-shadow: 0 0 12px ${color};
            cursor: pointer;
          "></div>
          <span style="
            position: absolute;
            left: 20px;
            top: -6px;
            background: #111827;
            color: ${isSelected ? '#60a5fa' : '#ffffff'};
            padding: 3px 8px;
            font-size: 11px;
            font-weight: ${isSelected ? '700' : '600'};
            border-radius: 6px;
            border: 1px solid #374151;
            white-space: nowrap;
            box-shadow: 0 2px 6px rgba(0,0,0,0.4);
          ">${c.name} • ${c.pm}</span>
        `,
        iconSize: [12, 12],
        iconAnchor: [6, 6]
      });

      const marker = L.marker([c.lat, c.lon], { icon: customIcon }).addTo(map);
      marker.on('click', () => {
        onSelectCity(c.id);
      });
    });
  }

  return (
    <div className="panel" style={{ position: 'relative', overflow: 'hidden' }}>
      <div className="panel-header">
        <h2 style={{ fontSize: '16px', fontWeight: '700' }}>🗺️ Pan-India Live Geographic Map</h2>
        <span className="grap-pill grap-severe">OpenStreetMap GIS</span>
      </div>
      
      <p style={{ fontSize: '12px', color: '#9ca3af', marginBottom: '14px' }}>
        Interactive real-world map locked to India region. Click any city node to switch telemetry.
      </p>

      <div 
        id="real-india-map" 
        style={{ 
          width: '100%', 
          height: '350px', 
          borderRadius: '10px', 
          border: '1px solid var(--border-color)',
          zIndex: 1
        }} 
      />
    </div>
  );
}