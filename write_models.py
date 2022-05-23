from os.path import isdir, join
import os
from n_grams import frequencies, write_table

def make_models(path_to_datafolder, n, limit):
    if not isdir("./models"):
        os.mkdir("./models")

    if not isdir(f"./models/{n}-{limit}"):
        os.mkdir(f"./models/{n}-{limit}")

    for filename in os.listdir(path_to_datafolder):
        language = filename.split("-")[0]
        encoding = filename.split("-")[1]

        with open(join(path_to_datafolder, filename), "r", encoding=encoding) as conn:
            content = conn.read()
            frequencies_dict = frequencies(content, n=n, limit=limit)
            write_table(frequencies_dict, f"./models/{n}-{limit}/{language}")


if __name__ == "__main__":
    make_models("./datafiles/training", n=3, limit=200)
    make_models("./datafiles/training", n=2, limit=200)