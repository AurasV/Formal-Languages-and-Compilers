import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
country_data = []

for country in soup.find_all('div', class_='country'):
    name = country.find('h3', class_='country-name').text.strip()
    capital = country.find('span', class_='country-capital').text.strip()
    population = country.find('span', class_='country-population').text.strip()
    area = country.find('span', class_='country-area').text.strip()

    country_data.append({
        'CountryName': name,
        'Capital': capital,
        'Population': population,
        'Area': area
    })

df = pd.DataFrame(country_data)
df.to_excel('countries_data.xlsx', index=False)

for link in soup.find_all('a', href=True):
    print(f"Link Text: {link.text.strip()} URL: {link['href']}")

print("Data extracted and saved to Excel. Check specific links output above.")

info_sections = soup.find_all('div', class_='col-md-6')
for section in info_sections:
    texts = [e for e in section.stripped_strings]
    formatted_text = ' '.join(texts)
    print(f"Info Section Text: {formatted_text}")
