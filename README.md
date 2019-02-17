# UncommonHacks-MemeSearch
Uncommon Hacks hackaton project. This project allows to people to search for memes by using keywords included in the text of the Meme images

## Inspiration
The Uncommon Hacks application inspired us to create a project to enhance the accessibility of image macros to the everyday user who may not have a large library of memes at their disposal.

## What it does
The meme-search engine allows you to search for memes based on the text inside, without relying on file names or metadata.

## How we built it
The scraper was written with python using the pushshift.io reddit API. We submit the images to Google Cloud using the python client. We then apply custom processing and built an inverted index from the text of each image. We serve our website through a Django server which searches and ranks all the memes in the database through the inverted index using a custom metric inspired by cosine similarity.

## Challenges we ran into
- Reddit API maxes out at 1000 posts, and not all posts are image links 
- The Cloud Vision API can be very slow and limits requests to 16 images each
- Memes have a tendency to overcrowd text
- weird django syntax

## Accomplishments that we're proud of
- The first ever meme text search engine.
- Working as a team with people we didn't know

## What we learned
- Hosting a website on Google Cloud Engine
- OCR using Google Cloud Vision
- Django
- The basics of Information Retrieval


## What's next for meme-search
- Allow users to upload images to the database
- Further refine search algorithm
- Train a custom ML model to recognize meme formats
- Sharing results
- MOAR SCRAPING
