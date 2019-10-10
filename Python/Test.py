import requests
import re

links = ['https://tech.co', 'https://nrkbeta.no', 'https://github.com',
         'https://fonts.googleapis.com', 'https://techcrunch.com', 'https://www.vice.com',
         'https://www.theregister.co.uk', 'https://blog.hackeriet.no', 'https://refsdalolsen.com',
         ]
for url in links:
    page = requests.get(url)
    print(page.text)


