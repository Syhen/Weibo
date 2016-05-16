# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:05:26 2016

@author: Shen
"""

import urllib2
import HandleCodesOfPage
import os

class getMessages:
    def __init__(self,id):
        self.id = id
    
    def setPath(self,path):
        self.path = self.JudgePath(path)
    
    def JudgePath(self,path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    
    def getWeiboContent(self,page):
        files = open(self.path+'/'+str(page)+'.txt','w')
        myurl = 'http://weibo.com/p/'+str(self.id)+'/home?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page='+str(page)+'#feedtop'
        htmlContent = urllib2.urlopen(myurl).read()
        HandleCodesOfPage.crawlFirstDataToLog(htmlContent,page,files)
        
        urlSecond = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page='+str(page)+'&pagebar=0&id='+str(self.id)+'&script_uri=/p/'+str(self.id)+'/home&feed_type=0&pre_page='+str(page)
        secondContent = urllib2.urlopen(urlSecond).read()
        HandleCodesOfPage.crawlOtherDataToLog(secondContent,page,files)
        
        urlThird = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page='+str(page)+'&pagebar=1&id='+str(self.id)+'&script_uri=/p/'+str(self.id)+'/home&feed_type=0&pre_page='+str(page)
        thirdContent = urllib2.urlopen(urlThird).read()
        HandleCodesOfPage.crawlOtherDataToLog(thirdContent,page,files)
        files.close()
        