import React, { createContext, useContext, useState, useEffect } from 'react';
import { translations } from './translations';

export const SUPPORTED_LANGUAGES = [
  { code: 'en', label: 'English', native: 'English' },
  { code: 'hi', label: 'Hindi', native: 'हिन्दी' },
  { code: 'mr', label: 'Marathi', native: 'मराठी' },
  { code: 'bn', label: 'Bengali', native: 'বাংলা' },
  { code: 'ta', label: 'Tamil', native: 'தமிழ்' },
  { code: 'te', label: 'Telugu', native: 'తెలుగు' },
  { code: 'kn', label: 'Kannada', native: 'ಕನ್ನಡ' },
  { code: 'ml', label: 'Malayalam', native: 'മലയാളം' },
  { code: 'gu', label: 'Gujarati', native: 'ગુજરાતી' },
  { code: 'pa', label: 'Punjabi', native: 'ਪੰਜਾਬੀ' },
  { code: 'or', label: 'Odia', native: 'ଓଡ଼ିଆ' },
  { code: 'as', label: 'Assamese', native: 'অসমীয়া' },
  { code: 'ur', label: 'Urdu', native: 'اردو' },
];

const LanguageContext = createContext(null);

export const LanguageProvider = ({ children }) => {
  const [language, setLanguageState] = useState(() => {
    try {
      return localStorage.getItem('aeromed_lang') || 'en';
    } catch {
      return 'en';
    }
  });

  const setLanguage = (lang) => {
    if (translations[lang]) {
      setLanguageState(lang);
      try {
        localStorage.setItem('aeromed_lang', lang);
      } catch (e) {
        // ignore
      }
    }
  };

  const isRtl = language === 'ur';

  useEffect(() => {
    document.documentElement.dir = isRtl ? 'rtl' : 'ltr';
    document.documentElement.lang = language;
  }, [language, isRtl]);

  /**
   * t(path, fallback)
   * Resolves dot notation keys like 'chrome.brand_name' or 'overview.kpi_current_aqi'
   */
  const t = (path, fallback = '') => {
    if (!path) return fallback;
    const parts = path.split('.');
    
    // 1. Try active language
    let cur = translations[language];
    let found = true;
    for (const part of parts) {
      if (cur && typeof cur === 'object' && part in cur) {
        cur = cur[part];
      } else {
        found = false;
        break;
      }
    }
    if (found && cur !== undefined && cur !== null) {
      return cur;
    }

    // 2. Try English fallback
    cur = translations.en;
    found = true;
    for (const part of parts) {
      if (cur && typeof cur === 'object' && part in cur) {
        cur = cur[part];
      } else {
        found = false;
        break;
      }
    }
    if (found && cur !== undefined && cur !== null) {
      return cur;
    }

    return fallback || path;
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t, isRtl, languages: SUPPORTED_LANGUAGES }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useTranslation = () => {
  const context = useContext(LanguageContext);
  if (!context) {
    // Provide a safe fallback if used outside provider
    return {
      language: 'en',
      setLanguage: () => {},
      t: (path, fallback = '') => fallback || path,
      isRtl: false,
      languages: SUPPORTED_LANGUAGES,
    };
  }
  return context;
};
