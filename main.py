import pandas as pd

# 1. Cargar el archivo CSV
df = pd.read_csv('Electric_Vehicle_Population_Data.csv')

# 2. Confirmar la carga mostrando las primeras filas
print("--- Vista previa de los datos ---")
print(df.head())

# 3. Mostrar el total de filas (vehículos registrados)
print(f"\nTotal de vehículos en la base de datos: {len(df)}")