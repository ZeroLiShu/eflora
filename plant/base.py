from .common import BeautifulSoup
from requests import Response

class BaseEflora:
    def _gen_soup(self, content):
        self._soup = BeautifulSoup(content)

    def _get_content(self):
        resp = self._session.get(self._url[:-1])
        return resp.content

    def _make_soup(self):
        if self._url and not self._soup:
            self._gen_soup(self._get_content())

    def refresh(self):
        # refresh self.soup's content
        self._gen_soup(self._get_content())
