import pandas as pd

data = {'EmployeeName': ['احمد','سارة','خالد','ليلى','محمد'],
        'Salary': [2000,2100,2050,1900,1950]
        }

df= pd.DataFrame(data)
std=df['Salary'].std()
variance = df['Salary'].var()
print(f"Standard Deviation of Salary: {std:.2f}")
print(f"Variance of Salary: {variance:.2f}")
