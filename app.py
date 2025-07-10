import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="MedPredict - Predictive Maintenance",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- CUSTOM CSS ----
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
    <div class="header-card">
        <img src="logo.png" width="60" style="vertical-align: middle; margin-right:10px;">
        <span class="header-title">MedPredict</span>
        <p class="header-subtitle">AI-powered predictive maintenance for medical devices</p>
    </div>
""", unsafe_allow_html=True)

# ---- MAIN LAYOUT ----
left_col, right_col = st.columns(2, gap="large")

# ---- LEFT: DASHBOARD ----
with left_col:
    st.markdown("""
        <div class="dashboard-card">
            <h2>📊 Dashboard Stats</h2>
            <p><strong>Devices Monitored:</strong> 127</p>
            <p><strong>Predictions Made:</strong> 452</p>
            <p><strong>Accuracy:</strong> 96.7%</p>
            <p><strong>Alerts Triggered:</strong> 23</p>
        </div>
    """, unsafe_allow_html=True)

# ---- RIGHT: UPLOAD + FORM ----
with right_col:
    st.markdown("""
        <div class="upload-card">
            <h2>📥 Upload logs and technical manual to get predictive insights</h2>
        </div>
    """, unsafe_allow_html=True)

    equipment_name = st.text_input("Equipment Name", placeholder="e.g., Surgical Microscope")
    company = st.text_input("Company", placeholder="e.g., Leica")
    model = st.text_input("Model", placeholder="e.g., Provido")
    log_file = st.file_uploader("Upload Logs (Excel .xlsx)", type=["xlsx"])
    manual_file = st.file_uploader("Upload Technical Manual (PDF)", type=["pdf"])

    if st.button("🔍 Analyze"):
        if log_file and manual_file:
            st.success("✅ Analysis complete! Download the recommendations.")
            # Ici on peut générer ou simuler un fichier
            with open("recommendations.pdf", "rb") as f:
                st.download_button("📥 Download Recommendations", f, file_name="recommendations.pdf")
        else:
            st.error("⚠️ Please upload both the log file and the technical manual.")

# ---- FOOTER ----
st.markdown("""
    <div class="footer">
        MedPredict © 2025 | Empowering Biomedical Maintenance with AI
    </div>
""", unsafe_allow_html=True)
