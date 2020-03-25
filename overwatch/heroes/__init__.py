from .crawler import Crawler as BaseCrawler


class Crawler:
    def __init__(self, default_url, downloader):
        self.default_url = default_url
        self.downloader = downloader
        self.page = "pt-br/heroes"

    async def init(self):
        crawler = BaseCrawler(self.default_url, self.downloader, self.page)
        await crawler.download()
        crawler.save()
