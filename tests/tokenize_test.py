import sys
sys.path.append('../')

from n_grams import tokenize

tokens = tokenize('This is <cough,cough> "HAL-9000".  Don\'t touch!')
print(tokens)

# Test:
if tokens == ['This', 'is', 'cough', 'cough', 'HAL-9000', "Don't", 'touch']:
    print("ok")
else:
    import sys
    print("Incorrect result", file=sys.stderr)