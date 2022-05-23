import sys
sys.path.append('../')

from n_grams import frequencies

top = frequencies("hiep, hiep, hoera!", n=3, limit=4)

print("top:", top)

if top == {'<hi': 2, 'hie': 2, 'ep>': 2, 'iep': 2}:
    print("ok")
else:
    import sys
    print("Incorrect result", file=sys.stderr)