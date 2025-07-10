import streamlit as st
import base64

# Configuration de la page
st.set_page_config(
    page_title="MedPredict",
    page_icon="🔬",
    layout="wide",
)

# Intégration du CSS Material Design
st.markdown("""
    <style>
    body {
        background-color: #0D47A1;
        color: #FFFFFF;
        font-family: 'Roboto', sans-serif;
    }
    .main {
        background-color: #0D47A1;
    }
    .card {
        background-color: #FFFFFF;
        color: #212121;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .upload-btn {
        background-color: #1565C0;
        color: #FFFFFF;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 16px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
        text-align: center;
    }
    .upload-btn:hover {
        background-color: #0D47A1;
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    }
    .footer {
        text-align: center;
        color: #FFFFFF;
        padding: 15px 0;
        margin-top: 40px;
        font-size: 14px;
    }
    .header-logo {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .header-logo img {
        height: 60px;
        margin-right: 15px;
    }
    h1, h2 {
        color: #FFFFFF;
    }
    label {
        color: #FFFFFF;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Affichage du header avec logo
logo_data = """
iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAB1klEQVR4nO3YwU3DMBCA4R2iwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAViwAVi9AU7lMP7N1sQ6lGtHNWz0XeAAAAABJRU5ErkJggg==
"""  # <-- ceci est une version raccourcie d’exemple. Je mettrai le vrai logo MedPredict complet pour toi.

st.markdown(f"""
<div class="header-logo">
    <img src="data:image/png;base64,{logo_data}">
    <h1>MedPredict</h1>
</div>
""", unsafe_allow_html=True)

# Dashboard Stats
with st.container():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📊 Dashboard Stats")
        st.markdown("**Devices Monitored:** 127")
        st.markdown("**Predictions Made:** 452")
        st.markdown("**Accuracy:** 96.7%")
        st.markdown("**Alerts Triggered:** 23")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📥 Upload logs and technical manual to get predictive insights")
        equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
        company = st.text_input("Company", placeholder="e.g., Leica")
        model = st.text_input("Model", placeholder="e.g., Provido")

        uploaded_logs = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"], label_visibility="visible")
        uploaded_manual = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"], label_visibility="visible")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    MedPredict © 2025 – Empowering Biomedical Maintenance with AI
</div>
""", unsafe_allow_html=True)
