# %%
import requests
import os

# DRAFT 01

cafile =  os.path.abspath('fiddler-certificate.crt')

proxies = {
  'https': 'http://127.0.0.1:8888',
  'http': 'http://127.0.0.1:8888'
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,la;q=0.6,de;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
 
res = requests.get(
    'https://automatetheboringstuff.com/files/rj.txt',
    proxies=proxies,
    timeout = 10,
    verify=cafile,
    headers=headers
    )
res.raise_for_status()

# %%
import bs4

res = requests.get(
    'http://www.amazon.com/Automate-Boring-Stuff-Python-Programmimg/dp/1593275994/'
    ,proxies=proxies
    ,timeout = 10
    ,verify=cafile
    ,headers=headers
    )

res.raise_for_status()

# %%
soup = bs4.BeautifulSoup(res.text)

# %%
elems = soup.select('#latestExtraProductInfoFeatureGroup .a-color-price')
price = elems[0].text.strip()

# %%
