
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Charger le modèle et le scaler
model = joblib.load('modele_pfe.pkl')
scaler = joblib.load('scaler_pfe.pkl')

# Titre de l'application
st.title("🔬 MedPredict - Maintenance Prédictive des Équipements Médicaux")
st.subheader("Prédisez les pannes des dispositifs médicaux grâce à l'IA")

# Upload du fichier Excel
uploaded_file = st.file_uploader("📂 Upload un fichier Excel contenant les logs :", type=['xlsx'])

if uploaded_file is not None:
    # Lire le fichier
    df = pd.read_excel(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(df.head())

    # Prétraitement : supprimer les colonnes inutiles
    X = df.drop(columns=['Label', 'ID_événement'], errors='ignore')

    # Encoder les colonnes texte
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    if 'Module_concerné' in X.columns:
        X['Module_concerné'] = le.fit_transform(X['Module_concerné'])

    # Normaliser les données
    X_scaled = scaler.transform(X)

    # Prédire avec Random Forest
    predictions = model.predict(X_scaled)
    df['Prédiction'] = predictions

    # Afficher les résultats
    st.write("🔮 Résultats des prédictions :")
    st.dataframe(df)

    # Télécharger les résultats
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df)
    st.download_button("💾 Télécharger les résultats", data=csv, file_name='resultats_predictions.csv', mime='text/csv')

    # Rapport de classification
    if 'Label' in df.columns:
        y_true = df['Label']
        y_pred = df['Prédiction']
        st.subheader("📊 Rapport de classification")
        report = classification_report(y_true, y_pred, output_dict=True)
        st.dataframe(pd.DataFrame(report).transpose())

        # Matrice de confusion
        st.subheader("🔲 Matrice de confusion")
        cm = confusion_matrix(y_true, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_xlabel('Prédit')
        ax.set_ylabel('Réel')
        st.pyplot(fig)
