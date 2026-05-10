import streamlit as st

# Page Configuration
st.set_page_config(page_title="Srinivas Tanakala | AI Portfolio", layout="wide", page_icon="🚀")

# Header Section
col_head1, col_head2 = st.columns([1, 4])

with col_head1:
    st.image("github.com/srinivasta/srinivasta/professional-profile1mb.png", width=180)

with col_head2:
    st.title("Appala Srinivas Tanakala")
    st.subheader("20+ Years Finance & Ops Expertise | 4+ Years AI & Data Science")
    st.markdown("📍 Visakhapatnam, India | [LinkedIn](https://www.linkedin.com/in/srinivas-t-a-557637119/) | [GitHub](https://github.com/srinivasta)")
    st.write("📧 tasrinivass@gmail.com")

st.write("---")

# Main categories
col1, col2 = st.columns(2)

with col1:
    st.header("🏢 FinTech & Business Intelligence")
    st.link_button("📈 TransitionControl: BPO Command Center", "https://transition-command-center-hwyfkbtfvwcitg94dufcwg.streamlit.app/")
    st.link_button("💰 CapitalVantage: GenAI Financial Auditor", "https://5nemtiurhbntuup3etwc8f.streamlit.app/")
    st.link_button("💳 CreditPulse-AI: Risk Engine", "https://creditpulse-ai-ow7sdnqsrbt6yf4ddtrxmc.streamlit.app/")
    st.link_button("🏗️ Moder 4C's: Mortgage Policy Engine", "https://moder-4c-s-dynamic-policy-engine-am7fzqxlcyxmxyqxsfpugp.streamlit.app/")
    st.link_button("💹 Multi-Stock Predictor App", "https://stock-predictor-app-cqwmt2o3nwmpti92u8n7j2.streamlit.app/")
    st.link_button("🏢 ConstructAI: Real Estate Dashboard", "https://gfxbyvznuvhyqbxwwyj4os.streamlit.app/")
    st.link_button("📊 Real-time Sales Dashboard", "https://real-time-sales-dashboard-key6zivh5fnkane3t8x6v2.streamlit.app/")
    st.link_button("🔮 Quantum AI Crypto Portfolio", "https://quantum-ai-portfolio-bffydmzkdbtjaejwf6huvh.streamlit.app/")

with col2:
    st.header("🧠 Generative AI & Computer Vision")
    st.link_button("🍲 Smart Bhojan: Nutrition AI", "https://smartbhojan-9hebtsjz3wun3adggzry6s.streamlit.app/")
    st.link_button("🎥 YouTube Video Summarizer", "https://geminitubesummarizer-5ra24rq4meqoogtkfbzpzt.streamlit.app/")
    st.link_button("🎤 Whisper AI Transcriber", "https://myvideosummarizer-g5xpetuztm8zfowruaeutm.streamlit.app/")
    st.link_button("🎨 Gemini AI Image Generator", "https://gemini-image-generator-bdyowfxxqb4q5htbrrgjzv.streamlit.app/")
    st.link_button("🤖 Multi-Agent Chatbot", "https://multi-agent-chatbot-yv35yj5g7obpbibcxnwrme.streamlit.app/")
    st.link_button("🖼️ Photo Background Changer", "https://photo-bg-changer-kdrxyvhjx3ibr4ccoddm3f.streamlit.app/")
    st.link_button("🛠️ AI Super Tool (All-in-One)", "https://ai-super-tool-uxhxpvn4lqyc7szmsdqtl8.streamlit.app/")
    st.link_button("🩺 Heart Failure Risk Predictor", "https://heartfailure-gaufwbwfmh2j2u8ytzfmm5.streamlit.app/")

st.write("---")

# Certifications & Achievements Section
st.header("🏆 Key Achievements")
acc1, acc2 = st.columns(2)
with acc1:
    st.write("🥇 Kaggle Bronze Medal: Santa 2024 Puzzle Challenge")
    st.write("🥇 Kaggle Bronze Medal: Predict Podcast Listening Time")
with acc2:
    st.write("🛰️ ISRO Certified: AI/ML for Geodata Analysis")
    st.write("🧠 ExcelR: Data Science & AI Masterclass")

st.info("💡 Recruiter Tip: These apps are live deployments. Click any button to interact with the models and data engines immediately.")
