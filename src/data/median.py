from statistics import median
import pandas as pd
def ComputeMean():
    dataframe = pd.read_csv('cleaned/file_merged.csv')
    dl=dataframe['views']
    dl=pd.DataFrame(dl)
    median=dl.median() #calcule la median 
    median=int(median)
    print("Nombre median des vues")
    print(median) #affiche la median des dislikes
    return ""
print(ComputeMean())

