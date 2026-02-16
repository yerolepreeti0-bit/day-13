import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

data = {
    "Age":[25,30,32,45,38,34,46,74,29,41],
    "Salary":[30000,40000,35000,32000,45000,42000,28000,18000,38000,45000],
    "Experince":[2,5,3,10,7,6,12,20,4,8],
    "Department":["HR","IT","Finance","IT","HR","Finance","IT","HR","Finance","IT"],
    "Gender":["M","F","M","F","F","M","F","M","F","M"]

}
df = pd.DataFrame(data)
print(df)
print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset shape(rows,columns):", df.shape)
print("\nDataset info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())