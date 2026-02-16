import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
data = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    "Experience": [2, 5, 8, 12, 15, 18, 22, 25],
    "Department": ["HR", "IT", "Finance", "Marketing", "HR", "IT", "Finance", "Marketing"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"]
               
}
df = pd.DataFrame(data)
print(df)
plt.figure()
sns.scatterplot(x="Age",y="Salary",data=df)
plt.title("Age vs Salary")
plt.show()

plt.figure()
sns.scatterplot(x="Experience",y="Salary",data=df)
plt.title("Experience vs Salary")
plt.show()

plt.figure()
sns.boxplot(x="Gender",y="Salary",data=df)
plt.title("Gender vs Salary")
plt.show()

plt.figure()
sns.boxplot(x="Department",y="Salary",data=df)
plt.title("Salary of Department")
plt.show()

corr_matrix =df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Boxplot for age
plt.figure()
sns.boxplot(x=df["Age"])
plt.title("Age Boxplot")
plt.show()

# Boxplot for Expeience
plt.figure()
sns.boxplot(x=df["Experience"])
plt.title("Experience Outliers")
plt.show()

print("\n==== SAMPLE INSIGHTS ====")
print("1. Salary increases with Experience and Age.")
print("2. Finance department shows higher salary range.")
print("3. No Extreme outliers detected in Age or Experience.")
print("4.Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")

