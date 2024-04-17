import re


def check_content(text):
    pattern = re.compile(r'^[a-z0-9*]*$')
    return bool(pattern.match(text))


correct = "abc123*"
print(check_content(correct))
incorrect = "abcA123"
print(check_content(incorrect))
