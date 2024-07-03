import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
radii = [1, 2, 2.5, 3]
for radius in radii:
    circle = plt.Circle((0, 0), radius, fill=False, color='blue', linestyle='--')
    ax.add_artist(circle)
x = np.linspace(-3, 3, 400)
x = x[x != 0]
y = -3 / x**2
ax.plot(x, y, color='red', label='Y = -3 / X^2')
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')
ax.set_title('Circles with Radii 1, 2, 2.5, 3 and Plot of Y = -3 / X^2')
ax.legend()
plt.show()
