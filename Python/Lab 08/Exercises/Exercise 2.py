given = "rectangle square sphere triangle cone cube cylinder"

words = given.split()

for word in words:
    if word.endswith("le") or word.endswith("re"):
        print(word)
