from unittest.mock import AsyncMock, patch

import pytest

from overwatch.heroes.crawler import Crawler


@pytest.mark.asyncio
@patch("downloader.Downloader", new_callable=AsyncMock)
async def test_crawler(downloader_mock, heroes_html, hero_html, hero2_html, snapshot):
    default_url = "https://playoverwatch.com"
    html1 = AsyncMock(text=heroes_html)
    html2 = AsyncMock(text=hero_html)
    html3 = AsyncMock(text=hero2_html)

    downloader = downloader_mock.return_value
    downloader.get.side_effect = [html1, html2, html3]

    crawler = Crawler(default_url, downloader, "pt-br/heroes")
    await crawler.download()
    snapshot.assert_match(crawler._heroes)
