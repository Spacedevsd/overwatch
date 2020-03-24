from bs4 import BeautifulSoup

from overwatch.heroes.parser import Parser


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


def test_extract_bio_from_ashe_hero(ashe_html, snapshot):
    response = BeautifulSoup(ashe_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_bio(response)
    snapshot.assert_match(parsed)
