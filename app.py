import streamlit as st
from PIL import Image
import pandas as pd
import joblib
import PyPDF2
import datetime
import time
import base64
from io import BytesIO

# Config de la page
st.set_page_config(
    page_title="MedPredict",
    page_icon="logo.png",
    layout="centered"
)

# 🌸 Bande pleine largeur avec couleur personnalisée
st.markdown(
    """
    <style>
        .header {
            background-color: #fcf5fc; /* couleur personnalisée */
            height: 200px;
            width: 100%;
            position: relative;
        }
        .logo-container {
            position: absolute;
            top: 100px; /* fait dépasser le logo */
            left: 50px; /* aligné à gauche */
            z-index: 2;
        }
    </style>
    <div class="header"></div>
    <div class="logo-container">
        <img src="logo.png" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

# Titre
st.markdown("<h1 style='text-align: center; color: #333333;'>MedPredict - Maintenance Prédictive</h1>", unsafe_allow_html=True)
st.write("Bienvenue sur votre application de maintenance prédictive.")

# 📋 Champs informations
equipment_name = st.text_input("Equipment Name", placeholder="Surgical Microscope")
company = st.text_input("Company", placeholder="Leica")
model = st.text_input("Model", placeholder="Provido")

# 📂 Upload fichiers
log_file = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
manual_file = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

# Charger modèle et scaler
model_pfe = joblib.load("modele_pfe.pkl")
scaler_pfe = joblib.load("scaler_pfe.pkl")

# Lire PDF pour Actions Recommandées
def extract_actions_from_pdf(pdf_file):
    actions = {}
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            for line in text.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    actions[key.strip()] = value.strip()
    return actions

# Jouer son d'alarme
def play_alert():
    audio_file = open('alert.mp3', 'rb')
    audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
    <audio autoplay="true">
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

# Télécharger le dataframe en Excel
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Results')
        writer.save()
    processed_data = output.getvalue()
    return processed_data

# Bouton Submit
if st.button("Submit"):
    if equipment_name and company and model and log_file and manual_file:
        st.success("✅ Informations et fichiers chargés avec succès.")

        try:
            # Lire fichier Excel
            data = pd.read_excel(log_file)
            st.write("✅ Données chargées :")
            st.dataframe(data.head())

            # Prétraitement
            data_scaled = scaler_pfe.transform(data.select_dtypes(include=['float64', 'int64']))

            # Prédiction
            predictions = model_pfe.predict(data_scaled)
            data['Prediction'] = predictions

            # Actions recommandées
            actions = extract_actions_from_pdf(manual_file)
            data['Recommended Action'] = data['Prediction'].map(actions)

            st.write("### 🔥 Résultat avec Actions Recommandées :")
            st.dataframe(data)

            # Bouton de téléchargement
            excel_data = to_excel(data)
            st.download_button(
                label="📥 Download Result as Excel",
                data=excel_data,
                file_name="medpredict_results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            # Alerte sonore si panne détectée
            if "Failure" in predictions:
                st.warning("⚠️ Une panne est détectée ! Alerte dans 30 minutes...")
                time.sleep(1800)  # attendre 30 min réelles
                play_alert()

        except Exception as e:
            st.error(f"❌ Erreur lors de l’analyse : {e}")

    else:
        st.error("❌ Veuillez remplir tous les champs et uploader les deux fichiers.")
