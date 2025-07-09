
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import fitz  # PyMuPDF
import time
import base64
from sklearn.preprocessing import LabelEncoder

# Configuration de la page Streamlit avec le logo MedPredict
st.set_page_config(
    page_title="MedPredict",
    page_icon="logo.png",  # Utilise le logo actuel
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre et description
st.markup("""
<div style='background-color:#1A237E; padding:15px; border-radius:10px;'>
    <h1 style='color:white; text-align:center;'>MedPredict</h1>
    <p style='color:white; text-align:center;'>AI-powered predictive maintenance for medical equipment</p>
</div>
""", unsafe_allow_html=True)
st.title("AI-powered Predictive Maintenance")

st.markdown(
    "Upload the equipment logs and technical manual to get predictive maintenance results and actionable recommendations."
)

# Charger le modèle et le scaler
model = joblib.load('modele_pfe.pkl')
scaler = joblib.load('scaler_pfe.pkl')

# Lire le manuel technique PDF et extraire des actions recommandées
def extract_actions_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    actions = {}
    for page in doc:
        text = page.get_text()
        lines = text.split('\n')
        for line in lines:
            if ':' in line:
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key, value = parts
                    actions[key.strip().lower()] = value.strip()
    return actions

# Fonction pour jouer un son MP3
def play_sound_mp3(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    md = f'''
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    '''
    st.markdown(md, unsafe_allow_html=True)

# Saisie des informations sur l'équipement
equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
company = st.text_input("Company", placeholder="e.g., Leica")
model_name = st.text_input("Model", placeholder="e.g., Provido")

# Upload des fichiers
uploaded_logs = st.file_uploader("📂 Upload a log file (Excel format):", type=['xlsx'])
uploaded_manual = st.file_uploader("📖 Upload the technical manual (PDF format):", type=['pdf'])

if uploaded_logs and uploaded_manual and equipment_name and company and model_name:
    st.success("✅ All inputs provided. Ready to process.")

    if st.button("🔮 Predict"):
        # Lire les logs
        df = pd.read_excel(uploaded_logs)

        # Prétraitement des données
        X = df.drop(columns=['Label', 'ID_événement'], errors='ignore')
        le = LabelEncoder()
        if 'Module_concerné' in X.columns:
            X['Module_concerné'] = le.fit_transform(X['Module_concerné'])
        X_scaled = scaler.transform(X)

        # Prédiction
        predictions = model.predict(X_scaled)
        df['Prediction'] = predictions

        # Extraction des actions recommandées
        st.info("📖 Extracting recommended actions from manual...")
        recommended_actions = extract_actions_from_pdf(uploaded_manual)
        df['Recommended Action'] = df['Prediction'].apply(
            lambda x: recommended_actions.get(str(x).lower(), "No action found in manual.")
        )

        # Vérifier si panne critique et lancer alerte
        if 1 in predictions:  # suppose que 1 = panne critique
            st.error("⚠️ Critical failure predicted! Intervention needed within 30 minutes.")
            play_sound_mp3('alarm.mp3')

        # Génération du nom de fichier intelligent
        file_name = f"{company}_{model_name}_{equipment_name}_predictions.csv".replace(' ', '_')
        df.to_csv(file_name, index=False)
        st.success(f"📥 File generated: {file_name}")

        with open(file_name, 'rb') as f:
            st.download_button("💾 Download Predictions", data=f, file_name=file_name, mime='text/csv')
