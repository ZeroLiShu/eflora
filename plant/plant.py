#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseEflora

class Plant(BaseEflora):

    def __init__(self, url, session=None):
        self.url = url
        self._session = session
