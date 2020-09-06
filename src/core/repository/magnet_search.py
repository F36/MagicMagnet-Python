import urllib

from src.core.repository.fetch_pages import fetch_pages
from src.core.repository.parse_data import parse_data


def magnet_search(search_content, **kwargs):
    google = kwargs.get('google')
    tpb = kwargs.get('tpb')
    l337x = kwargs.get('l1137x')
    nyaa = kwargs.get('nyaa')
    eztv = kwargs.get('eztv')
    yts = kwargs.get('yts')
    demonoid = kwargs.get('demonoid')
    ettv = kwargs.get('ettv')
    skytorrents = kwargs.get('skytorrents')
    limetorrents = kwargs.get('limetorrents')

    search_content = urllib.parse.quote_plus(f'{search_content}')

    search_result = []

    if google:
        params = {
            'search_url': f'https://www.google.com/search?q={search_content}+download+torrent',
            'start': '/url?q=',
            'not_in': ['accounts.google.com', '.org', 'youtube.com', 'facebook.com'],
            'slice_string': [7, -88]
        }

        search_result += fetch_pages(params['search_url'], start=params['start'], not_in=params['not_in'],
                                     slice_string=params['slice_string'])

    if tpb:
        for i in range(5):
            search_result += parse_data(
                f'https://tpb.party/search/{search_content}/{i + 1}/7/0')

    if l337x:
        params = {
            'search_url': f'https://www.1377x.to/search/{search_content}/1/',
            'start': '/torrent',
            'result_url': 'https://www.1377x.to'
        }

        search_result += fetch_pages(
            params['search_url'], result_url=params['result_url'], start=params['start'])

    if nyaa:
        for i in range(5):
            search_result += parse_data(
                f'https://nyaa.si/?q={search_content}&f=0&c=0_0&s=seeders&o=desc&p={i + 1}')

    if eztv:
        search_result += parse_data(f'https://eztv.io/search/{search_content}')

    if yts:
        params = {
            'search_url': f'https://yts.mx/browse-movies/{search_content}/all/all/0/latest',
            'start': 'https://yts.mx/movie/'
        }

        search_result += fetch_pages(params['search_url'], start=params['start'])

    if demonoid:
        params = {
            'search_url': f'https://demonoid.is/files/?category=0&subcategory=0&quality=0&seeded=2&external=2&query={search_content}&sort=',
            'start': '/files/details',
            'result_url': 'https://demonoid.is'
        }

        search_result += fetch_pages(
            params['search_url'], start=params['start'], result_url=params['result_url'])

    if ettv:
        params = {
            'search_url': f'https://www.ettv.to/torrents-search.php?search={search_content}',
            'start': '/torrent/',
            'result_url': 'https://www.ettv.to'
        }

        search_result += fetch_pages(
            params['search_url'], start=params['start'], result_url=params['result_url'])

    if skytorrents:
        for i in range(5):
            search_result += parse_data(
                f'https://www.skytorrents.to/?search={search_content}&page={i + 1}')

    if limetorrents:
        params = {
            'search_url': f'https://www.limetorrents.info/search/all/{f"{search_content[0].upper()}{search_content[1:]}".replace("+", "-")}/',
            'start': '/',
            'result_url': 'https://www.limetorrents.info',
            'not_in': [
                '/home/', '/register/', '/recover/', '/top100',
                '/latest100', '/search-cloud/', '/faq/',
                '/contact/', '/friends/', '/messages/', '/feedback/',
                '/upload/', '/bookmarks/', '/personal-rss/', '/profile/',
                '/searchrss/', '/dl.php', '/browse-torrents/',
                '/cat_top/', '/rss/', '/search/', '/privacy/', '/dmca/',
            ]
        }

        search_result += fetch_pages(params['search_url'], start=params['start'], result_url=params['result_url'],
                                     not_in=params['not_in'])

    return search_result

# Testing code
#
# magnet_links = magnet_search('avengers', tpb=True)
#
# for link in magnet_links:
#     print(link.torrent_name)
