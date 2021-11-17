import pandas as pd
import itertools
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

business = pd.read_csv('bars_business.csv')
review = pd.read_csv('bars_review.csv')

busi_revi = pd.merge(review, business, how='left', on='business_id')


def rm_punctuation(sent):
    return "".join([c for c in sent if c not in string.punctuation])


def lower_(sent):
    return sent.lower()


eng_words = set(nltk.corpus.words.words())


def rm_non_eng(words):
    return [w for w in words if w in eng_words or not w.isalpha()]


stop_words = stopwords.words('english')


def rm_stopwords(words):
    return [w for w in words if not w in stop_words]


def lemmatize(words):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in words]


busi_revi['text'] = busi_revi['text'].apply(rm_punctuation).apply(lower_).apply(
    word_tokenize).apply(rm_non_eng).apply(rm_stopwords).apply(lemmatize)
busi_revi.to_csv('busi_revi.csv', index=False)
