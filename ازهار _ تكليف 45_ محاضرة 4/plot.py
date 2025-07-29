from plotnine import *
from seaborn import load_dataset
import numpy as np

# Load the dataset
tips = load_dataset("tips")

# Set the theme for all plots
theme_set(theme_minimal() + theme(figure_size=(8, 5)))

# Mapping version - using aesthetic mapping
plot_map = (
    ggplot(tips)
    + aes(x='day', y='tip', color='sex', group='sex')
    + stat_summary(geom='line', fun_y=np.mean, size=1.5)
    + stat_summary(geom='point', fun_y=np.mean, size=3)
    + labs(
        title="Average Tips by Day and Gender",
        x="Day of Week",
        y="Average Tip Amount (USD)",
        color="Gender"
    )
    + scale_color_manual(values=["#1f77b4", "#d62728"])
    + theme(
        plot_title=element_text(size=12, ha='center', face='bold'),
        legend_position='right',
        axis_title=element_text(size=10)
    )
)

# Setting version - using direct properties
plot_set = (
    ggplot(tips)
    + aes(x='day', y='tip', group=1)
    + stat_summary(geom='line', fun_y=np.mean, color='darkblue', size=1.5)
    + stat_summary(geom='point', fun_y=np.mean, color='darkblue', size=3)
    + labs(
        title="Overall Average Tips by Day",
        x="Day of Week",
        y="Average Tip Amount (USD)"
    )
    + theme(
        plot_title=element_text(size=12, ha='center', face='bold'),
        axis_title=element_text(size=10)
    )
)

# ✅ الحل: عرض المخططات مباشرة باستخدام `draw(show=True)`
plot_map.draw(show=True)
plot_set.draw(show=True)
