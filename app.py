import streamlit as st

st.markdown("""
    <style>
        body {
            background-color: #0D1B2A; /* Bleu foncé élégant */
            color: #FFFFFF; /* Texte blanc */
        }
        .stApp {
            background-color: #0D1B2A; /* Appliquer au container principal */
        }
        .css-1d391kg {
            background-color: #FFFFFF; /* Cartes en blanc */
            color: #0D1B2A; /* Texte sombre pour lisibilité */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stTextInput > div > div > input {
            color: #0D1B2A; /* Texte dans les inputs */
            background-color: #FFFFFF; /* Inputs blancs */
        }
        .stFileUploader > div {
            background-color: #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)

# Config de la page
st.set_page_config(page_title="MedPredict",
                   page_icon="logo.png",
                   layout="wide")

# Header avec logo
st.markdown("""
<div class="header">
    <img src="logo.png" class="logo">
    <div>
        <h1>MedPredict</h1>
        <p>AI-powered predictive maintenance for medical devices</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Layout principal
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="card">
        <h2>📊 Dashboard Stats</h2>
        <p><strong>Devices Monitored:</strong> 127</p>
        <p><strong>Predictions Made:</strong> 452</p>
        <p><strong>Accuracy:</strong> 96.7%</p>
        <p><strong>Alerts Triggered:</strong> 23</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>📥 Upload logs and technical manual to get predictive insights</h2>
    </div>
    """, unsafe_allow_html=True)

    # Champs de saisie
    st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    st.text_input("Company", placeholder="e.g., Leica")
    st.text_input("Model", placeholder="e.g., Provido")

    # Upload de fichiers
    st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
    st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

    # Bouton
    st.button("🔮 Predict")

# Footer
st.markdown("""
<div class="footer">
    MedPredict © 2025 – Empowering Biomedical Maintenance with AI
</div>
""", unsafe_allow_html=True)
