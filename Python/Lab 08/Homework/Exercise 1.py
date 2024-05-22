import re


with open("HW8Ex1.html", "r") as file:
    html_content = file.read()

links = re.findall(r'<a\s+href="(.*?)">', html_content)
print("Links:")
for link in links:
    print(link)

labels = re.findall(r'<label\s+for="(.*?)">(.*?)</label>', html_content)
print("\nLabels:")
for label_for, label_text in labels:
    print(label_text)

input_fields = re.findall(r'<input\s+type="(.*?)"', html_content)
print("\nInput field types:")
for field_type in input_fields:
    print(field_type)

options = re.findall(r'<option\s+value="(.*?)">(.*?)</option>', html_content)
print("\nOptions:")
for option_value, option_text in options:
    print(option_value)

ids = re.findall(r'<input\s+type=".*?"\s+id="(.*?)"', html_content)
print("\nIDs in the form:")
print(ids)
