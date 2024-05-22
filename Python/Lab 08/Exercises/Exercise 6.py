import re


def match(text):
    pattern = re.compile(r'\b\w*q\w*\b', re.IGNORECASE)
    matches = pattern.findall(text)
    filtered_matches = [match for match in matches if not match.lower().startswith('q') and not match.lower().endswith('q')]
    return filtered_matches


correct = "The quick brown fox jumps over the lazy dog. Unique word goes here."
print(match(correct))
incorrect = "Quran is a holy book."
print(match(incorrect))
