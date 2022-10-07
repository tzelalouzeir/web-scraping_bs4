# webscrapping with bs4

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

```python
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup 

url = 'https://www.bestprice.gr/item/2156396846/sapphire-radeon-rx-6800-16gb-nitro.html'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
soup = soup(webpage, "html.parser")

# specify which column will be scraped in html code
lists = soup.find_all('div',attrs={'class':'prices__group'})
```
As we print(lists), will see bunch of HTML code. We can determine what we can to scrap. I would like to see name GPU and price for this reason but its so complex! There is one easy trick that you can find which title belong to name and price. 
- right click on price > Inspect > Right screen you will see Elements window
- <div class="prices__price"><a title="Sapphire Radeon RX 6800 16GB Nitro+ (11305-01-20G)" data-trackga="CTR Cluster|button|" rel="nofollow" href="/to/76138597/sapphire-radeon-rx-6800-16gb-nitro.html?from=&amp;seq=1&amp;bpref=itemPage">609,50€</a>
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
    price = i.find('div', attrs={'class':'prices__price'}).text[:8]
    title_data.append(title)
    price_data.append(price)
    
# another loop for href(links that starting with /item/ which they are products)    
for a in soup.find('div').find_all('a', href=re.compile('^/item/')):
    link_data.append(a['href'])
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[License](https://github.com/tzelalouzeir/webscrapping/blob/main/LICENSE)
