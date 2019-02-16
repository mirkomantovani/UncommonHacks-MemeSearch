# # Inverted Index
import preprocess
import math

# my inverted index is a python dictionary whose key are the words, it retrieves another dictionary indexed with
# doc number (already incremented by one so that it is the actual document cranfieldXXXX with XXXX the index of
# the inner dictionary)
def build_inverted_index(texts_list):
    documents = []

    for image_text in texts_list:
        documents.append(preprocess(image_text))

    n_images = len(documents)

    inverted_index = {}

    for doc in range(n_images):
        for word in documents[doc]:
            inverted_index.setdefault(word, {})[doc + 1] = inverted_index.setdefault(word, {}).get(doc + 1, 0) + 1


    # document frequency = number of docs containing a specific word, dictionary with key = word, value = num of docs
    df = {}
    # inverse document frequency
    idf = {}

    for key in inverted_index.keys():
        df[key] = len(inverted_index[key].keys())
        idf[key] = math.log(n_images / df[key], 2)


    def tf_idf(word, doc):
        return inverted_index[word][doc] * idf[word]