import numpy as np
height = [74, 67.5, 47, 30]
weight = [230, 140, 48.8, 30]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = 703*(np_weight/np_height**2)
print(np.round(bmi,2))