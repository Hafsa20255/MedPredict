import streamlit as st
from PIL import Image

# Charger le logo
logo = Image.open("logo.png")

# Page config
st.set_page_config(page_title="MedPredict",
                   page_icon="logo.png",
                   layout="wide")

# Charger le CSS externe
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <img src="logo.png" class="logo">
    <h1>MedPredict</h1>
    <p>AI-powered predictive maintenance for medical devices</p>
</div>
""", unsafe_allow_html=True)

# Layout : Dashboard + Upload
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="card">
        <h2>📊 Dashboard Stats</h2>
        <p><strong>Devices Monitored:</strong> 127</p>
        <p><strong>Predictions Made:</strong> 452</p>
        <p><strong>Accuracy:</strong> 96.7%</p>
        <p><strong>Alerts Triggered:</strong> 23</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>📥 Upload logs and technical manual to get predictive insights</h2>
    </div>
    """, unsafe_allow_html=True)

    # Formulaire d’entrée
    equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    company = st.text_input("Company", placeholder="e.g., Leica")
    model = st.text_input("Model", placeholder="e.g., Provido")

    # Upload des fichiers
    uploaded_logs = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
    uploaded_manual = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

    if st.button("🔮 Predict"):
        if uploaded_logs and uploaded_manual:
            st.success("Prediction complete! Report generated.")
        else:
            st.warning("Please upload both logs and technical manual.")

# Footer
st.markdown("""
<div class="footer">
    MedPredict © 2025 – Empowering Biomedical Maintenance with AI
</div>
""", unsafe_allow_html=True)
