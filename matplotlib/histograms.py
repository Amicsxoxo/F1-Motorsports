import numpy as np
import matplotlib.pyplot as plt

scores = np.random.normal(loc=80, scale= 10, size= 100)
#Loc is the median, where are the scores centered upon. Scale is the standard deviation, how far does the scores deviate from the loc, and size is the number of numbers your are outputing
scores = np.clip(scores, 0, 100)
#clips turns the numbers that cross its min and max values to the min and max values respectively, any number that crosses 0 turns to 0 and same for 100

plt.hist(scores, bins= 10, color="#25c454", edgecolor= "#042e1c")
#The hist function draws the histogram, the bins is the number of sections in the histogram

plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")

plt.show()