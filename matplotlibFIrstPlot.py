import matplotlib.pyplot as plt
height = [74, 67.5, 47, 30] #in inches
weight = [230, 140, 48.8, 30] #in lbs
plt.plot(height, weight)
plt.xlabel('height (inches)')
plt.ylabel('weight')
plt.title('heights and weights of the Jones family')
plt.yticks([0,50,100,150,200,250],
            ['0', '50 lbs', '100 lbs', '150 lbs', '200 lbs', '250 lbs'])
plt.show()