import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("matplotlib/data.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color= "#81630F", edgecolor= "#000000")

plt.title("No of Pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
#To ensure that everthing fits

plt.show()