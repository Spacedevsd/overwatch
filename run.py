from downloader import Downloader
from overwatch.crawler import Crawler


def main():
    default_url = "https://playoverwatch.com"
    downloader = Downloader()
    page = "pt-br/heroes"

    crawler = Crawler(default_url, downloader, page)
    content = crawler.download()
    content.save()


if __name__ == "__main__":
    main()
