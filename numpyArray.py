import numpy as np
height = [74, 67.5, 47, 30] #in inches
weight = [230, 140, 48.8, 30] #in lbs

#change lists to numpy arrays
np_height = np.array(height)
np_weight = np.array(weight)

#calculate bmi for each element in the lists
bmi = 703*(np_weight/np_height**2)
print(np.round(bmi,2))