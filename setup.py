#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import ast

from setuptools import setup, find_packages


def extract_version():
    with open('plant/__init__.py', 'rb') as f_version:
        ast_tree = re.search(
            r'__version__ = (.*)',
            f_version.read().decode('utf-8')
        ).group(1)
        if ast_tree is None:
            raise RuntimeError('Cannot find version information')
        return str(ast.literal_eval(ast_tree))


with open('README.md', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')


version = extract_version()

setup(
    name='eflora',
    version=version,
    keywords=['eflora', 'network', 'spider', 'html'],
    description='Eflora UNOFFICIAL API library in python2.x, '
                'with help of bs4, lxml, requests and.',
    long_description=readme,

    author='ZeroLiShu',
    author_email='lishufox@icloud.com',
    license='MIT',

    url='https://github.com/ZeroLiShu/eflora',
    download_url='https://github.com/ZeroLiShu/eflora',

    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    extras_require={
        'lxml': ['lxml']
    },
    packages=find_packages(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
