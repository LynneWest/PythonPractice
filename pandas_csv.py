import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cars = pd.read_csv("vehicletest.csv")
#print(cars)

x = cars['29'] #city mpg
y = cars['37'] #hwy mpg
print(np.corrcoef(x,y))
plt.scatter(x,y, s=1)
plt.xlabel('City mpg')
plt.ylabel('Highway mpg')
plt.title("Correlation of a vehicle's highway and city mpg")
plt.yticks([5,10,15,20,25,30,35,40,45,50])
plt.xticks([5,10,15,20,25,30,35,40,45,50])
plt.show()