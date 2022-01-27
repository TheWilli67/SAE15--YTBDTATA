from inspect import currentframe, getframeinfo
import pandas as pd
import numphy as np
dataframe = pd.read_csv('cleaned/file_merged.csv')
numphy = (dataframe.iloc[:, [0]])
print(numphy)
if len(numphy)<11 :
    

print(frameinfo)