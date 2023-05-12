import urllib
import requests
from bs4 import BeautifulSoup
def search_results(str):
  query = str
  query = query.replace(' ', '+')
  URL = f"https://google.com/search?q={query}+криптовалюта"
  # desktop user-agent
  USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
  headers = {"user-agent" : USER_AGENT}
  resp = requests.get(URL, headers=headers)
  if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
  results = []
  tmp = ''
  for g in soup.find_all('div', class_='MjjYud'):
    if tmp == '':
        tmp = g.find_all(class_ = 'yuRUbf')[0].next.attrs['href']
    anchors = g.find_all(class_ = 'hgKElc')
    if anchors:
        text = anchors[0]
        link = g.find_all(class_ = 'yuRUbf')
        link = link[0].next.attrs['href']
        item = {
            "text": text.text + '\nИсточник:\n',
            "link": link
        }
        results.append(item)
        break
  if results == []:
      item = {
            "text": 'Вот что мне удалось найти:\n\n',
            "link": tmp
        }
      results.append(item)
      
  return results[0]['text']+results[0]["link"]
    
