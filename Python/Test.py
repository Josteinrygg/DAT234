import requests
import re

r = requests.get('https://links.datapor.no')
test_str = r.text
string = str(test_str)
matches = re.findall(r'(.com)', string)
output = []
for x in matches:
    if x not in output:
        output.append(x)
print(output)
