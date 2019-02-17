import requests, urllib
import os, sys, time
import urllib.request
from inverted_index_builder import build_inverted_index
import pickle
import ocr

def getPosts(subreddit, n):
    # print('getPosts')
    urls = set()
    seconds = int(time.time())
    counter = 0
    for epoch_time in range(seconds, seconds - 21600 * n, -21600):
        print(counter)
        counter += 1
        url = f'https://api.pushshift.io/reddit/submission/search/?sort=new&subreddit={subreddit}&before={epoch_time}'
        headers = {
            'User-Agent': 'Reddit Wallpaper Scraper 1.0'
        }
        r = requests.get(url, headers=headers)
        if r.status_code == requests.codes.ok:
            data = r.json()
            for post in data['data']:
                urls.add(post['url'])
    return urls

def extractURLs(urls):
    images_urls = []
    allowed_suffixes = (".png", ".jpg", ".gif")
    for url in urls:
        # print(url)
        if url.endswith(allowed_suffixes):
            images_urls.append(url)
        else:
            print('not in allowed suffixes')
    return images_urls

# Calls Reddit API, retrieves JSON file, parses it and gets all urls in the specified
# subreddit with a limit of postLimit
def get_img_urls_from_subreddit(subreddit = 'AdviceAnimals'):
    urls = getPosts(subreddit, 1000)
    img_urls = extractURLs(urls)
    print(len(img_urls))
    return img_urls


def main():
    if len(sys.argv) > 1:
        meme_urls = get_img_urls_from_subreddit(sys.argv[1])
    else:
        meme_urls = get_img_urls_from_subreddit('AdviceAnimals')

    # quit(23)
    # API calls to Google Vision API of GCP
    dictionary_memes = ocr.process_image_urls(meme_urls)

    # Building inverted index
    inverted_index = build_inverted_index(dictionary_memes)

    # print(inverted_index)

    # Storing inverted index with pickle
    with open('memes_inverted_index.pickle', 'wb') as handle:
        pickle.dump(inverted_index, handle, protocol=pickle.HIGHEST_PROTOCOL)



if __name__ == '__main__':
    main()