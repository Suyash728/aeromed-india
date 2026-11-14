import React, { useState, useRef, useEffect } from 'react';
import { Search, Menu, Globe, ChevronDown, Check, Zap, FileText } from 'lucide-react';

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
  const [langDropdownOpen, setLangDropdownOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  
  const cityDropdownRef = useRef(null);
  const langDropdownRef = useRef(null);

  // Close dropdowns on outside click
  useEffect(() => {
    function handleClickOutside(event) {
      if (cityDropdownRef.current && !cityDropdownRef.current.contains(event.target)) {
        setCitySearchOpen(false);
      }
      if (langDropdownRef.current && !langDropdownRef.current.contains(event.target)) {
        setLangDropdownOpen(false);
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
  const activeLangObj = languages.find(l => l.code.toLowerCase() === selectedLanguage.toLowerCase()) || languages[0];

  // Quick switch language codes
  const quickPills = [
    { code: 'en', label: 'EN', full: 'English' },
    { code: 'hi', label: 'हिन्दी', full: 'Hindi' },
    { code: 'mr', label: 'मराठी', full: 'Marathi' },
  ];

  return (
    <header className="sticky top-0 z-30 bg-white/95 backdrop-blur-md border-b border-gray-200 px-4 sm:px-6 py-3 transition-all">
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
          <div className="relative" ref={cityDropdownRef}>
            <button
              onClick={() => setCitySearchOpen(!citySearchOpen)}
              className="flex items-center gap-2.5 px-3.5 py-1.5 bg-gray-50 hover:bg-gray-100 border border-gray-200 rounded-xl text-left transition group shadow-2xs cursor-pointer"
            >
              <div className="w-2.5 h-2.5 rounded-full bg-[#465FFF] animate-pulse" />
              <div>
                <div className="text-[10px] uppercase font-bold text-gray-400 tracking-wider leading-none">
                  Active Metro
                </div>
                <div className="text-sm font-bold text-gray-900 leading-tight flex items-center gap-1.5 mt-0.5 font-['Outfit']">
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
                          onSelectCity(city.name || city.id);
                          setCitySearchOpen(false);
                          setSearchQuery('');
                        }}
                        className={`
                          w-full flex items-center justify-between px-3 py-2 text-xs rounded-xl transition text-left cursor-pointer
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

        {/* Center / Right: Redesigned Popover Language Switcher + Actions */}
        <div className="flex items-center gap-3">
          
          {/* TailAdmin Language Switcher Component */}
          <div className="relative flex items-center gap-1.5 p-1 bg-gray-100/90 rounded-full border border-gray-200/90" ref={langDropdownRef}>
            
            {/* Active Language Main Pill */}
            <div className="flex items-center gap-1.5 pl-3 pr-2 py-1 text-xs font-bold text-[#465FFF] bg-white rounded-full shadow-2xs border border-gray-200/60">
              <Globe className="w-3.5 h-3.5 text-[#465FFF]" />
              <span className="font-sans">{activeLangObj?.native || 'English'}</span>
              <span className="text-[10px] text-gray-400 font-normal hidden sm:inline">• {activeLangObj?.name || 'English'}</span>
            </div>

            {/* 3 Quick Toggle Pills (EN, हिन्दी, मराठी) */}
            <div className="hidden md:flex items-center gap-1">
              {quickPills.map((pill) => {
                const isActive = selectedLanguage.toLowerCase() === pill.code.toLowerCase();
                return (
                  <button
                    key={pill.code}
                    onClick={() => onSelectLanguage(pill.code)}
                    className={`
                      px-2.5 py-1 rounded-full text-xs font-semibold transition cursor-pointer
                      ${isActive 
                        ? 'bg-[#465FFF] text-white shadow-xs' 
                        : 'text-gray-600 hover:text-gray-900 hover:bg-white/80'
                      }
                    `}
                    title={`Switch to ${pill.full}`}
                  >
                    {pill.label}
                  </button>
                );
              })}
            </div>

            {/* +10 More Popover Trigger Button */}
            <button
              onClick={() => setLangDropdownOpen(!langDropdownOpen)}
              className="flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold text-gray-700 hover:text-gray-900 hover:bg-white transition cursor-pointer"
            >
              <span>+{Math.max(1, languages.length - 3)} More</span>
              <ChevronDown className="w-3.5 h-3.5 text-gray-400" />
            </button>

            {/* 2-Column Full Indic Language Popover */}
            {langDropdownOpen && (
              <div className="absolute top-full right-0 mt-2 w-80 sm:w-96 bg-white border border-gray-200 rounded-2xl shadow-2xl p-3.5 z-50 animate-in fade-in slide-in-from-top-2 duration-150">
                <div className="flex items-center justify-between border-b border-gray-100 pb-2 mb-2.5">
                  <div>
                    <div className="font-bold text-gray-900 text-xs font-['Outfit'] flex items-center gap-1.5">
                      <Globe className="w-3.5 h-3.5 text-[#465FFF]" />
                      Select Surveillance Language
                    </div>
                    <div className="text-[10px] text-gray-400">
                      13 Indic scripts with verified medical lexicons
                    </div>
                  </div>
                  <span className="text-[10px] font-bold text-[#465FFF] bg-[#465FFF]/10 px-2 py-0.5 rounded-full">
                    {languages.length} Scripts
                  </span>
                </div>

                {/* 2-Column Grid */}
                <div className="grid grid-cols-2 gap-1.5 max-h-72 overflow-y-auto pr-1">
                  {languages.map((lang) => {
                    const isSelected = selectedLanguage.toLowerCase() === lang.code.toLowerCase();
                    return (
                      <button
                        key={lang.code}
                        onClick={() => {
                          onSelectLanguage(lang.code);
                          setLangDropdownOpen(false);
                        }}
                        className={`
                          flex items-center justify-between p-2 rounded-xl text-left transition border cursor-pointer
                          ${isSelected 
                            ? 'bg-[#465FFF]/10 border-[#465FFF] text-[#465FFF] font-bold shadow-2xs' 
                            : 'bg-gray-50/70 hover:bg-gray-100 border-gray-200/80 text-gray-700'
                          }
                        `}
                      >
                        <div className="min-w-0 pr-1">
                          <div className="text-xs font-extrabold text-gray-900 leading-tight">
                            {lang.native}
                          </div>
                          <div className="text-[10px] text-gray-500 leading-tight mt-0.5 truncate">
                            {lang.name}
                          </div>
                          <div className="text-[9px] text-gray-400 mt-0.5">
                            {lang.region || 'Indic'}
                          </div>
                        </div>
                        {isSelected && <Check className="w-4 h-4 text-[#465FFF] shrink-0" />}
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
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
          <div className="shrink-0 flex items-center gap-2 px-3 py-1.5 rounded-full border text-xs font-semibold shadow-2xs bg-white">
            {isLiveApi ? (
              <div className="flex items-center gap-2 text-emerald-700">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                </span>
                <span className="hidden sm:inline">Render API Connected • R² = 0.988</span>
                <span className="sm:hidden">Live API</span>
              </div>
            ) : (
              <div className="flex items-center gap-1.5 text-amber-700">
                <Zap className="w-3.5 h-3.5 text-amber-500" />
                <span className="hidden sm:inline">Instant Seed Mode (0ms)</span>
                <span className="sm:hidden">Seed Mode</span>
              </div>
            )}
          </div>
        </div>

      </div>
    </header>
  );
}
