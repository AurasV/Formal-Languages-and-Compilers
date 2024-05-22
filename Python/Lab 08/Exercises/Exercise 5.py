import re


def match(text):
    pattern = re.compile(r'^hi{2,3}$')
    if pattern.match(text):
        return True
    else:
        return False


correct = "hii"
print(match(correct))
incorrect = "hiiii"
print(match(incorrect))
