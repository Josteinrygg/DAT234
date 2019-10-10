
r = requests.get('https://tech.co')
text = r.text
l1 = re.findall('title>(.+?)</title', text)

r = requests.get('https://nrkbeta.no')
text = r.text
l2 = re.findall('title>(.+?)</title', text)

r = requests.get('https://github.com')
text = r.text
l3 = re.findall('title>(.+?)</title', text)

r = requests.get('https://fonts.googleapis.com')
text = r.text
l4 = re.findall('title>(.+?)</title', text)

r = requests.get('https://fonts.googleapis.com')
text = r.text
l5 = re.findall('title>(.+?)</title', text)

r = requests.get('https://www.vice.com')
text = r.text
l6 = re.findall('title>(.+?)</title', text)

r = requests.get('https://www.theregister.co.uk')
text = r.text
l7 = re.findall('title>(.+?)</title', text)

r = requests.get('https://blog.hackeriet.no')
text = r.text
l8 = re.findall('title>(.+?)</title', text)

r = requests.get('https://refsdalolsen.com')
text = r.text
l9 = re.findall('title>(.+?)</title', text)

r = requests.get('https://blog.jessfraz.com')
text = r.text
l10 = re.findall('title>(.+?)</title', text)

r = requests.get('https://carolynvanslyck.com')
text = r.text
l11 = re.findall('title>(.+?)</title', text)

r = requests.get('http://blog.disapped.com')
text = r.text
l12 = re.findall('title>(.+?)</title', text)

r = requests.get('https://hugo.md')
text = r.text
l13 = re.findall('title>(.+?)</title', text)

r = requests.get('https://blog.jonasbengtson.se')
text = r.text
l14 = re.findall('title>(.+?)</title', text)

r = requests.get('https://manfred.life')
text = r.text
l15 = re.findall('title>(.+?)</title', text)

r = requests.get('https://www.kode24.no')
text = r.text
l16 = re.findall('title>(.+?)</title', text)

r = requests.get('https://cxsecurity.com')
text = r.text
l17 = re.findall('title>(.+?)</title', text)

r = requests.get('http://netsec.ws')
text = r.text
l18 = re.findall('title>(.+?)</title', text)

r = requests.get('https://malicious.link')
text = r.text
l19 = re.findall('title>(.+?)</title', text)

r = requests.get('https://blog.0day.rocks')
text = r.text
l20 = re.findall('title>(.+?)</title', text)

r = requests.get('https://blog.0day.rocks')
text = r.text
l20 = re.findall('title>(.+?)</title', text)

r = requests.get('https://www.schneier.com')
text = r.text
l21 = re.findall('title>(.+?)</title', text)

r = requests.get('https://www.matteomalvica.com', text)
text = r.text
l22 = re.findall('title>(.+?)</title', text)

r = requests.get('https://canyouseeme.org')
text = r.text
l23 = re.findall('title>(.+?)</title', text)

r = requests.get('https://www.howsmyssl.com')
text = r.text
l24 = re.findall('title>(.+?)</title', text)

#r = requests.get('https://tools.pingdom.com')
#text = r.text
#l25 = re.findall('title>(.+?)</title', text)

r = requests.get('https://dnsdumpster.com')
text = r.text
l26 = re.findall('title>(.+?)</title', text)

r = requests.get('https://repl.it')
text = r.text
l27 = re.findall('title>(.+?)</title', text)

r = requests.get('https://gchq.github.io')
text = r.text
l28 = re.findall('title>(.+?)</title', text)

r = requests.get('http://fcc.io')
text = r.text
l29 = re.findall('title>(.+?)</title', text)

r = requests.get('http://exif.regex.info')
text = r.text
l30 = re.findall('title>(.+?)</title', text)

r = requests.get('https://www.yr.no')
text = r.text
l31 = re.findall('title>(.+?)</title', text)

r = requests.get('https://bgp.he.net')
text = r.text
l32 = re.findall('title>(.+?)</title', text)

r = requests.get('https://censys.io')
text = r.text
l33 = re.findall('title>(.+?)</title', text)

r = requests.get('https://crt.sh')
text = r.text
l34 = re.findall('title>(.+?)</title', text)

r = requests.get('https://ghostproject.fr')
text = r.text
l35 = re.findall('title>(.+?)</title', text)

r = requests.get('https://godbolt.org')
text = r.text
l36 = re.findall('title>(.+?)</title', text)

r = requests.get('https://coolors.co')
text = r.text
l37 = re.findall('title>(.+?)</title', text)

r = requests.get('https://palettegenerator.com')
text = r.text
l38 = re.findall('title>(.+?)</title', text)

r = requests.get('https://leovoel.github.io')
text = r.text
l39 = re.findall('title>(.+?)</title', text)

r = requests.get('https://flexboxfroggy.com')
text = r.text
l40 = re.findall('title>(.+?)</title', text)

r = requests.get('https://bolig.sia.no')
text = r.text
l41 = re.findall('title>(.+?)</title', text)

r = requests.get('https://uia.instructure.com')
text = r.text
l42 = re.findall('title>(.+?)</title', text)

r = requests.get('https://fsweb.no')
text = r.text
l43 = re.findall('title>(.+?)</title', text)

r = requests.get('https://cloud.timeedit.net')
text = r.text
l44 = re.findall('title>(.+?)</title', text)

r = requests.get('https://e5.onthehub.com')
text = r.text
l45 = re.findall('title>(.+?)</title', text)

r = requests.get('https://video.uia.no')
text = r.text
l46 = re.findall('title>(.+?)</title', text)

r = requests.get('http://cair.datapor.no')
text = r.text
l47 = re.findall('title>(.+?)</title', text)

r = requests.get('http://blog.disapped.com')
text = r.text
l48 = re.findall('title>(.+?)</title', text)

r = requests.get('http://netsec.ws')
text = r.text
l49 = re.findall('title>(.+?)</title', text)

r = requests.get('http://fcc.io')
text = r.text
l50 = re.findall('title>(.+?)</title', text)

r = requests.get('http://exif.regex.info')
text = r.text
l51 = re.findall('title>(.+?)</title', text)

r = requests.get('http://cair.datapor.no')
text = r.text
l52 = re.findall('title>(.+?)</title', text)


print(l1, l2, l3, l4, l5, l6, l7,l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l26, l27, l28, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, l51, l52)

