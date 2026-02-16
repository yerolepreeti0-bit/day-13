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
plt.figure()
sns.histplot(data["Age"],kde=True)
plt.title("Age Distribution")
plt.show()

plt.figure()
sns.histplot(data["Salary"],kde=True)
plt.title("Salary Distribution")
plt.show()

plt.figure()
sns.boxplot(x=data["Salary"])
plt.title("Salary Boxplot")
plt.show()

print("\nDepartment counts:")
print(pd.Series(data["Department"]).value_counts())
print("\nGender counts:")
print(pd.Series(data["Gender"]).value_counts())

plt.figure()
sns.countplot(x="Department",data=data)
plt.title("Department Distribution")
plt.show()

