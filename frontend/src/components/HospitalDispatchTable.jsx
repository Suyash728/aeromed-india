import React from 'react';

const dispatchLogs = [
  {
    id: 'LOG-001',
    city: 'Delhi',
    state: 'Delhi NCR',
    condition: 'Severe PM2.5 (173.6 µg/m³)',
    resource: '+17 ICU Beds & Nebulizers',
    grap: 'GRAP-III (Active)',
    statusColor: '#f43f5e',
  },
  {
    id: 'LOG-002',
    city: 'Amritsar',
    state: 'Punjab',
    condition: 'Crop Burning Peak (195.0 µg/m³)',
    resource: 'Mobile Oxygen Vans & Masks',
    grap: 'GRAP-IV (Emergency)',
    statusColor: '#ef4444',
  },
  {
    id: 'LOG-003',
    city: 'Bengaluru',
    state: 'Karnataka',
    condition: 'Normal Air Quality (38.5 µg/m³)',
    resource: 'Standard Monitoring',
    grap: 'Satisfactory',
    statusColor: '#34d399',
  },
  {
    id: 'LOG-004',
    city: 'Kolkata',
    state: 'West Bengal',
    condition: 'Elevated PM2.5 (142.0 µg/m³)',
    resource: 'Pediatric Surge Ward',
    grap: 'GRAP-III (Severe)',
    statusColor: '#f59e0b',
  },
];

export default function HospitalDispatchTable() {
  // Function to generate and download CSV file on click
  const handleExportLogs = () => {
    const headers = ['Log ID,City,State,Triggered Condition,Resource Dispatched,GRAP Status\n'];
    const rows = dispatchLogs.map(
      (log) => `"${log.id}","${log.city}","${log.state}","${log.condition}","${log.resource}","${log.grap}"`
    );
    const csvContent = 'data:text/csv;charset=utf-8,' + headers.concat(rows).join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'AeroMed_Emergency_Dispatch_Logs.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="panel" style={{ marginTop: '24px' }}>
      <div className="panel-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h2 style={{ fontSize: '16px', fontWeight: '700', color: '#f9fafb' }}>
            🚑 Live Hospital Surge & Emergency Dispatch Queue
          </h2>
          <p style={{ fontSize: '12px', color: '#9ca3af', marginTop: '2px' }}>
            Real-time automated resource allocation based on Adaption AI telemetry & GRAP triggers.
          </p>
        </div>
        <button 
          onClick={handleExportLogs}
          style={{
            background: 'rgba(59, 130, 246, 0.1)',
            border: '1px solid #3b82f6',
            color: '#60a5fa',
            padding: '6px 14px',
            borderRadius: '8px',
            fontSize: '12px',
            fontWeight: '600',
            cursor: 'pointer',
            transition: 'background 0.2s'
          }}
          onMouseOver={(e) => (e.currentTarget.style.background = 'rgba(59, 130, 246, 0.2)')}
          onMouseOut={(e) => (e.currentTarget.style.background = 'rgba(59, 130, 246, 0.1)')}
        >
          Export Logs 📥
        </button>
      </div>

      <div style={{ overflowX: 'auto', marginTop: '12px' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid var(--border-color)', color: '#9ca3af', fontSize: '11px', textTransform: 'uppercase' }}>
              <th style={{ padding: '10px 12px' }}>Metro / Node</th>
              <th style={{ padding: '10px 12px' }}>Triggered Condition</th>
              <th style={{ padding: '10px 12px' }}>Resource Dispatched</th>
              <th style={{ padding: '10px 12px' }}>GRAP Status</th>
            </tr>
          </thead>
          <tbody>
            {dispatchLogs.map((log) => (
              <tr key={log.id} style={{ borderBottom: '1px solid rgba(55, 65, 81, 0.3)' }}>
                <td style={{ padding: '14px 12px', fontWeight: '600', color: '#fff' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: log.statusColor }}></span>
                    {log.city}
                  </div>
                  <span style={{ fontSize: '10px', color: '#9ca3af', marginLeft: '16px' }}>{log.state}</span>
                </td>
                <td style={{ padding: '14px 12px', color: '#d1d5db' }}>
                  {log.condition}
                </td>
                <td style={{ padding: '14px 12px', fontWeight: '500', color: '#60a5fa' }}>
                  {log.resource}
                </td>
                <td style={{ padding: '14px 12px' }}>
                  <span style={{
                    background: `${log.statusColor}22`,
                    color: log.statusColor,
                    padding: '4px 10px',
                    borderRadius: '999px',
                    fontSize: '11px',
                    fontWeight: '700',
                    border: `1px solid ${log.statusColor}44`
                  }}>
                    {log.grap}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}