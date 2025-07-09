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

# CSS externe Material Design
def load_css():
    css_url = "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"
    st.markdown(f'<link href="{css_url}" rel="stylesheet">', unsafe_allow_html=True)

load_css()

# Header avec logo
st.markdown("""
<div style="background: linear-gradient(90deg, #1a237e, #3949ab); padding: 20px; border-radius: 8px; display: flex; align-items: center;">
    <img src="https://raw.githubusercontent.com/hafsa20255/MedPredict/main/logo.png" alt="MedPredict Logo" style="height:60px; margin-right:20px;">
    <div>
        <h1 style="color:white; margin:0;">MedPredict</h1>
        <p style="color:white; margin:0;">AI-powered predictive maintenance for medical devices</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Formulaire d'informations sur l'équipement
st.header("📋 Upload Equipment Information")
equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
company = st.text_input("Company", placeholder="e.g., Leica")
model = st.text_input("Model", placeholder="e.g., M530 OHX")

# Upload des fichiers
st.header("📂 Upload Files")
logs_file = st.file_uploader("Upload Logs (.csv or .xlsx)", type=["csv", "xlsx"])
manual_file = st.file_uploader("Upload Technical Manual (.pdf)", type=["pdf"])

# Bouton pour lancer la prédiction
if st.button("Run Prediction"):
    if logs_file and manual_file:
        # Simuler un temps de traitement
        with st.spinner("Analyzing data and generating predictions..."):
            time.sleep(3)  # Simuler un délai
        st.success("✅ Predictions generated successfully!")
        
        # Afficher un mini tableau de résultats simulés
        result_df = pd.DataFrame({
            "Component": ["Power Supply", "Motor", "Camera"],
            "Failure Probability": ["85%", "40%", "20%"],
            "Recommended Action": ["Replace power unit", "Inspect motor bearings", "Calibrate camera"]
        })
        st.subheader("📊 Prediction Results")
        st.dataframe(result_df)

        # Télécharger le rapport
        csv = result_df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{equipment_name}_{model}_report.csv">📥 Download Report</a>'
        st.markdown(href, unsafe_allow_html=True)

        # Déclencher une alarme sonore
        st.audio("https://raw.githubusercontent.com/hafsa20255/MedPredict/main/alarm.mp3", format="audio/mp3")
    else:
        st.error("⚠️ Please upload both the logs and the technical manual.")

# Footer moderne
st.markdown("""
<hr style="border:1px solid #ccc;">
<p style="text-align:center; color:#888;">
    MedPredict © 2025 • Empowering Biomedical Maintenance with AI
</p>
""", unsafe_allow_html=True)
