import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Exercise 1
    header = soup.select_one('div.col-sm-8.h1').get_text(strip=True)

    # Exercise 2
    buttons = [button.get_text(strip=True) for button in soup.find_all('button')]

    # Exercise 3
    products = soup.find_all('article', class_='product_pod')
    product_info = [{'title': product.h3.a['title'],
                     'price': product.find('p', class_='price_color').text}
                    for product in products]

    # Exercise 4
    categories = soup.find('ul', class_='nav nav-list').find_all('li')
    category_names = [category.get_text(strip=True) for category in categories[1:]]  # skip the first 'Books' category

    # Exercise 5
    images = soup.find_all('img', alt=True)
    img_alt_texts = [image['alt'] for image in images]

    print("Website Header:", header)
    print("\nButton Texts:", buttons)
    print("\nProduct Info:", product_info)
    print("\nCategory Names:", category_names)
    print("\nImage Alt Texts:", img_alt_texts)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

a = input()