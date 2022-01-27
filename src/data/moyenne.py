import pandas as pd
dataframe = pd.read_csv('cleaned/file_merged.csv')
l=dataframe['likes']
l=pd.DataFrame(l)
print(l) #affiche la colone likes
means=l.mean() #calcule la moyenne
print("Means of Each Column:")
print(means) #affiche la moyenne des likes