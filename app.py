import streamlit as st
from PIL import Image

# Config de la page
st.set_page_config(
    page_title="MedPredict",
    page_icon="logo.png",  # favicon
    layout="centered"
)

# 🌟 Bande bleue foncée pleine largeur
st.markdown(
    """
    <style>
        .full-width-header {
            background-color: #003366;
            height: 120px; /* Plus grand pour donner plus d'espace */
            width: 100%;
            margin: 0;
            padding: 0;
        }
        .logo-container {
            text-align: center;
            margin-top: -60px; /* Fait dépasser le logo de la bande */
        }
    </style>
    <div class="full-width-header"></div>
    """,
    unsafe_allow_html=True
)

# ✅ Logo (posé en dessous de la bande bleue)
st.markdown(
    """
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/Hafsa20255/MedPredict/main/logo.png" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

# Titre
st.markdown("<h1 style='text-align: center; color: #333333;'>MedPredict - Maintenance Prédictive</h1>", unsafe_allow_html=True)

st.write("Bienvenue sur votre application de maintenance prédictive.")

# 📋 Champs pour informations sur l'équipement avec exemples
st.header("📝 Equipment Information")
equipment_name = st.text_input("Equipment Name", placeholder="Surgical Microscope")
company = st.text_input("Company", placeholder="Leica")
model = st.text_input("Model", placeholder="Provido")

# 📂 Upload des fichiers
st.header("📂 Upload Files")
log_file = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
manual_file = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

# ✔️ Vérification upload et informations
if st.button("Submit"):
    if equipment_name and company and model and log_file and manual_file:
        st.success("✅ All information and files submitted successfully!")
        st.write("### 📌 Summary:")
        st.write(f"**Equipment Name:** {equipment_name}")
        st.write(f"**Company:** {company}")
        st.write(f"**Model:** {model}")
    else:
        st.error("❌ Please fill in all fields and upload both files.")

# Footer
st.markdown(
    """
    <hr style="border:1px solid #f0f0f0">
    <div style="text-align: center; color: #888888; font-size: 14px;">
        © MedPredict 2025 - Tous droits réservés
    </div>
    """,
    unsafe_allow_html=True
)

