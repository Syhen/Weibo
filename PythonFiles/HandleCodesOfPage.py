# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:19:49 2016

@author: Shen
"""

from bs4 import BeautifulSoup
#import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def crawlFirstDataToLog(htmlContent,page,files):
    bb = True
    try:
        ss = htmlContent.split("FM.view")
        maintext = ''
        for s in ss:
            if(len(s) > len(maintext)):
                maintext = s
        maintext = maintext[1:-19]
        mainjson = json.loads(maintext)
        text = mainjson['html']
        soup = BeautifulSoup(text,'lxml')
        mainStr = soup.find_all('div',class_='WB_feed WB_feed_v3')
        soupStr = str(mainStr[0])
    except Exception as e:
        soup = BeautifulSoup(htmlContent).find_all('script')[-2]
        ss = str(soup).split("FM.view")
        maintext = ss[1]
        maintext = maintext[1:-10]
        mainjson = json.loads(maintext)
        text = mainjson['html']
        soup = BeautifulSoup(text,'lxml')
        mainStr = soup.find_all('div',class_='WB_feed WB_feed_v3')
        soupStr = str(mainStr[0])
    
    if(len(mainStr) == 2):
        soupStr = str(mainStr[1])
    #开始解析
    ms = soupStr
    soup2 = BeautifulSoup(ms,'lxml', fromEncoding='utf8')
    RsAllNot = soup2.find_all('div',class_='WB_cardwrap WB_feed_type S_bg2 ')
    if RsAllNot == None:
        bb = False
    if bb:
        for ran in RsAllNot:
            b = False
            rsText = str(ran.find('div',class_='WB_text W_f14'))
            rsFrom = ran.find_all('div',class_='WB_from S_txt2')
            rsA = rsFrom[0].find_all('a',class_='S_txt2')
            timetext = rsA[0].string.strip()#本人转发或发送的时间
            try:
                fromtext = rsA[1].string.strip()#本人转发或发送的来源
            except Exception as e:
                fromtext = '无'
            trantext = rsText[rsText.find('>')+1:-7]
            textTrans = trantext.strip().replace('\n','').replace('\t','')#本人转发的评论或发送的正文
        #    tranText = ''#本人微博转发次数
        #    tranPingText = ''#本人微博评论次数
        #    tranZanText = ''#本人微博被赞次数
            yNameText = ''#转发的博主名
            yMainText = ''#转发的正文
            yTimeText = ''#转发的那条微博发送的时间
            yFromText = ''#转发的那条微博发送的来源
        #    yTranText = ''#该微博被转发次数
        #    yTranPingText = ''#该微博评论条数
        #    yTranZanText = ''#该微博被赞次数
            
            rsEmpty = ran.find('div',class_='WB_empty')
            if rsEmpty == None:
                b = True
            else:
                yMainText = '原文已删'
            if b:
                rsName = ran.find('a',class_='W_fb S_txt1')
                if rsName != None:
                    try:
                        yNameText = rsName.string.strip()
                    except Exception as e:
                        yNameText = 'Special Words'
                    rsMain = str(ran.find('div',class_='WB_feed_expand').find('div',class_='WB_text'))
    #                yMainText = modifyText(rsMain[rsMain.find('>')+1:-7]).strip().replace('\n','')
                    yMainText = rsMain[rsMain.find('>')+1:-7].strip().replace('\n','').replace('\t','')
    #                yMainText = ''
                    rsATran = ran.find('div',class_='WB_feed_expand').find('div',class_='WB_from S_txt2').find_all('a',class_='S_txt2')
                    yTimeText = rsATran[0].string.strip()
                    try:
                        yFromText = rsATran[1].string.strip()
                    except Exception as e:
                        yFromText = '无'
            line = timetext + '\t' + fromtext + '\t' +textTrans + '\t' + yNameText + '\t' + yMainText + '\t' + yTimeText + '\t' + yFromText + '\n'
            files.writelines(line)
#    print timetext,fromtext,textTrans

#        print text,"NOT"
#        print "#"*20

def crawlOtherDataToLog(secondContent,page,files):
    
    bb = True
    secondjson = json.loads(secondContent)
    soupStr = secondjson['data']
    ms = soupStr
    soup = BeautifulSoup(ms, fromEncoding='utf8')
    
    RsAllNot = soup.find_all('div',{'class':'WB_cardwrap WB_feed_type S_bg2 '})
    if RsAllNot == None:
        bb = False
#    RsAllYes = soup.find_all('div',{'class':'WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover'})
    if bb:
        for ran in RsAllNot:
            b = False
            rsText = str(ran.find('div',class_='WB_text W_f14'))
            rsFrom = ran.find_all('div',class_='WB_from S_txt2')
            rsA = rsFrom[0].find_all('a',class_='S_txt2')
            timetext = rsA[0].string.strip()#本人转发或发送的时间
            try:
                fromtext = rsA[1].string.strip()#本人转发或发送的来源
            except Exception as e:
                fromtext = '无'
            trantext = rsText[rsText.find('>')+1:-7]
            textTrans = trantext.strip().replace('\n','').replace('\t','')#本人转发的评论或发送的正文
        #    tranText = ''#本人微博转发次数
        #    tranPingText = ''#本人微博评论次数
        #    tranZanText = ''#本人微博被赞次数
            yNameText = ''#转发的博主名
            yMainText = ''#转发的正文
            yTimeText = ''#转发的那条微博发送的时间
            yFromText = ''#转发的那条微博发送的来源
        #    yTranText = ''#该微博被转发次数
        #    yTranPingText = ''#该微博评论条数
        #    yTranZanText = ''#该微博被赞次数
            
            rsEmpty = ran.find('div',class_='WB_empty')
            if rsEmpty == None:
                b = True
            else:
                yMainText = '原文已删'
            if b:
                rsName = ran.find('a',class_='W_fb S_txt1')
                if rsName != None:
                    try:
                        yNameText = rsName.string.strip()
                    except Exception as e:
                        yNameText = 'Special Words'
                    rsMain = str(ran.find('div',class_='WB_feed_expand').find('div',class_='WB_text'))
                    yMainText = rsMain[rsMain.find('>')+1:-7].strip().replace('\n','').replace('\t','')
                    rsATran = ran.find('div',class_='WB_feed_expand').find('div',class_='WB_from S_txt2').find_all('a',class_='S_txt2')
                    yTimeText = rsATran[0].string.strip()
                    try:                
                        yFromText = rsATran[1].string.strip()
                    except Exception as e:
                        yFromText = '无'
            line = timetext + '\t' + fromtext + '\t' +textTrans + '\t' + yNameText + '\t' + yMainText + '\t' + yTimeText + '\t' + yFromText + '\n'
            files.writelines(line)
    #        print text,"NOT"
#        print "#"*20