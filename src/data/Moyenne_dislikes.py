import pandas as pd
def ComputeMean():
    dataframe = pd.read_csv('cleaned/file_merged.csv')
    dl=dataframe['dislikes']
    dl=pd.DataFrame(dl)
    print(dl) #affiche la colone dislikes
    means=dl.mean() #calcule la moyenne
    means=int(means)
    print("Means of Each Column:")
    print(means) #affiche la moyenne des dislikes
    return ""
print(ComputeMean())
