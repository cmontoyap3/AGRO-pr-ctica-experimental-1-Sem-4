import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    dbname="agrobio_db", user="postgres", password="12345", host="localhost", port="5432"
)

# Cargar datos
df = pd.read_sql("SELECT cultivo, rendimiento, produccion, anio FROM cultivos", conn)

# 1. Gráfico de barras: Rendimiento por cultivo
plt.figure(figsize=(8, 4))
df.plot(kind='bar', x='cultivo', y='rendimiento', title='Rendimiento por cultivo', color='skyblue')
plt.xlabel('Cultivo')
plt.ylabel('Rendimiento (t/ha)')
plt.tight_layout()
plt.savefig('grafico_barras.png')
plt.show()

# 2. Gráfico de líneas: Producción por año/cultivo
plt.figure(figsize=(8, 4))
df.plot(kind='line', x='cultivo', y='produccion', marker='o', title='Producción por Cultivo', color='green')
plt.xlabel('Cultivo')
plt.ylabel('Producción Total')
plt.tight_layout()
plt.savefig('grafico_lineas.png')
plt.show()

conn.close()