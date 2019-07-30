#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nhomar G Hern\xe1ndez M'
SITENAME = u'Blog de Ger\xf3nimo'
SITEURL = 'http://nhomar.github.io'

PATH = 'content'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Vauxoo', 'http://www.vauxoo.com/'),
         ('Odoo', 'http://www.odoo.com/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#pelican-bootstrap3 stuff

import os
if os.path.isdir('../pelican-bootstrap3'):
    THEME='../pelican-bootstrap3/'
elif os.path.isdir(os.path.join(os.getenv('HOME'), 'pelican-bootstrap3')):
    THEME=os.path.join(os.getenv('HOME'), 'pelican-bootstrap3')

BOOTSTRAP_THEME = 'vauxoo'
SHOW_ARTICLE_AUTHOR = True
#DISQUS_DISPLAY_COUNTS = True

#Optional Stuff from pelican-bootstrap
DISPLAY_BREADCRUMBS = True
CC_LICENSE_DERIVATIVES = 'yes'
CC_LICENCE = 'CC-BY-SA'
#Social Stuff.
SOCIAL = (
          ('twitter', 'https://twitter.com/nhomar'),
          ('facebook', 'https://www.facebook.com/nhomar'),
          ('google+', 'https://plus.google.com/+NhomarHernandez'),
          ('youtube', 'https://www.youtube.com/user/nhomar00'),
          ('linkedin', 'http://www.linkedin.com/in/nhomar'),
          ('github', 'http://github.com/nhomar'),
          ('slideshare', 'http://www.slideshare.net/nhomar'),
          )
TWITTER_WIDGET_ID = 375896848369586176
TWITTER_USERNAME = 'nhomar'
TWITTER_CARDS = True

#OTHER PLUGINS
PLUGINS = [
    'pelican_youtube',
    'pelican_gist',
    #'local_plugins.disqus_static',
]

#TODO: Enble disqus
DISQUS_SITENAME = u'nhomarblog'

#Github Stuff
GITHUB_USER = 'nhomar'
GITHUB_REPO_COUNT = '10'
GITHUB_SHOW_USER_LINK = True
GITHUB_SKIP_FORK = True
ADDTHIS_PROFILE = 'ra-53fed39d222a7739'
TZINFOS = 'UTC'
