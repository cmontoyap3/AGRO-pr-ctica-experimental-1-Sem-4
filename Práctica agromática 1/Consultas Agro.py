import psycopg2
import pandas as pd

# Conexión
conn = psycopg2.connect(
    dbname="agrobio_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# 1. Total de cultivos registrados
cur.execute("SELECT COUNT(*) FROM cultivos")
total_cultivos = cur.fetchone()[0]
print("Total de cultivos registrados:", total_cultivos)

# 2. Producción total
cur.execute("SELECT SUM(produccion) FROM cultivos")
produccion_total = cur.fetchone()[0]
print("Producción total:", produccion_total)

# 3. Visualización en DataFrame
df = pd.read_sql("SELECT cultivo, rendimiento, produccion, anio FROM cultivos", conn)
print("\n--- DATOS TABULADOS ---")
print(df)

cur.close()
conn.close()