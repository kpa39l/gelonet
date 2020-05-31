#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEFAULT_LANG = 'ru'

AUTHOR = 'Kpa39l'
SITEURL = 'http://localhost:8000'
SITENAME = 'Стороженко Евгений Владимирович'
SITETITLE = 'Стороженко Евгений Владимирович'
SITESUBTITLE = 'Субьективно обо всем вокруг'
SITEDESCRIPTION = 'Взгляд ИТ-шника из маленького городка на происходящее'
SITELOGO = 'images/avatar1.jpg'
FAVICON = 'images/favicon.ico'
BROWSER_COLOR = '#333333'
USE_LESS = True
PYGMENTS_STYLE = 'monokai'
TIMEZONE = 'Europe/Moscow'

ROBOTS = 'index, follow'
THEME = "/home/kpa39l/pelican/projects/gelonet.ru/themes/Flex/"

PATH = 'content'
OUTPUT_PATH = 'output/'
ARTICLE_PATHS = ['blog', 'news']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'content']

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'summary']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.2,
        'pages': 0.1
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
SUMMARY_BEGIN_MARKER = '-----'
SUMMARY_END_MARKER = '====='
SUMMARY_USE_FIRST_PARAGRAPH = False

DATE_FORMATS = {
    'en': '%B %d, %Y',
    'ru': '%d %B, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Social widget
SOCIAL = (
    ('vk', 'https://vk.com/kpa39l'),
    ('github', 'https://github.com/kpa39l'),
    ('facebook', 'https://facebook.com/kpa39l'),
    ('twitter', 'https://twitter.com/kpa39l'),
    ('youtube', 'https://www.youtube.com/channel/UC0qtXmhsIHlguW6OHZEy0Tg?view_as=subscriber'),
    ('rss', '/blog/feeds/all.atom.xml'),
    # ('yandex-music', 'https://music.yandex.ru/users/kpa39l/playlists/1016')
)

MENUITEMS = (
             ('Архивы', '/archives.html'),
             ('Категории', '/categories.html'),
             ('Тэги', '/tags.html'),
            )

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
# Blogroll
LINKS = (
         ('Архивы', '/archives.html'),
         ('Категории', '/categories.html'),
         ('Тэги', '/tags.html'),
        )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
