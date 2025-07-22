import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from datetime import datetime


df = pd.read_csv('sales_data.csv')
print("معلومات عن البيانات:")
print(df.info())
print("\nإحصائيات وصفية للبيانات:")
print(df.describe())
print("\nعرض أول 5 صفوف من البيانات:")
print(df.head())
print("\nعدد القيم المفقودة في كل عمود:")
print(df.isnull().sum())