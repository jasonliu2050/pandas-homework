import pandas as pd
import numpy as np

data = pd.read_csv("insurance.csv")
# question 1 & 2
#data.to_string()
#print(data.index, data.ndim, data.shape, data.size, data.dtypes)
#print(data.info(), data.describe())

# question 3 , 4 & 5
#print(data.loc[:, "age"])
#print(data.loc[:, ["age","children", "charges"]])
#print(data.loc[0:4, ["age","children", "charges"]])

# question 6 & 7
#print("mean charges = ", data["charges"].mean())
#print("min charges = ", data["charges"].min())
#print("max charges = ", data["charges"].max())

df = data[data["charges"] == 10797.3362]
print(df.loc[:, ["age", "sex", "smoker"]])

# question 8
df = data[data["charges"] == data["charges"].max()]
print(df.loc[:, "age"])

#question 9 & 10
print(data.groupby("region").size())
print(data.children.sum())

#question 11 & 12
# A-11 the people get older, bmi get larger, the cost will be more higher,
print(data.corr())
