# ==============================================================================
# FASE 3: SCRIPT DE INTEGRACIÓN CON BASE DE DATOS (SQLite)
# ==============================================================================

import sqlite3
import pandas as pd

print("1. Conectando base de datos SQLite...")
conexion = sqlite3.connect("calidad_aire.db")
df_bd = pd.read_csv("calidad_aire_quito.csv", sep=';')

print("2. Guardando registros ambientales...")
df_bd.to_sql('registros_ambientales', conexion, if_exists='replace', index=False)

print("3. Ejecutando alertas simuladas...")
cursor = conexion.cursor()
cursor.execute("SELECT Fecha, Estacion, PM25 FROM registros_ambientales ORDER BY PM25 DESC LIMIT 3")
alertas = cursor.fetchall()

print("\n--- 🚨 ALERTAS DE CONTAMINACIÓN EN BD ---")
for alerta in alertas:
    print(f"ZONA: {alerta[1]} | FECHA: {alerta[0]} | NIVEL PM2.5: {alerta[2]} µg/m³")

conexion.close()
print("\n✅ Integración finalizada.")