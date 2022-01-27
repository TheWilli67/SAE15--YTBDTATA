import pandas as pd

dataframe = pd.read_csv('cleaned/file_merged.csv')
ff = dataframe.sort_values('likes', ascending=False)[:5]
dataframe.drop(dataframe.columns[0], axis=1, inplace=True)
dataframe.drop(dataframe.columns[1], axis=1, inplace=True)
dataframe.drop(dataframe.columns[3], axis=1, inplace=True)
dataframe.drop(dataframe.columns[5], axis=1, inplace=True)
dataframe.drop(dataframe.columns[10], axis=1, inplace=True)
dataframe.drop(dataframe.columns[11], axis=1, inplace=True)
dataframe.drop(dataframe.columns[12], axis=1, inplace=True)
dataframe.drop(dataframe.columns[4], axis=1, inplace=True)
ff.to_csv('cleaned/top_5.csv')
print(ff)

