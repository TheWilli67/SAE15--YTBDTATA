import pandas as pd
def ComputeMean():
    dataframe = pd.read_csv('cleaned/file_merged.csv')
    l=dataframe['likes']
    l=pd.DataFrame(l)
    print(l) #affiche la colone likes
    means=l.mean() #calcule la moyenne
    means=int(means)
    print(means) #affiche la moyenne des likes
    dl=dataframe['dislikes']
    dl=pd.DataFrame(dl)
    print(dl) #affiche la colone dislikes
    means=dl.mean() #calcule la moyenne
    means=int(means)
    print("Means of Each Column:")
    print(dl.means,l.means) #affiche la moyenne des dislikes
    return ""
print(ComputeMean())

