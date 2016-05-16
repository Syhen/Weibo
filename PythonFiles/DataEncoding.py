# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:32:31 2016

@author: Shen
"""

import urllib2
import rsa
import binascii
import base64
    
def get_userName(userName):
    userNameTemp = urllib2.quote(userName)
    su = base64.encodestring(userNameTemp)[:-1]
    return su

def get_pwd(password, servertime, nonce, pubkey):
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
    passwd = rsa.encrypt(message, key) #加密
    passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
    return passwd