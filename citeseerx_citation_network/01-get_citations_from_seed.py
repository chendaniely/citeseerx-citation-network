import os
import csv

import citations

HERE = os.path.abspath(os.path.dirname(__file__))

c = citations.Citations(doi='10.1.1.13.2424')
print(c.doi)
print(c.base_url)
print(c.url)

c.url = c.base_url + c.doi

citation_result_path = os.path.join([HERE, 'output.csv'])
c.\
    get_page_soup().\
    get_result_info().\
    get_num_results().\
    get_num_page_results().\
    get_num_results()

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    c.get_all_result_soup(save_to=writer)
