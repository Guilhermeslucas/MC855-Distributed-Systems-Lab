#!/usr/bin/env python3
import urllib.request

#really simple to download some datasets from dropbox

urls = ['https://www.dropbox.com/s/21v6bnz0lkcv2us/year-prediction-msd-train.txt.zip?dl=1',
        'https://www.dropbox.com/s/h1tavv5fwvi56nw/year-prediction-msd-test.txt.zip?dl=1']

names = ['year-prediction-msd-train.txt.zip','year-prediction-msd-test.txt.zip']

for i in range(0,2):
    u = urllib.request.urlopen(urls[i])
    data = u.read()
    u.close()

    with open(names[i], "wb") as f :
        f.write(data)

