#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as _Bs

try:
    __import__('lxml')
    BeautifulSoup = lambda makeup: _Bs(makeup, 'lxml')
except ImportError:
    BeautifulSoup = lambda makeup: _Bs(makeup, 'html.parser')

Default_Header = {'Referer': 'http://frps.eflora.cn',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
                  'Host': 'frps.eflora.cn'}

Eflora_URL = 'http://frps.eflora.cn'
Eflora_Search_URL = Eflora_URL + '/search'
