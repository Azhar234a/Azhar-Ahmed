import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Mapping: hue=sex
plt.figure(figsize=(8, 4))
sns.lineplot(data=tips, x="day", y="tip", hue="sex", estimator="mean")
plt.title("Seaborn Line Plot - Mapping")
plt.tight_layout()
plt.show()

# Setting: لون ثابت
plt.figure(figsize=(8, 4))
sns.lineplot(data=tips, x="day", y="tip", color="orange", estimator="mean")
plt.title("Seaborn Line Plot - Setting")
plt.tight_layout()
plt.show()
