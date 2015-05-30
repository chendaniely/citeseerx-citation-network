#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines citations search results from an article"""

import re

import requests
from bs4 import BeautifulSoup

import permalink


class Citations(permalink.DigitalObjectIdentifier):
    """Citations results from an Article
    """

    def __init__(self, article=None, doi=None, url=None,
                 base_url='http://citeseerx.ist.psu.edu/showciting?doi='):
        if article is not None:
            assert isinstance(article, object),\
                "article param needs to be an object, currently {}".\
                format(str(type(article)))
            self.article = article
            self.doi = article.doi
            self.url = url
            self.base_url = base_url
        else:
            super(Citations, self).__init__(doi=doi, url=url,
                                            base_url=base_url)

    def _get_result_info_soup(self, find_index=0):
        return(self.soup.find_all('div', id='result_info')[find_index])

    def _get_results_info_soup_clean(self, result_info_soup):
        stripped = result_info_soup.getText().strip()
        single_white_space = re.sub('\s+', ' ', stripped)
        match = re.match('^Results\s\d+\s-\s\d+\sof\s\d+', single_white_space)
        assert match is not None
        return(single_white_space)

    def get_result_info(self, find_index=0):
        """Get the number of results
        """
        assert self.soup is not None, "self.soup has a value of None"
        result_info_soup = self._get_result_info_soup(find_index)
        result_info_soup_clean = self.\
            _get_results_info_soup_clean(result_info_soup)
        self.result_info = result_info_soup_clean
        return(self)

    def get_page_soup(self, url=None):
        """Use self.url to get the HTML soup of the article
        and set the HTML soup to self.soup.  If no url is passed
        will use self.url to get soup

        :param url: url to get soup from, defaults to None
        :type url: str

        :returns: self
        """
        if url is None:
            r = requests.get(self.url)
        else:
            r = requests.get(url)
        data = r.text
        self.soup = BeautifulSoup(data)
        return(self)
