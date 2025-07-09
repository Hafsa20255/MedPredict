import streamlit as st
from PIL import Image
import pandas as pd
import time
import base64

# --- Configuration de la page ---
st.set_page_config(
    page_title="MedPredict - Predictive Maintenance",
    page_icon="🔬",
    layout="wide"
)

# --- Bande bleue supérieure (Header) ---
st.markdown("""
<div style='background-color:#1A237E; padding:20px; border-radius:10px; text-align:center;'>
    <h1 style='color:white; font-size:48px;'>MedPredict</h1>
    <p style='color:white; font-size:20px;'>Upload logs and manuals to predict failures and get recommended actions</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # espace

# --- Section image + formulaire ---
col1, col2 = st.columns([1, 2])

with col1:
    image = Image.open("banner.png")  # ton image banner ici
    st.image(image, use_column_width=True, caption="Predictive Maintenance in Action")

with col2:
    st.markdown("### Enter Equipment Information")
    equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    company = st.text_input("Company", placeholder="e.g., Leica")
    model = st.text_input("Model", placeholder="e.g., Provido")

# --- Upload des fichiers ---
st.markdown("### Upload Files")
uploaded_logs = st.file_uploader("Upload equipment log file (.xlsx)", type=["xlsx"])
uploaded_manual = st.file_uploader("Upload technical manual (PDF)", type=["pdf"])

# --- Bouton de prédiction ---
if st.button("Run Prediction"):
    with st.spinner("Analyzing data and generating insights..."):
        time.sleep(3)  # Simulation d'un traitement
        st.success("Predictions generated successfully!")
        st.markdown("Download your predictive maintenance report below:")
        st.download_button(
            label="📥 Download Report",
            data="Report content would be here...",
            file_name=f"{equipment_name}_{model}_report.csv",
            mime="text/csv"
        )

# --- Footer moderne ---
st.markdown("""
<hr style="border: 1px solid #1A237E;">
<div style='background-color:#1A237E; color:white; padding:10px; text-align:center; border-radius:8px;'>
    MedPredict © 2025 | Empowering Biomedical Maintenance with AI
</div>
""", unsafe_allow_html=True)


        with open(file_name, 'rb') as f:
            st.download_button("💾 Download Predictions", data=f, file_name=file_name, mime='text/csv')

# Fermer les divs HTML
st.markdown('</div></div>', unsafe_allow_html=True)
