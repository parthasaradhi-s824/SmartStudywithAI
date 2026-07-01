import streamlit as st

st.set_page_config(page_title="SmartStudywithAI", page_icon="🎓", layout="wide")

st.title("🎓 SmartStudywithAI")
st.subheader("YIP Innovation Project - AI Tutor, Math Quest & Smart Planner")
st.write("---")

# Sidebar for navigation
choice = st.sidebar.selectbox("മെനു തിരഞ്ഞെടുക്കുക", ["Home (ഹോം)", "AI Language Tutor", "Gamified Math Learning", "Smart Study Planner"])

if choice == "Home (ഹോം)":
    st.markdown("### SmartStudywithAI-ലേക്ക് സ്വാഗതം! 👋")
    st.write("വിദ്യാർത്ഥികൾക്ക് കളിയിലൂടെ കണക്ക് പഠിക്കാനും, AI സഹായത്തോടെ വിവിധ ഭാഷകൾ പരിശീലിക്കാനും, പഠന സമയം കൃത്യമായി പ്ലാൻ ചെയ്യാനും സഹായിക്കുന്ന ഒരൊറ്റ പ്ലാറ്റ്‌ഫോം.")

elif choice == "AI Language Tutor":
    st.markdown("### 🤖 AI Language Tutor (മലയാളം • संस्कृतम् • English • हिन्दी • العربية)")
    st.write("വ്യാകരണ നിയമങ്ങളും ക്വിസുകളും ലളിതമായി പഠിക്കാം. താഴെ നിങ്ങളുടെ ഭാഷ തിരഞ്ഞെടുക്കൂ:")
    
    lang = st.selectbox("പഠിക്കേണ്ട ഭാഷ ഏതാണ്?", ["Select Language", "മലയാളം", "संस्कृतम् (Sanskrit)", "English", "हिन्दी (Hindi)", "العربية (Arabic)"])
    
    # 1. MALAYALAM SECTION (Detailed)
    if lang == "മലയാളം":
        st.info("💡 മലയാളം വ്യാകരണ കോച്ച് പൂർണ്ണമായും സജീവമാണ്!")
        mal_topic = st.radio("പഠിക്കേണ്ട ഭാഗം തിരഞ്ഞെടുക്കുക:", ["സന്ധി നിയമങ്ങൾ (Sandhi)", "കാരകം (Kaarakam)", "സമാസം (Samasam)"])
        
        if mal_topic == "സന്ധി നിയമങ്ങൾ (Sandhi)":
            st.markdown("#### **മലയാളം സന്ധി നിയമങ്ങൾ**")
            st.write("രണ്ടു വാക്കുകൾ കൂടിച്ചേരുമ്പോൾ അക്ഷരങ്ങൾക്ക് ഉണ്ടാകുന്ന മാറ്റങ്ങളാണ് സന്ധി.")
            st.markdown("* **ലോപസന്ധി:** ഒരു അക്ഷരം ഇല്ലാതായി മാറുന്നു. (ഉദാ: കാട് + ആറ് = കാടാറ് -> 'ഉ' ലോപിച്ചു)")
            st.markdown("* **ആഗമസന്ധി:** പുതുതായി ഒരു അക്ഷരം വരുന്നു. (ഉദാ: തിരു + ഓണം = തിരുവോണം -> 'വ്' ആഗമിച്ചു)")
            st.markdown("* **ആദേശസന്ധി:** ഒരു അക്ഷരത്തിന് പകരം വേറൊരു അക്ഷരം വരുന്നു. (ഉദാ: വിൺ + തലം = വിണ്ടലം -> 'ത്' മാറി 'ട്' വന്നു)")
            st.markdown("* **দ্বിത്വസന്ധി (ദ്വിത്വം):** അക്ഷരം ഇരട്ടിക്കുന്നു. (ഉദാ: കടൽ + കര = കടൽക്കര)")
            
            st.write("---")
            st.markdown("🎯 **AI Evaluation Quiz:**")
            ans_mal1 = st.text_input("ചോദ്യം: 'പാല് + ഉണ്ടായി = പാലുണ്ടായി' - ഇത് ഏത് സന്ധിയാണ്?")
            if st.button("ഉത്തരം പരിശോധിക്കുക (സന്ധി)"):
                if "ലോപം" in ans_mal1 or "lopam" in ans_mal1.lower():
                    st.success("✅ ശരിയുത്തരം! പാല് (ഉ) എന്ന സ്വരം ഇല്ലാതായതിനാൽ ഇത് ലോപസന്ധിയാണ്.")
                else:
                    st.error("❌ തെറ്റാണ്! 'ഉ' എന്ന അക്ഷരം ലോപിച്ചു പോയതിനാൽ ഇത് ലോപസന്ധിയാണ്.")

        elif mal_topic == "കാരകം (Kaarakam)":
            st.markdown("#### **കാരകം**")
            st.write("ക്രിയയുമായി നാമപദങ്ങൾക്കുള്ള ബന്ധമാണ് കാരകം. വിഭക്തികളുമായി ഇത് ബന്ധപ്പെട്ടിരിക്കുന്നു.")
            st.markdown("* **കർത്താവ് (Nominative):** ക്രിയ ചെയ്യുന്നത് ആര്? (ഉദാ: രാമൻ കാട്ടിൽ പോയി. ഇവിടെ 'രാമൻ' കർത്താവാണ്)")
            st.markdown("* **കർമ്മം (Accusative):** ക്രിയയുടെ ഫലം അനുഭവിക്കുന്നത് എന്ത്/ആരെ? (ഉദാ: ലക്ഷ്മണൻ പഴം തിന്നു. ഇവിടെ 'പഴം' കർമ്മമാണ്)")
            
            st.write("---")
            st.markdown("🎯 **AI Evaluation Quiz:**")
            ans_mal2 = st.text_input("ചോദ്യം: 'അമ്മ കുട്ടിയെ വിളിച്ചു' - ഈ വാക്യത്തിലെ 'കുട്ടിയെ' എന്നത് കർത്താവാണോ കർമ്മമാണോ?")
            if st.button("ഉത്തരം പരിശോധിക്കുക (കാരകം)"):
                if "കർമ്മ" in ans_mal2 or "karmam" in ans_mal2.lower():
                    st.success("✅ ശരിയുത്തരം! വിളിക്കുക എന്ന ക്രിയയുടെ ഫലം കുട്ടിക്കായതിനാൽ 'കുട്ടിയെ' എന്നത് കർമ്മമാണ് (ദ്വിതീയാ വിഭക്തി).")
                else:
                    st.error("❌ തെറ്റാണ്. അമ്മയാണ് ഇവിടെ പ്രവർത്തി ചെയ്യുന്നത് (കർത്താവ്), കുട്ടി ഇവിടെ 'കർമ്മം' ആണ്.")

        elif mal_topic == "സമാസം (Samasam)":
            st.markdown("#### **സമാസം**")
            st.write("പരസ്പരം ബന്ധമുള്ള രണ്ട് പദങ്ങൾ ചേർന്ന് ഒരൊറ്റ പദമായി മാറുന്നതാണ് സമാസം.")
            st.markdown("* **തത്പുരുഷൻ:** ഉത്തരപദത്തിന് (രണ്ടാമത്തെ വാക്കിന്) പ്രാധാന്യമുള്ളത്. (ഉദാ: മരപ്പൊത്ത് = മരത്തിന്റെ പൊത്ത്)")
            st.markdown("* **ദ്വന്ദ്വൻ:** രണ്ട് പദങ്ങൾക്കും തുല്യ പ്രാധാന്യമുള്ളത്. (ഉദാ: രാമലക്ഷ്മണന്മാർ = രാമനും ലക്ഷ്മണനും)")
            
            st.write("---")
            st.markdown("🎯 **AI Evaluation Quiz:**")
            ans_mal3 = st.text_input("ചോദ്യം: 'കൈകാലുകൾ' എന്നത് ഏത് സമാസത്തിന് ഉദാഹരണമാണ്?")
            if st.button("ഉത്തരം പരിശോധിക്കുക (സമാസം)"):
                if "ദ്വന്ദ്വ" in ans_mal3 or "dwandwa" in ans_mal3.lower():
                    st.success("✅ മികച്ചത്! കൈയും കാലും എന്ന് രണ്ട് പദങ്ങൾക്കും പ്രാധാന്യമുള്ളതിനാൽ ഇത് ദ്വന്ദ്വസമാസമാണ്.")
                else:
                    st.error("❌ തെറ്റായ ഉത്തരമാണ്. കൈയും കാലും തുല്യ പ്രാധാന്യമുള്ളതിനാൽ ഇത് 'ദ്വന്ദ്വസമാസം' ആണ്.")

    # 2. SANSKRIT SECTION
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

    # 3. ENGLISH SECTION (Foreign Language 1)
    elif lang == "English":
        st.info("💡 English Grammar Coach is Active!")
        eng_topic = st.radio("Choose a Topic:", ["Tenses (Active/Passive)", "Prepositions"])
        
        if eng_topic == "Tenses (Active/Passive)":
            st.markdown("#### **Tenses & Sentence Voice**")
            st.write("Let's look at the Present Perfect Tense structure: `Subject + has/have + V3 (Past Participle)`")
            st.markdown("* *Active:* She has written a letter.")
            st.markdown("* *Passive:* A letter has been written by her.")
            
            st.write("---")
            st.markdown("🎯 **AI Evaluation Quiz:**")
            ans_eng = st.text_input("Change into Passive Voice: 'He killed a snake.'")
            if st.button("Evaluate English Answer"):
                clean_ans = ans_eng.strip().lower().replace(".", "")
                if "a snake was killed by him" in clean_ans:
                    st.success("✅ Perfect! Since 'killed' is Past Tense, we use 'was/were + V3'. Your answer is absolutely correct!")
                else:
                    st.error("❌ Incorrect. The correct Passive Voice is: 'A snake was killed by him.'")
                    
        elif eng_topic == "Prepositions":
            st.markdown("#### **Prepositions of Time & Place**")
            st.markdown("* **In:** Used for months/years/large places (e.g., *In Kerala*, *In 2026*)")
            st.markdown("* **On:** Used for days and dates (e.g., *On Monday*, *On 15th August*)")
            st.markdown("* **At:** Used for specific times/exact spots (e.g., *At 4 PM*, *At school*)")
            
            st.write("---")
            st.markdown("🎯 **AI Evaluation Quiz:**")
            ans_prep = st.text_input("Fill in the blank: 'The exam starts ____ 10:00 AM.' (in / on / at)")
            if st.button("Check Preposition"):
                if ans_prep.strip().lower() == "at":
                    st.success("✅ Correct! We always use 'at' before specific time expressions.")
                else:
                    st.error("❌ Wrong. The correct answer is 'at' (At 10:00 AM).")

    # 4. HINDI SECTION (Foreign Language 2)
    elif lang == "हिन्दी (Hindi)":
        st.info("💡 हिन्दी व्याकरण कोच सक्रिय है! (Hindi Coach is Active)")
        hin_topic = st.radio("विषय चुनिए (Select Topic):", ["कारक (Kaarak)", "काल (Tenses)"])
        
        if hin_topic == "कारक (Kaarak)":
            st.markdown("#### **हिन्दी कारक (Case Markers)**")
            st.write("संज्ञा या सर्वनाम का क्रिया से संबंध बताने वाले रूप को कारक कहते हैं।")
            st.markdown("* **कर्ता कारक (Subject):** इसका चिन्ह **'ने'** है। (उदाहरण: राम ने खाना खाया।)")
            st.markdown("* **कर्म कारक (Object):** इसका चिन्ह **'को'** है। (उदाहरण: उसने मोहन को देखा।)")
            st.markdown("* **करण कारक (Instrument):** इसका चिन्ह **'से'** है। (उदाहरण: वह कलम से लिखता है।)")
            
            st.write("---")
            st.markdown("🎯 **AI Evaluation Quiz:**")
            ans_hin1 = st.text_input("प्रश्न: 'पेड़ से पत्ता गिरा' - इस वाक्य में 'से' किस कारक का चिन्ह है? (करण / अपादान)")
            if st.button("उत्तर जाँचें (Check Hindi)"):
                if "अपादान" in ans_hin1 or "apadan" in ans_hin1.lower():
                    st.success("✅ सही उत्तर! अलग होने के अर्थ में 'से' का प्रयोग 'अपादान कारक' (Apadan Kaarak) में होता है।")
                else:
                    st.error("❌ गलत उत्तर। यहाँ पेड़ से पत्ता 'अलग' हो रहा है, इसलिए यह 'अपादान कारक' है।")

    # 5. ARABIC SECTION (Foreign Language 3)
    elif lang == "العربية (Arabic)":
        st.info("💡 لغة عربية - Arabic Language Coach is Active!")
        ara_topic = st.radio("اختر الموضوع (Select Topic):", ["أقسام الكلام (Parts of Speech)", "الضمائر (Pronouns)"])
        
        if ara_topic == "أقسام الكلام (Parts of Speech)":
            st.markdown("#### **أقسام الكلام (Words in Arabic)**")
            st.write("In Arabic, words are divided into three simple categories:")
            st.markdown("* **اِسْم (Noun):** Name of a person, place, or thing. (e.g., كِتَاب - Book, قَلَم - Pen)")
            st.markdown("* **فِعْل (Verb):** An action word. (e.g., كَتَبَ - He wrote, يَقْرَأُ - He reads)")
            st.markdown("* **حَرْف (Particle):** Letters or words that connect sentences. (e.g., فِي - In, عَلَى - On)")
            
            st.write("---")
            st.markdown("🎯 **AI Evaluation Quiz:**")
            ans_ara = st.text_input("Question: Is 'ذَهَبَ' (He went) an اِسْم (Noun) or فِعْل (Verb)?")
            if st.button("Verify Arabic Answer"):
                if "فعل" in ans_ara or "verb" in ans_ara.lower():
                    st.success("✅ ممتاز! (Excellent!) 'ذَهَبَ' indicates an action, so it is a فِعْل (Verb).")
                else:
                    st.error("❌ خطأ! (Wrong!) 'ذَهَبَ' is a past tense action, so it is a فِعْل (Verb).")

elif choice == "Gamified Math Learning":
    st.markdown("### 🧮 Math Quest (കണക്ക് കളിയിലൂടെ പഠിക്കാം)")
    st.write("USS / NuMaTS പരീക്ഷകൾക്കായുള്ള പ്രത്യേക ലോജിക്കൽ ചോദ്യങ്ങൾ താഴെ നൽകുന്നു.")
    
    score = 0
    ans1 = st.text_input("ചോദ്യം 1: 2, 4, 8, 16, ... അടുത്ത സംഖ്യ ഏത്?")
    if ans1 == "32":
        st.success("✅ ശരിയുത്തരം! +10 പോയിന്റ്സ്.")
        score += 10
        
        st.write("---")
        st.markdown("🌟 **ലെവൽ 2 (NuMaTS സ്പെഷ്യൽ):**")
        ans2 = st.text_input("ചോദ്യം 2: ഒരു സമചതുരത്തിന്റെ വശം ഇരട്ടിയാക്കിയാൽ പരപ്പളവ് എത്ര മടങ്ങാകും?")
        if st.button("ലെവൽ 2 പരിശോധിക്കുക"):
            if ans2 == "4":
                st.success("🎉 ഗംഭീരം! ശരിയുത്തരം. നിങ്ങൾ ഗെയിം ജയിച്ചിരിക്കുന്നു!")
            else:
                st.error("❌ തെറ്റായ ഉത്തരമാണ്. വീണ്ടും ചിന്തിച്ചു നോക്കൂ!")
    elif ans1 and ans1 != "32":
        st.error("❌ തെറ്റാണ്. വീണ്ടും ശ്രമിക്കൂ!")

elif choice == "Smart Study Planner":
    st.markdown("### 📅 Smart Study Planner")
    st.write("നിങ്ങളുടെ പഠന സമയം കൃത്യമായി പ്ലാൻ ചെയ്യൂ.")
    study_time = st.slider("ദിവസേന എത്ര മണിക്കൂർ പഠിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നു?", 1, 5, 2)
    if study_time <= 2:
        st.markdown("* **45 മിനിറ്റ്:** ഗണിതം (USS/NuMaTS പ്രെപ്പറേഷൻ)\n* **45 മിനിറ്റ്:** ഭാഷാ പഠനം (സംസ്കൃതം/ഇംഗ്ലീഷ്)\n* **30 മിനിറ്റ്:** റിവിഷനും ക്വിസും")
    else:
        st.markdown("* **60 മിനിറ്റ്:** ഗണിതം\n* **60 മിനിറ്റ്:** ഭാഷാ വ്യാകരണങ്ങൾ\n* **60 മിനിറ്റ്:** സയൻസ് പ്രോജക്റ്റുകൾ\n* **30 മിനിറ്റ്:** ബ്രേക്ക്")
