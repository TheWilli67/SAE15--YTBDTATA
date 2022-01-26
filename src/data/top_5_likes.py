import pandas as pd
dataframe = pd.read_csv('cleaned/file_merged.csv')
ff = dataframe.sort_values('likes', ascending=False)[:5]
ff.to_csv('cleaned/top_5.csv', index=True, header=None)
print(ff)

