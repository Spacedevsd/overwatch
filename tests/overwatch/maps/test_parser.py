from bs4 import BeautifulSoup

from overwatch.maps.parser import Parser


def test_extract_map_info(maps_html, snapshot):
    response = BeautifulSoup(maps_html, "html.parser")
    parser = Parser()
    parsed = parser.extract_map_info(response)
    snapshot.assert_match(parsed)
