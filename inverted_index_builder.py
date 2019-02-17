# # Inverted Index
from preprocess import preprocess
import math
import pickle

# my inverted index is a python dictionary whose key are the words, it retrieves another dictionary indexed with
# doc number

# document frequency = number of docs containing a specific word, dictionary with key = word, value = num of docs
df = {}
# inverse document frequency
idf = {}

inverted_index = {}

# texts_list
def build_inverted_index(meme_dict):

    # Approach with list of texts
    # documents = []
    #
    # for image_text in texts_list:
    #     documents.append(preprocess(image_text))
    #
    # n_images = len(documents)
    #
    # inverted_index = {}
    #
    # for doc in range(n_images):
    #     for word in documents[doc]:
    #         inverted_index.setdefault(word, {})[doc] = inverted_index.setdefault(word, {}).get(doc, 0) + 1

    # Approach with dictionary
    # documents = []

    for url in meme_dict.keys():
        meme_dict[url] = preprocess(meme_dict[url])

    n_images = len(meme_dict.keys())

    # print('len images')
    # print(n_images)


    for url in meme_dict.keys():
        for word in meme_dict[url]:
            inverted_index.setdefault(word, {})[url] = inverted_index.setdefault(word, {}).get(url, 0) + 1


    for key in inverted_index.keys():
        df[key] = len(inverted_index[key].keys())
        # print('len images2')
        #
        # print(n_images)
        # print(n_images / df[key])
        idf[key] = math.log(n_images / df[key], 2)

        # store idf

    with open('idf.pickle', 'wb') as handle:
        pickle.dump(idf, handle, protocol=pickle.HIGHEST_PROTOCOL)

    for word in inverted_index:
        for doc_key in inverted_index[word]:
            inverted_index[word][doc_key] = tf_idf(word, doc_key)

    return inverted_index





    # # document frequency = number of docs containing a specific word, dictionary with key = word, value = num of docs
    # df = {}
    # # inverse document frequency
    # idf = {}




def tf_idf(word, doc):
    return inverted_index[word][doc] * idf[word]