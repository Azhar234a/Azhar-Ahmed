data2= {
    'City': ['Sanaa' , 'Aden' , 'Taiz']
    'Population': [2_500_000, 800_000, 600_000]
}
df2 =pd.DataFrame(data2)
merged_df=pd.merged(df, df2, on='City')
print(merged_df)