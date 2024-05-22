from random import randint

l = []

for i in range(0,5):
    l.append(randint(-2147483647, 2147483647))

print("Randomized list:",l)