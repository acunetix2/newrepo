import matplotlib.pyplot as plt 
import numpy as np 
import  datetime 

date = datetime.datetime.now()

time = [1, 2, 3, 4, 5, 6, 7, 8, 9]
insulin_c = [0.5, 0.95, 2, 2.5, 0.7, 1.2, 1, 0.6, 1.6]

font = {"family":"serif", "color":"blue"}

plt.title("INSULIN CONCENTRATION", fontdict = font)
plt.xlabel("Time in seconds", fontdict = font)
plt.ylabel("Insulin concentration Volume  (cm3)", fontdict = font)

plt.plot(time, insulin_c, color = "g")
plt.grid(c = "green", ls = "dotted")
plt.show()
 
 
