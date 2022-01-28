import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('cleaned/file_merged.csv')
#df[['likes', 'dislikes']].plot(
 # xlabel='Nombres de vidéos',
 # title='Likes vs Dislikes')
#plt.show()
likes=df['likes']
dislikes=df['dislikes']
comparateur=0
longueurdf=len(df)
for index, row in df.iterrows():
    if row['likes'] > row['dislikes']:
        comparateur+=1
#print (comparateur)
comparateur=40723-comparateur
plt.figure(figsize = (8, 8))
x = [39500,comparateur]
plt.pie(x, labels = ['Likes', 'Dislikes'],
           colors = ['red', 'green'],
           explode = [0, 0.2],
           autopct = lambda x: str(round(x, 2)) + '%',
           pctdistance = 0.7, labeldistance = 1.4,
           shadow = False)
plt.legend()
plt.show()