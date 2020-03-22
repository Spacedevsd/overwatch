from unittest.mock import AsyncMock, patch

import pytest
from bs4 import BeautifulSoup

from overwatch.crawler import Crawler
from overwatch.parser import Parser


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


def test_extract_name(hero_html, snapshot):
    response = BeautifulSoup(hero_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_name(response)
    snapshot.assert_match(parsed)


def test_extract_role(hero_html, snapshot):
    response = BeautifulSoup(hero_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_role(response)
    snapshot.assert_match(parsed)


def test_extract_description(hero_html, snapshot):
    response = BeautifulSoup(hero_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_description(response)
    snapshot.assert_match(parsed)


def test_extract_abilities(hero_html, snapshot):
    response = BeautifulSoup(hero_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_abilities(response)
    snapshot.assert_match(parsed)


def test_extract_difficulty(hero_html, snapshot):
    response = BeautifulSoup(hero_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_difficulty(response)
    snapshot.assert_match(parsed)


def test_extract_bio(hero_html, snapshot):
    response = BeautifulSoup(hero_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_bio(response)
    snapshot.assert_match(parsed)


def test_extract_bio_from_reppear_hero(hero3_html, snapshot):
    response = BeautifulSoup(hero3_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_bio(response)
    snapshot.assert_match(parsed)
