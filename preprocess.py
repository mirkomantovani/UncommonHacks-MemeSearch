# Mirko Mantovani


import re
import string
from nltk.stem import PorterStemmer


# removing digits and returning the word
def replace_digits(st):
    return re.sub('\d', '', st)


# returns true if the word has less or equal 2 letters
def lesseq_two_letters(word):
    return len(word) <= 2


STOP_WORDS_PATH = "./stopwords.txt"

with open(STOP_WORDS_PATH, "r") as stop_file:
    stop_words = stop_file.readlines()

stop_words = list(map(lambda x: x[:-1], stop_words))

ps = PorterStemmer()


def stem(word):
    return ps.stem(word)


def preprocess(doc):
    # Splitting on whitespaces
    doc = doc.split()

    # Converting all words to lowercase
    doc = [x.lower() for x in doc]

    # Stop word elimination
    doc = [s for s in doc if s not in stop_words]
    # Porter Stemmer
    doc = list(map(stem, doc))

    # Applying stop word elimination again
    doc = [s for s in doc if s not in stop_words]


    # Removing punctuations in words
    doc = [''.join(c for c in s if c not in string.punctuation) for s in doc]

    # Replace numbers with empty string
    doc = map(replace_digits, doc)

    # Removing empty words
    doc = [s for s in doc if s]


    return doc
