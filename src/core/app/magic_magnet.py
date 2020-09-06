from src.core.repository.parse_data import parse_data


def magic_magnet():
    links = parse_data(
        'https://comandotorrentshd.net/vingadores-ultimato-torrent/')

    for i in links:
        print(i.torrent_name)

magic_magnet()
