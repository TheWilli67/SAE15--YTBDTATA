from base64 import encode
import pandas as pd
# encode = utf_8
df1 = pd.read_csv("data/raw/youtube-1.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])
# pd.read_csv lit le fichier dans les ( ) sep = separateur / names c'est les titre des categories
df2 = pd.read_csv("data/raw/youtube-2.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])
# pd.read_csv lit le fichier dans les ( ) sep = separateur / names c'est les titre des categories
df3 = pd.read_csv("data/raw/youtube-3.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])
# pd.read_csv lit le fichier dans les ( ) sep = separateur / names c'est les titre des categories
df4 = pd.read_csv("data/raw/youtube-4.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])
# pd.read_csv lit le fichier dans les ( ) sep = separateur / names c'est les titre des categories
df5 = pd.read_csv("data/raw/youtube-5.csv",
                  sep=',',
                  names=["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views,likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"])
# pd.read_csv lit le fichier dans les ( ) sep = separateur / names c'est les titre des categories

dataframe = pd.concat([df1, df2, df3, df4, df5])
print(dataframe)
# print dataframe pour voir ce qu'il va merge dans le fichier .csv

dataframe.to_csv('mrg.csv', index=False)
