# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:33:58 2016

@author: Shen
"""

import urllib2
#import cookielib
import re
import json

#url = 'http://i.sso.sina.com.cn/js/ssologin.js'
#def get_loginjs(url):
#    cookie = cookielib.CookieJar()
#    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#    
#    headers = {
#        "Date":"Mon, 21 Mar 2016 05:32:23 GMT",
#        "Content-Type":"application/x-javascript",
#        "Expires":"Mon, 21 Mar 2016 05:34:23 GMT",
#        "Last-Modified":"Fri, 08 Aug 2014 05:57:32 GMT",
#        "Age":"82",
#        "X-Cache":"HIT from ctc.cd.1cf2.32.spool.sina.com.cn"
#    }
#    
#    req = urllib2.Request(
#        headers = headers,
#        url = url
#    )
#    
#    res = opener.open(req)
#    doc = res.read()
#    return doc

def get_ServerInfo(serverUrl):
#    serverUrl = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTU4ODIxNzc0NjE%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=1458538406996'
    serverData = urllib2.urlopen(serverUrl).read()
    jd = re.compile("\((.*)\)")
    jsonData = jd.search(serverData).group(1)
    data = json.loads(jsonData)
    serverTime = str(data['servertime'])
    nonce = data['nonce']
    rsakv = data['rsakv']
    pubkey = data['pubkey']
    return serverTime,nonce,rsakv,pubkey