# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:50:20 2016

@author: Shen
"""

from threading import Thread
import time
import LogIn
import GetWeiboContents
import datetime

startTime =  datetime.datetime.now()
userName = ''
password = ''
LogIn.logIn(userName,password)
mokamoka = GetWeiboContents.getMessages('')#填入一个微博账号的数字id
path = 'E:/PythonLearning/PythonSpider/Weibo/Datas/Frends/'+str(mokamoka.id)#请自行修改path路径，没有将会被创建
mokamoka.setPath(path)
def CrawlKay(st,ed):
    p = st
    sum = 0
    while p <=ed:
        try:
            mokamoka.getWeiboContent(p)
            time.sleep(1)
        except Exception as e:
            sum += 1
            if sum >= 10:
                p += 1
                sum = 0
            continue
        p += 1

#def run():
threads = []
thr1 = Thread(target=CrawlKay,args=(1,15))
threads.append(thr1)
thr2 = Thread(target=CrawlKay,args=(16,30))
threads.append(thr2)

for t in threads:
    t.setDaemon(True)
    t.start()
t.join()
endTime =  datetime.datetime.now()
sec = (endTime-startTime).seconds
print sec