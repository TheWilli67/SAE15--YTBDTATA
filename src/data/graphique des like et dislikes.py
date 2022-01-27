import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('cleaned/file_merged.csv')
df[['likes', 'dislikes']].plot(
    xlabel='Nombres de vidéos',
    title='Likes vs Dislikes'
)

plt.show()