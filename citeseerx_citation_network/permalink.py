#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that defines a link that is composed of a base url and a doi"""


class DigitalObjectIdentifier(object):
    """DOI with a link
    """

    def __init__(self, doi=None, url=None, base_url=None, **kwargs):
        if doi is not None:
            self.doi = doi
        else:
            self.doi = None
        if url is not None:
            # If you pass in a full url, it can be used to parse and assign
            # the base url and the DOI
            # pass in the kwarg parse=False if you do not want this automatic
            # assignment
            self.url = url
            self.parse_url_into_base_doi(**kwargs)
        else:
            self.url = None
        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = None

    def parse_url_into_base_doi(self, url=None, delim='doi=',
                                url_index=0, doi_index=1, parse=True):
        """Parse a url into it's base and doi and set each part accordinly

        Primiarly used in the constructor, where the :param parse: can be
        set to False if the user does not want to auto assign self.base_url
        and self.doi

        :param url: url to be passed, if no URL is passed,
        then self.url will be used
        :type url: str

        :param delim: delimiter to parse the url with the delim will be
        appended to the base after the split.  Defaults to 'doi='
        :type delim: str

        :param url_index: index of split for the base_url, default index 0
        :type url_index: int

        :param doi_index: index of split for the doi, default index 1
        :type doi_index: int

        :param parse: Whether to set the base_url and doi class instance
        variables.  This is because the constructor will call this method
        and this parameter is here just incase the user does not want to
        assign compondents of a URL
        :type parse: bool
        """
        if parse is True:
            if url is None:
                assert self.url is not None,\
                    "Cannot parse a url with a value of 'None'"
                url = self.url
                self.base_url = url.split(delim)[url_index] + delim
                self.doi = url.split(delim)[doi_index]
        return(self)

    @property
    def base_url(self):
        """Get or set the base_url fot the DOI object
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        assert isinstance(base_url, str) or base_url is None,\
            "base_url is not of type string it is: {}".\
            format(str(type(base_url)))
        self._base_url = base_url

    @property
    def doi(self):
        """Get or set the doi to the citations of an article as a string
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        assert isinstance(doi, str) or doi is None,\
            "doi is not of type string it is: {}".format(str(type(doi)))
        self._doi = doi

    @property
    def url(self):
        """Get or set the url to the citations of an article
        """
        return self._url

    @url.setter
    def url(self, url):
        assert isinstance(url, str) or url is None,\
            "url is not of type string, it is: {}".format(str(type(url)))
        self._url = url
