import re


def match(text):
    pattern = re.compile(r'^m...n$')
    if pattern.match(text):
        return True
    else:
        return False


correct = "manan"
print(match(correct))
incorrect = "manaremeren"
print(match(incorrect))
