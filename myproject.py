mport pandas as pd
import numpy as np

data = pd.read_csv("housing.data", sep='\\s+')

print(data.info(), data.describe())
print("shape : ", data.shape)
print("Sum: ", data.sum)
print(data.corr())
