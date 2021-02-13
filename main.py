# %%
import requests
import bs4
import os
import sys
from urllib.parse import urlparse

url = ''
dev_environment = False

#  check if program was launched by terminal or another launcher
if sys.argv[0] == os.path.basename(__file__) or \
   sys.argv[0] == os.path.abspath(__file__):
    # cmd has launched program
    # check presence of command line arguments
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        print('Please provide a valid Amazon\'s product URL in order to get the price')
        exit(1)
else:
    # program was invoked by another origin,
    # we could check if origin is ipykernel launcher for example
    if 'ipykernel_launcher' in sys.argv[0]:
        dev_environment = True
        # in this dev environment define a fixed url
        url = 'https://www.amazon.com/Automate-Boring-Stuff-Python-Programmimg/dp/1593275994/'

domain = urlparse(url).netloc

if domain == '':
    print('Please provide a valide URL')
    if dev_environment:
        raise SystemExit("Stop IPython kernel") 
    else:
        exit(1)

if "amazon.com" not in domain:
    print('Please provide a URL of Amazon\'s domain (www.amazon.com)') 
    if dev_environment:
        raise SystemExit("Stop IPython kernel") 
    else:
        exit(1)
    
navigation_session = requests.Session()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,la;q=0.6,de;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

navigation_session.headers.update(headers) 

# %%
# - if you want to see requests in Fiddler run this cell, 
# - otherwise comment this block in the final program code    
cafile =  os.path.abspath('fiddler-certificate.crt')
proxies = {
  'https': 'http://127.0.0.1:8888',
  'http': 'http://127.0.0.1:8888'
}
navigation_session.proxies = proxies
navigation_session.verify = cafile

# %%
# - Methods
def get_amazon_price(product_url):
    try:
        res = navigation_session.get(
        product_url
        ,timeout = 10
        )
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        elems = soup.select('[data-feature-name=mediamatrix] .a-color-price')
        if len(elems) == 0:
            # try another price location
            elems = soup.select("[id^=mediaTab_heading].a-active span.mediaTab_subtitle")
        if len(elems) == 0:
            elems = soup.select("#tmmSwatches li.selected .a-color-price")
        if len(elems) == 0:
            elems = soup.select("#price_inside_buybox")    
        price = elems[0].text.strip()
    except Exception as err:
        #print(err)
        return ''
    return price

# %%
price = get_amazon_price(url)
if price == '':
    print('Price not found')
else:   
    print('The price is ' + price)
