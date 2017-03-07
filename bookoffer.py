# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

'''
The free ebook of today in https://www.packtpub.com/packt/offers/free-learning/

@author: mireiamoix
'''
import urllib2
from bs4 import BeautifulSoup
import subprocess


class Book(object):
    # baixar-se la web
    def get_web(self, page):
        web = urllib2.urlopen(page)
        html = web.read()
        web.close()
        return html

    # TODO: buscar el text
    def search_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        title_web = soup.find("div", "dotd-title")
        title = title_web.text
        return title.strip()  # strip elimina "/t" del title

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning/')
        title = self.search_title(web)

        # imprimeix el title via notificacio
        subprocess.Popen(["notify-send", "Free ebook of today: " + title])


if __name__ == '__main__':
    book = Book()
    book.main()
