import streamlit as st
from datetime import datetime

# 1. AUTOMATIC EXPERIENCE CALCULATOR
# This calculates years from your Kaggle registration (May 2022)
start_date = datetime(2022, 5, 1)
current_date = datetime.now()
experience_years = (current_date - start_date).days / 365.25
exp_display = f"{int(experience_years)}+"

# Page Configuration
st.set_page_config(page_title="Srinivas Tanakala | AI Portfolio", layout="wide", page_icon="🚀")

# Header Section
col_head1, col_head2 = st.columns([1, 4])

with col_head1:
    st.image("professional-profile1mb.png", width=180)

with col_head2:
    st.title("Hi 👋, I'm Appala Srinivas Tanakala")
    
    # Using a cleaner Markdown approach for the subheaders
    st.markdown("### 🚀 **Data Scientist** | 🧠 **AI + FinTech Explorer**")
    st.markdown("🛠️ **Streamlit Dev on GitHub** | 🌊 [**Visakhapatnam, India**](https://google.com)")
    st.write("---")

    # Clean, High-Visibility Contact Row with descriptive emojis
    st.markdown("""
    ### 👔 [LinkedIn](https://linkedin.com) | 📊 [Kaggle](https://kaggle.com) | 📧 [Email](mailto:tasrinivass@gmail.com) | 💻 [GitHub](https://github.com)
    """)

st.divider()


# --- ABOUT ME SECTION ---
# --- TABBED VIEW: PORTFOLIO VS RESUME ---
tab1, tab2 = st.tabs(["🚀 Live Portfolio", "📄 Professional CV"])

with tab1:
    # --- ABOUT ME ---
    st.markdown(f"**🎓 {exp_display} Years AI Experience** | **💼 20+ Years Finance Expertise**")
    st.write("Expert in leveraging AI tools and Python to deliver high-speed predictive modeling and risk assessment.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏢 FinTech & Business Intelligence")
        st.link_button("📈 TransitionControl", "https://streamlit.app")
        st.link_button("💰 CapitalVantage Auditor", "https://streamlit.app")
        st.link_button("💳 CreditPulse-AI", "https://streamlit.app")
        st.link_button("🏗️ Moder 4C's Engine", "https://streamlit.app")
        st.link_button("💹 Multi-Stock Predictor", "https://streamlit.app")

    with col2:
        st.subheader("🧠 Generative AI & CV")
        st.link_button("🍲 Smart Bhojan", "https://streamlit.app")
        st.link_button("🎥 YouTube Summarizer", "https://streamlit.app")
        st.link_button("🎤 Whisper AI Transcriber", "https://streamlit.app")
        st.link_button("🤖 Multi-Agent Chatbot", "https://streamlit.app")
        st.link_button("🛠️ AI Super Tool", "https://streamlit.app")

with tab2:
    st.subheader("Full Professional Resume")
    
    # 1. Provide a Download Button
    try:
        with open("Srinivas_Tanakala_CV.pdf", "rb") as f:
            pdf_data = f.read()
        st.download_button(label="📥 Download Resume (PDF)", data=pdf_data, file_name="Srinivas_Tanakala_CV.pdf", mime="application/pdf")
        
        # 2. Embed PDF in A4-style Viewer
        base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Resume PDF not found. Please upload 'Srinivas_Tanakala_CV.pdf' to your GitHub repository.")

st.divider()
st.info("💡 **Recruiter Tip:** Use the tabs above to switch between my live deployments and my full professional CV.")
