import requests


def task1():
    r = requests.get('https://links.datapor.no')
    print(r.text)

def task4():
    host = len(re.findall("Head", test_str))
    print(str(host))

