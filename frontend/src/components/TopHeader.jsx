import React, { useState, useRef, useEffect } from 'react';
import { Search, Menu, Globe, ChevronDown, Check, Zap, Server, FileText } from 'lucide-react';

export default function TopHeader({ 
  cities, 
  selectedCity, 
  onSelectCity, 
  languages, 
  selectedLanguage, 
  onSelectLanguage, 
  isLiveApi, 
  setSidebarOpen,
  onOpenExportModal
}) {
  const [citySearchOpen, setCitySearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const dropdownRef = useRef(null);

  // Close dropdown on outside click
  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setCitySearchOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const filteredCities = cities.filter(c => 
    c.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    (c.state && c.state.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  const activeCityObj = cities.find(c => c.id.toLowerCase() === selectedCity.toLowerCase()) || cities[0];

  return (
    <header className="sticky top-0 z-30 bg-white/95 backdrop-blur-md border-b border-gray-200 px-4 sm:px-6 py-3.5 transition-all">
      <div className="flex items-center justify-between gap-4">
        
        {/* Left Side: Mobile Menu & City Selector */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => setSidebarOpen(true)}
            className="lg:hidden p-2 text-gray-500 hover:text-gray-900 hover:bg-gray-100 rounded-xl transition"
            aria-label="Open Navigation"
          >
            <Menu className="w-5 h-5" />
          </button>

          {/* Quick City Dropdown with ⌘K Badge */}
          <div className="relative" ref={dropdownRef}>
            <button
              onClick={() => setCitySearchOpen(!citySearchOpen)}
              className="flex items-center gap-2.5 px-3.5 py-2 bg-gray-50 hover:bg-gray-100 border border-gray-200 rounded-xl text-left transition group shadow-2xs"
            >
              <div className="w-2.5 h-2.5 rounded-full bg-[#465FFF] animate-pulse" />
              <div>
                <div className="text-[10px] uppercase font-bold text-gray-400 tracking-wider leading-none">
                  Active Metro
                </div>
                <div className="text-sm font-bold text-gray-900 leading-tight flex items-center gap-1.5 mt-0.5">
                  {activeCityObj?.name || 'Delhi'}
                  <span className="text-xs text-gray-400 font-normal">({activeCityObj?.state})</span>
                </div>
              </div>
              <ChevronDown className="w-4 h-4 text-gray-400 group-hover:text-gray-700 transition ml-1" />
              <span className="hidden sm:inline-flex text-[10px] font-semibold text-gray-400 bg-white px-1.5 py-0.5 rounded border border-gray-200 ml-1">
                ⌘K
              </span>
            </button>

            {/* City Dropdown Menu */}
            {citySearchOpen && (
              <div className="absolute top-full left-0 mt-2 w-72 bg-white border border-gray-200 rounded-2xl shadow-xl p-2 z-50 animate-in fade-in slide-in-from-top-2 duration-150">
                <div className="relative mb-2">
                  <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                  <input
                    type="text"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    placeholder="Search 12 Indian Metros..."
                    className="w-full pl-9 pr-3 py-2 text-xs bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#465FFF]/30 focus:border-[#465FFF]"
                    autoFocus
                  />
                </div>
                <div className="max-h-60 overflow-y-auto space-y-1 pr-1">
                  {filteredCities.map((city) => {
                    const isSelected = city.id.toLowerCase() === selectedCity.toLowerCase();
                    return (
                      <button
                        key={city.id}
                        onClick={() => {
                          onSelectCity(city.id);
                          setCitySearchOpen(false);
                          setSearchQuery('');
                        }}
                        className={`
                          w-full flex items-center justify-between px-3 py-2 text-xs rounded-xl transition text-left
                          ${isSelected 
                            ? 'bg-[#465FFF]/10 text-[#465FFF] font-bold' 
                            : 'text-gray-700 hover:bg-gray-50 hover:text-gray-900'
                          }
                        `}
                      >
                        <div>
                          <div className="font-semibold">{city.name}</div>
                          <div className="text-[10px] text-gray-400 font-normal">{city.state}</div>
                        </div>
                        {isSelected && <Check className="w-4 h-4 text-[#465FFF]" />}
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Center / Right: Indic Language Selector Pill Bar */}
        <div className="flex items-center gap-3 overflow-hidden">
          {/* Scrollable Language Pill Bar */}
          <div className="hidden md:flex items-center gap-1.5 p-1 bg-gray-100/80 rounded-full border border-gray-200/80 max-w-xl overflow-x-auto no-scrollbar">
            <span className="pl-2.5 pr-1 text-gray-400 flex items-center gap-1 text-xs">
              <Globe className="w-3.5 h-3.5" />
            </span>
            {languages.map((lang) => {
              const isActive = selectedLanguage.toLowerCase() === lang.code.toLowerCase();
              return (
                <button
                  key={lang.code}
                  onClick={() => onSelectLanguage(lang.code)}
                  className={`
                    px-3 py-1 rounded-full text-xs transition-all whitespace-nowrap font-medium
                    ${isActive
                      ? 'bg-[#465FFF] text-white font-semibold shadow-xs'
                      : 'text-gray-600 hover:text-gray-900 hover:bg-white/60'
                    }
                  `}
                  title={`${lang.name} (${lang.native})`}
                >
                  <span className="font-sans mr-1">{lang.native}</span>
                  <span className="text-[10px] opacity-75 uppercase">({lang.code})</span>
                </button>
              );
            })}
          </div>

          {/* Export Health & GRAP Advisory Button */}
          <button
            onClick={onOpenExportModal}
            className="shrink-0 flex items-center gap-1.5 px-3 py-1.5 bg-[#465FFF]/10 hover:bg-[#465FFF]/20 text-[#465FFF] border border-[#465FFF]/30 rounded-full text-xs font-semibold shadow-2xs transition cursor-pointer"
            title="Export official printable hospital & citizen advisory bulletin"
          >
            <FileText className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Export Advisory</span>
            <span className="sm:hidden">Bulletin</span>
          </button>

          {/* Backend Connection Status Pill */}
          <div className="shrink-0 flex items-center gap-2 px-3 py-1.5 rounded-full border text-xs font-semibold shadow-2xs">
            {isLiveApi ? (
              <div className="flex items-center gap-2 text-emerald-700 bg-emerald-50 border-emerald-200">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                </span>
                <span className="hidden sm:inline">Render API Connected • R² = 0.988</span>
                <span className="sm:hidden">Live API</span>
              </div>
            ) : (
              <div className="flex items-center gap-1.5 text-amber-700 bg-amber-50 border-amber-200">
                <Zap className="w-3.5 h-3.5 text-amber-500" />
                <span className="hidden sm:inline">Instant Seed Mode (0ms)</span>
                <span className="sm:hidden">Seed Mode</span>
              </div>
            )}
          </div>
        </div>

      </div>

      {/* Mobile Language Bar (horizontal scroll below header on small screens) */}
      <div className="md:hidden mt-2.5 flex items-center gap-1.5 overflow-x-auto pb-1 no-scrollbar border-t border-gray-100 pt-2">
        <span className="text-[11px] text-gray-400 font-semibold uppercase shrink-0">Lang:</span>
        {languages.map((lang) => {
          const isActive = selectedLanguage.toLowerCase() === lang.code.toLowerCase();
          return (
            <button
              key={lang.code}
              onClick={() => onSelectLanguage(lang.code)}
              className={`
                px-2.5 py-0.5 rounded-full text-[11px] shrink-0 font-medium
                ${isActive ? 'bg-[#465FFF] text-white font-bold' : 'bg-gray-100 text-gray-700'}
              `}
            >
              {lang.native}
            </button>
          );
        })}
      </div>
    </header>
  );
}
