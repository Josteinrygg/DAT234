import requests
import re


def task1():
    print("Denne tasken printer ut Unicode fra https://links.datapor.no:")
    print("\n")
    r = requests.get('https://links.datapor.no')
    print(r.text)


def task2():
        test_str = "<html> <head> <meta charset=  utf-8-> <meta name=-author  content= https://github.com/0-l > <link rel= stylesheet  type= text/css  href= css/awoo.min.css > <link href= https://fonts.googleapis.com/css?family=Nunito:200|Roboto:100,400,700  rel= stylesheet > <link href= https://fonts.googleapis.com/icon?family=Material+Icons  rel= stylesheet > <link href= css/style.css  rel= stylesheet  type= text/css > <title>links.datapor.no</title> </head> <body> <div id= links  class= - > <div id= tabs  class= !- > <cols> <ul class= - indicator > <li active></li> </ul> <div class= + widgets col-end > <p class= time >00<span>:00</span></p> <div class= !+ + weather-config > <input name= color  type= text  placeholder= location > </div> <div class= + weather > <button class= !+ edit >edit</button> <p temperature>4ÂºC</p> <p weather class= + > <i class= material-icons  sunny>wb_sunny</i> </p> </div> </div> </cols> </div> <div id= panels > <ul class= Blogs  active> <div class= links > <li> <h1>Tech</h1> <a href= https://nrkbeta.no/ >Nrkbeta</a> <a href= https://tech.co/ >Tech.co</a> <a href= https://techcrunch.com/ >TechCrunch</a> <a href= https://www.vice.com/en_us/section/tech >ViceTech</a> <a href= https://www.theregister.co.uk/ >The Register</a> <a href= https://blog.hackeriet.no/ >Hackeriet</a> <a href= https://refsdalolsen.com/category/blog/ >Ros Blog</a> <a href= https://blog.jessfraz.com/ >Jessie Frazelle</a> <a href= https://carolynvanslyck.com/blog/ >Carolyn Van Slyck</a> <a href= http://blog.disapped.com/ >stian</a> <a href= https://hugo.md/ >hugo.md</a> <a href= https://blog.jonasbengtson.se/ >JONAS SPACE</a> <a href= https://manfred.life/ >Manfred</a> <a href= https://www.kode24.no/ >kode24</a> </li> <li> <h1> Security </h1> <a href= https://cxsecurity.com/ >CxSecurity</a> <a href= http://netsec.ws/ >Netsec Addict</a> <a href= https://malicious.link/post/ >Mubix</a> <a href= https://blog.0day.rocks/ >0day.rocks</a> <a href= https://www.schneier.com/ >Schneier</a> <a href= https://www.matteomalvica.com/ >MatteoMalvica</a> </li> </div> </ul> <ul class= Tools > <div class= links > <li> <h1>Tools</h1> <a href= https://canyouseeme.org/ >CanYouSeeMe</a> <a href= https://www.howsmyssl.com/ >HowsmySSL</a> <a href= https://tools.pingdom.com/ >Pingdom Tools</a> <a href= https://dnsdumpster.com/ >DNSdumpster</a> <a href= https://repl.it/languages >Repl.it</a> <a href= https://gchq.github.io/CyberChef/ >Cyberchef</a> <a href= http://fcc.io/ >FCC</a> <a href= http://exif.regex.info/exif.cgi >Img Metadata</a> <a href= http://fcc.io/ >FCC</a> <a href= https://www.yr.no/kart/ >YR Map</a> <a href= https://bgp.he.net/ >BGP</a> <a href= https://censys.io/ >Censys</a> <a href= https://crt.sh/ >Crtsh</a> <a href= https://ghostproject.fr/ >Ghosts</a> <a href= https://godbolt.org/ >Compiler Explorer</a> <a href= https://coolors.co/ >Colorscheme Gen</a> <a href= https://palettegenerator.com/ >Palette Gen</a> <a href= https://leovoel.github.io/embed-visualizer/ >Discord Embed</a> <a href= https://flexboxfroggy.com/ >Learn Css</a> </li> </div> </ul> <ul class= Github > <div class= links > <li> <h1>Github</h1> <a href= https://github.com/eugenekolo/sec-tools >secTools</a> <a href= https://github.com/swisskyrepo/PayloadsAllTheThings >Payloads</a> <a href= https://github.com/AlessandroZ/LaZagne >LaZagne</a> <a href= https://github.com/FortyNorthSecurity/EyeWitness >EyeWitness</a> <a href= https://github.com/wifiphisher/wifiphisher >Wifiphisher</a> <a href= https://github.com/trustedsec/ptf >PTF</a> <a href= https://github.com/Gallopsled/pwntools >Pwntools</a> <a href= https://github.com/dxa4481/truffleHog >truffleHog</a> </li> </div> </ul> <ul class= Awesome > <div class= links > <li> <h1>Awesome</h1> <a href= https://github.com/Kickball/awesome-selfhosted >Selfhosted</a> <a href= https://github.com/EbookFoundation/free-programming-books >Free Ebooks</a> <a href= https://github.com/Junnplus/awesome-python-books >Python Ebooks</a> <a href= https://github.com/0xAX/linux-insides >Linux Insides</a> </li> </div> </ul> <ul class= UiA > <div class= links > <li> <h1>University</h1> <a href= https://bolig.sia.no/logindirect >Sia Bolig</a> <a href= https://uia.instructure.com/ >Canvas</a> <a href= https://fsweb.no/studentweb/login.jsf?inst=FSUIA >Studentweb</a> <a href= https://cloud.timeedit.net/uia/web/tp/ >TimeEdit</a> <a href= https://e5.onthehub.com/WebStore/ProductsByMajorVersionList.aspx?ws=a584d5fe-5fff-e011-8e6c-f04da23e67f6&vsro=8 >Microsoft Imagine</a> <a href= https://video.uia.no/ >Video UiA</a> <a href= http://cair.datapor.no >Cair Calendar</a></a></a></a></a></a></a></a> </li> </div> </ul> </div> </div> <script type= text/javascript  src= js/strftime.js ></script> <script type= text/javascript  src= js/weather.js ></script> <script type= text/javascript  src= js/powerline.js ></script> <script type= text/javascript  src= js/script.js ></script> <script type= text/javascript  src= js/search.js ></script> </body> </html>"

        # Bruker re.findall til å finne alle "http"
        # Teller "http"
        count = len(re.findall("http:", test_str))

        # Skriver ut resultatet
        print("Antall http: i stringen er : "
              + str(count))

        # Bruker re.findall til å finne alle "http"
        # Teller "http"
        count = len(re.findall("https:", test_str))

        # Skriver ut resultatet
        print("Antall https: i stringen er : "
              + str(count))

        print("\n")



def task3():
    print('Dette er alle de unike TLD i den requestede URLen')
    r = requests.get('https://links.datapor.no')
    text = r.text
    string = str(text)
    list = re.findall('.*\://(?:www.)?([^\/]+)', text)
    s = set()

    for i in list:
        i = re.split('[.]', i)
        s.add(i[-1])

    print(s)

    print("\n")



def task4():
        test_str = "<html> <head> <meta charset= utf-8-> <meta name=-author content= https://github.com/0-l > <link rel= stylesheet type= text/css href= css/awoo.min.css > <link href= https://fonts.googleapis.com/css?family=Nunito:200|Roboto:100,400,700 rel= stylesheet > <link href= https://fonts.googleapis.com/icon?family=Material+Icons rel= stylesheet > <link href= css/style.css rel= stylesheet type= text/css > <title>links.datapor.no</title> </head> <body> <div id= links class= - > <div id= tabs class= !- > <cols> <ul class= - indicator > <li active></li> </ul> <div class= + widgets col-end > <p class= time >00<span>:00</span></p> <div class= !+ + weather-config > <input name= color type= text placeholder= location > </div> <div class= + weather > <button class= !+ edit >edit</button> <p temperature>4 ºC</p> <p weather class= + > <i class= material-icons sunny>wb_sunny</i> </p> </div> </div> </cols> </div> <div id= panels > <ul class= Blogs active> <div class= links > <li> <h1>Tech</h1> <a href= https://nrkbeta.no/ >Nrkbeta</a> <a href= https://tech.co/ >Tech.co</a> <a href= https://techcrunch.com/ >TechCrunch</a> <a href= https://www.vice.com/en_us/section/tech >ViceTech</a> <a href= https://www.theregister.co.uk/ >The Register</a> <a href= https://blog.hackeriet.no/ >Hackeriet</a> <a href= https://refsdalolsen.com/category/blog/ >Ros Blog</a> <a href= https://blog.jessfraz.com/ >Jessie Frazelle</a> <a href= https://carolynvanslyck.com/blog/ >Carolyn Van Slyck</a> <a href= http://blog.disapped.com/ >stian</a> <a href= https://hugo.md/ >hugo.md</a> <a href= https://blog.jonasbengtson.se/ >JONAS SPACE</a> <a href= https://manfred.life/ >Manfred</a> <a href= https://www.kode24.no/ >kode24</a> </li> <li> <h1> Security </h1> <a href= https://cxsecurity.com/ >CxSecurity</a> <a href= http://netsec.ws/ >Netsec Addict</a> <a href= https://malicious.link/post/ >Mubix</a> <a href= https://blog.0day.rocks/ >0day.rocks</a> <a href= https://www.schneier.com/ >Schneier</a> <a href= https://www.matteomalvica.com/ >MatteoMalvica</a> </li> </div> </ul> <ul class= Tools > <div class= links > <li> <h1>Tools</h1> <a href= https://canyouseeme.org/ >CanYouSeeMe</a> <a href= https://www.howsmyssl.com/ >HowsmySSL</a> <a href= https://tools.pingdom.com/ >Pingdom Tools</a> <a href= https://dnsdumpster.com/ >DNSdumpster</a> <a href= https://repl.it/languages >Repl.it</a> <a href= https://gchq.github.io/CyberChef/ >Cyberchef</a> <a href= http://fcc.io/ >FCC</a> <a href= http://exif.regex.info/exif.cgi >Img Metadata</a> <a href= http://fcc.io/ >FCC</a> <a href= https://www.yr.no/kart/ >YR Map</a> <a href= https://bgp.he.net/ >BGP</a> <a href= https://censys.io/ >Censys</a> <a href= https://crt.sh/ >Crtsh</a> <a href= https://ghostproject.fr/ >Ghosts</a> <a href= https://godbolt.org/ >Compiler Explorer</a> <a href= https://coolors.co/ >Colorscheme Gen</a> <a href= https://palettegenerator.com/ >Palette Gen</a> <a href= https://leovoel.github.io/embed-visualizer/ >Discord Embed</a> <a href= https://flexboxfroggy.com/ >Learn Css</a> </li> </div> </ul> <ul class= Github > <div class= links > <li> <h1>Github</h1> <a href= https://github.com/eugenekolo/sec-tools >secTools</a> <a href= https://github.com/swisskyrepo/PayloadsAllTheThings >Payloads</a> <a href= https://github.com/AlessandroZ/LaZagne >LaZagne</a> <a href= https://github.com/FortyNorthSecurity/EyeWitness >EyeWitness</a> <a href= https://github.com/wifiphisher/wifiphisher >Wifiphisher</a> <a href= https://github.com/trustedsec/ptf >PTF</a> <a href= https://github.com/Gallopsled/pwntools >Pwntools</a> <a href= https://github.com/dxa4481/truffleHog >truffleHog</a> </li> </div> </ul> <ul class= Awesome > <div class= links > <li> <h1>Awesome</h1> <a href= https://github.com/Kickball/awesome-selfhosted >Selfhosted</a> <a href= https://github.com/EbookFoundation/free-programming-books >Free Ebooks</a> <a href= https://github.com/Junnplus/awesome-python-books >Python Ebooks</a> <a href= https://github.com/0xAX/linux-insides >Linux Insides</a> </li> </div> </ul> <ul class= UiA > <div class= links > <li> <h1>University</h1> <a href= https://bolig.sia.no/logindirect >Sia Bolig</a> <a href= https://uia.instructure.com/ >Canvas</a> <a href= https://fsweb.no/studentweb/login.jsf?inst=FSUIA >Studentweb</a> <a href= https://cloud.timeedit.net/uia/web/tp/ >TimeEdit</a> <a href= https://e5.onthehub.com/WebStore/ProductsByMajorVersionList.aspx?ws=a584d5fe-5fff-e011-8e6c-f04da23e67f6&vsro=8 >Microsoft Imagine</a> <a href= https://video.uia.no/ >Video UiA</a> <a href= http://cair.datapor.no >Cair Calendar</a></a></a></a></a></a></a></a> </li> </div> </ul> </div> </div> <script type= text/javascript src= js/strftime.js ></script> <script type= text/javascript src= js/weather.js ></script> <script type= text/javascript src= js/powerline.js ></script> <script type= text/javascript src= js/script.js ></script> <script type= text/javascript src= js/search.js ></script> </body> </html>"

        # Finner alle links med https.
        https = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', test_str)

        # Printer kun unike links.
        output = []
        for x in https:
            if x not in output:
                output.append(x)
        print(output)

        # Finner alle links med http.
        http = re.findall('http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', test_str)

        # Printer kun unike links.
        output = []
        for x in http:
            if x not in output:
                output.append(x)
        print(output)

        print("\n")



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

    print("\n")



def task6():
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

    # r = requests.get('https://tools.pingdom.com')
    # text = r.text
    # l25 = re.findall('title>(.+?)</title', text)

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

    print(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l26,
    l27, l28, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42, l43, l44, l45, l46, l47, l48, l49,
    l50, l51, l52)



if __name__ == '__main__':
    print("\n")

    print('TASK 1')
    task1()
    print("\n")

    print('TASK 2')
    task2()
    print("\n")

    print('TASK 3')
    task3()
    print("\n")

    print('TASK 4')
    print("Dette er alle domenene hentet fra https://links.datapor.no:")
    task4()
    print("\n")

    print('TASK 5')
    print("Her er alle de unike HTML tagsene hentet fra https://links.datapor.no:")
    task5()
    print("\n")

    print('TASK 6')
    print("Her er titlene på de respektive siden funnet i http://links.datapor.no")
    print("LOADING...")
    task6()
    print("\n")
















