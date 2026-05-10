import streamlit as st
from datetime import datetime
import base64
from streamlit_pdf_viewer import pdf_viewer
import pytz

import streamlit as st

# Inject custom CSS to create a border around the entire main content
st.markdown(
    """
    <style>
    /* Target the main app container */
    .main .block-container {
        border: 2px solid #4CAF50; /* Set your color and thickness */
        padding: 3rem;             /* Space between border and content */
        border-radius: 20px;       /* Rounded corners */
        margin-top: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Optional shadow for depth */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your app content follows
st.title("🚀 My Interactive AI Portfolio")
st.write("Welcome to my bordered layout!")

# --- LIVE DATE & TIME CALCULATION ---
ist = pytz.timezone('Asia/Kolkata')
now_ist = datetime.now(ist)
# Formats as: 10 May 2026 | 13:04
live_date_time = now_ist.strftime('%d %b %Y | %H:%M')


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
    st.markdown("💼 20+ Years Finance & Ops |🚀 **Data Scientist** | 🧠 **AI + FinTech Explorer**")
    # Increased font size for the location and dev line
    # Added the 'f' before the quotes to enable the live clock
    st.markdown(f"""
        <p style='font-size: 22px; font-weight: 500; margin-top: -10px;'>
            🛠️ <b>Streamlit Dev on GitHub</b> | 🌊 <b>Visakhapatnam, India</b> | 🕒 <b>{live_date_time} (UTC +05:30)</b>
        </p>
    """, unsafe_allow_html=True)
    
    # Contact Row
    st.markdown("""
    ### 👔 [LinkedIn](https://www.linkedin.com/in/srinivas-t-a-557637119/) | 📊 [Kaggle](https://kaggle.com/srinivasta) | 📧 [Email](mailto:tasrinivass@gmail.com) | 💻 [GitHub](https://github.com/srinivasta)
    """)
        # THE BIG HIGHLIGHT LINK
    st.info("🌐 [**Explore My Interactive AI Portfolio & Digital Resume**](https://srinivasta-rpof88cn8owuvgyk3w9jcy.streamlit.app/)")

    
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
        st.header("🧠 Generative AI")
        st.link_button("🍲 Smart Bhojan: Nutrition AI", "https://smartbhojan-9hebtsjz3wun3adggzry6s.streamlit.app/")
        st.link_button("🎥 YouTube Summarizer", "https://geminitubesummarizer-5ra24rq4meqoogtkfbzpzt.streamlit.app/")
        st.link_button("🎤 Whisper AI Transcriber", "https://myvideosummarizer-g5xpetuztm8zfowruaeutm.streamlit.app/")
        st.link_button("🎨 Gemini AI Image Generator", "https://gemini-image-generator-bdyowfxxqb4q5htbrrgjzv.streamlit.app/")
        st.link_button("🤖 Multi-Agent Chatbot", "https://multi-agent-chatbot-yv35yj5g7obpbibcxnwrme.streamlit.app/")
        st.link_button("🖼️ Photo Background Changer", "https://photo-bg-changer-kdrxyvhjx3ibr4ccoddm3f.streamlit.app/")
        st.link_button("🛠️ AI Super Tool", "https://ai-super-tool-uxhxpvn4lqyc7szmsdqtl8.streamlit.app/")
        st.link_button("🩺 Heart Failure Risk", "https://heartfailure-gaufwbwfmh2j2u8ytzfmm5.streamlit.app/")

from streamlit_pdf_viewer import pdf_viewer

with tab2:
    st.subheader("Full Professional Resume")
    
    # 1. Path to your PDF in the GitHub repo
    pdf_file_path = "Srinivas_Tanakala_CV.pdf"
    
    try:
        # 2. Add a direct download button first
        with open(pdf_file_path, "rb") as f:
            pdf_bytes = f.read()
        
        st.download_button(
            label="📥 Download Resume (PDF)",
            data=pdf_bytes,
            file_name="Srinivas_Tanakala_CV.pdf",
            mime="application/pdf"
        )
        
        # 3. High-compatibility PDF Viewer
        # This component renders the PDF directly in the app
        pdf_viewer(pdf_file_path, width=800, height=1000)
        
    except FileNotFoundError:
        st.error("⚠️ Resume PDF not found. Please ensure 'Srinivas_Tanakala_CV.pdf' is uploaded to your GitHub repository.")

st.divider()
st.info("💡 **Recruiter Tip:** Use the tabs above to switch between my live deployments and my full professional CV.")
