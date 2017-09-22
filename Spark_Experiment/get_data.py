#!/usr/bin/env python3
import urllib.request

url_train = 'https://www.dropbox.com/s/21v6bnz0lkcv2us/year-prediction-msd-train.txt.zip?dl=1'
url_test = 'https://www.dropbox.com/s/h1tavv5fwvi56nw/year-prediction-msd-test.txt.zip?dl=1'

u = urllib.request.urlopen(url_train)
data = u.read()
u.close()

with open('year-prediction-msd-train.txt.zip', "wb") as f :
    f.write(data)
