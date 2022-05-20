import re

def tokenize(text):
    return re.sub(r"[!?\",.()<>]", " ", text).split()


def convert_to_ngrams(sequence, n=3):
    number_ngrams = len(sequence) - n + 1
    return [sequence[i:i+n] for i in range(number_ngrams)]