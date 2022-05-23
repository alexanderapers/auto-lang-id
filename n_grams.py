import re
from collections import Counter

def tokenize(text):
    return re.sub(r"[!?\",.()<>]", " ", text).split()


def convert_to_ngrams(sequence, n=3):
    number_ngrams = len(sequence) - n + 1
    return [sequence[i:i+n] for i in range(number_ngrams)]

def frequencies(text, n=3, limit=0):
    tokens = tokenize(text)
    angled = ["<" + token + ">" for token in tokens]
    ngrams = [convert_to_ngrams(word, n=n) for word in angled]
    all_ngrams = [ngram for word_ngrams in ngrams for ngram in word_ngrams]
    freq = Counter(all_ngrams)
    return dict(freq.most_common(n=limit))


