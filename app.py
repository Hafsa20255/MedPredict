import streamlit as st
import pandas as pd
import time
import base64
from datetime import timedelta

# Configuration générale
st.set_page_config(
    page_title="MedPredict",
    page_icon="https://raw.githubusercontent.com/hafsa20255/MedPredict/main/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Charger le style externe
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# Header avec logo
st.markdown("""
<div class="header">
    <img src="https://raw.githubusercontent.com/hafsa20255/MedPredict/main/logo.png" alt="MedPredict Logo" class="logo">
    <div class="title">
        <h1>MedPredict</h1>
        <p>AI-powered predictive maintenance for medical devices</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Formulaire d'informations sur l'équipement
st.subheader("📋 Upload Equipment Information")
equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
company = st.text_input("Company", placeholder="e.g., Leica")
model = st.text_input("Model", placeholder="e.g., M530 OHX")

# Upload des fichiers
st.subheader("📂 Upload Files")
logs_file = st.file_uploader("Upload Logs (.csv or .xlsx)", type=["csv", "xlsx"])
manual_file = st.file_uploader("Upload Technical Manual (.pdf)", type=["pdf"])

# Bouton pour lancer la prédiction
if st.button("🔮 Run Prediction"):
    if logs_file and manual_file:
        with st.spinner("🔄 Analyzing data and generating predictions..."):
            time.sleep(3)
        st.success("✅ Predictions generated successfully!")

        # Mini tableau de résultats
        result_df = pd.DataFrame({
            "Component": ["Power Supply", "Motor", "Camera"],
            "Failure Probability": ["85%", "40%", "20%"],
            "Recommended Action": ["Replace power unit", "Inspect motor bearings", "Calibrate camera"]
        })
        st.subheader("📊 Prediction Results")
        st.dataframe(result_df, use_container_width=True)

        # Télécharger le rapport
        csv = result_df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{equipment_name}_{model}_report.csv" class="download-btn">📥 Download Report</a>'
        st.markdown(href, unsafe_allow_html=True)

        # Alarme sonore
        st.audio("https://raw.githubusercontent.com/hafsa20255/MedPredict/main/alarm.mp3", format="audio/mp3")
    else:
        st.error("⚠️ Please upload both the logs and the technical manual.")

# Footer
st.markdown("""
<div class="footer">
    MedPredict © 2025 • Empowering Biomedical Maintenance with AI
</div>
""", unsafe_allow_html=True)
