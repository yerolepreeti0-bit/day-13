import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("housing_data.csv")   # Change filename if needed

print("First 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

plt.figure(figsize=(8,5))
sns.histplot(df['Price'], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness = df['Price'].skew()
kurtosis = df['Price'].kurt()

print("\nSkewness of Price:", skewness)
print("Kurtosis of Price:", kurtosis)

if skewness > 1:
    df['Log_Price'] = np.log(df['Price'])
    print("\nLog transformation applied to Price column.")

plt.figure(figsize=(8,5))
sns.countplot(x='City', data=df)
plt.title("Count of Houses by City")
plt.xticks(rotation=45)
plt.show()
