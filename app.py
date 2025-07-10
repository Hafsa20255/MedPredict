import streamlit as st
import pandas as pd
from PIL import Image

# ----- Page Config -----
st.set_page_config(page_title="MedPredict", page_icon="logo.png", layout="wide")

# ----- Custom CSS -----
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----- Full Background -----
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1E3C72, #2A5298);
    color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# ----- Header with Logo -----
st.markdown("""
    <div style='background: linear-gradient(135deg, #1A237E, #283593);
                padding: 30px; border-radius: 10px; color: white; display: flex; align-items: center;'>
        <img src="https://raw.githubusercontent.com/TON_USERNAME/TON_REPO/main/logo.png"
             style='height:60px; margin-right:20px;'>
        <div>
            <h1 style='margin:0; font-size:2.5rem;'>MedPredict</h1>
            <p style='margin:0; font-size:1.2rem;'>AI-powered predictive maintenance for medical devices</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# ----- Main Content -----
col1, col2 = st.columns([1, 2], gap="large")

# ----- LEFT: Dashboard Stats -----
with col1:
    st.markdown("""
    <div class="card">
        <h3>📊 Dashboard</h3>
        <ul>
            <li><b>Devices Monitored:</b> 127</li>
            <li><b>Predictions Made:</b> 452</li>
            <li><b>Accuracy:</b> 96.7%</li>
            <li><b>Alerts Triggered:</b> 23</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ----- RIGHT: Upload & Inputs -----
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='instruction'>📥 Upload logs and technical manual to get predictive insights</p>", unsafe_allow_html=True)

    equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    company = st.text_input("Company", placeholder="e.g., Leica")
    model = st.text_input("Model", placeholder="e.g., Provido")

    uploaded_logs = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
    uploaded_manual = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

    if st.button("🔮 Predict Failures"):
        if uploaded_logs and uploaded_manual:
            st.success("Prediction completed! Download the report below.")
            st.download_button("📥 Download Report", "Simulated Report Content", file_name="medpredict_report.pdf")
        else:
            st.warning("Please upload both the logs and the technical manual.")
    st.markdown("</div>", unsafe_allow_html=True)

# ----- Footer -----
st.markdown("""
<div class="footer">
    <p> MedPredict © 2025 • Empowering Biomedical Maintenance with AI</p>
</div>
""", unsafe_allow_html=True)

