from unittest.mock import AsyncMock, patch
from overwatch.maps.crawler import Crawler
import pytest


@pytest.mark.asyncio
@patch("downloader.Downloader", new_callable=AsyncMock)
async def test_crawler(downloader_mock, maps_html, snapshot):
    default_url = "https://playoverwatch.com/pt-br/maps"

    downloader = downloader_mock.return_value
    downloader.get.return_value = AsyncMock(text=maps_html)

    crawler = Crawler(default_url, downloader)
    await crawler.download()
    snapshot.assert_match(crawler._maps)
