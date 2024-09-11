import matplotlib.pyplot as plt
import numpy as np

# Generar valores de x
x = np.linspace(0, 10, 100)  # 100 puntos en el intervalo [0, 10]

# Crear funciones que simulen una estadística que se eleva al máximo
y1 = 0.1 * x**2  
y2 = 0.05 * x**2  
y3 = 0.02 * x**2  

# Crear la figura
plt.figure()

# Dibujar las líneas con estilos personalizados
plt.plot(x, y1, color='green', linewidth=0.2, linestyle='--', marker='o', markersize=0.9, label='Crecimiento Rápido')  # Línea verde
plt.plot(x, y2, color='blue', linewidth=0.3, linestyle='-.', marker='s', markersize=0.9, label='Crecimiento Moderado')  # Línea azul
plt.plot(x, y3, color='red', linewidth=0.4, linestyle=':', marker='^', markersize=0.9, label='Crecimiento Lento')  # Línea roja

# Etiquetas y título
plt.xlabel('Eje X (Tiempo)')
plt.ylabel('Eje Y (Crecimiento)')
plt.title('Crecimiento Estadístico con Estilos de Línea')

# Mostrar leyenda
plt.legend()

# Mostrar gráfico
plt.show()
