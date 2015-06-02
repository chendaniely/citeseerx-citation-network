import imp
import time

import article
import citations

imp.reload(article)
imp.reload(citations)

c = citations.Citations()
print(c)

print('-----')
# time.sleep(5)

c = citations.Citations(doi='10.1.1.13.2424')
print(c.doi)
print(c.base_url)
print(c.url)

# time.sleep(3.5)

print('======')

a = article.Article()
a.url = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi="\
        "10.1.1.13.2424"

c = citations.Citations(article=a)
print(c.article.url)
print(c.doi)
print(c.base_url)
print(c.url)

print('~~~~~')

a = article.Article(url="http://citeseerx.ist.psu.edu/viewdoc/summary?doi="
                    "10.1.1.13.2424")

c = citations.Citations(article=a)
print(c.article.url)
print(c.doi)
print(c.base_url)
print(c.url)
c.url = c.base_url + c.doi
c.parse_url_into_base_doi()
print(c.url)
print(c.doi)
print(c.base_url)

print('++++++++++')

c.get_page_soup().get_result_info().get_num_results().get_num_page_results()
# print(c.soup)
print("result info: ", c.result_info)
print("parsed num results: {}".format(str(c.num_results)))
print("num page results: {}".format(str(c.num_page_results)))

time.sleep(1)

# a = article.Article()

# a.url = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi="\
#         "10.1.1.13.2424"

# print(a.url)

# a.get_page_soup()

# # print(a.soup)

# # print(len(a.get_authors_soup()))
# print(a.get_authors())
# print(a.authors)

# # for blah in a.get_authors_soup():
# #     stripped = blah.strip()
# #     text = re.sub('^by\s+', '', stripped)
# #     cleaned_again = text.strip()
# #     print(cleaned_again)

# time.sleep(5)

# a = article.Article(doi='10.1.1.13.2424')
# print(a.url)
# a.get_page_soup()
# print(a.get_authors())
# print(a.authors)

# time.sleep(3.5)

# url = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi="\
#         "10.1.1.13.2424"
# a = article.Article(url=url)
# print(a.url)
# a.get_page_soup()
# print(a.get_authors())
# print(a.authors)
