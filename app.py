import streamlit as st
from datetime import datetime
import base64
from streamlit_pdf_viewer import pdf_viewer
import pytz
import qrcode
from PIL import Image
from io import BytesIO

# MUST be the absolute first streamlit command (Merged previous duplicates)
st.set_page_config(page_title="Srinivas Tanakala | AI Portfolio", layout="wide", page_icon="🚀")

st.markdown(
    """
    <style>
    /* 1. Target the absolute outer container */
    .stApp {
        border: 5px solid #4CAF50 !important;
        border-radius: 15px;
        margin: 10px;
        padding: 0px;
    }

    /* 2. Target the main content area specifically */
    .stMain {
        border: 2px solid #2e7d32 !important;
        border-radius: 10px;
        margin: 10px;
    }
    
    /* 3. Ensure the border is visible even with scrolling */
    [data-testid="stAppViewContainer"] {
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- LIVE DATE & TIME CALCULATION ---
ist = pytz.timezone('Asia/Kolkata')
now_ist = datetime.now(ist)
live_date_time = now_ist.strftime('%d %b %Y | %H:%M')

# 1. AUTOMATIC EXPERIENCE CALCULATOR
start_date = datetime(2022, 5, 1)
current_date = datetime.now()
experience_years = (current_date - start_date).days / 365.25
exp_display = f"{int(experience_years)}+"

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
    st.markdown(f"""
        <p style='font-size: 22px; font-weight: 500; margin-top: -10px;'>
            🛠️ <b>Streamlit Dev on GitHub</b> | 🌊 <b>Visakhapatnam, India</b> | 🕒 <b>{live_date_time} (UTC +05:30)</b>
        </p>
    """, unsafe_allow_html=True)
    
    # Contact Row
    st.markdown("""
    ### 👔 [LinkedIn](https://www.linkedin.com/in/srinivas-t-a-557637119/) | 📊 [Kaggle](https://kaggle.com/srinivasta) | 📧 [Email](mailto:tasrinivass@gmail.com) | 💻 [GitHub](https://github.com/srinivasta)
    """)
    st.info("🌐 [**Explore My Interactive AI Portfolio & Digital Resume**](https://srinivasta-rpof88cn8owuvgyk3w9jcy.streamlit.app/)")
    
st.divider()

# --- TABBED VIEW: PORTFOLIO VS RESUME ---
tab1, tab2 = st.tabs(["🚀 Live Portfolio", "📄 Professional CV"])

with tab1:
    # --- ABOUT ME ---
    st.markdown(f"**🎓 {exp_display} Years AI Experience** | **💼 20+ Years Finance Expertise**")
    st.write("Expert in leveraging AI tools and Python to deliver high-speed predictive modeling and risk assessment.")
    
    # Projects Grid
    col1, col2 = st.columns(2)

    with col1:
        st.header("🏢 FinTech & Business Intelligence")
    
        # --- Production Platforms (Highest Priority) ---
        st.link_button("📈 TransitionControl", "https://transition-command-center-hwyfkbtfvwcitg94dufcwg.streamlit.app/")
        st.link_button("💰 CapitalVantage Auditor", "https://5nemtiurhbntuup3etwc8f.streamlit.app/")
        st.link_button("💳 CreditPulse-AI", "https://creditpulse-ai-ow7sdnqsrbt6yf4ddtrxmc.streamlit.app/")
        st.link_button("🏗️ Moder 4C's Engine", "https://moder-4c-s-dynamic-policy-engine-am7fzqxlcyxmxyqxsfpugp.streamlit.app")
    
        # --- Analytical Tools & Dashboards (Medium Priority) ---
        st.link_button("📊 Real-time Sales Dashboard", "https://real-time-sales-dashboard-key6zivh5fnkane3t8x6v2.streamlit.app")
        st.link_button("🏢 ConstructAI Dashboard", "https://gfxbyvznuvhyqbxwwyj4os.streamlit.app")
        st.link_button("🔮 Quantum AI Crypto", "https://quantum-ai-portfolio-bffydmzkdbtjaejwf6huvh.streamlit.app")
        st.link_button("💹 Multi-Stock Predictor", "https://stock-predictor-app-cqwmt2o3nwmpti92u8n7j2.streamlit.app")
        st.link_button("📊 Stock Analysis Combo", "https://stock-analysis-combo-c7zmpbn2skp5h8rnrpchdy.streamlit.app/") 
    
        # --- Automation & Pipelines (Utility Priority) ---
        st.link_button("🧪 Fintech Regression Automation", "https://fintech-regression-automation-xmg7yrkex5apmvc29knpxl.streamlit.app/") 
        st.link_button("🛰️ Etihad Telemetry Pipeline", "https://etihad-telemetry-pipeline-hoxpbysyd8exh9xwrwjezj.streamlit.app/") 

    with col2:
        st.header("🧠 Generative AI & Operations")
    
        # --- Advanced GenAI Platforms (Highest Priority) ---
        st.link_button("💼 AI Recruiter", "https://airecruiter-bjhauwjq4ncyh6p8q7diot.streamlit.app/") 
        st.link_button("🤖 Multi-Agent Chatbot", "https://multi-agent-chatbot-yv35yj5g7obpbibcxnwrme.streamlit.app")
        st.link_button("🎨 Gemini AI Image Generator", "https://gemini-image-generator-bdyowfxxqb4q5htbrrgjzv.streamlit.app")
    
        # --- Specialized Intelligence Tools (Medium Priority) ---
        st.link_button("🍲 Smart Bhojan: Nutrition AI", "https://smartbhojan-9hebtsjz3wun3adggzry6s.streamlit.app")
        st.link_button("🎥 YouTube Summarizer", "https://geminitubesummarizer-5ra24rq4meqoogtkfbzpzt.streamlit.app")
        st.link_button("🎤 Whisper AI Transcriber", "https://myvideosummarizer-g5xpetuztm8zfowruaeutm.streamlit.app")
        st.link_button("🩺 Heart Failure Risk", "https://heartfailure-gaufwbwfmh2j2u8ytzfmm5.streamlit.app")
    
        # --- Basic Utilities & Training (Utility Priority) ---
        st.link_button("🛠️ AI Super Tool", "https://ai-super-tool-uxhxpvn4lqyc7szmsdqtl8.streamlit.app")
        st.link_button("🖼️ Photo Background Changer", "https://photo-bg-changer-kdrxyvhjx3ibr4ccoddm3f.streamlit.app")
        st.link_button("🌡️ Temperature Forecasting App", "https://example.com") 
        st.link_button("📱 Generated QR Code", "https://generatedqrcode-o4c9u7iprbc9bzkqrxqu4j.streamlit.app/") 
        st.link_button("📝 MS Office Training", "https://ms-office-training-zokxafpvnvpaoyxjyz5vtk.streamlit.app/") 
with tab2:
    st.subheader("Full Professional Resume")
    pdf_file_path = "Srinivas_Tanakala_CV.pdf"
    
    try:
        with open(pdf_file_path, "rb") as f:
            pdf_bytes = f.read()
        
        st.download_button(
            label="📥 Download Resume (PDF)",
            data=pdf_bytes,
            file_name="Srinivas_Tanakala_CV.pdf",
            mime="application/pdf"
        )
        pdf_viewer(pdf_file_path, width=800, height=1000)
        
    except FileNotFoundError:
        st.error("⚠️ Resume PDF not found. Please ensure 'Srinivas_Tanakala_CV.pdf' is uploaded to your GitHub repository.")

st.divider()

# --- FOOTER SECTION WITH QR CODE ---
col_foot1, col_foot2 = st.columns([3, 1])

with col_foot1:
    st.info("💡 **Recruiter Tip:** Use the tabs above to switch between my live deployments and my full professional CV.")
    st.markdown("💡 *“Bridging two decades of financial wisdom with modern AI to deliver real-world, data-powered solutions.”*")

with col_foot2:
    # Generate QR Code dynamically targeting your live portfolio
    portfolio_url = "https://srinivasta-rpof88cn8owuvgyk3w9jcy.streamlit.app/"
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(portfolio_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#2e7d32", back_color="white") # Custom green color matching your UI borders!
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.image(byte_im, caption="📱 Scan to Share Webapp", width=160)
