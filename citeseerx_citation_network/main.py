import imp
import time

import article
import citations

imp.reload(article)
imp.reload(citations)

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
