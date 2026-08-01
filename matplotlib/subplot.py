import numpy as np
import matplotlib.pyplot as plt

#Figure = The whole canvas
#Ax = A single plot (subplot)

x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2,2)
#(no of rows, no of columns)

axes[0, 0].plot(x, x**2, color= "#860b0b")
axes[0, 0].set_title("X to the power of 2")

axes[0, 1].plot(x, (x*2)**2, color= "#11c42e")
axes[0, 1].set_title("X mutipled by 2 and to the power of 2")

axes[1, 0].plot(x, x**3, color= "#02b5e2")
axes[1, 0].set_title("X to the power of 3")

axes[1, 1].plot(x, (x*3)**3, color= "#d38716")
axes[1, 1].set_title("X mutipled by 3 and to the power of 3")


plt.tight_layout()

plt.show()