import sys
sys.path.append('../')

from n_grams import cosine_similarity, magnitude

table1 = { "<he": 2, "het": 1 }
table2 = { "<he": 2, "hem": 1 }

score = cosine_similarity(table1, table2)

# The score *should be* 0.8, but we get floating point error
print(score)

if abs(score - 4/5) < 0.000001:
    print("ok")
else:
    import sys
    print("Incorrect result", file=sys.stderr)

