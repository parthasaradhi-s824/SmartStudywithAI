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
    
    lang = st.selectbox("പഠിക്കേണ്ട ഭാഷ ഏതാണ്?", ["Select Language", "संस्कृतम् (Sanskrit)", "മലയാളം", "English", "हिन्दी", "العربية"])
    
    if lang == "संस्कृतम् (Sanskrit)":
        st.info("💡 സംസ്കൃത വ്യാകരണ കോച്ച് സജീവമാണ്!")
        topic = st.radio("പഠിക്കേണ്ട ഭാഗം തിരഞ്ഞെടുക്കുക:", ["ലകാരങ്ങൾ (Lakarah - Tenses)", "സംസ്കൃത സന്ധി (Sanskrita Sandhi)"])
        
        if topic == "ലകാരങ്ങൾ (Lakarah - Tenses)":
            st.markdown("#### **ലകാരങ്ങൾ (വ്യാകരണ നിയമം)**")
            st.write("സംസ്കൃതത്തിൽ പ്രധാനമായും 5 ലകാരങ്ങളാണ് സ്കൂൾ തലത്തിൽ പഠിക്കാനുള്ളത്:")
            st.markdown("* **ലട് ലകാരഃ (लट् लकार):** വർത്തമാനകാലം (Present Tense) -> ഉദാ: पठति (വായിക്കുന്നു)")
            st.markdown("* **ലങ് ലകാരഃ (लङ् लकार):** ഭൂതകാലം (Past Tense) -> ഉദാ: अपठत् (വായിച്ചു)")
            st.markdown("* **ലൃട് ലകാരഃ (लृट् लकार):** ഭാവികാലം (Future Tense) -> ഉദാ: पठिष्यति (വായിക്കും)")
            
            st.write("---")
            st.markdown("🎯 **ലഘു ക്വിസ് (AI Evaluation):**")
            ans_sansk = st.text_input("ചോദ്യം: 'भवति' (ആകുന്നു) എന്നത് ഏത് ലകാരമാണ്? (ലട് / ലങ് / ലൃട്)")
            if st.button("AI മൂല്യനിർണ്ണയം"):
                if "ലട്" in ans_sansk or "lat" in ans_sansk.lower():
                    st.success("✅ ശരിയുത്തരം! 'भवति' എന്നത് ലട് ലകാരം (വർത്തമാനകാലം) ആണ്. മികച്ച പാണ്ഡിത്യം!")
                else:
                    st.error("❌ തെറ്റാണ്. ഭവതി (भवति) എന്നത് വർത്തമാനകാല രൂപമാണ്, അതുകൊണ്ട് അത് 'ലട് ലകാരം' ആണ്. വീണ്ടും ശ്രമിക്കൂ!")
                    
        elif topic == "സംസ്കൃത സന്ധി (Sanskrita Sandhi)":
            st.markdown("#### **സന്ധി നിയമങ്ങൾ**")
            st.write("മലയാള പാഠാവലിയിലും സംസ്കൃതത്തിലും പ്രധാനമായി പഠിക്കാനുള്ള സന്ധികൾ താഴെ നൽകുന്നു:")
            st.markdown("* **സവർണ്ണദീർഘസന്ധി:** ഒരേ സ്വരങ്ങൾ ചേർന്ന് ദീർഘമായി മാറുന്നു. (ഉദാ: വിദ്യ + അർത്ഥി = വിദ്യാർത്ഥി)")
            
            st.write("---")
            st.markdown("🎯 **ലഘു ക്വിസ് (AI Evaluation):**")
            ans_sandhi = st.text_input("ചോദ്യം: 'ഹിമാലയം' (ഹിമ + ആലയം) ഏത് സന്ധിക്ക് ഉദാഹരണമാണ്?")
            if st.button("സന്ധി പരിശോധിക്കുക"):
                if "സവർണ്ണ" in ans_sandhi or "savarna" in ans_sandhi.lower():
                    st.success("✅ കൃത്യമായ ഉത്തരം! ഇത് സവർണ്ണദീർഘസന്ധിയാണ്.")
                else:
                    st.error("❌ തെറ്റാണ്! ഹിമ (അ) + ആലയം (ആ) ചേർന്ന് 'മാ' (ദീർഘം) ആയതിനാൽ ഇത് സവർണ്ണദീർഘസന്ധിയാണ്.")

    elif lang == "മലയാളം":
        st.info("💡 മലയാളം വ്യാകരണ കോച്ച് സജീവമാണ്!")
        st.markdown("🎯 **മലയാളം ക്വിസ്:**")
        ans_mal = st.text_input("ചോദ്യം: 'കടൽ +ക്കര = കടൽക്കര' - ഇത് ഏത് സന്ധിയാണ്? (ആഗമ സന്ധി / ആദേശ സന്ധി / ദ്വിത്വ സന്ധി)")
        if st.button("ഉത്തരം പരിശോധിക്കുക"):
            if "ദ്വിത്വം" in ans_mal or "dwitva" in ans_mal.lower():
                st.success("✅ ശരിയുത്തരം! 'ക്' എന്ന അക്ഷരം ഇരട്ടിച്ചതിനാൽ ഇത് ദ്വിത്വസന്ധിയാണ്.")
            else:
                st.error("❌ തെറ്റാണ്! അക്ഷരം ഇരട്ടിക്കുന്നതിനാൽ ഇത് 'ദ്വിത്വ സന്ധി' ആണ്.")

    elif lang != "Select Language":
        st.warning(f"{lang} ഭാഷയ്ക്കുള്ള ചോദ്യങ്ങൾ ഇപ്പോൾ അപ്‌ഡേറ്റ് ചെയ്തുകൊണ്ടിരിക്കുകയാണ്. ഉടൻ ലഭ്യമാകും!")

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
                st.success("🎉 ഗംഭീരം! ശരിയുത്തരം. നിങ്ങൾ ലോഗ് ഔട്ട് ചെയ്യാതെ ഗെയിം ജയിച്ചിരിക്കുന്നു!")
            else:
                st.error("❌ തെറ്റായ ഉത്തരമാണ്. വീണ്ടും ചിന്തിച്ചു നോക്കൂ!")
    elif ans1 and ans1 != "32":
        st.error("❌ തെറ്റാണ്. വീണ്ടും ശ്രമിക്കൂ!")

elif choice == "Smart Study Planner":
    st.markdown("### 📅 Smart Study Planner")
    st.write("നിങ്ങളുടെ പഠന സമയം കൃത്യമായി പ്ലാൻ ചെയ്യൂ.")
    
    study_time = st.slider("ദിവസേന എത്ര മണിക്കൂർ പഠിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നു?", 1, 5, 2)
    st.write(f"നിങ്ങൾ {study_time} മണിക്കൂറാണ് തിരഞ്ഞെടുത്തത്. നിങ്ങൾക്കുള്ള ടൈംടേബിൾ താഴെ നൽകുന്നു:")
    
    if study_time <= 2:
        st.markdown("* **45 മിനിറ്റ്:** ഗണിതം (USS/NuMaTS പ്രെപ്പറേഷൻ)\n* **45 മിനിറ്റ്:** ഭാഷാ പഠനം (സംസ്കൃതം/ഇംഗ്ലീഷ്)\n* **30 മിനിറ്റ്:** റിവിഷനും ക്വിസും")
    else:
        st.markdown("* **60 മിനിറ്റ്:** ഗണിതം (അഡ്വാൻസ്ഡ് പ്രോബ്ലംസ്)\n* **60 മിനിറ്റ്:** ഭാഷാ വ്യാകരണങ്ങൾ\n* **60 മിനിറ്റ്:** സയൻസ് പ്രോജക്റ്റുകൾ\n* **30 മിനിറ്റ്:** ബ്രേക്ക് & ക്വിസ്")
