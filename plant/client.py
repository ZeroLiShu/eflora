#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from .common import *

class EfloraClient:

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(Default_Header)

    def search(self, name):
        pass
