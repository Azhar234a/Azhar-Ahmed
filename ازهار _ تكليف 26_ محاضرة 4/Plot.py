from plotnine import *
import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")
count_df = df.groupby(['day', 'sex']).size().reset_index(name='count')
total_per_day = count_df.groupby('day')['count'].transform('sum')
count_df['percentage'] = (count_df['count'] / total_per_day) * 100

plot = (
    ggplot(count_df, aes(x='day', y='percentage', fill='sex')) +
    geom_bar(stat='identity', position='dodge', color='black', width=0.7) +
    labs(
        title='نسبة الزبائن حسب الجنس خلال الأسبوع - plotnine',
        x='Day',
        y='Percentage %'
    ) +
    theme_minimal() +
    theme(
        axis_text_x=element_text(size=10),
        plot_title=element_text(size=12, weight='bold')
    )
)

# الامر المختلف هو حفظ الرسم باستخدام ggsave
plot.save('plotnine_percentage_plot.png', width=8, height=5, dpi=100)
