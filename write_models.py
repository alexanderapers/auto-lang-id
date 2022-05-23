from os.path import isdir, join
import os

def make_models(path, n, limit):
    if not isdir("./models"):
        os.mkdir("./models")

    if not isdir(f"./models/{n}-{limit}"):
        os.mkdir(f"./models/{n}-{limit}")





if __name__ == "__main__":
    make_models("./datafiles/training", n=3, limit=200)
    make_models("./datafiles/training", n=2, limit=200)