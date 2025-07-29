from plotnine import *
from seaborn import load_dataset

tips = load_dataset("tips")

plot = (
    ggplot(tips)
    + aes(
        x='total_bill',
        y='tip',
        color='time',
        size='size',
        shape='sex'
    )
    + geom_point(alpha=0.7, show_legend=True)
    + geom_text(
        aes(label='day'),
        size=8,
        va='bottom',
        ha='left',
        nudge_x=0.5,
        nudge_y=0.1,
        alpha=0.7,
        color='black'
    )
    + labs(
        title="Analysis of Bill Amount vs. Tip",
        x="Total Bill (USD)",
        y="Tip Amount (USD)",
        color="Meal Time",
        size="Party Size",
        shape="Gender"
    )
    + theme_minimal()
    + theme(
        figure_size=(10, 6),
        plot_title=element_text(size=14, ha='center'),
        legend_position='right',
        legend_box='vertical'
    )
    + scale_size_continuous(range=(2, 8))
    + guides(
        size=guide_legend(override_aes={"shape": "o"}),
        shape=guide_legend(override_aes={"size": 4})
    )
)

plot.draw(show=True)