#! /usr/bin/env python

import requests

from citeseerx_citation_network import article


def base_article_url_test():
    a = article.Article()
    assert(a.base_article_url() ==
           "http://citeseerx.ist.psu.edu/viewdoc/summary?doi=")


def create_full_url_test():
    a = article.Article()
    doi_string = "TEST_DOI_STRING"
    calculated_full_url = a.create_full_url(doi_string)
    expected_full_url = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi="\
                        "TEST_DOI_STRING"
    assert(calculated_full_url == expected_full_url)

    doi_string = "10.1.1.13.2424"
    calculated_full_url = a.create_full_url(doi_string)
    expected_full_url = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi="\
                        "10.1.1.13.2424"
    assert(calculated_full_url == expected_full_url)
    assert(requests.get(calculated_full_url).status_code == 200)
