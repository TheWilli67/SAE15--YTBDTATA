import pandas as pd

dataframe = pd.read_csv('cleaned/file_merged.csv')
dataframe.to_csv('cleaned/top_5.csv')
dataframe = dataframe.sort_values('likes', ascending=False)[:5]
dataframe.to_csv('cleaned/top_5.csv', index=False, header=None)  
print(dataframe)