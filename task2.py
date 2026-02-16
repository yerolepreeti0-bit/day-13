import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing_data.csv")
print(df.head())


plt.figure(figsize=(8,5))
sns.scatterplot(x='Area_sqft', y='Price', data=df)
plt.title("Area vs Price")
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='City', y='Price', data=df)
plt.title("City vs Price Distribution")
plt.xticks(rotation=45)
plt.show()