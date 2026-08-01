#Scatter graph
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([50, 68, 55, 70, 72, 78, 83, 88, 92, 95, 97])


plt.scatter(x1, y1, color= "#150d81", alpha= 0.5, s =200, label= "Class A")
plt.scatter(x2, y2, color= "#850909", alpha= 0.5, s =200, label= "Class B")

#alpha is the transparency, s is the size of the plots

plt.title("Test scores")

plt.xlabel("Hours studied")
plt.ylabel("Scores")
plt.legend()

plt.show()