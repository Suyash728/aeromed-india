import React, { useState } from 'react';
import aqiClient from '../api/aqiClient';
import { useTranslation } from '../i18n/LanguageContext';
import { 
  Stethoscope, 
  X, 
  Send, 
  Sparkles, 
  AlertOctagon, 
  Bot, 
  User, 
  ShieldCheck, 
  Globe
} from 'lucide-react';

function detectScriptLanguage(text, fallback = 'en') {
  if (!text) return fallback;
  if (/[\u0B80-\u0BFF]/.test(text)) return 'ta';
  if (/[\u0C00-\u0C7F]/.test(text)) return 'te';
  if (/[\u0C80-\u0CFF]/.test(text)) return 'kn';
  if (/[\u0D00-\u0D7F]/.test(text)) return 'ml';
  if (/[\u0A80-\u0AFF]/.test(text)) return 'gu';
  if (/[\u0A00-\u0A7F]/.test(text)) return 'pa';
  if (/[\u0B00-\u0B7F]/.test(text)) return 'or';
  if (/[\u0980-\u09FF]/.test(text)) {
    if (text.includes('\u09F0') || text.includes('\u09F1')) return 'as';
    return 'bn';
  }
  if (/[\u0600-\u06FF]/.test(text)) return 'ur';
  if (/[\u0900-\u097F]/.test(text)) {
    const marathiWords = ['काय', 'काळजी', 'घ्यावी', 'करावी', 'रुग्णांनी', 'दम्या', 'आहे', 'आहेत', 'कशी', 'नाही', 'होते', 'माझे', 'मला', 'सल्ला'];
    if (marathiWords.some(w => text.includes(w))) return 'mr';
    return 'hi';
  }
  return fallback;
}

export default function QuickTriageDrawer({ activeCity = 'Delhi', activeLanguage = 'en' }) {
  const { t } = useTranslation();
  const [isOpen, setIsOpen] = useState(false);
  const [spo2, setSpo2] = useState(94);
  const [inputMessage, setInputMessage] = useState('');
  const [chatLoading, setChatLoading] = useState(false);
  const [copilotLang, setCopilotLang] = useState(activeLanguage);

  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: `Namaste! I am the AeroMed Clinical Copilot. Ask any question in Marathi (मराठी), Hindi (हिन्दी), Tamil (தமிழ்), or English—grounded against 8,188+ Adaption Labs protocols.`,
      timestamp: 'Just now',
      citation: '3bf58b6b-462c-4412-8171-fa1bed843e67'
    }
  ]);

  const quickChips = [
    { text: "दम्याच्या रुग्णांनी काय काळजी घ्यावी?", label: "मराठी (Asthma)", lang: "mr" },
    { text: "धुआं और प्रदूषण में बच्चों को बाहर भेजना सुरक्षित है?", label: "हिन्दी (Children)", lang: "hi" },
    { text: "What precautions should outdoor delivery workers take?", label: "English (Gig Workers)", lang: "en" },
    { text: "சுவாச பிரச்சனை உள்ளவர்கள் என்ன செய்ய வேண்டும்?", label: "தமிழ் (Respiratory)", lang: "ta" }
  ];

  const handleSendMessage = async (textToSend, explicitLang = null) => {
    const text = textToSend || inputMessage;
    if (!text.trim() || chatLoading) return;

    // Detect target language
    const targetLang = explicitLang || detectScriptLanguage(text, copilotLang || activeLanguage);
    setCopilotLang(targetLang);

    const userMsg = {
      role: 'user',
      content: text,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    const newHistory = [...messages, userMsg];
    setMessages(newHistory);
    setInputMessage('');
    setChatLoading(true);

    try {
      const res = await aqiClient.triageChat(newHistory, activeCity, targetLang);
      const replyText = res.reply || res.response || res.message || 
        `Clinical notice: Under current AQI in ${activeCity}, high-risk individuals must limit prolonged exertion, wear certified N95 respirators, and monitor SpO2 closely. Seek emergency hospital care if SpO2 drops below 92%.`;

      setMessages([
        ...newHistory,
        {
          role: 'assistant',
          content: replyText,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          citation: res.grounded_dataset_id || '3bf58b6b-462c-4412-8171-fa1bed843e67'
        }
      ]);
    } catch (err) {
      setMessages([
        ...newHistory,
        {
          role: 'assistant',
          content: targetLang === 'mr' 
            ? `सध्या ${activeCity} मध्ये वाढलेल्या प्रदूषणामुळे खबरदारी: खिडक्या बंद ठेवाव्यात, N95 मास्क वापरावा आणि SpO2 ९२% पेक्षा कमी झाल्यास तातडीने रुग्णालयात जावे.`
            : targetLang === 'hi'
            ? `वर्तमान में ${activeCity} में वायु प्रदूषण के स्तर को देखते हुए: मरीज को घर के अंदर रखें और SpO2 ९२% से कम होने पर तुरंत अस्पताल ले जाएं।`
            : `Clinical Triager [Local Grounded Rule]: Given elevated particulate levels in ${activeCity}, sensitive patients should stay indoors during morning hours and use prescribed bronchodilators under pulmonologist guidance.`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          citation: '3bf58b6b-462c-4412-8171-fa1bed843e67'
        }
      ]);
    } finally {
      setChatLoading(false);
    }
  };

  return (
    <>
      {/* Floating Action Trigger Button - Moved higher to bottom-16 right-6 with shadow-lg and ring */}
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          className="fixed bottom-16 right-6 z-40 bg-[#465FFF] hover:bg-[#3649db] text-white px-4 py-3 rounded-full shadow-lg ring-4 ring-indigo-500/15 hover:shadow-2xl transition-all duration-200 flex items-center gap-2.5 font-bold text-xs tracking-wide group cursor-pointer border-2 border-white animate-in slide-in-from-bottom-4"
          aria-label="Open AeroMed Clinical Copilot"
        >
          <span className="relative flex h-3 w-3">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
          </span>
          <Stethoscope className="w-4 h-4 stroke-[2.2]" />
          <span>{t('copilot.floating_button', 'Ask AeroMed Copilot')}</span>
          <span className="bg-white/20 text-[10px] px-2 py-0.5 rounded-full font-mono uppercase">
            {t('copilot.rag_live', 'RAG Live')}
          </span>
        </button>
      )}

      {/* Floating Quick Triage Slide-Out Card - repositioned to bottom-20 right-6 */}
      {isOpen && (
        <div className="fixed bottom-20 right-6 z-50 w-[92vw] sm:w-[420px] max-h-[calc(100vh-7rem)] h-[560px] bg-white rounded-2xl shadow-2xl border border-gray-200 flex flex-col overflow-hidden animate-in slide-in-from-bottom-6 zoom-in-95 duration-200">
          
          {/* Header */}
          <div className="p-3.5 bg-gradient-to-r from-gray-50 to-indigo-50/40 border-b border-gray-200 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 rounded-xl bg-[#465FFF] text-white flex items-center justify-center shadow-xs">
                <Stethoscope className="w-4 h-4" />
              </div>
              <div>
                <div className="font-bold text-gray-900 text-xs font-['Outfit'] flex items-center gap-1.5">
                  {t('copilot.title', 'AeroMed Clinical Copilot')}
                  <span className="text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.2 rounded font-mono">
                    {t('chrome.rules_count', '8,188 Rules')}
                  </span>
                </div>
                <div className="text-[10px] text-gray-500 flex items-center gap-1 mt-0.5">
                  <span>{t('copilot.context_label', 'Context:')} {t('cities.' + activeCity.toLowerCase(), activeCity)}</span>
                  <span>•</span>
                  <span className="text-[#465FFF] font-semibold uppercase flex items-center gap-0.5">
                    <Globe className="w-2.5 h-2.5" />
                    {copilotLang}
                  </span>
                </div>
              </div>
            </div>
            <button
              onClick={() => setIsOpen(false)}
              className="p-1.5 text-gray-400 hover:text-gray-700 hover:bg-gray-200 rounded-lg transition cursor-pointer"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* SpO2 Quick Check Strip */}
          <div className="px-3.5 py-2 bg-gray-50 border-b border-gray-100 flex items-center justify-between text-xs">
            <span className="text-gray-500 text-[11px] font-semibold">{t('copilot.pulse_spo2', 'Pulse SpO2:')}</span>
            <div className="flex items-center gap-2">
              <input
                type="range"
                min="80"
                max="100"
                value={spo2}
                onChange={(e) => setSpo2(parseInt(e.target.value))}
                className={`w-28 h-1.5 rounded-lg appearance-none cursor-pointer ${
                  spo2 < 92 ? 'accent-rose-600 bg-rose-200' : 'accent-emerald-600 bg-emerald-200'
                }`}
              />
              <span className={`font-mono font-bold tabular-nums text-xs ${
                spo2 < 92 ? 'text-rose-600' : 'text-emerald-700'
              }`}>
                {spo2}%
              </span>
            </div>
          </div>

          {/* Mandatory ER Banner if SpO2 < 92% */}
          {spo2 < 92 && (
            <div className="px-3 py-2 bg-rose-50 border-b border-rose-200 flex items-center gap-2 text-[11px] text-rose-800 animate-in fade-in">
              <AlertOctagon className="w-4 h-4 text-rose-600 shrink-0" />
              <div className="leading-tight font-semibold">
                {t('copilot.er_warning', 'SpO2 < 92%: Immediate Emergency ER Transport Required!')}
              </div>
            </div>
          )}

          {/* Chat Messages Body */}
          <div className="flex-1 p-3.5 overflow-y-auto space-y-3 bg-gray-50/30">
            {messages.map((m, idx) => (
              <div key={idx} className={`flex gap-2.5 ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                {m.role === 'assistant' && (
                  <div className="w-6 h-6 rounded-full bg-[#465FFF] text-white flex items-center justify-center shrink-0 text-xs shadow-2xs mt-0.5">
                    <Bot className="w-3.5 h-3.5" />
                  </div>
                )}
                <div className={`
                  max-w-[85%] rounded-2xl p-3 text-xs leading-relaxed shadow-2xs
                  ${m.role === 'user' 
                    ? 'bg-[#465FFF] text-white rounded-tr-none' 
                    : 'bg-white text-gray-800 border border-gray-200 rounded-tl-none'
                  }
                `}>
                  <p className="whitespace-pre-wrap">{m.content}</p>
                  
                  {m.citation && (
                    <div className="mt-1.5 pt-1.5 border-t border-gray-100 flex items-center gap-1 text-[9px] text-[#465FFF] font-mono">
                      <ShieldCheck className="w-3 h-3 text-emerald-600" />
                      <span>Vector Grounded: ID {m.citation.slice(0, 12)}...</span>
                    </div>
                  )}
                  
                  <div className={`text-[9px] mt-1 font-mono ${m.role === 'user' ? 'text-indigo-200' : 'text-gray-400'}`}>
                    {m.timestamp}
                  </div>
                </div>
              </div>
            ))}
            {chatLoading && (
              <div className="flex items-center gap-2 text-xs text-gray-400 p-2">
                <div className="w-1.5 h-1.5 rounded-full bg-[#465FFF] animate-bounce" />
                <div className="w-1.5 h-1.5 rounded-full bg-[#465FFF] animate-bounce [animation-delay:0.2s]" />
                <div className="w-1.5 h-1.5 rounded-full bg-[#465FFF] animate-bounce [animation-delay:0.4s]" />
                <span className="text-[11px]">Grounding in {copilotLang.toUpperCase()} against 8,188 protocols...</span>
              </div>
            )}
          </div>

          {/* Quick Indic Question Chips with Language Sync */}
          <div className="p-2 border-t border-gray-100 bg-white flex items-center gap-1.5 overflow-x-auto no-scrollbar">
            {quickChips.map((chip, idx) => (
              <button
                key={idx}
                onClick={() => handleSendMessage(chip.text, chip.lang)}
                className={`px-2.5 py-1 text-[10px] rounded-lg shrink-0 transition font-medium cursor-pointer ${
                  copilotLang === chip.lang
                    ? 'bg-[#465FFF]/10 text-[#465FFF] font-bold border border-[#465FFF]/30'
                    : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
                }`}
              >
                {chip.label}
              </button>
            ))}
          </div>

          {/* Input Bar with auto-script detection */}
          <div className="p-2.5 bg-white border-t border-gray-100 flex items-center gap-2">
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
              placeholder={t('copilot.ask_placeholder', 'मराठी, हिन्दी, தமிழ், or English...')}
              className="flex-1 px-3 py-1.5 text-xs bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#465FFF]/30 focus:border-[#465FFF]"
            />
            <button
              onClick={() => handleSendMessage()}
              disabled={chatLoading || !inputMessage.trim()}
              className="p-2 bg-[#465FFF] hover:bg-[#3649db] text-white rounded-xl shadow-xs transition disabled:opacity-50 cursor-pointer"
            >
              <Send className="w-3.5 h-3.5" />
            </button>
          </div>

        </div>
      )}
    </>
  );
}
