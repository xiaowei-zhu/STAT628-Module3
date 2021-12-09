import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

busi_revi = pd.read_csv("busi_revi.csv")


def join_(lst):
    return " ".join(lst)


busi_revi['text'] = busi_revi['text'].apply(eval).apply(join_)


def tfidf(corpus):
    vectorizer = CountVectorizer(min_df=20)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray().sum(axis=0)

    tfidf_Ser = pd.Series(weight, index=word).sort_values(ascending=False)
    return tfidf_Ser
