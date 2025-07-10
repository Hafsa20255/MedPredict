import streamlit as st
from PIL import Image

# Config de la page avec ton logo en favicon
st.set_page_config(
    page_title="MedPredict",
    page_icon="logo.png",  # ton logo ici
    layout="centered"
)

# Appliquer le CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Afficher le logo et le titre
logo = Image.open("logo.png")
st.image(logo, width=150)
st.title("MedPredict - Maintenance Prédictive")

st.write("Bienvenue sur votre application de maintenance prédictive.")

# Upload des fichiers
st.header("📂 Upload des fichiers")
log_file = st.file_uploader("Uploader les logs (Excel .xlsx)", type=["xlsx"])
manual_file = st.file_uploader("Uploader le manuel technique (PDF)", type=["pdf"])

# Vérification upload
if log_file is not None:
    st.success("✅ Fichier de logs chargé avec succès.")

if manual_file is not None:
    st.success("✅ Manuel technique chargé avec succès.")

# Bouton pour analyser
if st.button("Analyser"):
    if log_file is not None and manual_file is not None:
        st.info("📊 Analyse en cours... (fonctionnalité à ajouter)")
    else:
        st.error("❌ Veuillez uploader les deux fichiers.")

# Footer
st.markdown(
    """
    <hr style="border:1px solid #f0f0f0">
    <div style="text-align: center; color: #888888; font-size: 14px;">
        MedPredict © 2025 - Empowering Biomedical Maintenance with AI
    </div>
    """,
    unsafe_allow_html=True
)
