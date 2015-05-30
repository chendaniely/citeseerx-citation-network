#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines citations search results from an article"""

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
