#Tools We need to import to scrape data
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.amazon.com/"#requesting data from amazon
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

product=[]  # a list to store products

table = soup.find('div', attrs = {'id':'all_product'})

for row in table.findAll('div', attrs = {'class':'col-7 col-lg-1 text-center margin-40px-bottom sm-margin-40px-top'}):
    product = {}
    product['theme'] = row.h5.text
    product['url'] = row.a['href']
    product['img'] = row.img['src']
    product['lines'] = row.img['alt'].split(" #")[0]
    product['review'] = row.img['alt'].split(" #")[1]
    product.append(product)

filename = 'porductInfo.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','review'])
    w.writeheader()
    for product in product:
        w.writerow(product)

