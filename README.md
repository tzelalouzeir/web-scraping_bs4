
# webscrapping with bs4 and saving as .csv

Sometimes it's so difficult for me to search GPU prices and I'm lazy. For this reason simply created program which is web scrapping with beautifulsoup4 (simply we can call bs4). This code is for educational.

- used [bestprice.gr](https://www.youtube.com/shorts/843c0Ek9Ys4) as scrapping
- knowledge HTML, CSS
- if using different website you should change some headers and titles.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bs4.

```bash
pip install beautifulsoup4
```

## Usage
- Python 3.10.5
- Beautifulsoup4
- pandas 1.3.4
```python
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
import re
from itertools import chain 

url = 'https://www.bestprice.gr/item/2156396846/sapphire-radeon-rx-6800-16gb-nitro.html'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
soup = soup(webpage, "html.parser")

# specify which column will be scraped in html code
lists = soup.find_all('div',attrs={'class':'prices__group'})
```
As we ```print(lists)```, will see bunch of HTML code. We can determine what we can to scrap. Lets search name GPU and prices but its so complex! There is one easy trick that you can find which title belong to name and price.
- go website (im searching rx 6800 gpus you can change it) 
- right click on price > Inspect > Right screen you will see Elements window
- ```<div class="prices__price"><a title="Sapphire Radeon RX 6800 16GB Nitro+ (11305-01-20G)" data-trackga="CTR Cluster|button|" rel="nofollow" href="/to/76138597/sapphire-radeon-rx-6800-16gb-nitro.html?from=&amp;seq=1&amp;bpref=itemPage">609,50€</a>```
- as we see prices_price is our title to find price 


```python
# create list for table 
title_data=[]
price_data=[]
link_data=[]

# using for loop for getting all information that we want
# used to remove some words and just pull price for this 

for i in lists:
    title = i.find('div', attrs={'class':'prices__title'}).text
    price = i.find('div', attrs={'class':'prices__price'}).text[:7]
    title_data.append(title)
    price_data.append(price)
 
# another loop for href(links that starting with /item/ which they are products)    
for a in soup.find('div').find_all('a', href=re.compile('^/item/')):
    link_data.append(a['href'])

# links need some page starting so which is bestprice.gr for me
link_data = list(dict.fromkeys(link_data))
link_head = 'https://www.bestprice.gr'
list3=pd.DataFrame(columns=link_data).add_prefix(link_head).columns.tolist()
```

```python
# while working on greek site remove greek characters cause need pure data
greek_codes   = chain(range(0x370, 0x3e2), range(0x3f0, 0x400))
greek_symbols = (chr(c) for c in greek_codes)
greek_letters = [c for c in greek_symbols if c.isalpha()]
str1 = ''.join(greek_letters)
removetable = str.maketrans('','',str1)
out_list = [s.translate(removetable) for s in title_data]
```
```python
from csv import writer
import csv

# Saving results to CSV file 
with open("gpu/6800.csv", "w", encoding='utf-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['Titles','Prices','Links']
    writer.writerow(header)
    for value in range(len(out_list)):
        writer.writerow([out_list[value], price_data[value], list3[value]])
```
## Results .csv



| Titles        | Prices           | Links  |
| ------------- |:-------------:| -----:|
|	Sapphire Radeon RX 6800 16GB Nitro+  (11305-01-20G) |627,50€ | https://www.bestprice.gr/item/2156893...
|	Sapphire Radeon RX 6800 16GB Nitro+| 	644,56€| https://www.bestprice.gr/item/215543...
|	VGA SAPPHIRE NITRO+ RADEON RX 6800 16GB Gaming GDDR6 OC  (UEFI)| 626,54€| https://www.bestprice.gr/item/234543..
|	SAPPHIRE NITRO+ RX 6800 16 GB GDDR6|631,96€| https://www.bestprice.gr/item/2173893...
|	Sapphire Radeon RX 6800 16GB Nitro+  (11305-01-20G)| 643,50€|https://www.bestprice.gr/item/09657...
|	Sapphire Radeon RX 6800 Nitro+ 16GB GDDR6 11305-01-20G| 719,13€|https://www.bestprice.gr/item/23475...
|	Sapphire Radeon Nitro+ RX 6800 16GB GDDR6, 256-Bit, HDMI, DP  (11305-01-20G)|749,04€|https://www.bestprice.gr/item/1257...
|   Sapphire NITRO+ RX 6800 - graphics card - Radeon RX 6800 - 16 GB| 767,00€|https://www.bestprice.gr/item/666...
|	Sapphire Radeon RX 6800 16GB Nitro+     | 961,50€|https://www.bestprice.gr/item/6969...

**If there is any bugs, please contact me.**

## Support me with Star ⭐
Thank for everyone.

## Authors 🗿
github: [Tzelal Ouzeir](https://github.com/tzelalouzeir) 

## License
- Copyright © 2022 [Tzelal Ouzeir](https://github.com/tzelalouzeir) 
- [MIT](https://github.com/tzelalouzeir/webscrapping/blob/main/LICENSE)
