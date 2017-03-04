#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

'''
The book of the day in https://www.packtpub.com/packt/offers/free-learning/

@author: miremoix
'''
import urllib2
from bs4 import BeautifulSoup

class Book(object):
    # baixar-se la web
    def get_web(self, page):
       f = urllib2.urlopen(page) # aixo et retorna un fitxer
       html = f.read()
       f.close()
       return html

    # TODO: buscar el text
    def search_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        ptitle = soup.find_all("div", "dotd-title")

        for element in ptitle:
            title = element.find("h2").text

        return title.strip() #strip() elimina /t del title que estan als dos extrems daquest

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning/')
        title = self.search_title(web)
        # FIXME: imprimir resultats
        print title

if __name__ == '__main__':

    book = Book()
    book.main()
