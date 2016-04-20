#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from .common import *

class EfloraClient:

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(Default_Header)

    def search(self, name):
        url = Eflora_Search_URL + '/' + name + '?page=1'
        print url
        r = self._session.get(url)
        soup = BeautifulSoup(r.content)
        divpage = soup.find('div', id='divpage')
        alist = divpage.find_all('a')
        pagenum = alist[len(alist) - 2].text
