import pickle
from preprocess import preprocess
import operator
from collections import Counter
import math

# Query text got from the HTML get request input in the search form
query_text = 'sex crush school'

with open('memes_inverted_index.pickle', 'rb') as handle:
    inverted_index = pickle.load(handle)

with open('idf.pickle', 'rb') as handle:
    idf = pickle.load(handle)


def inner_product_similarities(query_tokens):
    # dictionary in which I'll sum up the similarities of each word of the query_tokens with each document in
    # which the word is present, key is the doc number,
    # value is the similarity between query_tokens and document
    # UPDATED: I started to store tf idf in inverted index, no need of recompute them and wrong to do it now
    # it was like this before: similarity[doc] = similarity.get(doc, 0) + self.tf_idf(word, doc) * wq
    similarity = {}
    for word in query_tokens:
        wq = idf.get(word, 0)
        if wq != 0:
            for doc in inverted_index[word].keys():
                similarity[doc] = similarity.get(doc, 0) + inverted_index[word][doc] * wq
    return similarity


def cosine_similarities(query):
    similarity = inner_product_similarities(query)
    # for doc in similarity.keys():
        # similarity[doc] = similarity[doc] / doc_length[doc] / query_length(query)
    return similarity



query_tokens = preprocess(query_text)

ranking = cosine_similarities(query_tokens)


sorted_ranking = sorted(ranking.items(), key=operator.itemgetter(1),reverse=True)

print(sorted_ranking)



# def query_length(query):
#     length = 0
#     cnt = Counter()
#     for w in query:
#         cnt[w] += 1
#     for w in cnt.keys():
#         length += (cnt[w]*idf.get(w, 0)) ** 2
#     return math.sqrt(length)



