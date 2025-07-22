import pandas as pd

data={
    'Department':['HR', 'IT', 'IT', 'Finance', 'HR','Finance'],
    'Gender': ['Male','Female','Male','Female', 'Male', 'Male'],
    'Salary': [3000,4000,3500,4500,3200,5000]
}
df=pd.DataFrame(data)
pivot_table=pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='Gender',
    aggfunc='mean'
)
print(pivot_table)
