import numpy as np

ages = np.array([22, 25, 19, 30, 35, 40, 45, 50, 55, 60, 22, 25, 19, 30, 35, 40, 45, 50, 55, 60])
q1=np.percentile(ages,25)
median=np.percentile(ages,50)
q3=np.percentile(ages,75)

print(f"Q1 (25%): {q1} Years")
print(f"median (50%): {median} Years")
print(f"Q3 (75%): {q3} Years")
