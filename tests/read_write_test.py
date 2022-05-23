import sys
import os
sys.path.append('../')

from n_grams import frequencies, write_table, read_table

text = "Het valt voor, dat bij één roveroverval, één rover voorover over één roverval valt."
table = frequencies(text, 3, limit=10)
print(table)
write_table(table, "rover.10.TEMP")
reread_table = read_table("rover.10.TEMP")
print(reread_table)

if table == reread_table:
    print("ok")
else:
    import sys

    print("The round trip fails", file=sys.stderr)

# remove temporary file
os.remove("rover.10.TEMP")