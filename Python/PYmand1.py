import requests
import re


def task1():
    r = requests.get('https://links.datapor.no')
    print(r.text)

def task2():
    re.sub('(http|https)://[\w-]+(.[\w-]+)+\S*')


task1()













