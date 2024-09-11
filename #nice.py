import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generar valores de x
x = np.linspace(0, 10, 100)  # 100 puntos en el intervalo [0, 10]

# Crear funciones que simulen una estadística que se eleva al máximo
y1 = 0.1 * x**2  # Función cuadrática (rápido crecimiento)
y2 = 0.05 * x**2  # Función cuadrática (crecimiento moderado)
y3 = 0.02 * x**2  # Función cuadrática (crecimiento lento)

# Generar fechas simuladas
dates = pd.date_range(start='2024-01-01', periods=len(x), freq='D')
sample_dates = dates[[0, 25, 50, 75, 99]]  # Seleccionar fechas de muestra

# Tomar algunas muestras para la tabla
sample_indices = [0, 25, 50, 75, 99]  # Indices de muestra
sample_x = x[sample_indices]
sample_y1 = y1[sample_indices]
sample_y2 = y2[sample_indices]
sample_y3 = y3[sample_indices]
sample_dates_str = [date.strftime('%Y-%m-%d') for date in sample_dates]  # Convertir fechas a formato de cadena

import matplotlib.pyplot as plt
import pandas as pd

# Datos
fechas = ['01/01/2024', '03/01/2024', '07/01/2024', '10/01/2024', '15/01/2024', '20/01/2024', '25/01/2024']
numeros = [23, 56, 34, 78, 12, 45, 67]

# Convertir fechas a formato datetime
fechas = pd.to_datetime(fechas, format='%d/%m/%Y')

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(fechas, numeros, marker='o', linestyle='-', color='b')

# Etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Número')
plt.title('Gráfica Lineal de Estadísticas')

# Mostrar la gráfica
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
