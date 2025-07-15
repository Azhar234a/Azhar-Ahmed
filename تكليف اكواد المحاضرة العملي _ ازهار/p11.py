import  pandas as pd
data= {
    'Name': ['Ali' , 'Fatima' , 'Omar'],
    'Age': [25,30,22],
    'City': ['Sanaa' , 'Aden' , 'Taiz']
}
df=pd.DataFrame(data)
print(df)