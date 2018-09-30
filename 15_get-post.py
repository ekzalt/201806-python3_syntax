# Работа с Интернетом: GET, POST, Download
# urllib2 - python2, urllib - python3

############################################################

# GET

from urllib import request

res = request.urlopen('https://habr.com/')

output1 = res.read()
output2 = res.readlines()

print(output1)

for line in output2:
    print(line)

############################################################

# GET

import sys

from urllib import request, parse

url = 'https://www.google.com/search?'
query = {'q': 'git'}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

try:
    url = url + parse.urlencode(query)
    req = request.Request(url, headers=headers)
    res = request.urlopen(req)
    lines = res.readlines()

    for line in lines:
        print(line)
except Exception:
    print(sys.exc_info()[1])

############################################################

# Download

import sys

from urllib import request, parse

fromUrl = 'http://site.com/images/img01.jpg'
toFile = './images/img01.jpg'

try:
    request.urlretrieve(fromUrl, toFile)
except Exception:
    print(sys.exc_info())
    exit

print('Download and safe have been completed')
