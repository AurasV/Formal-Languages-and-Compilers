import re


def replace_caps_and_digits(source, target):
    pattern = re.compile(r'\b[A-Z0-9]+\b')

    with open(source, 'r') as file:
        content = file.read()

    modified = pattern.sub('$', content)

    with open(target, 'w') as file:
        file.write(modified)


source_file = 'ex4input.txt'
target_file = 'ex4output.txt'
replace_caps_and_digits(source_file, target_file)
