import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

plt.figure(figsize=(10, 6), dpi=100)
plt.style.use('seaborn-v0_8')
scatter = sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='time',
    style='sex',
    size='size',
    palette='Set1',
    alpha=0.7,
    sizes=(20, 200),
    edgecolor='black',
    linewidth=0.3
)

for i, row in tips.iterrows():
    plt.text(
        x=row['total_bill'] + 0.5,
        y=row['tip'] + 0.1,
        s=row['day'],
        fontsize=8,
        alpha=0.7,
        fontweight='normal',
        color='black'
    )

plt.title("Restaurant Tips Analysis: Bill Amount vs Tip", pad=20, fontsize=14)
plt.xlabel("Total Bill (USD)", labelpad=10)
plt.ylabel("Tip Amount (USD)", labelpad=10)

plt.legend(
    title_fontsize=10,
    bbox_to_anchor=(1.05, 1),
    loc='upper left',
    borderaxespad=0.
)

plt.tight_layout()
plt.show()