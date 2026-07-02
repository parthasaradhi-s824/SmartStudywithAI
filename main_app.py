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

# LANGUAGE TUTOR (Kept as before)
elif choice == "AI Language Tutor":
    st.markdown("### 🤖 AI Language Tutor")
    lang = st.selectbox("പഠിക്കേണ്ട ഭാഷ ഏതാണ്?", ["മലയാളം", "संस्कृतम् (Sanskrit)", "English", "हिन्दी (Hindi)", "العربية (Arabic)"])
    # ... (Language logic remains same) ...
    st.write("ഭാഷാ പഠന സെക്ഷൻ സജീവമാണ്.")

# AI GURU (Kept as before)
elif choice == "AI ഗുരു (AI Q&A Hub)":
    st.markdown("### 🤖 AI ഗുരു (പഠന സംശയനിവാരണ കേന്ദ്രം)")
    user_query = st.text_input("നിങ്ങളുടെ സംശയം ചോദിക്കൂ:")
    if st.button("സംശയം പരിഹരിക്കുക"):
        st.write("AI ഗുരു നിങ്ങളുടെ സംശയം വിശകലനം ചെയ്യുന്നു...") # Logic remains same

# UPDATED: VIDEO LECTURE CLASS (Added History + Your Video)
elif choice == "AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ":
    st.markdown("### 📺 AI വീഡിയോ ലെക്ചർ ക്ലാസുകൾ (Digital Video Classroom)")
    vid_subject = st.selectbox("ക്ലാസ് കാണേണ്ട വിഷയം തിരഞ്ഞെടുക്കുക:", ["Select Subject", "History (ചരിത്രം)", "Sanskrit (സംസ്കൃതം)", "Mathematics (ഗണിതം)"])
    
    if vid_subject == "History (ചരിത്രം)":
        st.markdown("#### 📜 ലക്ചർ വീഡിയോ: ഇന്ത്യൻ സ്വാതന്ത്ര്യസമരം")
        st.write("ഇന്ത്യയുടെ സ്വാതന്ത്ര്യസമര ചരിത്രം മനസ്സിലാക്കാൻ താഴെ നൽകിയിരിക്കുന്ന വീഡിയോ കാണുക:")
        st.video("https://www.youtube.com/watch?v=ofgIDZHTjTQ")
        st.caption("കടപ്പാട്: Educational Content")
        
    elif vid_subject == "Sanskrit (സംസ്കൃതം)":
        st.markdown("#### 📜 ലക്ചർ വീഡിയോ: സംസ്കൃതം അടിസ്ഥാനങ്ങൾ")
        st.video("https://www.youtube.com/watch?v=kSgS_wO5j2U")
        
    elif vid_subject == "Mathematics (ഗണിതം)":
        st.markdown("#### 📐 ലക്ചർ വീഡിയോ: ജ്യാമിതി സ്പെഷ്യൽ ക്ലാസ്")
        st.video("https://www.youtube.com/watch?v=kYorv8R2t2M")

# GAMIFIED MATH (Kept as before)
elif choice == "Gamified Math Learning":
    st.markdown("### 🧮 Gamified Math Learning")
    # ... (Math logic remains same) ...
    st.write("പഠനവും കളിയും തുടരുക!")

elif choice == "Smart Study Planner":
    st.markdown("### 📅 Smart Study Planner")
    # ... (Planner logic remains same) ...
    st.write("നിങ്ങളുടെ ടൈംടേബിൾ ഇവിടെ പ്ലാൻ ചെയ്യാം.")
