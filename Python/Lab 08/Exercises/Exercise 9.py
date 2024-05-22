import re


def match(text):
    pattern = re.compile(r'^[A-Z]+_[a-z]+$')
    return bool(pattern.match(text))


correct = "FILS_aurel"
print(match(correct))
incorrect = "FILS_Frimu"
print(match(incorrect))
