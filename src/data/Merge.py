from base64 import encode
from email import header
from pickle import NONE
from numpy import delete, true_divide
import pandas as pd
# encode = utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])

df2 = pd.read_csv("data/raw/youtube-2.csv", header=None)
df3 = pd.read_csv("data/raw/youtube-3.csv", header=None)
df4 = pd.read_csv("data/raw/youtube-4.csv", header=None)
df5 = pd.read_csv("data/raw/youtube-5.csv", header=None)
dataframe = pd.concat([df1, df2, df3, df4])
print(dataframe)
dataframe.to_csv('mrg.csv', index=False)
