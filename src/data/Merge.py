from base64 import encode
from email import header
from pickle import NONE
from numpy import delete, true_divide
import pandas as pd
# encode = utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv", header=None)
df2 = pd.read_csv("data/raw/youtube-2.csv", header=None)
df3 = pd.read_csv("data/raw/youtube-3.csv", header=None)
df4 = pd.read_csv("data/raw/youtube-4.csv", header=None)
df5 = pd.read_csv("data/raw/youtube-5.csv", header=None)
dataframe = pd.concat([df1, df2, df3, df4])
print(dataframe)
dataframe.to_csv('mrg.csv', index=False)

df = pd.read_csv("mrg.csv")


new_header = df.iloc[0]  # grab the first row for the header
df = df[1:]  # take the data less the header row
df.columns = new_header  # set the header row as the df header


print(dataframe)
dataframe.to_csv('mrgg.csv', index=False)
