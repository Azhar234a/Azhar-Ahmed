import pandas as pd
health_data = pd.read_csv("data_csv",header=0 ,sep=",")
health_data.dropna(axis=0 , inplace=True)

health_data["Average_Pulse"]=health_data["Average_Pulse"].astype(float)
health_data["Max_Pulse"]=health_data["Max_Pulse"].astype(float)

print(health_data.info())