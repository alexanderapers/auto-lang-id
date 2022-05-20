import re

def tokenize(text):
    return re.sub(r"[!?\",.()<>]", " ", text).split()
