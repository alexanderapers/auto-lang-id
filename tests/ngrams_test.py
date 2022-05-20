import sys
sys.path.append('../')

from n_grams import convert_to_ngrams

trigrams = convert_to_ngrams("R2.D2")
print(trigrams)

# Test:
if trigrams == ['R2.', '2.D', '.D2']:
    print("ok")
else:
    import sys

    print("Incorrect result", file=sys.stderr)

bigrams = convert_to_ngrams("R2.D2", 2)
print(bigrams)

# Test:
if bigrams == ['R2', '2.', '.D', 'D2']:
    print("ok")
else:
    import sys

    print("Incorrect result", file=sys.stderr)
