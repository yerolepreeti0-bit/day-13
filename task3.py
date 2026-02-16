import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("housing_data.csv")

print("First 5 rows:")
print(df.head())

df.columns = df.columns.str.strip()

print("\nColumn Names:")
print(df.columns)

corr_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(10,6))

sns.heatmap(
    corr_matrix,
    annot=True,        # show numbers
    cmap="coolwarm",  # color theme
    fmt=".2f",        # decimal format
    linewidths=0.5
)

plt.title("Correlation Matrix Heatmap")
plt.show()
print("\nHighly Correlated Feature Pairs (> 0.8):")

high_corr_pairs = []

for col1 in corr_matrix.columns:
    for col2 in corr_matrix.columns:
        if col1 != col2:
            corr_value = corr_matrix.loc[col1, col2]
            if abs(corr_value) > 0.8:
                high_corr_pairs.append((col1, col2, corr_value))

# Remove duplicates
seen = set()
for col1, col2, corr_value in high_corr_pairs:
    if (col2, col1) not in seen:
        print(f"{col1}  <-->  {col2}  =  {corr_value:.2f}")
        seen.add((col1, col2))

main_column = "Price"

if main_column in df.columns:

    plt.figure(figsize=(8,5))

    sns.boxplot(x=df[main_column])

    plt.title(f"Boxplot of {main_column}")
    plt.show()

else:
    print(f"\nColumn '{main_column}' not found. Change column name.")

