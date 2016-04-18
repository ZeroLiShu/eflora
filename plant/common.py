#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as _Bs

try:
    __import__('lxml')
    BeautifulSoup = lambda makeup: _Bs(makeup, 'lxml')
except ImportError:
    BeautifulSoup = lambda makeup: _Bs(makeup, 'html.parser')
