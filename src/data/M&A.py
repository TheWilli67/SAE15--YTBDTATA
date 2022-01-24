
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv('youtube-mrg.csv')
draft = data.select_dtypes(include=['int'])
