from .parser import Parser


class Crawler:
    def __init__(self, default_url, downloader) -> None:
        self.default_url = default_url
        self.downloader = downloader
        self.parser = Parser()
        self._maps = []

    async def download(self):
        response = await self.downloader.get(self.default_url)
        self._maps = self.parser.parse(response)

    def save(self):
        pass
