#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseEflora

class Plant(BaseEflora):

    def __init__(self, url, name=None, latin=None, alias=None, slug=None, session=None):
        self._url = url
        self._session = session
        self._name = name
        self._latin = name
        self._alias = alias
        self._slug = slug
    
    def position(self):
        if not self._position:
            _make_soup()
            self._position = []
            divrightcon = self._soup.find('div', class_='divrightcon')
            for span in divrightcon.find_all('span'):
                self._position.append(span.string)
    
    def relatives(self):
        pass
    
    def fullname(self):
        if not self._fullname:
            _make_soup()
            spSynSpan = self._soup.find('span', id='spSyn')
            self._fullname = spSynSpan.previous_sibling
        return self._fullname

    def description(self):
        if not self._description:
            _make_soup()
            description = []
            divkey = self._soup.find('div', id='divkey')
            for p in divkey.previous_siblings:
                if p.has_attr('style'):
                    description.append(p.string)
        for desc in description.reverse():
            self._description += desc
            self._description += '\r\n'
        return self._description
    
    def indextable(self):
        pass
    
    def subclass(self):
        pass

