import sys
import csv

from bs4 import BeautifulSoup

import article

f = open(sys.argv[1], 'rt')
w = open('ouput_results.csv', 'w')

try:
    reader = csv.reader(f)
    writer = csv.writer(w)

    for row in reader:
        html = row[3]
        to = row[0]
        soup = BeautifulSoup(html)
        results = soup.find_all('div', class_='result')
        for result in results:
            links = result.find_all('a', class_='remove doc_details')
            for link in links:
                doi = str(link.get('href').split('doi=')[1])
                a = article.Article(doi=doi)
                print(a.doi)
                from_to = (doi, to)
                writer.writerow(from_to)
finally:
    f.close()
    w.close()
