import re


def find_urls(input_file_path, output_file_path):
    url_pattern = re.compile(r'https?://(?:www\.)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z0-9-]+(?:/[^\s]*)?')

    found_urls = set()

    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            urls = url_pattern.findall(line)
            found_urls.update(urls)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for url in found_urls:
            file.write(url + '\n')


input_file_path = 'ex3input.txt'
output_file_path = 'ex3output.txt'
find_urls(input_file_path, output_file_path)
