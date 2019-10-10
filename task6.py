r = requests.get('https://tech.co')
text = r.text
l1 = re.findall('title>(.+?)</title', text)

r = requests.get('https://nrkbeta.no')
text = r.text
l2 = re.findall('title>(.+?)</title', text)

r = requests.get('https://github.com')
text = r.text
l3 = re.findall('title>(.+?)</title', text)

print(l1, l2, l3, l4, l5, l6, l7,l8, l9, l10, l11, l12, l13, l14, l15)





4'https://fonts.googleapis.com', 5'https://techcrunch.com', 6'https://www.vice.com',
7'https://www.theregister.co.uk', 8'https://blog.hackeriet.no', 9'https://refsdalolsen.com',
10'https://blog.jessfraz.com', 11'https://carolynvanslyck.com', 12'http://blog.disapped.com',
13'https://hugo.md', 14'https://blog.jonasbengtson.se', 15'https://manfred.life', 16'https://www.kode24.no',
17'https://cxsecurity.com', 18'http://netsec.ws', 19'https://malicious.link', 20'https://blog.0day.rocks', 21'https://www.schneier.com',
22'https://www.matteomalvica.com', 23'https://canyouseeme.org', 24'https://www.howsmyssl.com',
25'https://tools.pingdom.com', 26'https://dnsdumpster.com', 27'https://repl.it', 28'https://gchq.github.io',
29'http://fcc.io', 30'http://exif.regex.info', 31'https://www.yr.no', 32'https://bgp.he.net', 33'https://censys.io',
34'https://crt.sh', 35'https://ghostproject.fr', 36'https://godbolt.org', 37'https://coolors.co',
38'https://palettegenerator.com', 39'https://leovoel.github.io', 40'https://flexboxfroggy.com',
41'https://bolig.sia.no', 42'https://uia.instructure.com', 43'https://fsweb.no', 44'https://cloud.timeedit.net',
45'https://e5.onthehub.com', 46'https://video.uia.no', 47'http://cair.datapor.no',
48'http://blog.disapped.com', 49'http://netsec.ws', 50'http://fcc.io', 51'http://exif.regex.info', 52'http://cair.datapor.no'
