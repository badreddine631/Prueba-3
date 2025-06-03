# Prueba-3
# 🧠 Detección de Carga Cognitiva a partir de señales EEG

Este proyecto utiliza señales EEG recogidas durante la realización del test **n-Back** para predecir el nivel de carga cognitiva de un participante. El sistema incluye desde la carga de datos crudos hasta la visualización de resultados y una demo interactiva con Streamlit.

---

## 📂 Estructura del Proyecto

├── Carga_datos/ # Lectura y limpieza de EEG + eventos
├── Extraccion_features/ # Ventaneo + estadísticas por canal
├── Modelos/ # Entrenamiento y evaluación de clasificadores
├── Visualizaciones/ # PCA, importancia, gráficos por canal
├── Streamlit_app/ # Demo interactiva en tiempo real
├── modelo_carga_cognitiva.pkl
├── escalador_eeg.pkl
├── ventana_demo.csv
└── README.md

---

## 📄 Datos utilizados

- **Participantes:** 19
- **Test:** n-Back (niveles 1, 2, 3)
- **Formato:** señales EEG con 16 canales a 256 Hz
- **Ventanas:** 512 muestras (2 segundos), con solapamiento del 50%

Cada ventana se etiquetó con una carga cognitiva:
- 🟠 **Baja** (`n=1`)
- 🟢 **Media** (`n=2`)
- 🔵 **Alta** (`n=3`)

---

## ⚙️ Extracción de características

Por cada ventana (512 × 16):

- Media
- Desviación estándar
- Energía
- Curtosis
- Asimetría

Total: **80 features** (16 canales × 5 estadísticas)

---

## 🤖 Modelos evaluados

| Modelo         | Accuracy Medio |
|----------------|----------------|
| ✅ XGBoost      | **44.65%**      |
| ✅ RandomForest | 43.95%         |
| ✅ MLP          | 39.51%         |
| ✅ SVM (RBF)    | 35.30%         |

> Se seleccionó **RandomForestClassifier** como modelo final por su robustez, rendimiento competitivo y facilidad de despliegue.

---

## 📊 Visualizaciones

- 🔍 PCA de señales EEG
- 🔥 Importancia de características (Random Forest)
- 📈 Distribución por canal
- 🧱 Matriz de confusión

Estas visualizaciones permiten entender mejor los patrones ocultos y la dificultad del problema.

---

## 🖥️ Demo interactiva con Streamlit

Una demo simple y funcional que permite:

- Subir un archivo `.csv` con una ventana de señal EEG (`512 × 16`)
- Calcular las características estadísticas
- Escalar los datos y predecir el nivel de carga cognitiva
- Mostrar las probabilidades por clase

### 📎 Archivos requeridos:

- `modelo_carga_cognitiva.pkl` – modelo final Random Forest
- `escalador_eeg.pkl` – StandardScaler usado en el entrenamiento
- `ventana_demo.csv` – ejemplo válido para pruebas

### ▶️ Ejecutar localmente

```bash
streamlit run app.py

Licencia
MIT © 2025 – Uso académico y demostrativo. No se recomienda para diagnóstico clínico.

Créditos
Este proyecto fue desarrollado como parte de la asignatura de Técnicas de Aprendizaje Automático y forma parte de una evaluación práctica sobre análisis de señales biomédicas.
