import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del paraboloide hiperbólico (longitud de los semiejes)
a, b = 5, 10

# Crear una malla de puntos en los planos X y Y
x = np.linspace(-20, 20, 400)
y = np.linspace(-20, 20, 400)
x, y = np.meshgrid(x, y)

# Calcular Z usando la ecuación del paraboloide hiperbólico
z = (x**2) / a**2 - (y**2) / b**2

# Crear la figura y los ejes 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie del paraboloide hiperbólico
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.7)

# Formatear la ecuación del paraboloide hiperbólico con los valores específicos de a y b
equation = r"$z = \frac{x^2}{"+ str(a**2) + r"} - \frac{y^2}{"+ str(b**2) + r"}$"

# Añadir la ecuación en una esquina
ax.text2D(0.05, 0.95, equation, transform=ax.transAxes, fontsize=14, verticalalignment='top')

# Títulos y etiquetas
ax.set_title('Paraboloide Hiperbólico con vértice, ejes, y ecuación específica')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ajustar las proporciones de los ejes
ax.set_box_aspect([2*a, 2*b, 20])  # Ajusta las proporciones de los ejes

# Mostrar la gráfica
plt.show()
