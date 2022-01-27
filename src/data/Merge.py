import pandas as pd
import re
# encode = utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv", header=None)
df2 = pd.read_csv("data/raw/youtube-2.csv", header=None)
df3 = pd.read_csv("data/raw/youtube-3.csv", header=None)
df4 = pd.read_csv("data/raw/youtube-4.csv", header=None)
df5 = pd.read_csv("data/raw/youtube-5.csv", header=None)

dataframe = pd.concat([df1, df2, df3, df4, df5])
dataframe.to_csv('cleaned/file_merged.csv', index=False)

dataframe.drop(dataframe.columns[15], axis=1, inplace=True)
dataframe.drop(dataframe.columns[13], axis=1, inplace=True)# dropping the other usless column the "thumbnail_link" one
dataframe.drop(dataframe.columns[0], axis=0, inplace=True)
dataframe = dataframe.set_axis(["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views", "likes", "dislikes",
                                "comment_count", "comments_disabled", "ratings_disabled", "video_error_or_removed"], axis=1, inplace=False)


dataframe.to_csv('cleaned/file_merged.csv', index=False)
print(dataframe)


#   df1 = pd.read_csv("data/raw/youtube-1.csv",
#                       sep = ',',
#                       names = ["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])
