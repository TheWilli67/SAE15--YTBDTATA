import pandas as pd
import os
from encodings import utf_8
coding: utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])
df2 = pd.read_csv("data/raw/youtube-2.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])

df3 = pd.read_csv("data/raw/youtube-3.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])

df4 = pd.read_csv("data/raw/youtube-4.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])

df5 = pd.read_csv("data/raw/youtube-5.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])


final_dataframe = pd.concat([df1, df2, df3, df4, df5])
print(final_dataframe)

final_dataframe.to_csv('youtube-0.csv', index=False)
