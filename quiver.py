import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')

#make data
x = np.linspace(-4,4,6)
y = np.linspace(-4,4,6)
X, Y = np.meshgrid(x, y)

# functions
U = X + Y
V = Y - X

# plot
fig, ax = plt.subplots()

ax.quiver(X, Y, U, V, color="C0", angles='xy',
          scale_units='xy', scale=5, width=.015)
ax.set(xlim=(-5, 5),  ylim=(-5, 5))

plt.show()
