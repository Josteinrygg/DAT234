import requests
import re

urls = ['https://tech.co', 'https://nrkbeta.no', 'https://github.com']
for url in urls:
    page = requests.get(url)
    print(page.text)






'https://fonts.googleapis.com', 'https://techcrunch.com', 'https://www.vice.com',
'https://www.theregister.co.uk', 'https://blog.hackeriet.no', 'https://refsdalolsen.com',
'https://blog.jessfraz.com', 'https://carolynvanslyck.com', 'http://blog.disapped.com',
'https://hugo.md', 'https://blog.jonasbengtson.se', 'https://manfred.life', 'https://www.kode24.no',
'https://cxsecurity.com', 'http://netsec.ws', 'https://malicious.link', 'https://blog.0day.rocks', 'https://www.schneier.com',
'https://www.matteomalvica.com', 'https://canyouseeme.org', 'https://www.howsmyssl.com',
'https://tools.pingdom.com', 'https://dnsdumpster.com', 'https://repl.it', 'https://gchq.github.io',
'http://fcc.io', 'http://exif.regex.info', 'https://www.yr.no', 'https://bgp.he.net', 'https://censys.io',
'https://crt.sh', 'https://ghostproject.fr', 'https://godbolt.org', 'https://coolors.co',
'https://palettegenerator.com', 'https://leovoel.github.io', 'https://flexboxfroggy.com',
'https://bolig.sia.no', 'https://uia.instructure.com', 'https://fsweb.no', 'https://cloud.timeedit.net',
'https://e5.onthehub.com', 'https://video.uia.no', 'http://cair.datapor.no',
'http://blog.disapped.com', 'http://netsec.ws', 'http://fcc.io', 'http://exif.regex.info', 'http://cair.datapor.no'
