from urllib.parse import urljoin

from db import DB

from .parser import Parser
from contextlib import suppress


class Crawler:
    def __init__(self, default_url, downloader, page) -> None:
        self.default_url = urljoin(default_url, page)
        self.downloader = downloader
        self.parser = Parser()
        self._heroes = []

    async def download(self):
        response = await self.downloader.get(self.default_url)
        params = self.parser.extract_url_params(response)

        with suppress(StopAsyncIteration):
            for param in params:
                response_hero = await self.get_hero_page(param)
                self._heroes.append(self.parser.parse(response_hero))

    def save(self):
        with DB() as database:
            for hero in self._heroes:
                database.heroes.insert(hero)
                print(f"{hero['name']} has been saved!")

    async def get_hero_page(self, param):
        url = urljoin(self.default_url, param["href"])
        return await self.downloader.get(url)
