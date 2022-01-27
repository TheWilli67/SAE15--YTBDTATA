import pandas as pd
def ComputeMean():
    dataframe = pd.read_csv('cleaned/file_merged.csv')
    l=dataframe['likes']
    l=pd.DataFrame(l)
    print(l) #affiche la colone likes
    means=l.mean() #calcule la moyenne
    means=int(means)
    print("Means of Each Column:")
    print(means) #affiche la moyenne des likes
    return ""
print(ComputeMean())

