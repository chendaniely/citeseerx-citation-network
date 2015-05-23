#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines individual articles within citeseerx"""

import re

from bs4 import BeautifulSoup
import requests


class Article(object):
    """An article from the citeseer-x database"""

    # def __init__(self):
    #     return(self)

    def base_article_url(self):
        """Returns the base URL that will link to a paper
        after a DOI string is appended

        :returns: string -- base URL string
        """
        return("http://citeseerx.ist.psu.edu/viewdoc/summary?doi=")

    def create_full_url(self, doi_string):
        """Create full url to article from a DOI string

        :param doi_string:
        """
        return(self.base_article_url() + doi_string)

    def _get_authors_soup(self, find_index=0):
        author_sting = self.soup.\
                       find_all('div', id="docAuthors")[find_index]
        return(author_sting)

    def _get_authors_soup_text(self, author_soup):
        author_soup_text = author_soup.\
                       getText().\
                       split(',')
        return(author_soup_text)

    def _get_authors_soup_text_clean(self, author_soup_text):
        authors = []
        for author in author_soup_text:
            initial_strip = author.strip()
            clean_text = re.sub('^by\s+', '', initial_strip)
            strip_again = clean_text.strip()
            authors.append(strip_again)
        return(authors)

    def get_authors(self, find_index=0):
        author_soup = self._get_authors_soup(find_index)
        author_soup_text = self._get_authors_soup_text(author_soup)
        author_soup_text_clean = self.\
            _get_authors_soup_text_clean(author_soup_text)
        self.authors = author_soup_text_clean
        return(self)

    def get_page_soup(self, url=None):
        """Use self.url to get the HTML soup of the article
        and set the HTML soup to self.soup

        :returns: self
        """
        if url is None:
            r = requests.get(self.url)
        else:
            r = requests.get(url)
        data = r.text
        self.soup = BeautifulSoup(data)
        return(self)

    @property
    def authors(self):
        """Get or set the the Articles of the paper as a list
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        assert isinstance(authors, list), 'value of authors is not a list'
        self._authors = authors

    @property
    def doi(self):
        """Get or set the article's DOI as a string
        """
        return self._doi

    @doi.setter
    def doi(self, value):
        assert isinstance(value, str),\
               "doi value passed is of type %s".format(str(type(value)))
        self._doi = value

    @property
    def url(self):
        """Get or set the URL to the article as a string
        """
        return self._url

    @url.setter
    def url(self, full_url):
        self._url = full_url

    @property
    def soup(self):
        """Get or set the html soup from the article page
        """
        return self._soup

    @soup.setter
    def soup(self, soup_text):
        self._soup = soup_text
