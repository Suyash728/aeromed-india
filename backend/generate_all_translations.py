# -*- coding: utf-8 -*-
import json

cities_data = {
    "en": {
        "delhi": "Delhi", "mumbai": "Mumbai", "navi mumbai": "Navi Mumbai", "bengaluru": "Bengaluru",
        "kolkata": "Kolkata", "chennai": "Chennai", "hyderabad": "Hyderabad", "ahmedabad": "Ahmedabad",
        "pune": "Pune", "amritsar": "Amritsar", "bhubaneswar": "Bhubaneswar", "guwahati": "Guwahati",
        "delhi ncr": "Delhi NCR", "maharashtra": "Maharashtra", "karnataka": "Karnataka",
        "west bengal": "West Bengal", "tamil nadu": "Tamil Nadu", "telangana": "Telangana",
        "gujarat": "Gujarat", "punjab": "Punjab", "odisha": "Odisha", "assam": "Assam"
    },
    "hi": {
        "delhi": "दिल्ली", "mumbai": "मुंबई", "navi mumbai": "नवी मुंबई", "bengaluru": "बेंगलुरु",
        "kolkata": "कोलकाता", "chennai": "चेन्नई", "hyderabad": "हैदराबाद", "ahmedabad": "अहमदाबाद",
        "pune": "पुणे", "amritsar": "अमृतसर", "bhubaneswar": "भुवनेश्वर", "guwahati": "गुवाहाटी",
        "delhi ncr": "दिल्ली एनसीआर", "maharashtra": "महाराष्ट्र", "karnataka": "कर्नाटक",
        "west bengal": "पश्चिम बंगाल", "tamil nadu": "तमिलनाडु", "telangana": "तेलंगाना",
        "gujarat": "गुजरात", "punjab": "पंजाब", "odisha": "ओडिशा", "assam": "असम"
    },
    "mr": {
        "delhi": "दिल्ली", "mumbai": "मुंबई", "navi mumbai": "नवी मुंबई", "bengaluru": "बंगळुरू",
        "kolkata": "कोलकाता", "chennai": "चेन्नई", "hyderabad": "हैदराबाद", "ahmedabad": "अहमदाबाद",
        "pune": "पुणे", "amritsar": "अमृतसर", "bhubaneswar": "भुवनेश्वर", "guwahati": "गुवाहाटी",
        "delhi ncr": "दिल्ली एनसीआर", "maharashtra": "महाराष्ट्र", "karnataka": "कर्नाटक",
        "west bengal": "पश्चिम बंगाल", "tamil nadu": "तमिळनाडू", "telangana": "तेलंगणा",
        "gujarat": "गुजरात", "punjab": "पंजाब", "odisha": "ओडिशा", "assam": "आसाम"
    },
    "bn": {
        "delhi": "দিল্লি", "mumbai": "মুম্বাই", "navi mumbai": "নভি মুম্বাই", "bengaluru": "বেঙ্গালুরু",
        "kolkata": "কলকাতা", "chennai": "চেন্নাই", "hyderabad": "হায়দ্রাবাদ", "ahmedabad": "আহমেদাবাদ",
        "pune": "পুনে", "amritsar": "অমৃতসর", "bhubaneswar": "ভুবনেশ্বর", "guwahati": "গুয়াহাটি",
        "delhi ncr": "দিল্লি এনসিআর", "maharashtra": "মহারাষ্ট্র", "karnataka": "কর্ণাটক",
        "west bengal": "পশ্চিমবঙ্গ", "tamil nadu": "তামিলনাড়ু", "telangana": "তেলেঙ্গানা",
        "gujarat": "গুজরাট", "punjab": "পাঞ্জাব", "odisha": "ওড়িশা", "assam": "আসাম"
    },
    "ta": {
        "delhi": "தில்லி", "mumbai": "மும்பை", "navi mumbai": "நவி மும்பை", "bengaluru": "பெங்களூரு",
        "kolkata": "கொல்கத்தா", "chennai": "சென்னை", "hyderabad": "ஹைதராபாத்", "ahmedabad": "அகமதாபாத்",
        "pune": "புனே", "amritsar": "அமிர்தசரஸ்", "bhubaneswar": "புவனேஸ்வர்", "guwahati": "குவஹாத்தி",
        "delhi ncr": "தில்லி என்சிஆர்", "maharashtra": "மகாராஷ்டிரா", "karnataka": "கர்நாடகா",
        "west bengal": "மேற்கு வங்கம்", "tamil nadu": "தமிழ்நாடு", "telangana": "தெலுங்கானா",
        "gujarat": "குஜராத்", "punjab": "பஞ்சாப்", "odisha": "ஒடிசா", "assam": "அசாம்"
    },
    "te": {
        "delhi": "ఢిల్లీ", "mumbai": "ముంబై", "navi mumbai": "నవీ ముంబై", "bengaluru": "బెంగళూరు",
        "kolkata": "కోల్‌కతా", "chennai": "చెన్నై", "hyderabad": "హైదరాబాద్", "ahmedabad": "అహ్మదాబాద్",
        "pune": "పూణే", "amritsar": "అమృత్‌సర్", "bhubaneswar": "భువనేశ్వర్", "guwahati": "గౌహతి",
        "delhi ncr": "ఢిల్లీ ఎన్‌సిఆర్", "maharashtra": "మహారాష్ట్ర", "karnataka": "కర్ణాటక",
        "west bengal": "పశ్చిమ బెంగాల్", "tamil nadu": "తమిళనాడు", "telangana": "తెలంగాణ",
        "gujarat": "గుజరాత్", "punjab": "పంజాబ్", "odisha": "ఒడిశా", "assam": "అస్సాం"
    },
    "kn": {
        "delhi": "ದೆಹಲಿ", "mumbai": "ಮುಂಬೈ", "navi mumbai": "ನವಿ ಮುಂಬೈ", "bengaluru": "ಬೆಂಗಳೂರು",
        "kolkata": "ಕೋಲ್ಕತ್ತಾ", "chennai": "ಚೆನ್ನೈ", "hyderabad": "ಹೈದರಾಬಾದ್", "ahmedabad": "ಅಹಮದಾಬಾದ್",
        "pune": "ಪುಣೆ", "amritsar": "ಅಮೃತಸರ", "bhubaneswar": "ಭುವನೇಶ್ವರ", "guwahati": "ಗುವಾಹಾಟಿ",
        "delhi ncr": "ದೆಹಲಿ ಎನ್‌ಸಿಆರ್", "maharashtra": "ಮಹಾರಾಷ್ಟ್ರ", "karnataka": "ಕರ್ನಾಟಕ",
        "west bengal": "ಪಶ್ಚಿಮ ಬಂಗಾಳ", "tamil nadu": "ತಮಿಳುನಾಡು", "telangana": "ತೆಲಂಗಾಣ",
        "gujarat": "ಗುಜರಾತ್", "punjab": "ಪಂಜಾಬ್", "odisha": "ಒಡಿಶಾ", "assam": "ಅಸ್ಸಾಂ"
    },
    "ml": {
        "delhi": "ദില്ലി", "mumbai": "മുംബൈ", "navi mumbai": "നവി മുംബൈ", "bengaluru": "ബംഗളൂരു",
        "kolkata": "കൊൽക്കത്ത", "chennai": "ചെന്നൈ", "hyderabad": "ഹൈദരാബാദ്", "ahmedabad": "അഹമ്മദാബാദ്",
        "pune": "പൂനെ", "amritsar": "അമൃത്സർ", "bhubaneswar": "ഭുവനേശ്വർ", "guwahati": "ഗുവാഹത്തി",
        "delhi ncr": "ഡൽഹി എൻസിആർ", "maharashtra": "മഹാരാഷ്ട്ര", "karnataka": "കർണാടക",
        "west bengal": "പശ്ചിമ ബംഗാൾ", "tamil nadu": "തമിഴ്നാട്", "telangana": "തെലങ്കാന",
        "gujarat": "ഗുജറാത്ത്", "punjab": "പഞ്ചാബ്", "odisha": "ഒഡീഷ", "assam": "അസം"
    },
    "gu": {
        "delhi": "દિલ્હી", "mumbai": "મુંબઈ", "navi mumbai": "નવી મુંબઈ", "bengaluru": "બેંગલુરુ",
        "kolkata": "કોલકાતા", "chennai": "ચેન્નઈ", "hyderabad": "હૈદરાબાદ", "ahmedabad": "અમદાવાદ",
        "pune": "પુણે", "amritsar": "અમૃતસર", "bhubaneswar": "ભુવનેશ્વર", "guwahati": "ગુવાહાટી",
        "delhi ncr": "દિલ્હી એનસીઆર", "maharashtra": "મહારાષ્ટ્ર", "karnataka": "કર્ણાટક",
        "west bengal": "પશ્ચિમ બંગાળ", "tamil nadu": "તમિલનાડુ", "telangana": "તેલંગાણા",
        "gujarat": "ગુજરાત", "punjab": "પંજાબ", "odisha": "ઓડિશા", "assam": "આસામ"
    },
    "pa": {
        "delhi": "ਦਿੱਲੀ", "mumbai": "ਮੁੰਬਈ", "navi mumbai": "ਨਵੀਂ ਮੁੰਬਈ", "bengaluru": "ਬੈਂਗਲੁਰੂ",
        "kolkata": "ਕੋਲਕਾਤਾ", "chennai": "ਚੇਨਈ", "hyderabad": "ਹੈਦਰਾਬਾਦ", "ahmedabad": "ਅਹਿਮਦਾਬਾਦ",
        "pune": "ਪੁਣੇ", "amritsar": "ਅੰਮ੍ਰਿਤਸਰ", "bhubaneswar": "ਭੁਵਨੇਸ਼ਵਰ", "guwahati": "ਗੁਵਾਹਾਟੀ",
        "delhi ncr": "ਦਿੱਲੀ ਐੱਨਸੀਆਰ", "maharashtra": "ਮਹਾਰਾਸ਼ਟਰ", "karnataka": "ਕਰਨਾਟਕ",
        "west bengal": "ਪੱਛਮੀ ਬੰਗਾਲ", "tamil nadu": "ਤਾਮਿਲਨਾਡੂ", "telangana": "ਤੇਲੰਗਾਨਾ",
        "gujarat": "ਗੁਜਰਾਤ", "punjab": "ਪੰਜਾਬ", "odisha": "ਓਡੀਸ਼ਾ", "assam": "ਅਸਾਮ"
    },
    "or": {
        "delhi": "ଦିଲ୍ଲୀ", "mumbai": "ମୁମ୍ବାଇ", "navi mumbai": "ନୂଆ ମୁମ୍ବାଇ", "bengaluru": "ବେଙ୍ଗାଲୁରୁ",
        "kolkata": "କୋଲକାତା", "chennai": "ଚେନ୍ନାଇ", "hyderabad": "ହାଇଦ୍ରାବାଦ", "ahmedabad": "ଅହମ୍ମଦାବାଦ୍",
        "pune": "ପୁଣେ", "amritsar": "ଅମୃତସର", "bhubaneswar": "ଭୁବନେଶ୍ୱର", "guwahati": "ଗୁଆହାଟୀ",
        "delhi ncr": "ଦିଲ୍ଲୀ ଏନସିଆର", "maharashtra": "ମହାରାଷ୍ଟ୍ର", "karnataka": "କର୍ଣ୍ଣାଟକ",
        "west bengal": "ପଶ୍ଚିମବଙ୍ଗ", "tamil nadu": "ତାମିଲନାଡୁ", "telangana": "ତେଲେଙ୍ଗାନା",
        "gujarat": "ଗୁଜରାଟ", "punjab": "ପଞ୍ଜାବ", "odisha": "ଓଡ଼ିଶା", "assam": "ଆସାମ"
    },
    "as": {
        "delhi": "দিল্লী", "mumbai": "মুম্বাই", "navi mumbai": "নৱী মুম্বাই", "bengaluru": "বেংগালুৰু",
        "kolkata": "কলকাতা", "chennai": "চেন্নাই", "hyderabad": "হায়দৰাবাদ", "ahmedabad": "আহমেদাবাদ",
        "pune": "পুনে", "amritsar": "অমৃতসৰ", "bhubaneswar": "ভুৱনেশ্বৰ", "guwahati": "গুৱাহাটী",
        "delhi ncr": "দিল্লী এনচিআৰ", "maharashtra": "মহাৰাষ্ট্ৰ", "karnataka": "কৰ্ণাটক",
        "west bengal": "পশ্চিমবংগ", "tamil nadu": "তামিলনাডু", "telangana": "তেলেংগানা",
        "gujarat": "গুজৰাট", "punjab": "পঞ্জাৱ", "odisha": "ওড়িশা", "assam": "অসম"
    },
    "ur": {
        "delhi": "دہلی", "mumbai": "ممبئی", "navi mumbai": "نئی ممبئی", "bengaluru": "بنگلور",
        "kolkata": "کولکتہ", "chennai": "چنئی", "hyderabad": "حیدرآباد", "ahmedabad": "احمد آباد",
        "pune": "پونے", "amritsar": "امرتسر", "bhubaneswar": "بھونیشور", "guwahati": "گوہاٹی",
        "delhi ncr": "دہلی این سی آر", "maharashtra": "مہاراشٹر", "karnataka": "کرناٹک",
        "west bengal": "مغربی بنگال", "tamil nadu": "تمل ناڈو", "telangana": "تلنگانہ",
        "gujarat": "گجرات", "punjab": "پنجاب", "odisha": "اوڈیشہ", "assam": "آسام"
    }
}

print("Cities data defined for all 13 languages.")
