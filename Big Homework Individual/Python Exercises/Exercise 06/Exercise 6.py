import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://www.scrapethissite.com/pages/forms/'
response = requests.get(url)


def scrape():
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    data = pd.read_html(str(table))[0]
    csv_file_path = 'Exercise 6.csv'
    data.to_csv(csv_file_path, index=False)


def show():
    data = pd.read_csv('Exercise 6.csv')
    data['City'] = data['Team Name'].apply(lambda x: ' '.join(x.split()[:-1]))
    teams_by_city = data.groupby('City')['Team Name'].apply(list).to_dict()
    print("Teams by city:\n")
    for city, teams in teams_by_city.items():
        print(f"{city}: {', '.join(teams)}")


def show_wins():
    data = pd.read_csv('Exercise 6.csv')
    ordered_teams = data.sort_values(by='Wins', ascending=False)
    print("\n----------------------------------------")
    print("Teams by wins:\n")
    for index, row in ordered_teams.iterrows():
        print(f"{row['Team Name']} - Wins: {row['Wins']}")


def extra(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    search_form = soup.find('form', {'class': 'form-inline'})
    search_action = search_form.get('action') if search_form else "No form found"

    pagination = soup.find('ul', {'class': 'pagination'})
    pagination_text = ' '.join(
        link.text.strip() for link in pagination.find_all('a')) if pagination else "No pagination found"

    info_sections = soup.find_all('div', class_='col-md-6')
    for section in info_sections:
        texts = [e for e in section.stripped_strings]
        formatted_text = ' '.join(texts)
        print(f"Info Section Text: {formatted_text}")

    print(f"Search form action: {search_action}")
    print(f"Pagination details: {pagination_text}")


def main():
    scrape()
    show()
    show_wins()
    extra(response.text)


if __name__ == "__main__":
    main()
