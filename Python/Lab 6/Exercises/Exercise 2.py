import random

l = []

n=int(input("Elements in list:"))
for i in range(0,n):
    x=int(input("Enter element:"))
    l.append(x)
print("List:",l)

print("Randomized list:")
random.shuffle(l)
print(l)