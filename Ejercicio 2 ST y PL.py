import numpy as np
import matplotlib.pyplot as plt

# Definir la función y sus derivadas
def g(x):
    return np.arctan(x)

# Polinomio de Lagrange
def lagrange_polynomial(x, x_values, y_values):
    polynomial = 0
    for i in range(len(y_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += term
    return polynomial

# Puntos para graficar
x = np.linspace(0, 2, 400)
y = g(x)

# Puntos para el polinomio de Lagrange
x_values = np.array([0, 1, 2])
y_values = g(x_values)

# Calcular el polinomio de Lagrange
y_lagrange = lagrange_polynomial(x, x_values, y_values)

# Serie de Taylor hasta el término (x-1)^2
def g_taylor(x):
    return np.pi/4 + (1/2)*(x - 1) - (1/4)*(x - 1)**2

# Calcular la serie de Taylor
y_taylor = g_taylor(x)

# Imprimir la serie de Taylor y la mejor aproximación
x0 = 1
g0 = g(x0)
g1 = 1 / (1 + x0**2)
g2 = -2 * x0 / (1 + x0**2)
print("\nSerie de Taylor de g(x) en x0 = 1:")
print(f"g(x) ≈ {g0} + ({g1} * (x - 1)) + ({g2 / 2} * (x - 1)^2)")

# Mejor aproximación
if g1 == 0:
    if g2 != 0:
        print("La mejor aproximación es de orden 2")
else:
    print("La mejor aproximación es de orden 1")


# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='g(x) = arctan(x)', color='blue')
plt.plot(x, y_lagrange, label='Polinomio de Lagrange', color='green', linestyle='--')
plt.plot(x, y_taylor, label='Aproximación de Taylor', color='red', linestyle=':')
plt.scatter(x_values, y_values, color='black', label='Puntos de interpolación')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Polinomio de Lagrange y Serie de Taylor de g(x) = arctan(x) en x0 = 1')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.show()



