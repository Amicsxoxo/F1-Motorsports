#Bar chart
import numpy as np
import matplotlib.pyplot as plt

categories = ["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"]
values = np.array([4, 3, 2, 5, 3, 1])

# plt.bar(categories, values, color= "#03484d")
plt.barh(categories, values, color= "#03484d")


plt.title("Daily Consumption")
plt.xlabel("Foods")
plt.ylabel("Quantity")

plt.show()