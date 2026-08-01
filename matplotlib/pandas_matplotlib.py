import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("matplotlib/data.csv")

print(df["Type1"].value_counts())