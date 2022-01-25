from base64 import encode
import os
from numpy import delete, true_divide
import pandas as pd

# encode = utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv", header=None)

dataframe = pd.concat([df1])
print(dataframe)

dataframe.to_csv('mrg.csv', index=False)

df = pd.read_csv("mrg.csv",
                 sep=',',
                 names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])

dataframe.to_csv('mrrg.csv', index=False)
os.remove('mrg.csv')
