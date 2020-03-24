from db import DB
from urllib.parse import urljoin

from .parser import Parser


class Crawler:
    def __init__(self, default_url, downloader, page=None) -> None:
        self.default_url = urljoin(default_url, page)
        self.downloader = downloader
        self.parser = Parser()
        self._maps = []

    async def download(self):
        response = await self.downloader.get(self.default_url)
        self._maps = self.parser.parse(response)

    def save(self):
        with DB() as db:
            for map in self._maps:
                db.maps.insert(map)
                print(f"The map: {map['title']} has been saved!")
