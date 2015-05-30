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

