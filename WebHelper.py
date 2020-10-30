import requests
from bs4 import BeautifulSoup


class GoogleNews:
    def __init__(self, query='Russia', lang='en', country='US'):
        self.url = f'https://news.google.com/search?q={query}&hl={lang}-{country}&gl={country}&ceid=US%3A{lang}'
        self.html = self.get_html()
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False
