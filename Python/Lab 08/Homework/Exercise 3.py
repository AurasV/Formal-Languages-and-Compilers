import re


html_tag_pattern = re.compile(r'^<([a-zA-Z][^\s<>]*)(?:\s+[^<>]*)?>.*?<\/\1>$')

examples = [
    "<p, p>",
    "<id=“>",
    "“<p>”",
    "<p/>",
    "<p>Some content</div>",
    "<p class='content'>Some content</p>"
]

for example in examples:
    if html_tag_pattern.match(example):
        print(f"{example}: Correct")
    else:
        print(f"{example}: Incorrect")
