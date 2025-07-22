import pandas as pd

data = {'EmployeeName': ['احمد','سارة','خالد','ليلى','محمد'], 'Salary': [2000,2500,3000,10000,2000]}
df=pd.DataFrame(data)
mean_salary = df['Salary'].mean()
print(f"Mean of Salary: {mean_salary:.2f}")
median_salary = df['Salary'].median()
print(f"Median of Salary: {median_salary:.2f}")
mode_salary = df=df['Salary'].mode()
print(f"Mode of Salary: {mode_salary}")