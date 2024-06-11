import numpy as np
import matplotlib.pyplot as plt

# Definir la función y sus derivadas
def f(x):
    return 1 / (25 * x**2 + 1)

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

# Serie de Taylor hasta el término x^2
def f_taylor(x):
    return 1 - 25 * x**2

# Puntos para graficar
x = np.linspace(-1, 1, 400)
y = f(x)

# Puntos para el polinomio de Lagrange
x_values = np.array([-1, 0, 1])
y_values = f(x_values)

# Calcular el polinomio de Lagrange
y_lagrange = lagrange_polynomial(x, x_values, y_values)

# Calcular la serie de Taylor
f_taylor_values = f_taylor(x)

# Imprimir la serie de Taylor y la mejor aproximación
x0 = 0
f0 = f(x0)
f1 = -50 * x0
f2 = -50
print("\nSerie de Taylor de la función en x0 = 0:")
print(f"f(x) ≈ {f0} + ({f1} * x) + ({f2 / 2} * x^2)")

# Mejor aproximación
if f1 == 0:
    if f2 != 0:
        print("La mejor aproximación es de orden 2")
else:
    print("La mejor aproximación es de orden 1")


# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = 1 / (25x^2 + 1)', color='blue')
plt.plot(x, y_lagrange, label='Polinomio de Lagrange', color='red', linestyle='--')
plt.plot(x, f_taylor_values, label='Serie de Taylor', color='green', linestyle=':')
plt.scatter(x_values, y_values, color='black', label='Puntos de interpolación')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Polinomio de Lagrange y Serie de Taylor de f(x) = 1 / (25x^2 + 1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

