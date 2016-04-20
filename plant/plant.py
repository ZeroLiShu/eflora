#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseEflora

class Plant(BaseEflora):

    def __init__(self, url, name=None, latin=None, alias=None, slug=None, session=None):
        self.url = url
        self._session = session
        self._name = name
        self._latin = name
        self._alias = alias
        self._slug = slug
    
    def position(self):
        pass
    
    def relatives(self):
        pass
    
    def fullname(self):
        pass
    
    def description(self):
        pass
    
    def indextable(self):
        pass
    
    def subclass(self):
        pass

