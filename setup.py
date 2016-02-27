#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================================
Markdown Simple Chemistry Extension Distutils Setup
==============================================

:website: https://github.com/dmishin/markdown-simplechem
:copyright: Copyright 2016 Dmitry Shintyakov
:license: MIT, see LICENSE.MIT for details.
"""

from setuptools import setup
from codecs import open as codec_open
from os import path


HERE = path.abspath(path.dirname(__file__))


# Get the long description from the relevant file
with codec_open(path.join(HERE, 'DESCRIPTION.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name='MarkdownSimplechem',

    version='1.0.0',  # PEP 440 Compliant Semantic Versioning

    keywords='text filter markdown html chemistry',
    description='Python-Markdown extension to allow for convenient formatting of chemical equations.',
    long_description=LONG_DESCRIPTION,

    author='Dmitry Shintyakov',
    author_email='shintyakov at gmail',

    url='https://github.com/dmishin/markdown-simplechem',

    py_modules=['mdx_simplechem'],
    install_requires=['Markdown>=2.4'],

    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
