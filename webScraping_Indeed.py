# import libraries 

from bs4 import BeautifulSoup
import requests

def get(page) :
  headers = {'User-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
 # https://uk.indeed.com/jobs?q=Data+Analyst&l=United+Kingdom&start=0
 #https://in.indeed.com/jobs?q=Data+Analyst&l=India&start=10
  url = f'http://in.indeed.com/jobs?q=Data+Analyst&l=India&start={page}'
  r = requests.get(url, headers)
  soup = BeautifulSoup(r.content, 'html.parser')
  return soup


def transform(soup) :
  divs = soup.find_all('div',class_ = 'jobs-unified-top-card t-14')
  return len(divs)



c = get(0)
print(c)
print(transform(c))
