import re

txt = "12 apples, 33 oranges, 25 bananas, 11 watermelon, 72 pears, 43 peaches, 86 plums, 27 strawberries, 65 cherries, 41 grapes, 32 blueberries"
pattern = re.compile(r"(\d+) (\w+)")
matches = pattern.findall(txt)

print("All matches:")
for match in matches:
    print(match)

for match in pattern.finditer(txt):
    quantity = match.group(1)
    stuff = match.group(2)
    print(f"Quantity: {quantity}, Stuff: {stuff}")
