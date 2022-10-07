from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup  
import pandas as pd
import re
from csv import writer
import csv
from itertools import chain

url = 'https://www.bestprice.gr/item/2156396846/sapphire-radeon-rx-6800-16gb-nitro.html'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
soup = soup(webpage, "html.parser")

# specify which column will be scraped in html code
lists = soup.find_all('div',attrs={'class':'prices__group'})

# create list for table
title_data=[]
price_data=[]
link_data=[]

# using for loop for getting all information that we want
for i in lists:
    title = i.find('div', attrs={'class':'prices__title'}).text
    price = i.find('div', attrs={'class':'prices__price'}).text[:7]
    title_data.append(title)
    price_data.append(price)
    
# another loop for href(links that starting with /item/ which they are products)    
for a in soup.find('div').find_all('a', href=re.compile('^/item/')):
    link_data.append(a['href'])
    
# while we are working on greek sites remove greek characters
greek_codes   = chain(range(0x370, 0x3e2), range(0x3f0, 0x400))
greek_symbols = (chr(c) for c in greek_codes)
greek_letters = [c for c in greek_symbols if c.isalpha()]
str1 = ''.join(greek_letters)
removetable = str.maketrans('','',str1)
out_list = [s.translate(removetable) for s in title_data]

# links need some page starting so which is bestprice.gr for me
link_data = list(dict.fromkeys(link_data))
link_head = 'https://www.bestprice.gr'
list3=pd.DataFrame(columns=link_data).add_prefix(link_head).columns.tolist()

with open("gpu/6800.csv", "w", encoding='utf-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['Titles','Prices','Links']
    writer.writerow(header)
    for value in range(len(out_list)):
        writer.writerow([out_list[value], price_data[value], list3[value]])
