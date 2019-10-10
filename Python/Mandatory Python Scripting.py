import requests
import re


def task1():

    r = requests.get('https://google.com')
    text = r.text
    list1 = re.findall('title>(.+?)</title', text)

    print(list1)

task1()