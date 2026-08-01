#Basic graph
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([20, 30, 25, 35])
y3 = np.array([18, 24, 35, 15])



line_style = dict(marker= ".", markersize= 20, markerfacecolor ="#1cd3fc", markeredgecolor ="#1cd3fc", linestyle = "solid", linewidth= 4)

#The marker style is being specified in marker, the marker size is an integer, markerfacecolor of mfc the color of the marker face , markeredgecolor or mec is the color of marker edge

plt.plot(x, y1, color= "#1a63b8", **line_style)
plt.plot(x, y2, color= "#1b9439", **line_style)
plt.plot(x, y3, color= "#861010", **line_style)


plt.show()