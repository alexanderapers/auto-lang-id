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

    if limit == 0:
        return {k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}

    return dict(freq.most_common(n=limit))


def write_table(freq_table, filename):
    with open(filename, "w", encoding="utf8") as conn:
        for ngram in freq_table:
            conn.write(str(freq_table[ngram]) + " " + ngram + "\n")


def read_table(filename):
    result = dict()

    with open(filename, "r", encoding="utf8") as conn:
        lines = conn.read()
        for line in lines.split("\n"):
            if line is not "":
                line_values = line.split(" ")
                value = int(line_values[0])
                key = line_values[1]
                result[key] = value

    return result
