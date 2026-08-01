#Basic graph customization
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([20, 30, 25, 35])
y3 = np.array([18, 24, 35, 15])

plt.title("Class size", fontsize= 25, family="Arial", fontweight= "bold", color= "#06065c")
#The title of the graph

plt.xlabel("Year", family= "Arial", fontsize= 20, fontweight= "bold", color= "#08d5f0")
plt.ylabel("Students", family= "Arial", fontsize= 20, fontweight= "bold", color= "#08d5f0")
#The x and y labels 

plt.tick_params(axis="both", colors= "#08d5f0")

plt.plot(x, y1, color= "#1a63b8")
plt.plot(x, y2, color= "#1b9439")
plt.plot(x, y3, color= "#861010")
#The plots on the graph

plt.xticks(x)
#Making sure the ticks are only on the x values, no futher seperations

plt.show()