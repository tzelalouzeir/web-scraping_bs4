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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[License](https://github.com/tzelalouzeir/webscrapping/blob/main/LICENSE)
