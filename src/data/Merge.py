import pandas as pd
# encode = utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv", header=None)
df2 = pd.read_csv("data/raw/youtube-2.csv", header=None)
df3 = pd.read_csv("data/raw/youtube-3.csv", header=None)
df4 = pd.read_csv("data/raw/youtube-4.csv", header=None)
df5 = pd.read_csv("data/raw/youtube-5.csv", header=None)
dataframe = pd.concat([df1, df2, df3, df4, df5])
dataframe.to_csv('mrg.csv', index=False)
print('mrg.csv')
dataframe.drop(dataframe.columns[15], axis=1, inplace=True)#dropping the column n°15 (description)
dataframe.drop(dataframe.columns[13], axis=1, inplace=True)# dropping the other usless column the "thumbnail_link" one
new_header = dataframe.iloc[0]  # grab the first row for the header
dataframe = dataframe[1:]  # take the data less the header row
dataframe.columns = new_header  # set the header row as the df header
dataframe.to_csv('mrg.csv', index=False)
print(dataframe)
