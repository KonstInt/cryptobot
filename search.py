import urllib
import requests
from bs4 import BeautifulSoup
def search_results(str):
  query = str
  query = query.replace(' ', '+')
  URL = f"https://google.com/search?q={query}"
  # desktop user-agent
  USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
  headers = {"user-agent" : USER_AGENT}
  resp = requests.get(URL, headers=headers)
  if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    print(resp.content)
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
        #title = g.find('h3').text
        item = {
            "text": text.text,
            "link": link
        }
        results.append(item)
        break
  if results == []:
      item = {
            "text": 'К сожалению я не смог найти короткого ответа на ваш вопрос, однако, возможно, то, что вы ищите, находится по ссылке:',
            "link": tmp
        }
      results.append(item)
      
  return results[0]['text']+'\n'+results[0]["link"]
    
def search_results2():
  query = 'Что такое майнинг'
  query = query.replace(' ', '+')
  URL = f"https://yandex.ru/search/?text={query}"
  # desktop user-agent
  USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
  headers = {"user-agent" : USER_AGENT}
  resp = requests.get(URL)
  if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    print(resp.content)
  results = []
  tmp = ''
  g = soup.find_all('li',class_='serp-item serp-item_card')
  for g in soup.find_all('div', class_='MjjYud'):
    if tmp == '':
        tmp = g.find_all(class_ = 'yuRUbf')[0].next.attrs['href']
    anchors = g.find_all(class_ = 'hgKElc')
    if anchors:
        text = anchors[0]
        link = g.find_all(class_ = 'yuRUbf')
        link = link[0].next.attrs['href']
        #title = g.find('h3').text
        item = {
            "text": text.text,
            "link": link
        }
        results.append(item)
        break
  if results == []:
      item = {
            "text": 'К сожалению я не смог найти короткого ответа на ваш вопрос, однако, возможно, то, что вы ищите, находится по ссылке:',
            "link": tmp
        }
      results.append(item)
      
  return results[0]['text']+'\n'+results[0]["link"]
    
