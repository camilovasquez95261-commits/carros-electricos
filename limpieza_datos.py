import pandas as pd

# Cargar la base de datos desde tu repositorio propio de GitHub
ruta = "https://raw.githubusercontent.com/camilovasquez95261-commits/carros-electricos/main/Electric_Vehicle_Population_Data.csv"
df = pd.read_csv(ruta)

print("=" * 50)
print("1. PRIMERAS FILAS DE LA BASE DE DATOS")
print(df.head())
print("=" * 50)

print("=" * 50)
print("2. INFORMACIÓN GENERAL (TIPOS DE DATOS Y NULOS)")
print(df.info())
print("=" * 50)

print("=" * 50)
print("3. ESTADÍSTICAS DESCRIPTIVAS")
print(df.describe())
print("=" * 50)

print("=" * 50)
print("4. NOMBRE DE TODAS LAS COLUMNAS")
print(df.columns)
print("=" * 50)

print("=" * 50)
print("5. CONTEO DE DATOS FALTANTES (NULOS POR COLUMNA)")
print(df.isnull().sum())
print("=" * 50)

print("=" * 50)
print("6. DIMENSIONES DE LA TABLA (FILAS, COLUMNAS)")
print(df.shape)
print("=" * 50)

print("=" * 50)
print("7. CONSULTA DE UNA COLUMNA INDIVIDUAL (MARCAS)")
print(df["Make"])
print("=" * 50)

print("=" * 50)
print("8. SELECCIÓN DE VARIAS COLUMNAS (MARCA, MODELO Y AUTONOMÍA)")
print(df[["Make", "Model", "Electric Range"]])
print("=" * 50)

print("=" * 50)
print("9. FILTRADO: ÚNICAMENTE VEHÍCULOS DE MARCA TESLA")
print(df[df["Make"] == "TESLA"])
print("=" * 50)