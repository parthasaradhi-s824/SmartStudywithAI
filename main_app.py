import streamlit as str

str.set_page_config(page_title="SmartStudywithAI", page_icon="🎓", layout="wide")

str.title("🎓 SmartStudywithAI")
str.subheader("YIP Innovation Project - AI Tutor, Math Quest & Smart Planner")
str.write("---")

# Sidebar for navigation
choice = str.sidebar.selectbox("മെനു തിരഞ്ഞെടുക്കുക", ["Home (ഹോം)", "AI Language Tutor", "Gamified Math Learning", "Smart Study Planner"])

if choice == "Home (ഹോം)":
    str.markdown("### SmartStudywithAI-ലേക്ക് സ്വാഗതം! 👋")
    str.write("വിദ്യാർത്ഥികൾക്ക് കളിയിലൂടെ കണക്ക് പഠിക്കാനും, AI സഹായത്തോടെ വിവിധ ഭാഷകൾ പരിശീലിക്കാനും, പഠന സമയം കൃത്യമായി പ്ലാൻ ചെയ്യാനും സഹായിക്കുന്ന ഒരൊറ്റ പ്ലാറ്റ്‌ഫോം.")

elif choice == "Gamified Math Learning":
    str.markdown("### 🧮 Math Quest (കണക്ക് കളിയിലൂടെ പഠിക്കാം)")
    str.write("USS / NuMaTS പരീക്ഷകൾക്കായുള്ള പ്രത്യേക ചോദ്യങ്ങൾ താഴെ നൽകുന്നു.")
    
    # Simple UI interactive check
    ans1 = str.text_input("ചോദ്യം 1: 2, 4, 8, 16, ... അടുത്ത സംഖ്യ ഏത്?")
    if str.button("Check Answer"):
        if ans1 == "32":
            str.success("✅ ശരിയുത്തരം! +10 പോയിന്റ്സ്.")
        else:
            str.error("❌ തെറ്റാണ്. വീണ്ടും ശ്രമിക്കൂ!")

elif choice == "AI Language Tutor":
    str.markdown("### 🤖 AI Language Tutor (മലയാളം • संस्कृतम् • English • हिन्दी • العربية)")
    str.write("ഭാഷകളും വ്യാകരണ നിയമങ്ങളും പഠിക്കാൻ നിങ്ങളെ സഹായിക്കുന്ന AI അസിസ്റ്റന്റ്.")
    str.info("Note: AI API വരും ദിവസങ്ങളിൽ പൂർണ്ണമായി കണക്ട് ചെയ്യപ്പെടുന്നതാണ്.")

elif choice == "Smart Study Planner":
    str.markdown("### 📅 Smart Study Planner")
    str.write("നിങ്ങളുടെ പഠന സമയം കൃത്യമായി പ്ലാൻ ചെയ്യൂ.")
