# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:28:37 2016

@author: Shen
"""
import DataEncoding
import GetLogInInfo
import urllib
import urllib2
import re
import cookielib
from win32api import GetSystemMetrics
import json


#url = 'http://weibo.com/p/1005051777696784/home?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop'
userName = ''
password = ''

def getRedirectUrl(text):
    reUrl = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
    rediUrl = reUrl.search(text).group(1)
#    print rediUrl
    return rediUrl

def logIn(userName,password):
    url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    userName = DataEncoding.get_userName(userName)
    serverUrl = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)'
    serverTime,nonce,rsakv,pubkey = GetLogInInfo.get_ServerInfo(serverUrl)
    password = DataEncoding.get_pwd(password,serverTime,nonce,pubkey)
    cookie = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    headers = {
        "Host":"login.sina.com.cn",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#        "Accept-Encoding":"gzip, deflate",
        "Referer":"http://weibo.com/",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    
    data = {
        "entry":"weibo",
        "gateway":"1",
        "from":"",
        "savestate":"7",
        "useticket":"1",
        "pagerefer":"http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F",
        "vsnf":"1",
        "su":userName,
        "service":"miniblog",
        "servertime":serverTime,
        "nonce":nonce,
        "pwencode":"rsa2",
        "rsakv":rsakv,
        "sp":password,
        "sr":str(GetSystemMetrics(0)) + "*" + str(GetSystemMetrics(1)),
        "encoding":"UTF-8",
#        "prelt":"106",
        "url":"http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "returntype":"META"
    }
    
    postData = urllib.urlencode(data)
    
    req = urllib2.Request(
        headers = headers,
        url = url,
        data = postData
    )
    
    result = opener.open(req)
    
    text = result.read()
    
    rediUrl = getRedirectUrl(text)
    docs = urllib2.urlopen(rediUrl).read()
    rePage = re.compile("feedBackUrlCallBack\((.*?)\)")
    textPage = rePage.search(docs).group(1)
    pageJson = json.loads(textPage)
    id = pageJson['userinfo']['uniqueid']
    userdomain = pageJson['userinfo']['userdomain']
    return id,userdomain
    