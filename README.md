# 🌍 Sistema Predictivo y Ético de Calidad del Aire (PM2.5) en Quito

Este repositorio contiene el prototipo funcional de un sistema de análisis predictivo de datos socioambientales, enfocado en la medición de la contaminación por partículas finas (PM2.5) en la ciudad de Quito. El proyecto combina el análisis de datos históricos de la red gubernamental con Inteligencia Artificial y una profunda reflexión ética sobre la justicia ambiental.

## 📊 Hallazgos Clave del Proyecto
* **Justicia Ambiental:** El análisis de los datos históricos oficiales de la REMMAQ reveló que la estación de **El Camal** (al sur de la ciudad) registra la mayor concentración de material particulado, superando los 20 µg/m³.
* **Impacto Climático vs Humano:** El modelo de Machine Learning determinó que las variables climáticas solo explican el **1%** de la contaminación (R-cuadrado = 0.01), evidenciando que el 99% restante obedece a factores antropogénicos. Además, se aisló matemáticamente el impacto del viento, el cual reduce la contaminación en 1.36 puntos por cada m/s de incremento.

## 📌 Entregables del Proyecto
* **Notebook de Jupyter:** Análisis exploratorio, conexión a datos reales de la REMMAQ, generación de datos sintéticos y entrenamiento del modelo de Regresión Lineal Múltiple.
* **Script de Integración SQL (`integracion_db.py`):** Motor autocontenido en Python para el almacenamiento local de alertas ambientales y consultas usando SQLite.
* **Informe Técnico (PDF):** Documento integral con la metodología, métricas del modelo (RMSE: 11.42) y reflexión ética sobre el sesgo de datos y la distribución del riesgo en la ciudad.
* **Presentación:** ▶️ **[Haz clic aquí para ver el Video Explicativo](pendiente de subir)**

## 🛠️ Herramientas Utilizadas
* Python 3
* Pandas, NumPy, Matplotlib, Seaborn (Análisis de Datos y Visualización)
* Scikit-Learn (Machine Learning)
* SQLite (Bases de Datos)
