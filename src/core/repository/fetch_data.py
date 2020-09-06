import requests
from bs4 import BeautifulSoup, SoupStrainer


def fetch_data(url):
    try:
        request = requests.get(url)
        return [request.status_code, BeautifulSoup(request.content, 'lxml', parse_only=SoupStrainer('a'))]
    except:
        print(f'Cannot fetch data for URL: {url}')
        return 'Error'
