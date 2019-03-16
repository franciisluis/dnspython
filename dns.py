import requests
import sys
from bs4 import BeautifulSoup
url = sys.argv[1]

site = 'https://www.whois.com/whois/{0}'.format(url)
header = {'Host': 'www.whois.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br'}

def get_data_info(site,url):
    req = requests.get(site, headers = header)
    code = req.status_code
    if code == 200:
        print("[+] Requisited! \n")
        html= req.text
        bs = BeautifulSoup(html,'lxml')
        div = bs.find_all('pre', {'class':'df-raw'})
        for divs in div:
            print(divs.get_text())
get_data_info(site,url)