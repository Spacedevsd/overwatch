from bs4 import BeautifulSoup


class Parser:
    def parse(self, response):
        html = BeautifulSoup(response.text, "html.parser")
        return self.extract_map_info(html)

    def extract_map_info(self, response):
        maps = response.find_all("a", class_="Map CardLink")
        content = []

        for map in maps:
            flag = map.find("span", class_="Map-flag").img["src"]
            title = map.find("h5", class_="Card-title").text
            map_type = map.find_all("div", class_="MapType-tooltip")

            content.append(
                {
                    "flag": flag,
                    "title": title,
                    "map_type": [tp["data-ow-tooltip-text"] for tp in map_type],
                }
            )

        return content
