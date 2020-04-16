import operator
import json
from collections import Counter
from nltk.corpus import stopwords
import string

from twitterdataminer import preprocess

fname = '../json/tweets.json'

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'rt', 'via']

with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # terms_all = [term for term in preprocess(tweet['text'])]
        # Update the counter
        count_all.update(terms_stop)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))
