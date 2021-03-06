import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('cleaned/file_merged.csv')
df[['likes', 'dislikes']].plot(
    xlabel='x',
    ylabel='y',
    title='Grapique des vidéos les + et - likées'
)

plt.show()
