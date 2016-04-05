#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dexiong Chen'
SITENAME = u'Genetic Determinants Selection'
SITEURL = 'file:///home/thoth/dchen/Projects/code/website/output'
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = None
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

TYPOGRIFY=True

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 100

STATIC_PATHS = ['images', 'static']

# Uncomment following line if you want document-relative URLs when developing
SITEURL = 'http://localhost:8000/'
RELATIVE_URLS = True
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']

THEME = "theme"