import article

a = article.Article()

a.url = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi="\
        "10.1.1.13.2424"

print(a.url)

a.get_page_soup()

print(a.soup)
