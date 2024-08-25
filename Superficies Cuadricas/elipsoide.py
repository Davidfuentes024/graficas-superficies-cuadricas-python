import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros de la elipsoide (longitud de los semiejes)
a, b, c = 5, 10, -10

# Desplazamiento de la elipsoide
x0, y0, z0 = 3, -4, 2

# Ángulos esféricos en coordenadas polares
theta = np.linspace(0, 2*np.pi, 2000)
phi = np.linspace(0, np.pi, 1000)
theta, phi = np.meshgrid(theta, phi)

# Transformación de coordenadas con desplazamiento
x = a * np.sin(phi) * np.cos(theta) + x0
y = b * np.sin(phi) * np.sin(theta) + y0
z = c * np.cos(phi) + z0

# Crear la figura y los ejes 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie desplazada
ax.plot_surface(x, y, z, color='salmon', alpha=0.7)

# Ajustar las proporciones de los ejes
ax.set_box_aspect([a, b, abs(c)])  # Ajusta las proporciones de los ejes

# Añadir el centro de la elipsoide desplazada
ax.scatter(x0, y0, z0, color='black', s=100)  # Punto en el nuevo centro (desplazado)

# Mostrar los ejes principales de la elipsoide desplazada
ax.quiver(x0, y0, z0, a, 0, 0, color='red', linewidth=1)   # Eje X
ax.quiver(x0, y0, z0, 0, b, 0, color='green', linewidth=1) # Eje Y
ax.quiver(x0, y0, z0, 0, 0, c, color='blue', linewidth=1)  # Eje Z

# Añadir una etiqueta para el nuevo centro
ax.text(x0, y0, z0, f'Centro ({x0}, {y0}, {z0})', color='black', fontsize=10)

# Formatear la ecuación de la elipsoide con los valores específicos de a, b, c
equation = r"$\frac{(x - " + str(x0) + r")^2}{" + str(a**2) + r"} + \frac{(y - " + str(y0) + r")^2}{" + str(b**2) + r"} + \frac{(z - " + str(z0) + r")^2}{" + str(abs(c)**2) + r"} = 1$"

# Añadir la ecuación en una esquina
ax.text2D(0.05, 0.95, equation, transform=ax.transAxes, fontsize=14, verticalalignment='top')

# Títulos y etiquetas
ax.set_title('Elipsoide desplazada con centro, ejes, y ecuación específica')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la gráfica
plt.show()
