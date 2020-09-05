from fetch_data import fetch_data
from parse_torrent_name import parse_torrent_name
# from core.models import SearchResult


class SearchResult:
    def __init__(self, torrent_name, magnet_link):
        self.torrent_name = torrent_name
        self.magnet_link = magnet_link


def parse_data(url):
    if url.endswith('/&s'):
        url = url[:-2]

    print(f'Searching in {url}')

    found_links = []

    try:
        data = fetch_data(url)

        if (data[0] == 200):
            print(f'Sucess! Status code: {data[0]}')
            data = data[1]

            for i in data.find_all('a', href=True):
                if i.get('href') != None and i.get('href').startswith('magnet:?xt=') and len(i.get('href')) > 64:

                    found_link = SearchResult(
                        parse_torrent_name(i.get('href')), i.get('href'))

                    if found_link not in found_links:
                        found_links.append(found_link)

            return found_links
        else:
            print(f'Error! Status code: {data[0]}')
    except:
        print(f'Failed to parse: {url}')
        return found_links


links = parse_data(
    'https://comandotorrentshd.net/vingadores-ultimato-torrent/')

for i in links:
    print(i.torrent_name)
