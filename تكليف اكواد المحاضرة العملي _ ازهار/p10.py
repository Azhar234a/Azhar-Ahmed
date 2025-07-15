import pandas as pd
health_data = pd.read_csv("data_csv",header=0 ,sep=",")
pd.set_option('display.max_columns' ,None)
print(health_data.describe())