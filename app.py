import streamlit as st
from PIL import Image
import pandas as pd
import pypdf
import base64
from io import BytesIO

# 🎨 Config de la page
st.set_page_config(
    page_title="MedPredict",
    page_icon="logo.png",
    layout="centered"
)

# 🌸 Bande pleine largeur + logo à gauche
st.markdown(
    """
    <style>
        .header {
            background-color: #fcf5fc; /* couleur personnalisée */
            height: 200px;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            width: 100vw; /* pleine largeur */
            z-index: -1;
        }
        .logo-container {
            margin-top: 120px;
            margin-left: 30px;
        }
    </style>
    <div class="header"></div>
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/Hafsa20255/MedPredict/main/logo.png" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

# 🏷️ Titre
st.markdown("<h1 style='text-align: center; color: #333333; margin-top:220px;'>MedPredict - Maintenance Prédictive</h1>", unsafe_allow_html=True)
st.write("Bienvenue sur votre application de maintenance prédictive.")

# 📋 Champs informations
equipment_name = st.text_input("Equipment Name", placeholder="Surgical Microscope")
company = st.text_input("Company", placeholder="Leica")
model = st.text_input("Model", placeholder="Provido")

# 📂 Upload fichiers
log_file = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
manual_file = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

# 📑 Lire PDF pour Actions Recommandées
def extract_actions_from_pdf(pdf_file):
    actions = {}
    reader = pypdf.PdfReader(pdf_file)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            for line in text.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    actions[key.strip()] = value.strip()
    return actions

# 📥 Télécharger dataframe en Excel
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Results')
        writer.save()
    processed_data = output.getvalue()
    return processed_data

# 🚀 Bouton Submit (sans modèle)
if st.button("Submit"):
    if equipment_name and company and model and log_file and manual_file:
        st.success("✅ Informations et fichiers chargés avec succès.")

        try:
            # 📊 Lire fichier Excel
            data = pd.read_excel(log_file)
            st.write("✅ Données chargées :")
            st.dataframe(data.head())

            # 📑 Actions recommandées
            actions = extract_actions_from_pdf(manual_file)
            data['Recommended Action'] = "Example action here"  # Placeholder

            st.write("### 🔥 Résultat (sans prédiction) :")
            st.dataframe(data)

            # 📥 Bouton téléchargement Excel
            excel_data = to_excel(data)
            st.download_button(
                label="📥 Download Result as Excel",
                data=excel_data,
                file_name="medpredict_results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"❌ Erreur lors de l’analyse : {e}")

    else:
        st.error("❌ Veuillez remplir tous les champs et uploader les deux fichiers.")
