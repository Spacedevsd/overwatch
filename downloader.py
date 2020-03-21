import httpx
from collections import namedtuple

Response = namedtuple("Response", ["text", "status_code", "url"])


class Downloader:
    def __init__(self):
        self.downloader = httpx.Client()

    def get(self, url, params=None):
        response = self.downloader.get(url, params=params)

        response.raise_for_status()

        return Response(
            text=response.text, status_code=response.status_code, url=response.url
        )

