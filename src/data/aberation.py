from email import header
from matplotlib.pyplot import axis
from numpy import NaN, true_divide
import pandas as pd

dataframe = pd.read_csv('cleaned/file_merged.csv')
dataframe = dataframe[dataframe['video_id'].notna()]
#dataframe = dataframe[dataframe['ratings_disabled'].notna()]

print(dataframe)
dataframe.to_csv('cleaned/abb.csv', index=False)
