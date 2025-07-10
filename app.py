import streamlit as st
from PIL import Image
import base64
import time
import pandas as pd

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="MedPredict - Predictive Maintenance",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- CUSTOM CSS ----
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- HEADER ----
col1, col2 = st.columns([1, 5])
with col1:
    st.image("medpredict_logo.png", width=80)
with col2:
    st.markdown("""
        <div class="header-card">
            <h1>MedPredict</h1>
            <p>AI-powered predictive maintenance for medical devices</p>
        </div>
    """, unsafe_allow_html=True)

# ---- MAIN LAYOUT ----
left_col, right_col = st.columns(2, gap="large")

# ---- LEFT: DASHBOARD ----
with left_col:
    st.markdown("""
        <div class="dashboard-card">
            <h2>📊 Dashboard Stats</h2>
            <p><strong>Devices Monitored:</strong> 127</p>
            <p><strong>Predictions Made:</strong> 452</p>
            <p><strong>Accuracy:</strong> 96.7%</p>
            <p><strong>Alerts Triggered:</strong> 23</p>
        </div>
    """, unsafe_allow_html=True)

# ---- RIGHT: UPLOAD + FORM ----
with right_col:
    st.markdown("""
        <div class="upload-card">
            <h2>📥 Upload logs and technical manual to get predictive insights</h2>
        </div>
    """, unsafe_allow_html=True)

    equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    company = st.text_input("Company", placeholder="e.g., Leica")
    model = st.text_input("Model", placeholder="e.g., Provido")
    log_file = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
    manual_file = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

    if st.button("🔍 Analyze"):
        if log_file and manual_file:
            st.success("✅ Analysis complete! Download the recommendations.")
            with open("recommendations.pdf", "rb") as f:
                btn = st.download_button("📥 Download Recommendations", f, file_name="recommendations.pdf")
        else:
            st.error("⚠️ Please upload both the log file and the technical manual.")

# ---- FOOTER ----
st.markdown("""
    <div class="footer">
        MedPredict © 2025 | Empowering Biomedical Maintenance with AI
    </div>
""", unsafe_allow_html=True)

