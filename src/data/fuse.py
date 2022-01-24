import pandas as pd

df1 = pd.read_csv('data/raw/youtube-1.csv')
df2 = pd.read_csv('data/raw/youtube-2.csv')
df3 = pd.read_csv('data/raw/youtube-3.csv')
df4 = pd.read_csv('data/raw/youtube-4.csv')
df5 = pd.read_csv('data/raw/youtube-5.csv')

final_dataframe = pd.concat([df1, df2, df3, df4, df5, ])

print(final_dataframe)

final_dataframe.to_csv(
    'youtube-0.csv', index=False)
