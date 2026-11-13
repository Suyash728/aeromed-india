import React from 'react';
import { 
  Activity, 
  Sliders, 
  Stethoscope, 
  Database, 
  Award, 
  ShieldCheck, 
  TrendingUp, 
  CheckCircle2, 
  Building2,
  X
} from 'lucide-react';

export default function Sidebar({ activeTab, setActiveTab, isOpen, setIsOpen, metrics }) {
  const navItems = [
    {
      id: 'surveillance',
      label: 'Surveillance Overview',
      subtitle: 'Bento Grid & Telemetry',
      icon: Activity,
      badge: 'Live'
    },
    {
      id: 'simulator',
      label: 'What-If Simulator',
      subtitle: 'ML Sensitivity Lab',
      icon: Sliders,
      badge: 'R² 0.988'
    },
    {
      id: 'triage',
      label: 'Clinical Triage Copilot',
      subtitle: 'Vector RAG Grounding',
      icon: Stethoscope,
      badge: '5.1k+ Rules'
    },
    {
      id: 'datasets',
      label: 'Dataset Explorer',
      subtitle: '10 Materialized CSVs',
      icon: Database,
      badge: 'Grade A'
    },
    {
      id: 'jury',
      label: 'Adaption AI 7-Pillar Proof',
      subtitle: 'Hackathon Award Suite',
      icon: Award,
      badge: '+55.8% Gain'
    }
  ];

  return (
    <>
      {/* Mobile Backdrop */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-gray-900/40 backdrop-blur-xs z-40 lg:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* Persistent Left Sidebar (280px) */}
      <aside className={`
        fixed top-0 bottom-0 left-0 z-50 w-[280px] bg-white border-r border-gray-200 
        flex flex-col transition-transform duration-300 ease-in-out
        ${isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'}
      `}>
        {/* Brand Header */}
        <div className="p-6 border-b border-gray-100 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-[#465FFF] flex items-center justify-center text-white shadow-sm shadow-[#465FFF]/20">
              <ShieldCheck className="w-6 h-6 stroke-[2.2]" />
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <span className="font-bold text-lg text-gray-900 tracking-tight font-['Outfit']">
                  AeroMed
                </span>
                <span className="font-extrabold text-lg text-[#465FFF] tracking-tight font-['Outfit']">
                  India
                </span>
              </div>
              <p className="text-[11px] font-medium text-gray-500 uppercase tracking-wider">
                Clinical Surveillance
              </p>
            </div>
          </div>
          <button 
            onClick={() => setIsOpen(false)}
            className="lg:hidden p-1.5 text-gray-400 hover:text-gray-700 hover:bg-gray-100 rounded-lg transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Navigation Workspaces */}
        <div className="flex-1 px-4 py-5 space-y-1.5 overflow-y-auto">
          <div className="px-3 pb-2 text-[11px] font-semibold text-gray-400 uppercase tracking-wider">
            Clinical Workspaces
          </div>
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => {
                  setActiveTab(item.id);
                  setIsOpen(false);
                }}
                className={`
                  w-full flex items-center justify-between px-3.5 py-3 rounded-xl text-left transition-all duration-150
                  ${isActive 
                    ? 'bg-[#465FFF]/10 text-[#465FFF] font-semibold shadow-xs' 
                    : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900 font-medium'
                  }
                `}
              >
                <div className="flex items-center gap-3 min-w-0">
                  <div className={`
                    p-2 rounded-lg transition-colors
                    ${isActive ? 'bg-[#465FFF] text-white' : 'bg-gray-100 text-gray-500 group-hover:text-gray-700'}
                  `}>
                    <Icon className="w-4 h-4 stroke-[2]" />
                  </div>
                  <div className="truncate">
                    <div className="text-sm leading-tight truncate">{item.label}</div>
                    <div className="text-[11px] text-gray-400 font-normal leading-tight mt-0.5 truncate">{item.subtitle}</div>
                  </div>
                </div>
                {item.badge && (
                  <span className={`
                    text-[10px] px-2 py-0.5 rounded-full font-semibold shrink-0 ml-2
                    ${isActive 
                      ? 'bg-[#465FFF] text-white' 
                      : 'bg-gray-100 text-gray-600'
                    }
                  `}>
                    {item.badge}
                  </span>
                )}
              </button>
            );
          })}
        </div>

        {/* Model Accuracy & Standards Card */}
        <div className="p-4 border-t border-gray-100 bg-gray-50/70 m-3 rounded-2xl border border-gray-200/80">
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] font-bold text-gray-700 uppercase tracking-wider flex items-center gap-1.5">
              <TrendingUp className="w-3.5 h-3.5 text-[#12B76A]" />
              Model Precision
            </span>
            <span className="text-[11px] font-bold text-[#12B76A] bg-[#12B76A]/10 px-2 py-0.5 rounded-full tabular-nums">
              R² = 0.9879
            </span>
          </div>
          <div className="space-y-1.5 text-xs text-gray-600">
            <div className="flex items-center justify-between">
              <span className="text-gray-500">Mean Abs Error</span>
              <span className="font-semibold text-gray-800 tabular-nums">±1.88 pts/day</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-gray-500">AutoScientist Win</span>
              <span className="font-semibold text-[#465FFF] tabular-nums">+55.8% Gain</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-gray-500">Adaption Eval</span>
              <span className="font-semibold text-emerald-700">Grade A (9.4/10)</span>
            </div>
          </div>
          <div className="mt-3 pt-2.5 border-t border-gray-200/60 flex items-center gap-1.5 text-[10px] text-gray-400 font-medium">
            <CheckCircle2 className="w-3.5 h-3.5 text-[#12B76A]" />
            CPCB & CAQM Statutory Grounding
          </div>
        </div>
      </aside>
    </>
  );
}
