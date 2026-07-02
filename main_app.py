import streamlit as st

st.set_page_config(page_title="SmartStudywithAI", page_icon="🎓", layout="wide")

st.title("🎓 SmartStudywithAI")
st.subheader("YIP Innovation Project - AI Tutor, Math Quest & Smart Planner")
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
            if "अादान" in ans_hin1 or "apadan" in ans_hin1.lower():
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

# UPDATED FEATURE: SMART AI GURU (Q&A RESOLUTION)
elif choice == "AI ഗുരു (AI Q&A Hub)":
    st.markdown("### 🤖 AI ഗുരു (പഠന സംശയനിവാരണ കേന്ദ്രം)")
    st.write("പഠനവുമായി ബന്ധപ്പെട്ട നിങ്ങളുടെ ഏത് കഠിനമായ സംശയങ്ങളും ഇവിടെ ടൈപ്പ് ചെയ്ത് ചോദിക്കാം. AI ഗുരു അത് വിശദമായി പരിഹരിച്ചു തരും!")
    
    user_query = st.text_input("നിങ്ങളുടെ സംശയം ഇവിടെ വ്യക്തമായി ടൈപ്പ് ചെയ്യുക:")
    
    if st.button("സംശയം പരിഹരിക്കുക"):
        if user_query:
            query_lower = user_query.lower()
            st.markdown("#### **👨‍🏫 AI ഗുരുവിന്റെ വിശദീകരണം:**")
            
            # Intelligent Multi-Query Identification
            if "സന്ധി" in query_lower:
                st.success("🔍 **സന്ധി നിയമം വിശദമായി:**")
                st.write("രണ്ട് പദങ്ങൾ ചേരുമ്പോൾ ഉണ്ടാകുന്ന വ്യത്യാസമാണ് സന്ധി. പ്രധാനമായും 4 സന്ധികളാണ് മലയാളത്തിലുള്ളത്:")
                st.write("1. **ലോപം:** ഒരു അക്ഷരം ഇല്ലാതാകുന്നു (ഉദാ: ഒന്നു + അറ്റ = ഒന്നറ്റ).")
                st.write("2. **ആഗമം:** ഒരു പുതിയ അക്ഷരം വരുന്നു (ഉദാ: പൂ + അമ്പ് = പൂവമ്പ്).")
                st.write("3. **ആദേശം:** ഒരു അക്ഷരത്തിന് പകരം വേറൊന്ന് വരുന്നു (ഉദാ: കൺ + പീലി = കപ്പീലി).")
                st.write("4. **ദ്വിത്വം:** അക്ഷരം ഇരട്ടിക്കുന്നു (ഉദാ: കിളി + കൂട് = കിളിക്കൂട്).")
                
            elif "ലകാരം" in query_lower or "ലകാരങ്ങൾ" in query_lower or "lakar" in query_lower:
                st.success("🔍 **സംസ്കൃത ലകാരങ്ങൾ (Tenses):**")
                st.write("സംസ്കൃതത്തിൽ കാലങ്ങളെയും ഭാവങ്ങളെയും സൂചിപ്പിക്കാൻ ലകാരങ്ങൾ ഉപയോഗിക്കുന്നു. പ്രധാനപ്പെട്ടവ താഴെ പറയുന്നവയാണ്:")
                st.write("* **ലട് ലകാരഃ (लट्):** വർത്തമാനകാലം (Present Tense) -> ഉദാ: पठति (വായിക്കുന്നു)")
                st.write("* **ലങ് ലകാരഃ (लङ्):** ഭൂതകാലം (Past Tense) -> ഉദാ: अपठत् (വായിച്ചു)")
                st.write("* **ലൃട് ലകാരഃ (लृट्):** ഭാവികാലം (Future Tense) -> ഉദാ: पठिष्यति (വായിക്കും)")
                st.write("* **ലോട് ലകാരഃ (लोट्):** അനുജ്ഞ/കല്പന (Imperative Mood) -> ഉദാ: पठതു (വായിക്കൂ)")
                
            elif "ഓർമ്മ" in query_lower or "പഠിക്കാൻ" in query_lower or "മറന്നു" in query_lower:
                st.info("🧠 **പഠന തന്ത്രങ്ങൾ (Study Tips):**")
                st.write("പഠിച്ച കാര്യങ്ങൾ പെട്ടെന്ന് മറക്കാതിരിക്കാൻ ഈ സ്മാർട്ട് വഴികൾ നോക്കൂ:")
                st.write("1. **ഫെയ്ൻമാൻ ടെക്നിക് (Feynman Technique):** നിങ്ങൾ പഠിച്ച കാര്യം നിങ്ങളുടെ ഒരു കൂട്ടുകാരന് ലളിതമായി പറഞ്ഞു കൊടുക്കുന്നത് പോലെ സ്വയം ഉറക്കെ പറഞ്ഞു പഠിക്കുക.")
                st.write("2. **പോമോഡോറോ രീതി:** 25 മിനിറ്റ് ശ്രദ്ധയോടെ പഠിക്കുക, ശേഷം 5 മിനിറ്റ് ബ്രേക്ക് എടുക്കുക. ഇത് തലച്ചോറിന് ഉന്മേഷം നൽകും.")
                st.write("3. **ചിത്രങ്ങൾ ഉപയോഗിക്കുക:** വലിയ പാരഗ്രാഫുകൾ പഠിക്കുന്നതിന് പകരം മൈൻഡ് മാപ്പുകളും ഫ്ലോചാർട്ടുകളും വരച്ചു പഠിക്കുക.")
                
            elif "കണക്ക്" in query_lower or "math" in query_lower or "uss" in query_lower or "numats" in query_lower:
                st.warning("🔢 **ഗണിത സഹായം (Math Solutions):**")
                st.write("USS, NuMaTS പരീക്ഷകളിൽ സാധാരണയായി ചോദിക്കുന്ന പ്രധാന സൂത്രവാക്യങ്ങൾ:")
                st.write("* **തുടർച്ചയായ ഇരട്ട സംഖ്യകളുടെ തുക:** $n(n+1)$")
                st.write("* **തുടർച്ചയായ ഒറ്റ സംഖ്യകളുടെ തുക:** $n^2$")
                st.write("* **ഒരു വശത്തിന്റെ നീളം തന്നാൽ സമചതുരത്തിന്റെ വിസ്തീർണ്ണം:** വശം $\times$ വശം ($a^2$)")
                
            else:
                st.write(f"✨ **AI വിവേചനം:** '{user_query}' എന്ന വിഷയത്തെക്കുറിച്ചുള്ള ചോദ്യം വളരെ നല്ലതാണ്! നിങ്ങളുടെ ഈ സംശയം കൃത്യമായി പരിഹരിക്കാൻ സ്കൂൾ പാഠപുസ്തകത്തിലെ പ്രസക്തമായ ഭാഗങ്ങൾ നോക്കാവുന്നതാണ്. ഭാഷാ വ്യാകരണങ്ങളോ കണക്കോ ആണെങ്കിൽ മെനുവിലെ മറ്റ് സെക്ഷനുകൾ ഉപയോഗിച്ച് നിങ്ങൾക്ക് സ്വയം ക്വിസ് പരിശീലിക്കാനും സാധിക്കും.")
        else:
            st.error("ദയവായി നിങ്ങളുടെ സംശയം ബോക്സിൽ ടൈപ്പ് ചെയ്യുക.")

# NEW FEATURE: AI VIDEO LECTURES
elif choice == "AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ":
    st.markdown("### 📺 AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ (Digital Video Classroom)")
    st.write("വിഷയങ്ങൾ കണ്ടു മനസ്സിലാക്കാൻ മികച്ച വീഡിയോ ക്ലാസുകൾ താഴെ തിരഞ്ഞെടുക്കാം:")
    
    vid_subject = st.selectbox("ക്ലാസ് കാണേണ്ട വിഷയം തിരഞ്ഞെടുക്കുക:", ["Select Subject", "Sanskrit (സംസ്കൃതം ക്ലാസുകൾ)", "Mathematics (ഗണിതശാസ്ത്രം ക്ലാസുകൾ)"])
    
    if vid_subject == "Sanskrit (സംസ്കൃതം ക്ലാസുകൾ)":
        st.markdown("#### 📜 ലക്ചർ വീഡിയോ: സംസ്കൃതം അടിസ്ഥാനങ്ങൾ ലളിതമായി")
        st.write("സംസ്കൃത ഭാഷയിലെ അക്ഷരങ്ങളും ലകാരങ്ങളും മനസ്സിലാക്കാൻ താഴെ നൽകിയിരിക്കുന്ന വീഡിയോ കാണുക:")
        # Embedding an educational Sanskrit YouTube video safely
        st.video("https://www.youtube.com/watch?v=kSgS_wO5j2U")
        st.caption("കടപ്പാട്: Kite Victers / Educational Content")
        
    elif vid_subject == "Mathematics (ഗണിതശാസ്ത്രം ക്ലാസുകൾ)":
        st.markdown("#### 📐 ലക്ചർ വീഡിയോ: USS / NuMaTS ജ്യാമിതി സ്പെഷ്യൽ ക്ലാസ്")
        st.write("ത്രികോണങ്ങളും കോണുകളും അടിസ്ഥാനമാക്കിയുള്ള കണക്കുകൾ എളുപ്പത്തിൽ പഠിക്കാൻ താഴെ കാണുന്ന വീഡിയോ പ്ലേ ചെയ്യുക:")
        # Embedding an educational Math YouTube video safely
        st.video("https://www.youtube.com/watch?v=kYorv8R2t2M")
        st.caption("കടപ്പാട്: Educational Class / Geometry Tips")

elif choice == "Gamified Math Learning":
    st.markdown("### 🧮 Math Quest (കണക്ക് കളിയിലൂടെ പഠിക്കാം)")
    ans1 = st.text_input("ചോദ്യം 1: 2, 4, 8, 16, ... അടുത്ത സംഖ്യ ഏത്?")
    if ans1 == "32":
        st.success("✅   രിയുത്തരം!")
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
