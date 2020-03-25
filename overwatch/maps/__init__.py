from .crawler import Crawler as BaseCrawler
from config import load

configuration = load()


class Crawler:
    def __init__(self, downloader):
        self.default_url = configuration.get("app", "default_url")
        self.downloader = downloader
        self.page = "pt-br/maps"

    async def init(self):
        crawler = BaseCrawler(self.default_url, self.downloader, self.page)
        await crawler.download()
        crawler.save()
