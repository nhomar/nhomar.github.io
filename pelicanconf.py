#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nhomar G Hern\xe1ndez M'
SITENAME = u'Blog de Ger\xf3nimo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#pelican-bootstrap3 stuff

import os
for i in os.listdir('.'):
    print 'Dir found ...... %s' % (i)
if os.path.isdir('../pelican-bootstrap3'):
    THEME='../pelican-bootstrap3/'
elif os.path.isdir('~/pelican-bootstrap3'):
    THEME='~/pelican-bootstrap3/'

BOOTSTRAP_THEME = 'vauxoo'
SHOW_ARTICLE_AUTHOR = True
