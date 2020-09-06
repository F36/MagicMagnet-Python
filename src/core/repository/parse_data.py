from src.core.models.search_result import SearchResult
from src.core.repository.fetch_data import fetch_data
from src.core.repository.parse_torrent_name import parse_torrent_name


def parse_data(url):
    if url.endswith('/&s'):
        url = url[:-2]

    print(f'Searching in {url}')

    found_links = []

    data = fetch_data(url)

    if data[0] == 200:
        print(f'Success! Status code: {data[0]}')
        data = data[1]

        for link in data.find_all('a', href=True):
            if link.get('href') is not None and link.get('href').startswith('magnet:?xt=') and len(
                    link.get('href')) > 64:

                found_link = SearchResult(
                    parse_torrent_name(link.get('href')), link.get('href'))

                if found_link not in found_links:
                    found_links.append(found_link)

        return found_links if found_links is not None else []
