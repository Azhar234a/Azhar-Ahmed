#مخطط نقاط مبعثر
from plotnine import *
from seaborn import load_dataset

# تحميل البيانات
tips = load_dataset("tips")

# رسم Scatter Plot
plot = (ggplot(tips, aes(x='total_bill', y='tip', color='day'))
        + geom_point()
        + labs(title='Scatter Plot - Plotnine'))
plot.show()






