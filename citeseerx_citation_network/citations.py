#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines citations search results from an article"""

import permalink


class Citations(permalink.DigitalObjectIdentifier):
    """Citations results from an Article
    """

    def __init__(self, article=None, **kwargs):
        super(Citations, self).__init__(**kwargs)

        # if article is not None:
        #     pass
        # elif doi is not None:
        #     self.doi = doi
        # elif url is not None:
        #     self.url = url
        # else:
        #     self.doi = None
        #     self.url = None

    # @property
    # def doi(self):
    #     """Get or set the doi to the citations of an article as a string
    #     """
    #     return self._doi

    # @doi.setter
    # def doi(self, doi):
    #     assert isinstance(doi, str) or doi is None,\
    #         "doi is not of type string it is: {}".format(str(type(doi)))
    #     self._doi = doi

    # @property
    # def url(self):
    #     """Get or set the url to the citations of an article
    #     """
    #     return self._url

    # @url.setter
    # def url(self, url):
    #     assert isinstance(url, str) or url is None,\
    #         "url is not of type string, it is: {}".format(str(type(url)))
    #     self._url = url
