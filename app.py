import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import StandardScaler

# Cargar modelo y escalador
modelo = joblib.load("modelo_carga_cognitiva.pkl")
scaler = joblib.load("escalador_eeg.pkl")

st.title("🧠 Detección de Carga Cognitiva en EEG")
st.markdown("Sube una **ventana de señal EEG** (2 segundos, 512 muestras × 16 canales) en formato `.csv` para predecir el nivel de carga cognitiva.")

uploaded_file = st.file_uploader("📤 Subir CSV de señal EEG", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        if df.shape != (512, 16):
            st.error(f"❌ El archivo debe tener exactamente 512 filas y 16 columnas. Tiene {df.shape}.")
        else:
            st.success("✅ Archivo válido.")

            # Extraer características
            def extraer_features(ventana):
                features = []
                for canal in range(ventana.shape[1]):
                    señal = ventana[:, canal]
                    features.extend([
                        np.mean(señal),
                        np.std(señal),
                        np.sum(señal**2),
                        pd.Series(señal).kurt(),
                        pd.Series(señal).skew()
                    ])
                return features

            ventana = df.values.astype("float32")
            features = np.array([extraer_features(ventana)])

            # Escalado y predicción
            features_scaled = scaler.transform(features)
            pred = modelo.predict(features_scaled)[0]
            prob = modelo.predict_proba(features_scaled)[0]

            label_map = {0: "baja", 1: "media", 2: "alta"}
            st.markdown(f"### 🧠 Nivel de carga cognitiva detectado: **{label_map[pred].capitalize()}**")
            st.bar_chart(pd.Series(prob, index=["Baja", "Media", "Alta"]))

    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
