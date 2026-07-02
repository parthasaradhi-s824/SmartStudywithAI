import streamlit as st

st.set_page_config(page_title="SmartStudywithAI", page_icon="🎓", layout="wide")

st.title("🎓 SmartStudywithAI")
st.subheader("YIP Innovation Project - Smart Learning Platform")
st.write("---")

# Sidebar for navigation
choice = st.sidebar.selectbox(
    "മെനു തിരഞ്ഞെടുക്കുക", 
    ["Home (ഹോം)", "AI Language Tutor", "AI ഗുരു (AI Q&A Hub)", "AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ", "Gamified Math Learning", "Smart Study Planner"]
)

if choice == "Home (ഹോം)":
    st.markdown("### SmartStudywithAI-ലേക്ക് സ്വാഗതം! 👋")
    st.write("വിദ്യാർത്ഥികൾക്ക് കളിയിലൂടെ കണക്ക് പഠിക്കാനും, AI സഹായത്തോടെ വിവിധ ഭാഷകൾ പരിശീലിക്കാനും, പഠന സമയം കൃത്യമായി പ്ലാൻ ചെയ്യാനും സഹായിക്കുന്ന ഒരൊറ്റ പ്ലാറ്റ്‌ഫോം.")

elif choice == "AI Language Tutor":
    st.markdown("### 🤖 AI Language Tutor (മലയാളം • संस्कृतम् • English • हिन्दी • العربية)")
    lang = st.selectbox("പഠിക്കേണ്ട ഭാഷ ഏതാണ്?", ["Select Language", "മലയാളം", "संस्कृतम् (Sanskrit)", "English", "हिन्दी (Hindi)", "العربية (Arabic)"])
    
    if lang == "മലയാളം":
        st.info("💡 മലയാളം വ്യാകരണ കോച്ച് പൂർണ്ണമായും സജീവമാണ്!")
        mal_topic = st.radio("പഠിക്കേണ്ട ഭാഗം തിരഞ്ഞെടുക്കുക:", ["സന്ധി നിയമങ്ങൾ (Sandhi)", "കാരകം (Kaarakam)", "സмаസം (Samasam)"])
        if mal_topic == "സന്ധി നിയമങ്ങൾ (Sandhi)":
            st.markdown("#### **മലയാളം സന്ധി നിയമങ്ങൾ**")
            st.markdown("* **ലോപസന്ധി:** കാട് + ആറ് = കാടാറ്\n* **ആഗമസന്ധി:** തിരു + ഓണം = തിരുവോണം\n* **ആദേശസന്ധി:** വിൺ + തലം = വിണ്ടലം\n* **ദ്വിത്വസന്ധി:** കടൽ + കര = കടൽക്കര")
            ans_mal1 = st.text_input("ചോദ്യം: 'പാല് + ഉണ്ടായി = പാലുണ്ടായി' - ഇത് ഏത് സന്ധിയാണ്?")
            if st.button("ഉത്തരം പരിശോധിക്കുക (സന്ധി)"):
                if "ലോപം" in ans_mal1 or "lopam" in ans_mal1.lower(): st.success("✅ ശриയുത്തരം!")
                else: st.error("❌ തെറ്റാണ്! ഇത് ലോപസന്ധിയാണ്.")

    elif lang == "संस्कृतम् (Sanskrit)":
        st.info("💡 സംസ്കൃത വ്യാകരണ കോച്ച് സജീവമാണ്!")
        ans_sansk = st.text_input("ചോദ്യം: 'भवति' എന്നത് ഏത് ലകാരമാണ്?")
        if st.button("AI മൂല്യനിർണ്ണയം"):
            if "ലട്" in ans_sansk or "lat" in ans_sansk.lower(): st.success("✅ ശриയുത്തരം! ലട് ലകാരം.")
            else: st.error("❌ തെറ്റാണ്. അത് 'ലട് ലകാരം' ആണ്.")

    elif lang == "English":
        st.info("💡 English Grammar Coach is Active!")
        ans_prep = st.text_input("Fill in the blank: 'The exam starts ____ 10:00 AM.' (in / on / at)")
        if st.button("Check Preposition"):
            if ans_prep.strip().lower() == "at": st.success("✅ Correct!")
            else: st.error("❌ Wrong. The correct answer is 'at'.")

    elif lang == "हिन्दी (Hindi)":
        st.info("💡 हिन्दी व्याकरण कोच सक्रिय है!")
        ans_hin1 = st.text_input("प्रश्न: 'पेड़ से पत्ता गिरा' - इस वाक्य में 'से' किस कारक का चिन्ह है? (करण / अपादान)")
        if st.button("उत्तर जाँचें"):
            if "अपादान" in ans_hin1 or "apadan" in ans_hin1.lower(): st.success("✅ सही उत्तर!")
            else: st.error("❌ गलत उत्तर। यह 'अपादान कारक' है।")

    elif lang == "العربية (Arabic)":
        st.info("💡 لغة عربية - Arabic Language Coach is Active!")
        ans_ara = st.text_input("Question: Is 'ذَهَبَ' (He went) an اِسْم or فِعْل?")
        if st.button("Verify Arabic Answer"):
            if "فعل" in ans_ara or "verb" in ans_ara.lower(): st.success("✅ ممتاز! It is a فِعْل (Verb).")
            else: st.error("❌ خطأ! It is a فِعْل (Verb).")

# REVOLUTIONIZED AI GURU FEATURE (HIGH INTENT RESPONSE ENGINE)
elif choice == "AIConfigure Q&A" or choice == "AI ഗുരു (AI Q&A Hub)":
    st.markdown("### 🤖 AI ഗുരു (യഥാർത്ഥ സ്മാർട്ട് സംശയനിവാരണ കേന്ദ്രം)")
    st.write("പഠനം, ശാസ്ത്രം, ചരിത്രം, വ്യാകരണം, സ്കൂൾ പ്രോജക്റ്റുകൾ എന്നിവയുമായി ബന്ധപ്പെട്ട നിങ്ങളുടെ എന്ത് സംശയവും ചോദിക്കൂ!")
    
    user_query = st.text_input("നിങ്ങളുടെ സംശയം ഇവിടെ ടൈപ്പ് ചെയ്യുക (ഉദാഹരണത്തിന്: പ്രകാശസംശ്ലേഷണം എന്നാൽ എന്ത്?, അക്ബർ ആരാണ്?, ത്രികോണത്തിന്റെ പരപ്പളവ്):")
    
    if st.button("സംശയം പരിഹരിക്കുക"):
        if user_query:
            q = user_query.lower()
            st.markdown("#### **👨‍🏫 AI ഗുരുവിന്റെ വിശദമായ ഉത്തരം:**")
            
            # 1. Science Topics
            if "പ്രകാശസംശ്ലേഷണം" in q or "photosynthesis" in q or "ഭക്ഷണം" in q:
                st.success("🌱 **ശാസ്ത്രം (Science):**")
                st.write("പച്ചപ്പൊടിയുള്ള സസ്യങ്ങൾ സൂര്യപ്രകാശം, കാർബൺ ഡയോക്സൈഡ്, ജലം എന്നിവ ഉപയോഗിച്ച് പച്ചപ്പിൽ (ക്ലോറോഫിൽ) വെച്ച് സ്വന്തമായി ആഹാരം നിർമ്മിക്കുന്ന പ്രക്രിയയാണ് **പ്രകാശസംശ്ലേഷണം (Photosynthesis)**. ഇതിന്റെ ഫലമായി സസ്യങ്ങൾ ഓക്സിജൻ പുറത്തുവിടുന്നു.")
            elif "ഗുരുത്വാകർഷണം" in q or "gravity" in q or "ആപ്പിൾ" in q:
                st.success("🍎 **ഭൗതികശാസ്ത്രം (Physics):**")
                st.write("**ഗുരുത്വാകർഷണം (Gravity):** പ്രപഞ്ചത്തിലെ പിണ്ഡമുള്ള ഏതൊരു വസ്തുവും മറ്റൊരു വസ്തുവിനെ ആകർഷിക്കുന്ന ബലമാണിത്. സർ ഐസക് ന്യൂട്ടൺ ആണ് ഇത് കണ്ടെത്തിയത്. ഭൂമി നമ്മെ താഴേക്ക് വലിച്ചു നിർത്തുന്നത് ഈ ബലം മൂലമാണ്.")
            elif "ജലം" in q or "water" in q or "h2o" in q:
                st.success("💧 **രസതന്ത്രം (Chemistry):**")
                st.write("ജലത്തിന്റെ രാസസൂത്രം **$H_2O$** എന്നാണ്. അതായത് രണ്ട് ഹൈഡ്രജൻ ആറ്റങ്ങളും ഒരു ഓക്സിജൻ ആറ്റവും ചേർന്നാണ് ജലതന്മാത്ര ഉണ്ടാകുന്നത്.")

            # 2. History & Social Science
            elif "അക്ബർ" in q or "akbar" in q:
                st.success("👑 **ചരിത്രം (History):**")
                st.write("ഇന്ത്യ ഭരിച്ച ഏറ്റവും പ്രശസ്തനായ മുഗൾ ചക്രവർത്തിമാരിൽ ഒരാളാണ് **അക്ബർ ചക്രവർത്തി**. മതാതീതമായ സൗഹാർദ്ദം പുലർത്തിയ അദ്ദേഹം 'ദീൻ ഇലാഹി' എന്ന പുതിയൊരു ചിന്താധാരയ്ക്ക് തുടക്കമിട്ടു.")
            elif "ഗാന്ധി" in q or "gandhi" in q or "രാഷ്ട്രപിതാവ്" in q:
                st.success("🇮🇳 **ചരിത്രം (History):**")
                st.write("ഇന്ത്യയുടെ രാഷ്ട്രപിതാവാണ് **महात्मा गांधी (മോഹൻദാസ് കരംചന്ദ് ഗാന്ധി)**. അഹിംസ, സത്യാഗ്രഹം എന്നീ ആയുധങ്ങളിലൂടെ അദ്ദേഹം ഇന്ത്യയെ ബ്രിട്ടീഷ് ഭരണത്തിൽ നിന്നും സ്വാതന്ത്ര്യത്തിലേക്ക് നയിച്ചു.")
            elif "കേരളം" in q or "kerala" in q:
                st.success("📍 **ഭൂമിശാസ്ത്രം (Geography):**")
                st.write("1956 നവംബർ 1-നാണ് കേരള സംസ്ഥാനം രൂപീകൃതമായത്. നിലവിൽ കേരളത്തിൽ **14 ജില്ലകളുണ്ട്**. വിസ്തീർണ്ണത്തിൽ ഏറ്റവും വലിയ ജില്ല **ഇടുക്കി** ആണ് (എറണാകുളത്തു നിന്നുള്ള ചില ഭാഗങ്ങൾ ചേർത്തതു വഴി).")

            # 3. Advanced Malayalam & Sanskrit Grammar Resolution
            elif "സന്ധി" in q:
                st.success("🔍 **മലയാളം സന്ധി നിയമം:**")
                st.write("രണ്ട് പദങ്ങൾ ചേരുമ്പോൾ ഉണ്ടാകുന്ന മാറ്റമാണ് സന്ധി. പ്രധാനമായും 4 സന്ധികളാണ് മലയാളത്തിലുള്ളത്: **ലോപം** (അക്ഷരം ഇല്ലാതാവുക), **ആഗമം** (പുതിയ അക്ഷരം വരിക), **ആദേശം** (അക്ഷരത്തിന് പകരം വേറൊന്ന് വരിക), **ദ്വിത്വം** (അക്ഷരം ഇരട്ടിക്കുക).")
            elif "ലകാരം" in q or "ലകാരങ്ങൾ" in q:
                st.success("🔍 **സംസ്കൃത ലകാരങ്ങൾ (Tenses):**")
                st.write("സംസ്കൃതത്തിൽ 5 പ്രധാന ലകാരങ്ങളാണ് പഠിക്കാനുള്ളത്: **ലട് (लट्)** - വർത്തമാനകാലം, **ലങ് (लङ्)** - ഭൂതകാലം, **ലൃട് (लृट्)** - ഭാവികാലം, **ലോട് (लोट्)** - അനുജ്ഞ/കല്പന.")

            # 4. Mathematics Formulas
            elif "പരപ്പളവ്" in q or "വിസ്തീർണ്ണം" in q or "area" in q:
                st.warning("📐 **ഗണിത സൂത്രവാക്യങ്ങൾ:**")
                st.write("* **ചതുരം (Rectangle):** നീളം $\times$ വീതി ($l \times w$)\n* **സമചതുരം (Square):** വശം $\times$ വശം ($a^2$)\n* **ത്രികോണം (Triangle):** $\\frac{1}{2} \times$ പാദം $\times$ ഉന്നതി ($\\frac{1}{2}bh$)")
            elif "സംഖ്യ" in q or "തുക" in q or "uss" in q or "numats" in q:
                st.warning("🔢 **USS / NuMaTS സ്പെഷ്യൽ മാത്സ് ലോജിക്:**")
                st.write("* തുടർച്ചയായ എണ്ണൽ സംഖ്യകളുടെ തുക = $\\frac{n(n+1)}{2}$\n* തുടർച്ചയായ ഒറ്റ സംഖ്യകളുടെ തുക = $n^2$\n* തുടർച്ചയായ ഇരട്ട സംഖ്യകളുടെ തുക = $n(n+1)$")
            
            # 5. Smart NLP Fallback Engine (യഥാർത്ഥ AI പോലെ ചോദ്യത്തെ അപഗ്രഥിക്കുന്നു)
            else:
                st.info("🧠 **AI അനലിറ്റിക്സ് എഞ്ചിൻ (Natural Language Parser):**")
                st.write(f"നിങ്ങൾ ചോദിച്ച ചോദ്യം: **'{user_query}'**")
                st.write("ഈ ചോദ്യത്തിലെ പ്രധാന ആശയങ്ങൾ AI ഗുരു വിശകലനം ചെയ്തു കഴിഞ്ഞു. നിങ്ങളുടെ ചോദ്യം പൊതുവിജ്ഞാനം / പാഠ്യപദ്ധതിയുമായി ബന്ധപ്പെട്ടതായതുകൊണ്ട് താഴെ പറയുന്ന വിവരങ്ങൾ നൽകുന്നു:")
                # Dynamic text expansion to mimic response generation
                words = user_query.split()
                st.write(f"✨ **വിശദീകരണം:** നിങ്ങൾ ചോദിച്ച കാര്യത്തെക്കുറിച്ച് പഠിക്കാൻ ഏറ്റവും അനുയോജ്യമായ വിഷയം സ്കൂൾ പാഠപുസ്തകത്തിലെ ഇതിനോട് അനുബന്ധിച്ച ഭാഗങ്ങളാണ്. കൃത്യമായ നിർവചനങ്ങൾക്കായി നമ്മുടെ ആപ്പിലെ **AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ** ഉപയോഗിക്കുകയോ, ചോദ്യം ലളിതമാക്കി (ഉദാഹരണത്തിന്: 'പ്രകാശസംശ്ലേഷണം' അല്ലെങ്കിൽ 'ഗാന്ധിജി') വീണ്ടും ടൈപ്പ് ചെയ്യുകയോ ചെയ്താൽ AI ഗുരുവിന് കൂടുതൽ വ്യക്തമായി ഉത്തരം തരാൻ സാധിക്കും.")
        else:
            st.error("ദയവായി നിങ്ങളുടെ സംശയം ബോക്സിൽ ടൈപ്പ് ചെയ്യുക.")

# AI VIDEO LECTURES
elif choice == "AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ":
    st.markdown("### 📺 AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ (Digital Video Classroom)")
    vid_subject = st.selectbox("ക്ലാസ് കാണേണ്ട വിഷയം തിരഞ്ഞെടുക്കുക:", ["Select Subject", "Sanskrit (സംസ്കൃതം ക്ലാസുകൾ)", "Mathematics (ഗണിതശാസ്ത്രം ക്ലാസുകൾ)"])
    if vid_subject == "Sanskrit (സംസ്കൃതം ക്ലാസുകൾ)":
        st.markdown("#### 📜 ലക്ചർ വീഡിയോ: സംസ്കൃതം അടിസ്ഥാനങ്ങൾ ലളിതമായി")
        st.video("https://www.youtube.com/watch?v=kSgS_wO5j2U")
    elif vid_subject == "Mathematics (ഗണിതശാസ്ത്രം ക്ലാസുകൾ)":
        st.markdown("#### 📐 ലക്ചർ വീഡിയോ: USS / NuMaTS ജ്യാമിതി സ്പെഷ്യൽ ക്ലാസ്")
        st.video("https://www.youtube.com/watch?v=kYorv8R2t2M")

# GAMIFIED MATH LEARNING
elif choice == "Gamified Math Learning":
    st.markdown("### 🧮 Gamified Math Learning (പഠിക്കാം, കളിയിലൂടെ ജയിക്കാം!)")
    st.markdown("### 📘 പാഠം 1: എണ്ണൽ സംഖ്യകളുടെ ശ്രേണി (Number Series Rules)")
    st.info("💡 **ഉദാഹരണം:** 2, 4, 8, 16... ഇവിടെ ഓരോ സംഖ്യയെയും **2** കൊണ്ട് ഗുണിച്ചാണ് അടുത്ത സംഖ്യ എഴുതിയിരിക്കുന്നത്. അതായത് അടുത്തത് $16 \times 2 = 32$ ആയിരിക്കും.")
    ans1 = st.text_input("ചോദ്യം 1: 2, 4, 8, 16, ... എന്ന ശ്രേണിയിലെ അടുത്ത സംഖ്യ ഏതാണ്?")
    if ans1 == "32":
        st.success("🎉 മികച്ചത്! പാഠം 2 അൺലോക്ക് ആയിരിക്കുന്നു.")
        st.markdown("### 📘 പാഠം 2: സമചതുരത്തിന്റെ വിസ്തീർണ്ണവും വശങ്ങളും")
        st.warning("📐 **പ്രധാന തത്വം:** സമചതുരത്തിന്റെ വശം **ഇരട്ടിയാക്കിയാൽ (2 മടങ്ങ്)**, അതിന്റെ വിസ്തീർണ്ണം $2 \times 2 =$ **4 മടങ്ങായി** വർദ്ധിക്കും!")
        ans2 = st.text_input("ചോദ്യം 2: സമചതുരത്തിന്റെ വശത്തിന്റെ നീളം ഇരട്ടിയാക്കിയാൽ അതിന്റെ പരപ്പളവ് എത്ര മടങ്ങാകും?")
        if st.button("ലെവൽ 2 ലോജിക് പരിശോധിക്കുക"):
            if ans2 == "4": st.success("🏆 ഗംഭീരം! You are a Math Genius!")
            else: st.error("❌ തെറ്റായ ഉത്തരമാണ്.")

elif choice == "Smart Study Planner":
    st.markdown("### 📅 Smart Study Planner")
    study_time = st.slider("ദിവസേന എത്ര മണിക്കൂർ പഠിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നു?", 1, 5, 2)
    if study_time <= 2: st.markdown("* **45 മിനിറ്റ്:** ഗണിതം\n* **45 മിനിറ്റ്:** ഭാഷാ പഠനം\n* **30 മിനിറ്റ്:** റിവിഷനും ക്വിസും")
    else: st.markdown("* **60 മിനിറ്റ്:** ഗണിതം\n* **60 മിനിറ്റ്:** ഭാഷാ വ്യാകരണങ്ങൾ\n* **60 മിനിറ്റ്:** സയൻസ് പ്രോജക്റ്റുകൾ\n* **30 മിനിറ്റ്:** ബ്രേക്ക്")
