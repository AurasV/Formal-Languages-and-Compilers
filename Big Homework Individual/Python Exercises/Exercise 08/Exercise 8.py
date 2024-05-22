import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


def fetch_data(team_name):
    url = f"https://www.scrapethissite.com/pages/forms/?q={team_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table_rows = soup.find_all('tr', class_='team')

    data = []
    for row in table_rows:
        cells = row.find_all('td')
        data.append({
            'Year': int(cells[1].text.strip()),
            'Wins': int(cells[2].text.strip()),
            'Losses': int(cells[3].text.strip())
        })
    return data


def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def plot_data(data):
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 5))
    plt.bar(df['Year'] - 0.2, df['Wins'], width=0.4, label='Wins', color='b')
    plt.bar(df['Year'] + 0.2, df['Losses'], width=0.4, label='Losses', color='r')
    plt.xlabel('Year')
    plt.ylabel('Number of Games')
    plt.title(f'Team Performance')
    plt.xticks(df['Year'])
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    team_name = input("Enter a team name: ")
    data = fetch_data(team_name)
    save_to_csv(data, f"{team_name.replace(' ', '_').lower()}_data.csv")
    plot_data(data)
