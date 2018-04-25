#!/usr/bin/env python
"""
Cryptography URI Locator Key
cilok.py 
created by Rolly Maulana Awangga

"""
import config
import pymongo
import urllib
import random
import time
import redis
from Crypto.Cipher import AES

keyuri = config.keyuri
tokenuri = config.tokenuri
	
	
def rndm(ln):
               ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
               chars=[]
               for i in range(ln):
                       chars.append(random.choice(ALPHABET))
               return "".join(chars)

def urlEncode16(uri):
	ln = len(uri)
	multihex = (ln/16)*16+16
	sp = multihex - ln - len(str(ln))
	if ln>9:
		dt = str(ln)+uri+rndm(sp)
	else:
		dt = "0"+str(ln)+uri+rndm(sp-1)
	return encodeData16(dt)

def urlDecode16(uri):
	if len(uri)%16 == 0:
		dt = decodeData16(uri)
		try:
			int(dt[:2])
			ln = int(dt[:2])
			ret = dt[2:2+ln]
		except ValueError:
			ret = dt
	else:
		ret = uri
	return ret		

def setTTL(token):
	myredis = redis.Redis()
	return myredis.setex(token,"valid",config.urltimeout)

def getTTL(token):
	myredis = redis.Redis()
	return myredis.get(token)

def encodeData(msg):
	obj=AES.new(self.key,AES.MODE_CFB,self.iv)
	cp = obj.encrypt(msg)
	return cp.encode("hex")

def decodeData(msg):
	obj=AES.new(self.key,AES.MODE_CFB,self.iv)
	dec = msg.decode("hex")
	return obj.decrypt(dec)

def encodeData16(msg):
	obj=AES.new(config.key,AES.MODE_CBC,config.iv)
	cp = obj.encrypt(msg)
	return cp.encode("hex")

def decodeData16(msg):
	obj=AES.new(config.key,AES.MODE_CBC,config.iv)
	dec = msg.decode("hex")
	return obj.decrypt(dec)

def getHtmlBegin():
	with open(self.viewspath+'begin.batik', 'r') as myfile:
	    data=myfile.read().replace('\n', '')
	return data

def getHtmlEnd():
	with open(self.viewspath+'end.batik', 'r') as myfile:
	    data=myfile.read().replace('\n', '')
	return data

def getHtml(route):
	with open(self.viewspath+route+'/index.batik', 'r') as myfile:
	    data=myfile.read().replace('\n', '')
	return data
	
def getHtmlForm(self):
	return config.html_form

def getMenu(uri):
	if uri == config.keyuri:
		opsi = "key"
	elif uri == config.tokenuri:
		opsi = "token"
	else:
		opsi = "other"
	return opsi

def getTokenData(token):
	url = config.tokenurl+token
	response = urllib.urlopen(url)
	html = response.read()
	return html

def emailAcl(email):
	if email.split('@')[1] == config.domainacl:
		return True
	else:
		return False

def tokenValidation(token):
	html = self.getTokenData(token)
	if (html.find(config.aud)>0) and (html.find(config.iss)>0):
		ret = "valid"
	else:
		ret = "invalid"
	return ret

def getJsonData(name,json):
	lookup = '"%s": "'%name
	b = json.find(lookup)
	c = json[b:].find(':')
	c+=1
	b = b+c
	c = json[b:].find(',')
	c = b+c
	data = json[b:c].strip().strip('"')
	return data

