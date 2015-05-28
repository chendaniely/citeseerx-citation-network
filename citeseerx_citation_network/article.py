#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines individual articles within citeseerx"""

import re

from bs4 import BeautifulSoup
import requests


class Article(object):
    """An article from the citeseer-x database"""

    def __init__(self, doi=None, url=None,
                 base_url="http://citeseerx.ist.psu.edu/viewdoc/summary?doi="):
        self.base_url = base_url
        if doi is not None:
            assert isinstance(doi, str), "doi needs to be a string"
            self.doi = doi
            self.url = self.base_url + doi
        elif url is not None:
            assert isinstance(url, str), "url needs to be a string"
            self.url = url
            self.doi = self.parse_url_get_doi(self.url)
        else:
            self.doi = None
            self.url = None

        self.authors = None
        self.soup = None

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
        """Get the authors HTML from self.soup
        """
        author_sting = self.soup.\
            find_all('div', id="docAuthors")[find_index]
        return(author_sting)

    def _get_authors_soup_text(self, author_soup):
        """Get the string contents from the authors soup
        """
        author_soup_text = author_soup.\
            getText().\
            split(',')
        return(author_soup_text)

    def _get_authors_soup_text_clean(self, author_soup_text):
        """Clean the text of the authors text and add each author to a list
        """
        authors = []
        for author in author_soup_text:
            initial_strip = author.strip()
            clean_text = re.sub('^by\s+', '', initial_strip)
            strip_again = clean_text.strip()
            authors.append(strip_again)
        return(authors)

    def get_authors(self, find_index=0):
        """Set the authors of the paper to self.authors from self.soup
        """
        assert self.soup is not None, 'self.soup has a value of None'
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
        assert isinstance(authors, list) or authors is None,\
            'value of authors is not a list'
        self._authors = authors

    @property
    def base_url(self):
        """Get or set the base_url of the paper
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        assert isinstance(base_url, str), ""
        self._base_url = base_url
    def doi(self):
        """Get or set the article's DOI as a string
        """
        return self._doi

    @doi.setter
    def doi(self, value):
        assert isinstance(value, str) or value is None,\
               "doi value passed is of type %s".format(str(type(value)))
        self._doi = value

    @property
    def soup(self):
        """Get or set the html soup from the article page
        """
        return self._soup

    @soup.setter
    def soup(self, soup_text):
        self._soup = soup_text

    @property
    def url(self):
        """Get or set the URL to the article as a string
        """
        return self._url

    @url.setter
    def url(self, full_url):
        self._url = full_url
