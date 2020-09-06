from src.core.repository.fetch_data import fetch_data
from src.core.repository.parse_data import parse_data


def fetch_pages(url, **kwargs):
    result_url = kwargs.get('result_url')
    start = kwargs.get('start')
    not_in = kwargs.get('not_in')
    slice_string = kwargs.get('slice_string')

    data = fetch_data(url)[1]

    magnet_links = []

    for i in data.find_all('a', href=True):
        valid = False

        if i.get('href').startswith(start) and i.get('href') not in magnet_links and '#download' not in i.get('href'):
            valid = True

        if (start is not None) and (not_in is not None):
            for link in not_in:
                if link in i.get('href'):
                    valid = False

        if valid:
            magnet_links.append(i.get('href'))

            if result_url is not None:
                if slice_string is not None:
                    result = parse_data(f'{result_url}{i.get("href")[slice_string[0]:slice_string[1]]}')
                else:
                    result = parse_data(f'{result_url}{i.get("href")}')
            else:
                if slice_string is not None:
                    result = parse_data(i.get('href')[slice_string[0]:slice_string[1]])
                else:
                    magnet_links += parse_data(i.get('href'))

                if result is not None:
                    magnet_links += result

    return magnet_links
