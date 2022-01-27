import pandas as pd
import numphy as np
dataframe = pd.read_csv('cleaned/file_merged.csv')
numphy = (dataframe.iloc[:, [8]])
print(numphy)
if len(numphy)<0 :
