#Turning on grids
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 10, 15, 20, 25])

plt.grid(axis="y", linewidth= 2, color= "lightgray", linestyle= "dashdot")

plt.plot(x, y)
plt.show()