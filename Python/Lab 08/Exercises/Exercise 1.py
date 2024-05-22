import re

a = "rectangle"
b = "square"
c = "sphere"
d = "triangle"
e = "cone"
f = "cube"
g = "cylinder"

pattern = re.compile(r'^(c|s).*e$')

words = [a, b, c, d, e, f, g]

for word in words:
    if pattern.match(word):
        print(word)
