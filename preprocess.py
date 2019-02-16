# Mirko Mantovani


import re
import string

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
    doc = [s for s in doc if not lesseq_two_letters(s)]

    # Converting all words to lowercase
    doc = [x.lower() for x in doc]

    return doc
