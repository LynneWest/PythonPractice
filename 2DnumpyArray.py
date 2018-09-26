#height and weight list
height_weight = [[74, 230],[67.5, 140], [47, 48.8], [30, 30]]
import numpy as np
#change list to 2D numpy array
height_weight_np = np.array(height_weight)
#calculate bmi from 2D numpy array
bmi=703*(height_weight_np[:,1]/height_weight_np[:,0]**2)
print(bmi)