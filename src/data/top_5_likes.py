import pandas as pd
dataframe = pd.read_csv('cleaned/file_merged.csv')
ff = dataframe.sort_values('dislikes', ascending=False)[:4]
dataframe.drop(dataframe.columns['video_id'], axis=1, inplace=True)
ff.to_csv('cleaned/top_5.csv')
print(ff)

