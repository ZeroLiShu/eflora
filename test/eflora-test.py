#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ZeroLiShu'

from plant import EfloraClient, Plant

def test_plant():
    client.search('a')

def test():
    test_plant()

if __name__ == '__main__':
    client = EfloraClient()
    test()
