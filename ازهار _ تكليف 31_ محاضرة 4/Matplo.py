import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
tips = sns.load_dataset("tips")

# Configure visual properties
shape_mapping = {'Male': 'o', 'Female': 's'}  # Circle for Male, Square for Female
color_mapping = {'Lunch': '#1f77b4', 'Dinner': '#d62728'}  # Seaborn default blue/red

# Set up figure with better proportions
plt.figure(figsize=(10, 6), dpi=100)
plt.style.use('seaborn-v0_8-whitegrid')  # Clean style with grid

# Create scatter plot with custom aesthetics
for sex in tips['sex'].unique():
    subset = tips[tips['sex'] == sex]
    scatter = plt.scatter(
        x=subset['total_bill'],
        y=subset['tip'],
        c=subset['time'].map(color_mapping),
        s=subset['size'] * 20,  # Increased size multiplier
        marker=shape_mapping[sex],
        alpha=0.8,
        edgecolors='white',  # Add white border
        linewidths=0.5,
        label=sex
    )

    # Add day labels with improved formatting
    for _, row in subset.iterrows():
        plt.text(
            x=row['total_bill'] + 0.5,  # Increased offset
            y=row['tip'],
            s=row['day'],
            fontsize=8,
            alpha=0.8,
            color='black',
            fontweight='normal',
            verticalalignment='center'
        )

# Add titles and labels with improved formatting
plt.title("Restaurant Tips Analysis: Bill vs Tip by Gender and Time",
          pad=20, fontsize=14, fontweight='bold')
plt.xlabel("Total Bill (USD)", labelpad=10)
plt.ylabel("Tip Amount (USD)", labelpad=10)

# Improve legend
legend = plt.legend(
    title="Gender",
    title_fontsize=12,
    fontsize=10,
    frameon=True,
    framealpha=0.9,
    borderpad=1
)

# Add color legend for meal times
from matplotlib.lines import Line2D

color_legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Lunch',
           markerfacecolor=color_mapping['Lunch'], markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Dinner',
           markerfacecolor=color_mapping['Dinner'], markersize=10)
]
plt.legend(handles=color_legend_elements, title="Meal Time",
           bbox_to_anchor=(1.05, 1), loc='upper left')

# Add the gender legend back (since we overwrote it)
plt.gca().add_artist(legend)

# Adjust layout and show
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()