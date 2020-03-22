from downloader import Downloader
from overwatch.crawler import Crawler
import asyncio


async def main():
    default_url = "https://playoverwatch.com"
    downloader = Downloader()
    page = "pt-br/heroes"

    crawler = Crawler(default_url, downloader, page)
    content = await crawler.download()
    content.save()


if __name__ == "__main__":
    asyncio.run(main())
