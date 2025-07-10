import streamlit as st
from PIL import Image

# Config de la page avec ton logo en favicon
st.set_page_config(
    page_title="MedPredict",
    page_icon="logo.png",
    layout="centered"
)

# Afficher le logo et le titre
logo = Image.open("logo.png")
st.image(logo, width=150)
st.title("MedPredict - Maintenance Prédictive")

st.write("Bienvenue sur votre application de maintenance prédictive.")

# 📋 Champs pour informations sur l'équipement
st.header("📝 Equipment Information")
equipment_name = st.text_input("Equipment Name")
company = st.text_input("Company")
model = st.text_input("Model")

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
        MedPredict © 2025 - Empowering Biomedical Maintenance with AI
    </div>
    """,
    unsafe_allow_html=True
)
