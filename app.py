import streamlit as st
from datetime import datetime, timedelta
import base64
import time

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="MedPredict",
    page_icon="logo.png",  # Chemin vers ton logo
    layout="wide"
)

# ---- CUSTOM CSS ----
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
    <div class="header">
        <img src="https://raw.githubusercontent.com/hafsa20255/MedPredict/main/logo.png" class="logo">
        <div class="header-text">
            <h1>MedPredict</h1>
            <p>AI-powered predictive maintenance for medical devices</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---- LAYOUT ----
col1, col2 = st.columns([1, 2], gap="large")

# --- DASHBOARD STATS ---
with col1:
    st.markdown("""
        <div class="dashboard">
            <h3>📊 Dashboard Stats</h3>
            <ul>
                <li><b>Devices Monitored:</b> 127</li>
                <li><b>Predictions Made:</b> 452</li>
                <li><b>Accuracy:</b> 96.7%</li>
                <li><b>Alerts Triggered:</b> 23</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --- UPLOAD SECTION ---
with col2:
    st.markdown("""
        <div class="upload-section">
            <h3>📥 Upload logs and technical manual to get predictive insights</h3>
        </div>
    """, unsafe_allow_html=True)

    equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    company = st.text_input("Company", placeholder="e.g., Leica")
    model = st.text_input("Model", placeholder="e.g., Provido")
    log_file = st.file_uploader("Upload Logs (.xlsx)", type="xlsx")
    manual_file = st.file_uploader("Upload Technical Manual (.pdf)", type="pdf")

    if st.button("🔍 Predict Failures"):
        if log_file and manual_file:
            st.success("✅ Prediction completed. Download your report below:")
            st.download_button("📥 Download Report", "Report content here...", file_name=f"{equipment_name}_Prediction_Report.txt")
        else:
            st.error("⚠️ Please upload both log file and technical manual.")

# ---- ALERT SYSTEM ----
st.markdown("""
    <div class="footer">
        <p>🔔 Next scheduled check: <span id="timer">Loading...</span></p>
    </div>
""", unsafe_allow_html=True)

def start_timer(minutes):
    end_time = datetime.now() + timedelta(minutes=minutes)
    while datetime.now() < end_time:
        remaining = end_time - datetime.now()
        mins, secs = divmod(remaining.seconds, 60)
        timer_str = f"{mins:02d}:{secs:02d}"
        st.markdown(f"<script>document.getElementById('timer').innerText='{timer_str}';</script>", unsafe_allow_html=True)
        time.sleep(1)
    play_audio("alert.mp3")

def play_audio(file):
    audio_file = open(file, "rb")
    audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Uncomment this line to enable 30 min timer
# start_timer(30)
