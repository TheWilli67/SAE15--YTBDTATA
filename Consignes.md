# Data sets location
This directory contains three another ones related to the data sets and called **raw**, **processed**, **cleaned**. A description of each one is given below. 

## Raw directory
This directory contains original and immutable data sets. Do not edit your raw data, especially with Excel, open files only in read only mode. This directory contains four csv files, each one contains a part of the dataset. Each date file is structured as follows, however only the first one has an header :

- video_id : an uniq video ID
- trending_date : when the data are registered in this dataset
- title : video title
- channel_title : the video creator
- category_id : category ID
- publish_time : whan the video has been published
- tags : keywords related to the video
- views : number of views
- likes : number of likes
- dislikes : number of dislikes
- comment_count : number of comments 
- thumbnails_links : web link to the thumbnails
- comment_disabled : if the video comment is disabled
- ratings_disabled : if the video rating is disabled
- video_error or removed : if the video has been removed 
- description : a brief description 

## Processed directory
This directory contains intermediate transformed data sets. This working directory could contain multiple data sets.

## Cleaned directory
This directory contains canonical data sets could be used for publication. Theses data sets would be used for the analysis.
