import requests
import re


def task1():
    r = requests.get('https://links.datapor.no')
    print(r.text)

1
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


def task5():
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


if __name__ == '__main__':
    task1()
    task2()
    task5()














