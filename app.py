import streamlit as st
import pandas as pd
import base64

# ----- Page config -----
st.set_page_config(page_title="MedPredict", layout="wide")

# ----- Custom CSS -----
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----- Header -----
st.markdown("""
<div class="header">
    <img src="https://raw.githubusercontent.com/votre_username/votre_repo/main/logo.png" class="logo">
    <div class="header-text">
        <h1>MedPredict</h1>
        <p>AI-powered predictive maintenance for medical devices</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ----- Main content -----
col1, col2 = st.columns([1, 2])  # Colonne gauche = stats / droite = inputs

# LEFT COLUMN (Stats Dashboard)
with col1:
    st.markdown("""
    <div class="stats-card">
        <h3>📊 Dashboard Stats</h3>
        <ul>
            <li><b>Devices Monitored:</b> 127</li>
            <li><b>Predictions Made:</b> 452</li>
            <li><b>Accuracy:</b> 96.7%</li>
            <li><b>Alerts Triggered:</b> 23</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# RIGHT COLUMN (Inputs)
with col2:
    st.markdown("<div class='instruction'>📥 Upload logs and technical manual to get predictive insights</div>", unsafe_allow_html=True)

    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
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
    <p> MedPredict © 2025 • Empowering Biomedical Maintenance with AI.</p>
</div>
""", unsafe_allow_html=True)
