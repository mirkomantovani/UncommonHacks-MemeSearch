import requests, urllib
import os, sys, time
import urllib.request

counter = 0


def getPosts(subreddit, postLimit):
    print('getPosts')
    url = 'http://www.reddit.com/r/' + subreddit + '/.json?limit=' + str(postLimit)
    headers = {
    'User-Agent': 'Reddit Wallpaper Scraper 1.0'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print('Sleeping for 1 seconds...\n')
        time.sleep(1)
        return data['data']['children']
    else:
        print('Sorry, but there was an error retrieving the subreddit\'s data!')
        return None


def saveImages(posts, scoreLimit, save_dir='reddit_memes'):
    print('saveImages')
    for post in posts:
        url = post['data']['url']
        print(url)
        score = post['data']['score']
        title = post['data']['title']
        if 'i.imgur.com' in url and score > scoreLimit:
            saveImage(url, title, save_dir)


def extractURLs(posts, scoreLimit, save_dir='reddit_memes'):
    print('extract URLS')
    images_urls = []
    for post in posts:
        url = post['data']['url']
        print(url)
        score = post['data']['score']
        title = post['data']['title']
        allowed_suffixes = (".png", ".jpg", ".gif")
        if str(url).endswith(allowed_suffixes):
            images_urls.append(str(url))
        else:
            print('not in allowed suffixes')


    return images_urls


def saveImage(url, title, save_dir='reddit_memes'):
    global counter
    save_dir = makeSaveDir(save_dir)
    dot_location = url.rfind('.')
    # print(title)
    # print(url)
    filename = './' + save_dir+title
    # filename = (save_dir + title.replace('/', ':') + url[dot_location: dot_location + 4]).encode('utf-8')
    if not os.path.exists(filename):
        # print('Saving ' + filename + '!\n')
        counter += 1
        urllib.request.urlretrieve(url, filename)


def makeSaveDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir + '/'


def downloadImagesFromReddit(subreddits = 'AdviceAnimals', postLimit=10, scoreLimit=20):
    for subreddit in subreddits:
        posts = getPosts(subreddit, postLimit)
        # we don't need to store images, just need the URLs to make a request to google vision API
        memes_urls = extractURLs(posts, scoreLimit, subreddit.lower())
        # saveImages(posts, scoreLimit, subreddit.lower())
    print(str(len(memes_urls)) + ' images have been scraped!')
    print(memes_urls)


def main():
    if len(sys.argv) > 1:
        downloadImagesFromReddit(sys.argv[1:])
    else:
        downloadImagesFromReddit([
            'AdviceAnimals',
            'memes'
        ])

if __name__ == '__main__':
    main()