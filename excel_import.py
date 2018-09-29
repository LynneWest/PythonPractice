import pandas as pd
import numpy as np
hw = pd.read_excel("height_weight.xlsx")
#put data in 2D numpy array
hw_np = np.array(hw)
#calculate bmi from 2D numpy array
bmi=703*(hw_np[:,1]/hw_np[:,0]**2)
print(bmi)