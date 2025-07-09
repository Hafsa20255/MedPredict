import streamlit as st
import pandas as pd
import joblib
import time

# --------- CONFIGURATION PAGE ---------
st.set_page_config(
    page_title="MedPredict - Predictive Maintenance",
    page_icon="logo.png",  # Ton logo ici
    layout="wide"
)

# --------- CSS MATERIAL DESIGN ---------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
        background-color: #F5F7FA;
    }

    .main-header {
        background: linear-gradient(90deg, #1A237E 0%, #3949AB 100%);
        padding: 20px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    .main-header img {
        height: 50px;
        margin-right: 15px;
    }

    .main-header h1 {
        font-size: 2.5rem;
        margin: 0;
    }

    .card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .btn-primary {
        background-color: #3949AB;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 6px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .btn-primary:hover {
        background-color: #303F9F;
    }

    .alert {
        background-color: #FF5252;
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# --------- HEADER ---------
st.markdown("""
    <div class="main-header">
        <img src="https://raw.githubusercontent.com/hafsa20205/MedPredict/main/logo.png" alt="MedPredict Logo">
        <h1>MedPredict</h1>
    </div>
""", unsafe_allow_html=True)

# --------- FORMULAIRE (dans une carte) ---------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Upload Equipment Information")
equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
company = st.text_input("Company", placeholder="e.g., Leica")
model = st.text_input("Model", placeholder="e.g., Provido")
log_file = st.file_uploader("Upload Equipment Logs (.xlsx)", type=['xlsx'])
manual_file = st.file_uploader("Upload Technical Manual (PDF)", type=['pdf'])

st.markdown('</div>', unsafe_allow_html=True)

# --------- PREDICTION BUTTON (stylé) ---------
if st.button("Run Prediction", key="predict_btn", help="Click to analyze and predict failures"):
    if log_file and manual_file:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.success("Files uploaded successfully. Processing...")
        time.sleep(2)  # Simule un délai de traitement

        # Load Model
        model_loaded = joblib.load('modele_pfe.pkl')
        scaler_loaded = joblib.load('scaler_pfe.pkl')

        data = pd.read_excel(log_file)
        scaled_data = scaler_loaded.transform(data)
        predictions = model_loaded.predict(scaled_data)

        # Results
        result_df = data.copy()
        result_df['Prediction'] = predictions
        file_name = f"{equipment_name}_{company}_{model}_Predictions.xlsx".replace(" ", "_")
        result_df.to_excel(file_name, index=False)
        st.download_button("📥 Download Prediction Results", data=open(file_name, "rb"), file_name=file_name)

        # Alert if failure predicted
        if 1 in predictions:
            st.markdown('<div class="alert">🚨 Critical Failure Predicted! Immediate Action Required.</div>', unsafe_allow_html=True)
            st.markdown("""
                <audio autoplay>
                    <source src="alarm.mp3" type="audio/mpeg">
                </audio>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div style='text-align:center;'>
                    <img src="https://media.giphy.com/media/3o7btMCltyDvSgF92E/giphy.gif" alt="Alert GIF" width="300">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.success("✅ No failure predicted. Equipment is operating normally.")

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("⚠️ Please upload both the logs and the technical manual.")

# --------- FOOTER ---------
st.markdown("""
    <hr style='border:1px solid #1A237E'>
    <p style='text-align:center; color:#777;'>MedPredict © 2025 | Empowering Biomedical Maintenance with AI</p>
""", unsafe_allow_html=True)
