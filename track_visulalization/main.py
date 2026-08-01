import fastf1 as f1
from turtle import Turtle
from turtle import Screen
import time
import random


ver = Turtle(shape= "circle")
ver.color("#0B00A7", "#0B00A7")



ham = Turtle(shape= "circle")
ham.color("#E20909", "#E20909")

for _ in range(100):
  if _ < 20:
    x = random.randint(1,20)
    y = random.randint(1,20)
  elif _ > 20 and _ < 50:
    x = random.randint(20, 50)
    y = random.randint(20, 50)
  elif _ > 50 and _ < 75:
    x = random.randint(50, 75)
    y = random.randint(50, 75)
  else:
    x = random.randint(75, 100)
    y = random.randint(75, 100)
  ver.pendown()
  ver.goto(x, y)

  ham.pendown()
  ham.goto(x, y)
  time.sleep(.05)

ver.goto(0, 0)
ham.goto(0, 0)



#To get the difference in speed between cars i need to use the percentage difference in speed and use the delay funcion for all of them
