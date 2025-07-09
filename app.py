import streamlit as st
import pandas as pd
import joblib
import time

# Bande bleue en haut
st.markdown("""
    <div style='background-color:#1A237E; padding:15px; border-radius:10px;'>
        <h1 style='color:white; text-align:center;'>MedPredict</h1>
        <p style='color:white; text-align:center;'>AI-powered predictive maintenance for medical equipment</p>
    </div>
""", unsafe_allow_html=True)

# GIF animé d’alerte
def animated_alert():
    alert_html = """
        <div style='text-align:center; margin-top:20px;'>
            <img src="https://media.giphy.com/media/3o7btMCltyDvSgF92E/giphy.gif" alt="Alert GIF" width="300">
        </div>
    """
    st.markdown(alert_html, unsafe_allow_html=True)

# Jouer le son d’alarme
def play_alarm_sound():
    sound_html = """
        <audio autoplay>
            <source src="alarm.mp3" type="audio/mpeg">
        </audio>
    """
    st.markdown(sound_html, unsafe_allow_html=True)

# Saisie des infos de l’équipement
st.subheader("Enter Equipment Details")
equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
company = st.text_input("Company", placeholder="e.g., Leica")
model = st.text_input("Model", placeholder="e.g., Provido")

# Upload des fichiers
st.subheader("Upload Files")
log_file = st.file_uploader("Upload the equipment log file (.xlsx)", type=["xlsx"])
manual_file = st.file_uploader("Upload the technical manual (.pdf)", type=["pdf"])

# Chargement du modèle et scaler
model_file = "modele_pfe.pkl"
scaler_file = "scaler_pfe.pkl"
model_loaded = joblib.load(model_file)
scaler_loaded = joblib.load(scaler_file)

# Analyse et prédiction
if log_file is not None and manual_file is not None:
    st.success("Files uploaded successfully. Ready to predict.")
    data = pd.read_excel(log_file)
    scaled_data = scaler_loaded.transform(data)
    predictions = model_loaded.predict(scaled_data)

    # Résultats
    result_df = data.copy()
    result_df['Prediction'] = predictions
    file_name = f"{equipment_name}_{company}_{model}_Predictions.xlsx".replace(" ", "_")
    result_df.to_excel(file_name, index=False)
    st.download_button("Download Prediction Results", data=open(file_name, "rb"), file_name=file_name)

    # Si panne détectée
    if 1 in predictions:
        st.error("⚠️ Failure predicted! Immediate action required.")
        animated_alert()
        play_alarm_sound()
        st.warning("Technician should refer to the technical manual for maintenance steps.")
    else:
        st.success("✅ No failure predicted. Equipment is operating normally.")

# Footer moderne
st.markdown("""
    <hr style='border:1px solid #1A237E'>
    <p style='text-align:center; color:gray;'>MedPredict © 2025 | Empowering Biomedical Maintenance with AI</p>
""", unsafe_allow_html=True)
