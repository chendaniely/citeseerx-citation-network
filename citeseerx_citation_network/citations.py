#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines citations search results from an article"""

import re
import math
import random
import time

import requests
from bs4 import BeautifulSoup
from progressbar import ProgressBar

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

    def _get_page_soup_text(self, url):
        if url is None:
            r = requests.get(self.url)
        else:
            r = requests.get(url)
        data = r.text
        return(BeautifulSoup(data))

    def get_all_result_soup(self, save_to=None, list_append=True,
                            base_result_page_url=None,
                            base_search_result_url='&sort=cite&start=',
                            max_pause=120):
        """Iteratively get search result pages

        Iteratevely gets the search result pages, by default it will just
        print the values to screen and be stored in a variable.
        If a CSV or Database handler is passed, it will append to the
        file or database at the end of each iteration.  This could potentially
        be used to save work as the loop progresses

        :param save_to: where to save results to, default is None, which will
        only save values to a python list.
        :type save_to: str

        :param list_append: Whether the values should be stored in a list.
        :type list_append: bool

        :param base_result_page_url: base url of page results. Defaults to
        appending the appropriate suffix to self.url (which contains the doi)
        :type base_result_page_url: str

        :param base_search_ressult_url: appended to the base_result_page_url
        :type base_search_result_url: str

        :param max_pause: maximum number of seconds to pause between results.
        Defaults to 120 seconds (2 minutes)
        :type max_pause: int
        """
        if base_result_page_url is None:
            base_result_page_url = self.url + base_search_result_url
        else:
            base_result_page_url = base_result_page_url + \
                                   base_search_result_url

        assert self.num_page_results.is_integer(),\
            'self.num_page_results is not a whole number'

        if list_append is True:
            list_of_result_soup = []

        pbar = ProgressBar()

        for page in pbar(range(int(self.num_page_results) + 1)[:3]):
            start_citation = page * 10
            page_url = base_result_page_url + str(start_citation)
            list_of_result_soup.\
                append(self.get_page_soup(url=page_url, return_method='str'))
            pause_time = random.randrange(max_pause) + random.random()
            time.sleep(pause_time)
        if list_append is True:
            self.list_all_result_page_soup = list_of_result_soup
        return(self)

    def get_num_results(self, result_info=None,
                        split1=' of ', idx1=1,
                        split2=' ', idx2=0):
        if result_info is None:
            result_info = self.result_info

        num_results = result_info.\
            split(split1)[idx1].\
            split(split2)[idx2]
        self.num_results = int(num_results)
        print(num_results)
        return(self)

    def get_num_page_results(self, num_results=None, num_results_per_page=10,
                             offset=1):
        """Get the number of search page results from a given number of results

        :param num_results: number of results from a search, defaults to None
        because self.num_results typically needs to be caculated first
        :type num_results: int

        :param num_results_per_page: number of results per page, default to 10
        :type num_results_per_page: int

        :param offset: offset value for number of page result calculation.
        Default is 1.
        :type offset: int

        :returns: self

        The offset value exists because citeseerx does not count by page
        results, but rather it shows the result number to start from.
        if the num_results_per_page is 10, then the second page will show
        10.  This offset is so that we can multiply the num_page_results
        value by 10, and know which result number will be on the last page.
        """
        if num_results is None:
            num_results = self.num_results
        self.num_page_results = \
            math.ceil(num_results / float(num_results_per_page)) - offset
        return(self)

    def get_result_info(self, find_index=0):
        """Get the number of results
        """
        assert self.soup is not None, "self.soup has a value of None"
        result_info_soup = self._get_result_info_soup(find_index)
        result_info_soup_clean = self.\
            _get_results_info_soup_clean(result_info_soup)
        self.result_info = result_info_soup_clean
        return(self)

    def get_page_soup(self, url=None, return_method='self'):
        """Get the HTML soup of the article
        Depending on return_method, the soup would either be returned
        as a string, or set to self.soup and return self

        If no url is passed, then the relevent class variable will be used

        :param url: url to get soup from, defaults to None
        :type url: str

        :param return_method: how to set the soup - 'self' or 'str'
        :type return_method: str

        :returns: self
        """
        if return_method == 'self':
            self.soup = self._get_page_soup_text(url)
            return(self)
        if return_method == 'str':
            return(self._get_page_soup_text(url))
