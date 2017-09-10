#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joao Moreira'
SITENAME = 'Joao Moreira'
SITESUBTITLE = 'Data Scientist'
SITEURL = ''
BIO = 'Data scientist. Iron Man fan.'
PROFILE_IMAGE = 'avatar.jpg'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

# Disable caching and versioning of static resources since GitHub pages
# caches stuff for only 10 mins
ASSET_CONFIG = (
    ('url_expire', False),
    ('manifest', False),
    ('cache', False),
)

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%B %-d, %Y'

THEME = 'pelican-hyde'

DISPLAY_PAGES_ON_MENU = True

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Obfuscate email with: http://www.jottings.com/obfuscator/
# Then replace your `coded` and `key` js variables below
EMAIL_CODED = 'dZ8Z.8J.kZ3ME38@Jk8EF.LZk'
EMAIL_KEY = '59bOciUfrngQj8xYMmzwFCAyhPBuGLEvt3sJodq1X7k6NpW4TSaIHeVKRl2D0Z'

# Social widget
SOCIAL = (
    # Email obfuscated using the above variables
    ('email', ''),
    ('github-square', 'https://github.com/jagmoreira'),
    ('linkedin', 'https://www.linkedin.com/in/joao-moreira'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
