from base64 import encode
from numpy import delete, true_divide
import pandas as pd
# encode = utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv")
df2 = pd.read_csv("data/raw/youtube-2.csv")
df3 = pd.read_csv("data/raw/youtube-3.csv")
df4 = pd.read_csv("data/raw/youtube-4.csv")
df5 = pd.read_csv("data/raw/youtube-5.csv")
dataframe = pd.concat([df1])
print(dataframe)
if 'mrg.csv' == True:
    delete('mrg.csv')
dataframe.to_csv('mrg.csv', index=False)
