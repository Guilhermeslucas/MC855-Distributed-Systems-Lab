import urllib.request as ur
from bs4 import BeautifulSoup

f = open('github_links.txt','r')

def try_connection(link):
    from time import sleep
    try:
        return ur.urlopen(link).read()
    except Exception as e:
        print(e)
        sleep(5)
        return try_connection(link)

for link in f.read().split('\n'):
    if link == '':
        break
    response = try_connection(link)
    soup = BeautifulSoup(response,'html.parser')     
    for links in soup.find_all('div', {'class':'repo-list-item'}):
        a = links.find('a')
        print(a['href'])

f.close()
