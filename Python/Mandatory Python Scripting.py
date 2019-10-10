import requests
import re


def task1():

    r = requests.get('https://google.com')
    text = r.text
    string = str(text)
    list = re.findall('title>(.+?)</title', text)
    s = set()

    for i in list:
        i = re.split('[.]', i)
        s.add(i[-1])

    print(s)

task1()