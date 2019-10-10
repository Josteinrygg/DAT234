import requests
import re

def task5():

    r = requests.get('https://links.datapor.no')
    test_str = r.text
    string = str(test_str)
    list = re.findall('[<][a-zA-Z0-9]+[\s]|[<][a-zA-Z0-9]+[>]', string)
    s = set()

    for i in list:
        i = re.split('[<|>]', i)
        s.add(i[1])

    print(s)

task5()