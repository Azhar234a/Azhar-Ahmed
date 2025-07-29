import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
avg_tip = tips.groupby(['day', 'sex'])['tip'].mean().unstack()

# Mapping: لون مختلف لكل جنس
plt.figure(figsize=(8, 4))
for sex in avg_tip.columns:
    plt.plot(avg_tip.index, avg_tip[sex], label=sex)
plt.title("Matplotlib Line Plot - Mapping")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.legend(title="Sex")
plt.grid(True)
plt.tight_layout()
plt.show()

# Setting: لون موحد للجميع
plt.figure(figsize=(8, 4))
for sex in avg_tip.columns:
    plt.plot(avg_tip.index, avg_tip[sex], color='teal')
plt.title("Matplotlib Line Plot - Setting")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.grid(True)
plt.tight_layout()
plt.show()
