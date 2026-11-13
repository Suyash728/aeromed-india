import React from 'react';
import { Truck, Download, AlertTriangle, ShieldAlert, CheckCircle2 } from 'lucide-react';

const dispatchLogs = [
  {
    id: 'DISP-0891',
    city: 'Delhi',
    state: 'Delhi NCR',
    condition: 'Hazardous PM2.5 (173.6 µg/m³)',
    resource: '+17 ICU Ventilators & Nebulizers',
    grap: 'Stage III (Severe)',
    urgency: 'critical',
    eta: '12 mins',
  },
  {
    id: 'DISP-0892',
    city: 'Amritsar',
    state: 'Punjab',
    condition: 'Stubble Smog Peak (195.0 µg/m³)',
    resource: '3 Mobile Oxygen Units & N95 Supplies',
    grap: 'Stage IV (Emergency)',
    urgency: 'critical',
    eta: '8 mins',
  },
  {
    id: 'DISP-0893',
    city: 'Kolkata',
    state: 'West Bengal',
    condition: 'Industrial Particulates (142.0 µg/m³)',
    resource: 'Pediatric Surge Ward Expansion',
    grap: 'Stage III (Severe)',
    urgency: 'high',
    eta: '25 mins',
  },
  {
    id: 'DISP-0894',
    city: 'Ahmedabad',
    state: 'Gujarat',
    condition: 'Vehicular Dust Cloud (110.0 µg/m³)',
    resource: 'Emergency Bronchodilator Reserve',
    grap: 'Stage II (Very Poor)',
    urgency: 'moderate',
    eta: '30 mins',
  },
  {
    id: 'DISP-0895',
    city: 'Bengaluru',
    state: 'Karnataka',
    condition: 'Optimal Airflow (45.0 µg/m³)',
    resource: 'Standard Baseline Surveillance',
    grap: 'Good / Moderate',
    urgency: 'normal',
    eta: 'Standby',
  },
];

export default function HospitalDispatchTable() {
  const handleExportLogs = () => {
    const headers = ['Log ID,City,State,Triggered Condition,Resource Dispatched,GRAP Status,Urgency,ETA\n'];
    const rows = dispatchLogs.map(
      (log) => `"${log.id}","${log.city}","${log.state}","${log.condition}","${log.resource}","${log.grap}","${log.urgency}","${log.eta}"`
    );
    const csvContent = 'data:text/csv;charset=utf-8,' + headers.concat(rows).join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'AeroMed_Emergency_Hospital_Dispatch_Queue.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const getUrgencyBadge = (urgency) => {
    switch (urgency) {
      case 'critical':
        return 'bg-rose-50 text-rose-700 border-rose-200';
      case 'high':
        return 'bg-orange-50 text-orange-700 border-orange-200';
      case 'moderate':
        return 'bg-amber-50 text-amber-700 border-amber-200';
      default:
        return 'bg-emerald-50 text-emerald-700 border-emerald-200';
    }
  };

  return (
    <div className="tailadmin-card p-5">
      {/* Table Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
        <div>
          <h3 className="font-bold text-gray-900 text-base font-['Outfit'] flex items-center gap-2">
            <Truck className="w-4 h-4 text-[#465FFF]" />
            Live Hospital Surge & Emergency Dispatch Queue
          </h3>
          <p className="text-xs text-gray-500 mt-0.5">
            Automated bed, ventilator, and oxygen van allocation triggered by real-time ML risk & CAQM GRAP stages.
          </p>
        </div>
        
        <button
          onClick={handleExportLogs}
          className="flex items-center gap-1.5 px-3 py-1.5 bg-white hover:bg-gray-50 text-gray-700 border border-gray-200 rounded-xl text-xs font-semibold shadow-2xs transition self-start sm:self-auto cursor-pointer"
        >
          <Download className="w-3.5 h-3.5 text-gray-500" />
          Export Queue CSV
        </button>
      </div>

      {/* Table */}
      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs">
          <thead>
            <tr className="border-b border-gray-100 text-[11px] font-bold text-gray-400 uppercase tracking-wider bg-gray-50/50">
              <th className="py-2.5 px-3 rounded-l-lg">ID</th>
              <th className="py-2.5 px-3">Metro Hub</th>
              <th className="py-2.5 px-3">Atmospheric Trigger</th>
              <th className="py-2.5 px-3">Resource Allocation</th>
              <th className="py-2.5 px-3">CAQM GRAP Stage</th>
              <th className="py-2.5 px-3 text-right rounded-r-lg">Dispatch ETA</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {dispatchLogs.map((log) => (
              <tr key={log.id} className="hover:bg-gray-50/70 transition">
                <td className="py-3 px-3 font-mono font-semibold text-gray-500">
                  {log.id}
                </td>
                <td className="py-3 px-3">
                  <div className="font-bold text-gray-900">{log.city}</div>
                  <div className="text-[10px] text-gray-400">{log.state}</div>
                </td>
                <td className="py-3 px-3">
                  <div className="font-medium text-gray-700 flex items-center gap-1.5">
                    {log.urgency === 'critical' && <ShieldAlert className="w-3.5 h-3.5 text-rose-500 shrink-0" />}
                    {log.condition}
                  </div>
                </td>
                <td className="py-3 px-3 font-semibold text-[#465FFF]">
                  {log.resource}
                </td>
                <td className="py-3 px-3">
                  <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold border ${getUrgencyBadge(log.urgency)}`}>
                    {log.grap}
                  </span>
                </td>
                <td className="py-3 px-3 text-right font-bold text-gray-900 tabular-nums">
                  {log.eta}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
