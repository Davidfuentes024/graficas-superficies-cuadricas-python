import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del cono elíptico (longitud de los semiejes de la base y la altura)
a, b, c = 10, 10, 10

# Desplazamiento del cono elíptico
x0, y0, z0 = 0, 0, 0

# Ángulos en coordenadas polares para el cono
theta = np.linspace(0, 2 * np.pi, 200)
z = np.linspace(-c, c, 100)  # Variable de altura z desde 0 hasta c
theta, z = np.meshgrid(theta, z)

# Transformación de coordenadas para el cono elíptico
x = a * (z / c) * np.cos(theta) + x0
y = b * (z / c) * np.sin(theta) + y0
z = z + z0  # Desplazamiento en z

# Crear la figura y los ejes 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie del cono elíptico
ax.plot_surface(x, y, z, color='salmon', alpha=0.7)

# Añadir el vértice del cono elíptico
ax.scatter(x0, y0, z0, color='black', s=100)  # Punto en el vértice

# Mostrar los ejes principales del cono elíptico
ax.quiver(x0, y0, z0, a, 0, 0, color='red', linewidth=1)   # Eje X
ax.quiver(x0, y0, z0, 0, b, 0, color='green', linewidth=1) # Eje Y
ax.quiver(x0, y0, z0, 0, 0, c, color='blue', linewidth=1)  # Eje Z

# Añadir una etiqueta para el vértice del cono
ax.text(x0, y0, z0, f'Vértice ({x0}, {y0}, {z0})', color='black', fontsize=10)

# Formatear la ecuación del cono elíptico con los valores específicos de a, b, c
equation = r"$\frac{(x - " + str(x0) + r")^2}{" + str(a**2) + r"} + \frac{(y - " + str(y0) + r")^2}{" + str(b**2) + r"} = \frac{(z - " + str(z0) + r")^2}{" + str(c**2) + r"}$"

# Añadir la ecuación en una esquina
ax.text2D(0.05, 0.95, equation, transform=ax.transAxes, fontsize=14, verticalalignment='top')

# Títulos y etiquetas
ax.set_title('Cono elíptico con vértice, ejes, y ecuación específica')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la gráfica
plt.show()
