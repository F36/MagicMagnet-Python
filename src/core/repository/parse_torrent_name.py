import urllib.parse


def parse_torrent_name(magnet_link):
    torrent_name = magnet_link.split('tr=')[0][64:-1]

    if torrent_name.startswith(';dn=') and torrent_name.endswith('&amp'):
        torrent_name = torrent_name[4:-4]

    return urllib.parse.unquote_plus(torrent_name)
