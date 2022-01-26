from faulthandler import disable
from xml.etree.ElementTree import Comment
import pandas as pd
dataframe  = pd.read_csv('mrg.csv')
dataframe = dataframe[dataframe['comments_disabled'] == True ]
dataframe.to_csv('cleaned/commentaire.csv', index=False)
print(dataframe)

    
