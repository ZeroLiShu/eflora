#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from .common import *

class EfloraClient:

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(Default_Header)

    def search(self, name):
        pageurl = Eflora_Search_URL + '/' + name + '?page=1'
        r = self._session.get(pageurl)
        soup = BeautifulSoup(r.content)
        divpage = soup.find('div', id='divpage')
        alist = divpage.find_all('a')
        pagenum = int(alist[len(alist) - 2].text)
        
        table = soup.find('div', cellSpacing='0')
        for tr in table.find_all('tr', style=True):
            tdlist = tr.find_all('td')
            assert 5 == len(tdlist)
            name = tdlist[0].text
            latin = tdlist[1].text
            alias = tdlist[2].text
            slug = tdlist[3].text
            url = Eflora_URL + tdlist[4]['href']
