#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

from .common import *

class EfloraClient:

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(Default_Header)

    def _get_plant_list_from_page(self, name, pageindex):
        plantlist = []

        pageurl = Eflora_Search_URL + '/' + name + '?page=' + str(pageindex)
        r = self._session.get(pageurl)
        soup = BeautifulSoup(r.content)

        for tr in soup.find_all('tr'):
            if tr.has_attr('style'):
                assert 5 == len(tr.children)
                plantdict = {}
                plantdict['name'] = tr.children[0].string
                plantdict['latin'] = tr.children[1].string
                plantdict['alias'] = tr.children[2].string
                plantdict['slug'] = tr.children[3].string
                plantdict['url'] = Eflora_URL + tr.children[4]['href']
                plantlist.append(plantdict)

        return plantlist

    def search(self, name):
        plantlist = []

        pageurl = Eflora_Search_URL + '/' + name + '?page=1'
        r = self._session.get(pageurl)
        soup = BeautifulSoup(r.content)
        alist = soup.select('div#divpage > a')
        print alist
        alist_len = len(alist)
        if alist_len < 2:
            return
        pagenum = int(alist[len(alist) - 2].text)
        print pagenum

        for pageindex in range(1, pagenum + 1):
            plantlist.extend(self._get_plant_list_from_page(name, pageindex))

        print plantlist
        return json.dumps(plantlist)
