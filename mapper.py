#!/usr/bin/env python3

import urllib.request as ur
from bs4 import BeautifulSoup

def try_connection(link):
    """
    funtion used to request a web page and return it in a readable way.
    in case of excepetion, tries again.
    Paramenters:
    ------------
        link: link to be requested
    Return:
    -------
        ur.urlopen(link).read(): html parsed in a readable way
    """
    from time import sleep
    try:
        return ur.urlopen(link).read()
    except Exception as e:
        sleep(5)
        return try_connection(link)

for link in sys.stdin:
    if link == '':
        break
    response = try_connection(link)
    soup = BeautifulSoup(response,'html.parser')     
    for links in soup.find_all('div', {'class':'repo-list-item'}):
        a = links.find('a')
        print(a['href'])
