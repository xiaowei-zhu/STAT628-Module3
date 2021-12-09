import pandas as pd
import numpy as np
import scipy
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

busi_revi = pd.read_csv("busi_revi.csv")
business = pd.read_csv('bars_business.csv')


def join_(lst):
    return " ".join(lst)


busi_revi['text'] = busi_revi['text'].apply(eval).apply(join_)

d = dict()
wordlist = ['service', 'wait', 'table', 'time', 'staff', 'bartender', 'hour', 'food', 'chicken',
            'burger', 'cheap', 'affordable', 'expensive', 'drink', 'beer', 'cocktail', 'place', 'music', 'quiet']
for word in wordlist:
    d[word] = word

comment_df = pd.DataFrame(data=np.nan, index=business.index, columns=wordlist)
comment_df['business_id'] = business['business_id']
business = business.merge(comment_df, on='business_id')


def compare_test(business_id, keyword, alpha, comment):
    a = (busi_revi[busi_revi['text'].str.contains(keyword)])['stars_x'].values
    b = (busi_revi[(busi_revi['text'].str.contains(keyword)) & (
        busi_revi['business_id'] == business_id)])['stars_x'].values
    t, pval = scipy.stats.ttest_ind(a, b, equal_var=False)
    # Null hypothesis: Rating_a <= Rating b
    # Alternative hypothesis: Rating_a > Rating_b
    if t > 0 and pval / 2 < alpha:
        return comment
    return np.nan


for i, b_id in enumerate(business['business_id']):
    for kw in wordlist:
        business.loc[i, kw] = compare_test(b_id, kw, 0.05, d[kw])


def give_rating(business_id, keyword):
    if keyword == 'overall':
        a = busi_revi['stars_x'].values
        b = busi_revi[busi_revi['business_id']
                      == business_id]['stars_x'].values
    else:
        a = (busi_revi[busi_revi['text'].str.contains(keyword)])[
            'stars_x'].values
        b = (busi_revi[(busi_revi['text'].str.contains(keyword)) & (
            busi_revi['business_id'] == business_id)])['stars_x'].values
    return a.mean(), b.mean()


wordlist_rating = ['service', 'food', 'drink', 'place', 'overall']
wordlist_rating_plus = [w + '_rating' for w in wordlist_rating]
wordlist_rating_plus += [w + '_rating_total' for w in wordlist_rating]

rating_df = pd.DataFrame(
    data=np.nan, index=business.index, columns=wordlist_rating_plus)
rating_df['business_id'] = business['business_id']
business = business.merge(rating_df, on='business_id')

for i, b_id in enumerate(business['business_id']):
    for kw in wordlist_rating:
        business.loc[i, kw + '_rating_total'], business.loc[i,
                                                            kw + '_rating'] = give_rating(b_id, kw)

business_rating.to_csv('business_rating.csv')
