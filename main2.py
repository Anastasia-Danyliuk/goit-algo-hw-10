import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

def f(x):
    return 2*x + 0.5

a = 0
b = 2

def monte_carlo_integral(f, a, b, num_samples=10000):
    count = 0
    max_y = f(b)
    for _ in range(num_samples):
        x_rand = random.uniform(a, b)
        y_rand = random.uniform(0, max_y)
        if y_rand <= f(x_rand):
            count += 1
    area = (count / num_samples) * (b - a) * max_y
    return area

num_samples = 10000
monte_carlo_result = monte_carlo_integral(f, a, b, num_samples)

quad_result, error = spi.quad(f, a, b)

print(f"Метод Монте-Карло ({num_samples} точок): {monte_carlo_result}")
print(f"Метод quad: {quad_result} (похибка: {error})")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = 2*x+0.5 від {a} до {b}')
plt.grid()
plt.show()
