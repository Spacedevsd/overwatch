from bs4 import BeautifulSoup


class Parser:
    def parse(self, response):
        html = BeautifulSoup(response.text, "html.parser")
        return {
            "name": self.extract_name(html),
            "role": self.extract_role(html),
            "description": self.extract_description(html),
            "abilities": self.extract_abilities(html),
            "difficulty": self.extract_difficulty(html),
        }

    def extract_name(self, response):
        return response.find("h1", class_="hero-pose-name").text

    def extract_role(self, response):
        return response.find("h4", class_="hero-detail-role-name").text

    def extract_description(self, response):
        return response.find("p", class_="hero-detail-description").text

    def extract_abilities(self, response):
        items = response.find_all("div", class_="hero-ability-descriptor")
        abilities = []

        for item in items:
            abilities.append({"name": item.h4.text, "description": item.p.text})
        return abilities

    def extract_difficulty(self, response):
        items = response.select("div.hero-detail-difficulty span")
        return len([item for item in items if "m-empty" not in item["class"]])

    def extract_url_params(self, response):
        parsed = BeautifulSoup(response.text, "html.parser")
        return parsed.select("a.hero-portrait-detailed")
