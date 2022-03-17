import pandas as pd
import numpy as np

# Pandas dataframe to csv

path=''
file = pd.read_excel(path+'file.xlsx')
file.to_csv(path+'file.csv', index=False)

# Numpy array to csv

a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
np.savetxt(path+"file.csv", a, delimiter=",")

