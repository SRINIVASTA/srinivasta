import streamlit as st
from datetime import datetime
import base64

# 1. AUTOMATIC EXPERIENCE CALCULATOR
start_date = datetime(2022, 5, 1)
current_date = datetime.now()
experience_years = (current_date - start_date).days / 365.25
exp_display = f"{int(experience_years)}+"

# Page Configuration
st.set_page_config(page_title="Srinivas Tanakala | AI Portfolio", layout="wide", page_icon="🚀")

# Header Section
col_head1, col_head2 = st.columns([1, 4])

with col_head1:
    try:
        st.image("professional-profile1mb.png", width=180)
    except:
        st.write("👤")

with col_head2:
    st.title("Hi 👋, I'm Appala Srinivas Tanakala")
    st.markdown("### 🚀 **Data Scientist** | 🧠 **AI + FinTech Explorer**")
    st.markdown("🛠️ **Streamlit Dev on GitHub** | 🌊 [**Visakhapatnam, India**](https://google.com)")
    
    # Contact Row
    st.markdown("""
    ### 👔 [LinkedIn](https://linkedin.com) | 📊 [Kaggle](https://kaggle.com) | 📧 [Email](mailto:tasrinivass@gmail.com) | 💻 [GitHub](https://github.com)
    """)

st.divider()

# --- TABBED VIEW: PORTFOLIO VS RESUME ---
tab1, tab2 = st.tabs(["🚀 Live Portfolio", "📄 Professional CV"])

with tab1:
    # --- ABOUT ME ---
    st.markdown(f"**🎓 {exp_display} Years AI Experience** | **💼 20+ Years Finance Expertise**")
    st.write("Expert in leveraging AI tools and Python to deliver high-speed predictive modeling and risk assessment.")
    
    # Projects Grid (Now correctly indented inside tab1)
    col1, col2 = st.columns(2)

    with col1:
        st.header("🏢 FinTech & Business Intelligence")
        st.link_button("📈 TransitionControl", "https://transition-command-center-hwyfkbtfvwcitg94dufcwg.streamlit.app/")
        st.link_button("💰 CapitalVantage Auditor", "https://5nemtiurhbntuup3etwc8f.streamlit.app/")
        st.link_button("💳 CreditPulse-AI", "https://creditpulse-ai-ow7sdnqsrbt6yf4ddtrxmc.streamlit.app/")
        st.link_button("🏗️ Moder 4C's Engine", "https://moder-4c-s-dynamic-policy-engine-am7fzqxlcyxmxyqxsfpugp.streamlit.app/")
        st.link_button("💹 Multi-Stock Predictor", "https://stock-predictor-app-cqwmt2o3nwmpti92u8n7j2.streamlit.app/")
        st.link_button("🏢 ConstructAI Dashboard", "https://gfxbyvznuvhyqbxwwyj4os.streamlit.app/")
        st.link_button("📊 Real-time Sales Dashboard", "https://real-time-sales-dashboard-key6zivh5fnkane3t8x6v2.streamlit.app/")
        st.link_button("🔮 Quantum AI Crypto", "https://quantum-ai-portfolio-bffydmzkdbtjaejwf6huvh.streamlit.app/")

    with col2:
        st.header("🧠 Generative AI & CV")
        st.link_button("🍲 Smart Bhojan: Nutrition AI", "https://smartbhojan-9hebtsjz3wun3adggzry6s.streamlit.app/")
        st.link_button("🎥 YouTube Summarizer", "https://geminitubesummarizer-5ra24rq4meqoogtkfbzpzt.streamlit.app/")
        st.link_button("🎤 Whisper AI Transcriber", "https://myvideosummarizer-g5xpetuztm8zfowruaeutm.streamlit.app/")
        st.link_button("🎨 Gemini AI Image Generator", "https://gemini-image-generator-bdyowfxxqb4q5htbrrgjzv.streamlit.app/")
        st.link_button("🤖 Multi-Agent Chatbot", "https://multi-agent-chatbot-yv35yj5g7obpbibcxnwrme.streamlit.app/")
        st.link_button("🖼️ Photo Background Changer", "https://photo-bg-changer-kdrxyvhjx3ibr4ccoddm3f.streamlit.app/")
        st.link_button("🛠️ AI Super Tool", "https://ai-super-tool-uxhxpvn4lqyc7szmsdqtl8.streamlit.app/")
        st.link_button("🩺 Heart Failure Risk", "https://heartfailure-gaufwbwfmh2j2u8ytzfmm5.streamlit.app/")

with tab2:
    st.subheader("Full Professional Resume")
    try:
        with open("Srinivas_Tanakala_CV.pdf", "rb") as f:
            pdf_data = f.read()
            
        st.download_button(label="📥 Download Resume (PDF)", data=pdf_data, file_name="Srinivas_Tanakala_CV.pdf", mime="application/pdf")
        
        # New encoding method using <embed> for better browser support
        base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ Resume PDF not found. Ensure 'Srinivas_Tanakala_CV.pdf' is in your GitHub repository.")

st.divider()
st.info("💡 **Recruiter Tip:** Use the tabs above to switch between my live deployments and my full professional CV.")
