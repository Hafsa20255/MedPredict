import streamlit as st
from datetime import datetime
import base64

# Inject custom CSS directly
st.markdown("""
<style>
/* Background */
body, .stApp {
    background-color: #0D47A1; /* Bleu foncé */
    color: #FFFFFF;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Header Card */
.header {
    background-color: #FFFFFF;
    color: #0D47A1;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    display: flex;
    align-items: center;
}

/* Logo in header */
.header img {
    height: 60px;
    margin-right: 15px;
}

/* Dashboard Card */
.dashboard {
    background-color: #FFFFFF;
    color: #0D47A1;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}

/* Upload Card */
.upload {
    background-color: #FFFFFF;
    color: #0D47A1;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}

/* Input labels */
label {
    color: #FFFFFF;
    font-weight: bold;
}

/* Footer */
footer {
    background-color: #0D47A1;
    color: #FFFFFF;
    text-align: center;
    padding: 10px;
    margin-top: 30px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# App Title with Logo
st.markdown("""
<div class="header">
    <img src="logo.png" alt="MedPredict Logo">
    <div>
        <h1 style="margin:0;">MedPredict</h1>
        <p style="margin:0;">AI-powered predictive maintenance for medical devices</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Dashboard & Upload layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="dashboard">
        <h3>📊 Dashboard Stats</h3>
        <p><strong>Devices Monitored:</strong> 127</p>
        <p><strong>Predictions Made:</strong> 452</p>
        <p><strong>Accuracy:</strong> 96.7%</p>
        <p><strong>Alerts Triggered:</strong> 23</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="upload">
        <h3>📥 Upload logs and technical manual to get predictive insights</h3>
    </div>
    """, unsafe_allow_html=True)

    equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    company = st.text_input("Company", placeholder="e.g., Leica")
    model = st.text_input("Model", placeholder="e.g., Provido")

    uploaded_logs = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
    uploaded_manual = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

    if st.button("Generate Report"):
        st.success("Report generated successfully!")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{equipment_name}_{model}_report_{timestamp}.pdf"
        st.download_button("Download Report", "Your report content here...", file_name=filename)

# Footer
st.markdown("""
<footer>
    MedPredict © 2025 – Empowering Biomedical Maintenance with AI
</footer>
""", unsafe_allow_html=True)
