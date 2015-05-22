#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines individual articles within citeseerx"""

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
