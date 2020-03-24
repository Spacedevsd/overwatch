import re
from bs4 import BeautifulSoup

GET_REAL_NAME_AND_AGE = r"(.+:\s+|)(.+),\s+(.+:)\s+(\w+)"


class Parser:
    def parse(self, response):
        html = BeautifulSoup(response.text, "html.parser")
        return {
            "name": self.extract_name(html),
            "role": self.extract_role(html),
            "description": self.extract_description(html),
            "abilities": self.extract_abilities(html),
            "difficulty": self.extract_difficulty(html),
            "bio": self.extract_bio(html),
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

    def extract_bio(self, response):
        content = response.find("li", class_="name").span
        realname, age = re.search(GET_REAL_NAME_AND_AGE, content.text).group(2, 4)

        occupation = self._normalize_extract_content(
            response.find("li", class_="occupation")
        )
        base = self._normalize_extract_content(response.find("li", class_="base"))
        affiliation = self._normalize_extract_content(
            response.find("li", class_="affiliation")
        )
        stories = response.select("div.hero-bio-backstory p")
        story = "".join([story.text for story in stories if story.text])

        return {
            "realname": realname,
            "age": age,
            "occupation": occupation,
            "base": base,
            "affiliation": affiliation,
            "story": story,
        }

    def _normalize_extract_content(self, t):
        return t.span.text.split(": ")[1]
