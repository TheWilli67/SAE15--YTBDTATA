from statistics import median
import pandas as pd
def ComputeMedian():
    dataframe = pd.read_csv('cleaned/file_merged.csv')
    l=dataframe['likes']
    l=pd.DataFrame(l)
    median=l.median() #calcule la median des likes
    median=int(median)
    dl=dataframe['dislikes']
    dl=pd.DataFrame(dl)
    #print(l,dl) #affiche la colone des likes et des dislikes
    median1=dl.median() #calcule la median des dislikes
    median1=int(median1)
    print("Median of Each Column:")
    print("likes",median,"dislikes",median1) #affiche les medians
    return ""
print(ComputeMedian())
