
import pandas as pd
# La méthode dropna() permet de supprimer les données manquantes: on peut spécifier l'axe de suppression axis=0 on supprime les lignes où il y a des données manquantes, axis=1 on supprime les colonnes où il y a des données manquantes
# On peut imputer les valeurs manquantes avec la valeur moyenne ou encore avec la valeur la plus présente dans la colonne.
dfm = pd.read_csv('youtube-mrg.csv')
# df.fillna(df.mean())  # moyenne

pd.concat('youtube-mrg.csv')
print([dfm])
