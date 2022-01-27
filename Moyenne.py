import pandas as pd
def ComputeMean():
    dataframe = pd.read_csv('cleaned/file_merged.csv')
    l=dataframe['likes']
    l=pd.DataFrame(l)
    means=l.mean() #calcule la moyenne des likes
    means=int(means)
    dl=dataframe['dislikes']
    dl=pd.DataFrame(dl)
    #print(l,dl) #affiche la colone des likes et des dislikes
    means1=dl.mean() #calcule la moyenne des dislikes
    means1=int(means1)
    print("Means of Each Column:")
    print("likes",means,"dislikes",means1) #affiche les moyennes
    return ""
print(ComputeMean())
