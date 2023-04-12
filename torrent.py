from torrentp import TorrentDownloader

link = "magnet:..."
torrent_file = TorrentDownloader(link, ".")
torrent_file.start_download()
