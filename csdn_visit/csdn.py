import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import random
import datetime
from time import sleep
from threading import Thread

random.seed(datetime.datetime.now())
article_list = []
proxy_list = []

User_Agent = [
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) "
    "Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) "
    "Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, "
    "like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) "
    "AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; OMNIA7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 60; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)"
]


def get_article_list():
    for i in range(1, 5):
        r = requests.get('https://blog.csdn.net/ssjdoudou/article/list/' + str(i),
                         headers={
                             'user-agent': User_Agent[random.randint(0, len(User_Agent) - 1)],
                             'referer': 'https://blog.csdn.net/ssjdoudou'
                         },
                         )
        html = r.text
        bsobj = BeautifulSoup(html, 'lxml')
        for h4 in bsobj.findAll('h4'):
            article_list.append(h4.a['href'])
        sleep(2)

    print('Done--get_article_list!', 'total articles:{}'.format(len(article_list)))
    f = open('article_list.txt', 'w')
    for j in article_list:
        f.write(j + '\n')
    f.close()


cookie = list()
cookie.append({'cookie': '79705eee-d157-4485-8ca3-c156fab8b1c8'})


def get_proxy_list():
    for row in urlopen('http://proxylist.fatezero.org/proxy.list').readlines():
        item = json.loads(row)
        if item['type'] == 'http' and item['anonymity'] == 'high_anonymous' and item['response_time'] < 7:
            proxy_list.append(item['host'] + ':' + str(item['port']))
    print('Done--get_proxy_list!')
    f = open('proxy_list.txt', 'w')
    for ip in proxy_list:
        f.write(ip + '\n')
    f.close()


def csdn():
    article_lists = []
    try:
        fa = open('/Users/Arithmetic/wuhan/article_list.txt', 'r')
        article_file = fa.readlines()
        for i in article_file:
            article_lists.append(i.strip('\n'))
        fa.close()
    except:
        print('read txt fail')
    article = article_lists[random.randint(0, len(article_lists) - 1)]
    proxy = {'http': proxy_list[random.randint(0, len(proxy_list) - 1)]}
    header = {'User-Agent': User_Agent[random.randint(0, len(User_Agent) - 1)],
              'referer': 'http://blog.csdn.net'}
    try:
        requests.get(article.replace('https', 'http'), headers=header, proxies=proxy,
                     cookies=cookie[random.randint(0, len(cookie) - 1)], timeout=7)
        print('ok ip:' + proxy['http'])
    except:
        print('no')


def csdn_exists():
    article_lists = []
    proxy_lists = []
    try:
        f1 = open('/Users/Arithmetic/wuhan/article_list.txt', 'r')
        article_file = f1.readlines()
        for i in article_file:
            article_lists.append(i.strip('\n'))
        f2 = open('/Users/Arithmetic/wuhan/proxy_list.txt', 'r')
        proxy_file = f2.readlines()
        for j in proxy_file:
            proxy_lists.append(j.strip('\n'))
        f1.close()
        f2.close()
    except:
        print('read txt fail')
    article = article_lists[random.randint(0, len(article_lists) - 1)]
    proxy = {'http': proxy_lists[random.randint(0, len(proxy_lists) - 1)]}
    header = {'User-Agent': User_Agent[random.randint(0, len(User_Agent) - 1)],
              'referer': 'http://blog.csdn.net'}
    try:
        requests.get(article.replace('https', 'https'), headers=header, proxies=proxy,
                     cookies=cookie[random.randint(0, len(cookie) - 1)], timeout=7)
        print('ok ip:' + proxy['http'])
    except:
        print('no')


get_proxy_list()
# get_article_list()


def do():
    while True:
        csdn()
        # csdn_exists()
        # if len(proxy_list)<200:
        #   f=open('output.out','w')
        #  print(proxy_list,file=f)
        # f.close()
        # exit()


mission = list()  # 多线程跑的快
nums = 50
for i in range(nums):
    mission.append(Thread(target=do))
for i in range(nums):
    mission[i].setDaemon(True)
    mission[i].start()
for i in range(nums):
    mission[i].join()
