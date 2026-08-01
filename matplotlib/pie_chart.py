#Pie chart
import numpy as np
import matplotlib.pyplot as plt


categories = ["Freshmen", "Sophomore", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225])
#Np arrays are much faster
colors = ["#2e0e44", "#154b07", "#0f1d2b", "#413e1a"]

plt.pie(values, labels= categories, autopct= "%1.1f%%", colors=colors, explode= [0, 0, 0, .1], shadow=True, startangle=90)
#The values, the labels, autopct is to show the percentage, explode is how shifted each section is seprated from the main pie, shadow is shadow and startangle is the angle to rotate the whole chart

plt.title("Chima's College")

plt.show()