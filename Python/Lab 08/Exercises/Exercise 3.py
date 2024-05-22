def replace_chars(input):
    modified = input.replace("a", "u")
    modified = modified.replace("i", "e")
    return modified


given = "This is an example string chosen randomly, why? I don't know either."
result = replace_chars(given)
print(result)
