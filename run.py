import asyncio
from importlib import import_module

from downloader import Downloader


async def main():
    module = "maps"
    default_url = "https://playoverwatch.com"

    crawler = import_module(f"overwatch.{module}")
    c = crawler.Crawler(default_url, Downloader(), "maps")
    await c.init()


if __name__ == "__main__":
    asyncio.run(main())
