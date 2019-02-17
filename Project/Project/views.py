from django.http import HttpResponse
from django.template import loader
import pickle
import re
import string
import operator
from collections import Counter
import math


# removing digits and returning the word
def replace_digits(st):
    return re.sub('\d', '', st)


# returns true if the word has less or equal 2 letters
def lesseq_two_letters(word):
    return len(word) <= 2


def preprocess(doc):
    # Splitting on whitespaces
    doc = doc.split()

    # Removing punctuations in words
    doc = [''.join(c for c in s if c not in string.punctuation) for s in doc]

    # Replace numbers with empty string
    doc = map(replace_digits, doc)

    # Removing empty words
    doc = [s for s in doc if s]

    # Removing words with len less or equal to 2
    # doc = [s for s in doc if not lesseq_two_letters(s)]

    # Converting all words to lowercase
    doc = [x.lower() for x in doc]

    return doc

def inner_product_similarities(query_tokens,idf,inverted_index):
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


def cosine_similarities(query,idf,inverted_index):
    similarity = inner_product_similarities(query,idf,inverted_index)
    # for doc in similarity.keys():
        # similarity[doc] = similarity[doc] / doc_length[doc] / query_length(query)
    return similarity


def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

def results(request):
    query_text = request.GET['query']
    #INSERT PROCESSING HERE #

    with open('/home/abhishekvasudevan/apps/django/django_projects/Project/Project/memes_inverted_index.pickle', 'rb') as handle:
        inverted_index = pickle.load(handle)

    with open('/home/abhishekvasudevan/apps/django/django_projects/Project/Project/idf.pickle', 'rb') as handle:
        idf = pickle.load(handle)
    query_tokens = preprocess(query_text)
    ranking = cosine_similarities(query_tokens,idf,inverted_index)
    sorted_ranking = sorted(ranking.items(), key=operator.itemgetter(1), reverse=True)
    res = []
    for item in sorted_ranking:
        res.append(item[0])
    #res = ["https://i.redd.it/flnltgom9zg21.jpg","https://i.redd.it/20ine7d2ntg21.jpg","https://i.redd.it/uwtae12j0tg21.jpg"]
    template = loader.get_template("results.html")
    context = {'images' : res,'query':query_text}
    return HttpResponse(template.render(context,request))



def home(request):
    template = loader.get_template("home.html")
    context = {'value' : ""}
    return HttpResponse(template.render(context,request))





