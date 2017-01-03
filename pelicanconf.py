#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joao Moreira'
SITENAME = 'Joao Moreira'
SITEURL = ''
BIO = 'lorem ipsum doler umpalum paluuu'
PROFILE_IMAGE = "avatar.jpg"

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%B %-d, %Y'

THEME = "pelican-hyde"

DISPLAY_PAGES_ON_MENU = True

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github-square', 'https://github.com/jagmoreira'),
          ('linkedin', 'https://www.linkedin.com/in/joao-moreira'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
