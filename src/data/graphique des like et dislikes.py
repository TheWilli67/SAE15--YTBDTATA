import matplotlib.pyplot as plt
import pandas as pd
#df = pd.read_csv('cleaned/file_merged.csv')
#df[['likes', 'dislikes']].plot(
   #xlabel='Nombres de vidéos',
  #title='Likes vs Dislikes')

#plt.show()
dataframe = pd.read_csv('cleaned/file_merged.csv')
df=dataframe['like']
df=pd.DataFrame(df)
print(df)
df[df[["likes"] > 700000 ]].plot(
   xlabel='Nombres de vidéos',
   title='Likes vs Dislikes')

plt.show()
