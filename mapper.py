import urllib.request as ur
from time import sleep
from bs4 import BeautifulSoup

f = open('github_links.txt','r')

for link in f.read().split('\n'):
    response = ur.urlopen(link).read()
    soup = BeautifulSoup(response,'html.parser')     
    for links in soup.find_all('div', {'class':'repo-list-item'}):
        a = links.find('a')
        print(a['href'])
    sleep(1)

f.close()
