from unittest.mock import patch, Mock
from overwatch.crawler import Crawler
from bs4 import BeautifulSoup
from overwatch.parser import Parser


@patch("downloader.Downloader")
def test_crawler(downloader_mock, heroes_html, hero_html, hero2_html, snapshot):
    default_url = "https://playoverwatch.com"
    html1 = Mock(text=heroes_html)
    html2 = Mock(text=hero_html)
    html3 = Mock(text=hero2_html)

    downloader = downloader_mock.return_value
    downloader.get.side_effect = [html1, html2, html3]

    crawler = Crawler(default_url, downloader, "pt-br/heroes")
    content = crawler.download()
    snapshot.assert_match(content._heroes)


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
