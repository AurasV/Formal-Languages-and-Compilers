import re


def transform_string(input_string):
    switched_string = ''.join(char.upper() if char.islower() else char.lower() for char in input_string)
    print(f"Swap case: {switched_string}")

    result_string = re.sub(r'[A-Z]', '', switched_string)
    print(f"Remove Uppercase: {result_string}")

    return result_string


examples = ["StuDeNT", "Python", "RegularEXPRESSION", "Example123"]
for example in examples:
    print(f"\nOriginal: {example}")
    transform_string(example)
