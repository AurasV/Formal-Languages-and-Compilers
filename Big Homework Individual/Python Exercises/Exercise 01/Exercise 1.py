import re


def to_snake_case(s):
    words = re.findall(r'[A-Za-z][a-z]*|\d+', s)
    snake_case = '_'.join(words).lower()
    return snake_case


examples = ["Hello JavaScript", "ThisIsCamelCase", "HiPython", "Another Example DUh"]
snake_cases = [to_snake_case(example) for example in examples]
for original, converted in zip(examples, snake_cases):
    print(f"Original: {original} -> Snake case: {converted}")
