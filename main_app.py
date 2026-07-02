import streamlit as st

st.set_page_config(page_title="SmartStudywithAI", page_icon="🎓", layout="wide")

st.title("🎓 SmartStudywithAI")
st.subheader("YIP Innovation Project - AI Tutor, Math Quest & Smart Planner")
st.write("---")

# Sidebar for navigation
choice = st.sidebar.selectbox(
    "മെനു തിരഞ്ഞെടുക്കുക", 
    ["Home (ഹോം)", "AI Language Tutor", "AI ഗുരു (AI Q&A)", "AI ലക്ചർ ക്ലാസുകൾ", "Gamified Math Learning", "Smart Study Planner"]
)

if choice == "Home (ഹോം)":
    st.markdown("### SmartStudywithAI-ലേക്ക് സ്വാഗതം! 👋")
    st.write("വിദ്യാർത്ഥികൾക്ക് കളിയിലൂടെ കണക്ക് പഠിക്കാനും, AI സഹായത്തോടെ വിവിധ ഭാഷകൾ പരിശീലിക്കാനും, പഠന സമയം കൃത്യമായി പ്ലാൻ ചെയ്യാനും സഹായിക്കുന്ന ഒരൊറ്റ പ്ലാറ്റ്‌ഫോം.")

elif choice == "AI Language Tutor":
    st.markdown("### 🤖 AI Language Tutor (മലയാളം • संस्कृतम् • English • हिन्दी • العربية)")
    st.write("വ്യാകരണ നിയമങ്ങളും ക്വിസുകളും ലളിതമായി പഠിക്കാം. താഴെ നിങ്ങളുടെ ഭാഷ തിരഞ്ഞെടുക്കൂ:")
    
    lang = st.selectbox("പഠിക്കേണ്ട ഭാഷ ഏതാണ്?", ["Select Language", "മലയാളം", "संस्कृतम् (Sanskrit)", "English", "हिन्दी (Hindi)", "العربية (Arabic)"])
    
    # MALAYALAM SECTION
    if lang == "മലയാളം":
        st.info("💡 മലയാളം വ്യാകരണ കോച്ച് പൂർണ്ണമായും സജീവമാണ്!")
        mal_topic = st.radio("പഠിക്കേണ്ട ഭാഗം തിരഞ്ഞെടുക്കുക:", ["സന്ധി നിയമങ്ങൾ (Sandhi)", "കാരകം (Kaarakam)", "സമാസം (Samasam)"])
        
        if mal_topic == "സന്ധി നിയമങ്ങൾ (Sandhi)":
            st.markdown("#### **മലയാളം സന്ധി നിയമങ്ങൾ**")
            st.markdown("* **ലോപസന്ധി:** ഒരു അക്ഷരം ഇല്ലാതായി മാറുന്നു. (ഉദാ: കാട് + ആറ് = കാടാറ്)")
            st.markdown("* **ആഗമസന്ധി:** പുതുതായി ഒരു അക്ഷരം വരുന്നു. (ഉദാ: തിരു + ഓണം = തിരുവോണം)")
            st.markdown("* **ആദേശസന്ധി:** ഒരു അക്ഷരത്തിന് പകരം വേറൊരു അക്ഷരം വരുന്നു. (ഉദാ: വിൺ + തലം = വിണ്ടലം)")
            st.markdown("* **দ্বിത്വസന്ധി (ദ്വിത്വം):** അക്ഷരം ഇരട്ടിക്കുന്നു. (ഉദാ: കടൽ + കര = കടൽക്കര)")
            
            ans_mal1 = st.text_input("ചോദ്യം: 'പാല് + ഉണ്ടായി = പാലുണ്ടായി' - ഇത് ഏത് സന്ധിയാണ്?")
            if st.button("ഉത്തരം പരിശോധിക്കുക (സന്ധി)"):
                if "ലോപം" in ans_mal1 or "lopam" in ans_mal1.lower():
                    st.success("✅ ശриയുത്തരം! പാല് (ഉ) എന്ന സ്വരം ഇല്ലാതായതിനാൽ ഇത് ലോപസന്ധിയാണ്.")
                else:
                    st.error("❌ തെറ്റാണ്! 'ഉ' എന്ന അക്ഷരം ലോപിച്ചു പോയതിനാൽ ഇത് ലോപസന്ധിയാണ്.")

        elif mal_topic == "കാരകം (Kaarakam)":
            st.markdown("#### **കാരകം**")
            st.markdown("* **കർത്താവ്:** ക്രിയ ചെയ്യുന്നത് ആര്? (ഉദാ: രാമൻ കാട്ടിൽ പോയി)")
            st.markdown("* **കർമ്മം:** ക്രിയയുടെ ഫലം അനുഭവിക്കുന്നത് എന്ത്/ആരെ? (ഉദാ: ലക്ഷ്മണൻ പഴം തിന്നു)")
            
            ans_mal2 = st.text_input("ചോദ്യം: 'അമ്മ കുട്ടിയെ വിളിച്ചു' - ഈ വാക്യത്തിലെ 'കുട്ടിയെ' എന്നത് കർത്താവാണോ കർമ്മമാണോ?")
            if st.button("ഉത്തരം പരിശോധിക്കുക (കാരകം)"):
                if "കർമ്മ" in ans_mal2 or "karmam" in ans_mal2.lower():
                    st.success("✅ ശരിയുത്തരം! 'കുട്ടിയെ' എന്നത് കർമ്മമാണ് (ദ്വിതീയാ വിഭക്തി).")
                else:
                    st.error("❌ തെറ്റാണ്. അമ്മയാണ് ഇവിടെ പ്രവർത്തി ചെയ്യുന്നത് (കർത്താവ്), കുട്ടി ഇവിടെ 'കർമ്മം' ആണ്.")

        elif mal_topic == "സമാസം (Samasam)":
            st.markdown("#### **സമാസം**")
            st.markdown("* **തത്പുരുഷൻ:** ഉത്തരപദത്തിന് പ്രാധാന്യമുള്ളത്. (ഉദാ: മരപ്പൊത്ത് = മരത്തിന്റെ പൊത്ത്)")
            st.markdown("* **ദ്വന്ദ്വൻ:** രണ്ട് പദങ്ങൾക്കും തുല്യ പ്രാധാന്യമുള്ളത്. (ഉദാ: രാമലക്ഷ്മണന്മാർ = രാമനും ലക്ഷ്മണനും)")
            
            ans_mal3 = st.text_input("ചോദ്യം: 'കൈകാലുകൾ' എന്നത് ഏത് സമാസത്തിന് ഉദാഹരണമാണ്?")
            if st.button("ഉത്തരം പരിശോധിക്കുക (സമാസം)"):
                if "ദ്വന്ദ്വ" in ans_mal3 or "dwandwa" in ans_mal3.lower():
                    st.success("✅ മികച്ചത്! കൈയും കാലും എന്ന് രണ്ട് പദങ്ങൾക്കും പ്രാധാന്യമുള്ളതിനാൽ ഇത് ദ്വന്ദ്വസമാസമാണ്.")
                else:
                    st.error("❌ തെറ്റായ ഉത്തരമാണ്. കൈയും കാലും തുല്യ പ്രാധാന്യമുള്ളതിനാൽ ഇത് 'ദ്വന്ദ്വസമാസം' ആണ്.")

    # SANSKRIT SECTION
    elif lang == "संस्कृतम् (Sanskrit)":
        st.info("💡 സംസ്കൃത വ്യാകരണ കോച്ച് സജീവമാണ്!")
        topic = st.radio("പഠിക്കേണ്ട ഭാഗം തിരഞ്ഞെടുക്കുക:", ["ലകാരങ്ങൾ (Lakarah)", "Sanskrita Sandhi"])
        if topic == "ലകാരങ്ങൾ (Lakarah)":
            st.markdown("* **ലട് ലകാരഃ (लट् लकार):** Present Tense (പഠതി - വായിക്കുന്നു)")
            st.markdown("* **ലങ് ലകാരഃ (लङ् लकार):** Past Tense (അപഠത് - വായിച്ചു)")
            ans_sansk = st.text_input("ചോദ്യം: 'भवति' എന്നത് ഏത് ലകാരമാണ്?")
            if st.button("AI മൂല്യനിർണ്ണയം"):
                if "ലട്" in ans_sansk or "lat" in ans_sansk.lower():
                    st.success("✅ ശരിയുത്തരം! ലട് ലകാരം.")
                else:
                    st.error("❌ തെറ്റാണ്. അത് 'ലട് ലകാരം' ആണ്.")

    # ENGLISH SECTION
    elif lang == "English":
        st.info("💡 English Grammar Coach is Active!")
        eng_topic = st.radio("Choose a Topic:", ["Tenses (Active/Passive)", "Prepositions"])
        if eng_topic == "Tenses (Active/Passive)":
            st.markdown("* *Active:* She has written a letter.\n* *Passive:* A letter has been written by her.")
            ans_eng = st.text_input("Change into Passive Voice: 'He killed a snake.'")
            if st.button("Evaluate English Answer"):
                if "a snake was killed by him" in ans_eng.strip().lower().replace(".", ""):
                    st.success("✅ Perfect! Your answer is absolutely correct!")
                else:
                    st.error("❌ Incorrect. The correct Passive Voice is: 'A snake was killed by him.'")
        elif eng_topic == "Prepositions":
            ans_prep = st.text_input("Fill in the blank: 'The exam starts ____ 10:00 AM.' (in / on / at)")
            if st.button("Check Preposition"):
                if ans_prep.strip().lower() == "at":
                    st.success("✅ Correct! We use 'at' before specific time expressions.")
                else:
                    st.error("❌ Wrong. The correct answer is 'at'.")

    # HINDI SECTION
    elif lang == "हिन्दी (Hindi)":
        st.info("💡 हिन्दी व्याकरण कोच सक्रिय है!")
        st.markdown("* **कर्ता कारक:** इसका चिन्ह **'ने'** है।\n* **कर्म कारक:** इसका चिन्ह **'को'** है।")
        ans_hin1 = st.text_input("प्रश्न: 'पेड़ से पत्ता गिरा' - इस वाक्य में 'से' किस कारक का चिन्ह है? (करण / अपादान)")
        if st.button("उत्तर जाँचें"):
            if "अपादान" in ans_hin1 or "apadan" in ans_hin1.lower():
                st.success("✅ सही उत्तर! यह 'अपादान कारक' है।")
            else:
                st.error("❌ गलत उत्तर। यह 'अपादान कारक' है।")

    # ARABIC SECTION
    elif lang == "العربية (Arabic)":
        st.info("💡 لغة عربية - Arabic Language Coach is Active!")
        st.markdown("* **اِسْم (Noun):** كِتَاب (Book)\n* **فِعْل (Verb):** كَتَبَ (He wrote)\n* **حَرْف (Particle):** فِي (In)")
        ans_ara = st.text_input("Question: Is 'ذَهَبَ' (He went) an اِسْم or فِعْل?")
        if st.button("Verify Arabic Answer"):
            if "فعل" in ans_ara or "verb" in ans_ara.lower():
                st.success("✅ ممتاز! It is a فِعْل (Verb).")
            else:
                st.error("❌ خطأ! It is a فِعْل (Verb).")

# NEW FEATURE 1: AI GURU (Q&A)
elif choice == "AI guru (AI Q&A)":
    st.markdown("### 🤖 AI ഗുരു (AI Smart Q&A Hub)")
    st.write("പഠനസംബന്ധമായ നിങ്ങളുടെ ഏത് സംശയങ്ങളും ഇവിടെ ടൈപ്പ് ചെയ്ത് ചോദിക്കാം. AI ഗുരു ഉടനടി മറുപടി നൽകുന്നതാണ്!")
    
    user_query = st.text_input("നിങ്ങളുടെ ചോദ്യം ഇവിടെ ടൈപ്പ് ചെയ്യുക (ഉദാഹരണത്തിന്: സവർണ്ണദീർഘസന്ധി, ഓർമ്മശക്തി കൂട്ടാൻ വഴി, USS മാത്സ്):")
    
    if st.button("ചോദിക്കുക (Ask Guru)"):
        if user_query:
            query_lower = user_query.lower()
            st.markdown("#### **🤖 AI ഗുരുവിന്റെ മറുപടി:**")
            
            if "സന്ധി" in query_lower or "sandhi" in query_lower:
                st.success("💡 **സന്ധി സംശയം:** മലയാളത്തിലും സംസ്കൃതത്തിലും ഒരേ സ്വരങ്ങൾ (അ, ഇ, ഉ, ഋ) ചേർന്ന് ദീർഘമായി മാറുന്നതിനെ 'സവർണ്ണദീർഘസന്ധി' എന്ന് വിളിക്കുന്നു. ഉദാഹരണത്തിന്: വിദ്യ + അർത്ഥി = വിദ്യാർത്ഥി, രവി + ഇന്ദ്രൻ = രവീന്ദ്രൻ.")
            elif "ഓർമ്മ" in query_lower or "study tips" in query_lower or "പഠിക്കാൻ" in query_lower:
                st.info("🧠 **പഠന ടിപ്പ്:** കാര്യങ്ങൾ മറന്നുപോകാതിരിക്കാൻ 'Active Recall' (വായിച്ച ശേഷം പുസ്തകം അടച്ചുവെച്ച് ഓർത്തുനോക്കൽ), 'Spaced Repetition' (തുടർച്ചയായ ദിവസങ്ങളിൽ റിവിഷൻ ചെയ്യൽ) എന്നീ വഴികൾ ഉപയോഗിക്കുക. കൂടാതെ പഠനത്തിനിടയിൽ ചെറിയ ബ്രേക്കുകൾ എടുക്കുക!")
            elif "കണക്ക്" in query_lower or "math" in query_lower or "uss" in query_lower or "numats" in query_lower:
                st.warning("🔢 **ഗണിത സൂത്രവാക്യം:** USS/NuMaTS പരീക്ഷകൾക്ക് തുടർച്ചയായ എണ്ണൽ സംഖ്യകളുടെ തുക കാണാൻ $n(n+1)/2$ എന്ന സമവാക്യം ഉപയോഗിക്കാം. (ഉദാഹരണത്തിന് 1 മുതൽ 10 വരെയുള്ള സംഖ്യകളുടെ തുക = $10 \times 11 / 2 = 55$).")
            else:
                st.write("✨ **പൊതു നിർദ്ദേശം:** മികച്ച ചോദ്യം! നിങ്ങളുടെ ഈ സംശയത്തെക്കുറിച്ച് കൂടുതൽ മനസ്സിലാക്കാൻ പാഠപുസ്തകത്തിലെ അനുബന്ധ ഭാഗങ്ങൾ റെഫർ ചെയ്യുകയോ, നിങ്ങളുടെ മെന്ററോട് കൂടുതൽ ചർച്ച ചെയ്യുകയോ ചെയ്യാവുന്നതാണ്. നിരന്തരം പരിശീലിക്കുക!")
        else:
            st.error("ദയവായി ഒരു ചോദ്യം ടൈപ്പ് ചെയ്ത ശേഷം ബട്ടൺ ക്ലിക്ക് ചെയ്യുക.")

# NEW FEATURE 2: AI LECTURE CLASS
elif choice == "AI ലക്ചർ ക്ലാസുകൾ":
    st.markdown("### 🎙️ AI ലക്ചർ ക്ലാസുകൾ (Smart Digital Lecture Room)")
    st.write("ക്ലാസ് മുറിയിലെ അധ്യാപകനെപ്പോലെ പ്രധാനപ്പെട്ട പാഠഭാഗങ്ങൾ ലളിതമായി ഡിജിറ്റൽ നോട്സിലൂടെയും വിശദീകരണങ്ങളിലൂടെയും AI ഇവിടെ പഠിപ്പിക്കുന്നു.")
    
    subject_select = st.selectbox("പഠിക്കേണ്ട വിഷയം തിരഞ്ഞെടുക്കുക:", ["Select Subject", "Sanskrit (സംസ്കൃതം പാഠശാല)", "Mathematics (സ്മാർട്ട് മാത്സ് ക്ലാസ്)"])
    
    if subject_select == "Sanskrit (സംസ്കൃതം പാഠശാല)":
        st.markdown("### 📜 ലക്ചർ 1: സംസ്കൃതത്തിലെ സുഭാഷിതങ്ങളും ആശയങ്ങളും")
        st.info("👨‍🏫 **AI പ്രൊഫസർ പറയുന്നു:** കുട്ടികളേ, സുഭാഷിതങ്ങൾ എന്നാൽ നല്ല വാക്കുകൾ എന്നാണ് അർത്ഥം. ജീവിതമൂല്യങ്ങൾ പഠിക്കാൻ ഇവ സഹായിക്കുന്നു.")
        st.markdown("> **“വിദ്യാധനം സർവ്വധനാൽ പ്രധാനം”**\n>\n> * **അർത്ഥം:** വിദ്യയാകുന്ന ധനം മറ്റ് എല്ലാ ധനത്തെക്കാളും ഏറ്റവും ശ്രേഷ്ഠമായതാണ്. കള്ളന്മാർക്ക് ഇത് മോഷ്ടിക്കാൻ കഴിയില്ല, കൊടുക്കുംതോറും ഏറിടും!")
        st.write("💡 *ലക്ചർ ടിപ്പ്:* ഈ ശ്ലോകം പരീക്ഷയ്ക്ക് ആശയവിശദീകരണത്തിന് സാധാരണയായി ചോദിക്കാറുള്ളതാണ്. നോട്ട്ബുക്കിലേക്ക് കുറിച്ചുവെക്കുക.")
        
    elif subject_select == "Mathematics (സ്മാർട്ട് മാത്സ് ക്ലാസ്)":
        st.markdown("### 📐 ലക്ചർ 1: കോണുകളും ജ്യാമിതിയും (Geometry Special)")
        st.info("👨‍🏫 **AI പ്രൊഫസർ പറയുന്നു:** ഇന്ന് നമ്മൾ ജ്യാമിതിയിലെ ഒരു പ്രധാന നിയമമാണ് പഠിക്കുന്നത്. ത്രികോണങ്ങളെക്കുറിച്ചാണത്.")
        st.markdown("* **പ്രധാന നിയമം:** ഒരു ത്രികോണത്തിലെ മൂന്ന് കോണുകളുടെയും തുക എപ്പോഴും **180°** ആയിരിക്കും.")
        st.markdown("* **USS മാതൃക ചോദ്യം:** ഒരു ത്രികോണത്തിലെ രണ്ട് കോണുകൾ 50°, 60° ആയാൽ മൂന്നാമത്തെ കോൺ എത്ര?")
        
        if st.checkbox("ഉത്തരം കാണുക"):
            st.success("💡 **ഉത്തരം:** മൂന്നാമത്തെ കോൺ = 180° - (50° + 60°) = 180° - 110° = **70°**.")

elif choice == "Gamified Math Learning":
    st.markdown("### 🧮 Math Quest (കണക്ക് കളിയിലൂടെ പഠിക്കാം)")
    ans1 = st.text_input("ചോദ്യം 1: 2, 4, 8, 16, ... അടുത്ത സംഖ്യ ഏത്?")
    if ans1 == "32":
        st.success("✅ ശരിയുത്തരം!")
        ans2 = st.text_input("ചോദ്യം 2: ഒരു സമചതുരത്തിന്റെ വശം ഇരട്ടിയാക്കിയാൽ പരപ്പളവ് എത്ര മടങ്ങാകും?")
        if st.button("ലെവൽ 2 പരിശോധിക്കുക"):
            if ans2 == "4":
                st.success("🎉 ഗംഭീരം! ശരിയുത്തരം.")
            else:
                st.error("❌ തെറ്റായ ഉത്തരമാണ്.")

elif choice == "Smart Study Planner":
    st.markdown("### 📅 Smart Study Planner")
    study_time = st.slider("ദിവസേന എത്ര മണിക്കൂർ പഠിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നു?", 1, 5, 2)
    if study_time <= 2:
        st.markdown("* **45 മിനിറ്റ്:** ഗണിതം\n* **45 മിനിറ്റ്:** ഭാഷാ പഠനം\n* **30 മിനിറ്റ്:** റിവിഷനും ക്വിസും")
    else:
        st.markdown("* **60 മിനിറ്റ്:** ഗണിതം\n* **60 മിനിറ്റ്:** ഭാഷാ വ്യാകരണങ്ങൾ\n* **60 മിനിറ്റ്:** സയൻസ് പ്രോജക്റ്റുകൾ\n* **30 മിനിറ്റ്:** ബ്രേക്ക്")
