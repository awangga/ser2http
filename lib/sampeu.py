#!/usr/bin/env python
"""
Settings and Modules of Peuyeum
sampeu.py 
created by Rolly Maulana Awangga

"""
import config
import urllib
import os

keyuri = config.keyuri
tokenuri = config.tokenuri
viewspath="./apps/views/"
templatepath="./apps/templates/"

def generateView(route):
	return os.system('python '+templatepath+route+'.py') # if int 0 its executed
	
def getHtmlBegin():
	with open(viewspath+'begin.batik', 'r') as myfile:
	    data=myfile.read().replace('\n', '')
	return data

def getHtmlEnd():
	with open(viewspath+'end.batik', 'r') as myfile:
	    data=myfile.read().replace('\n', '')
	return data

def getHtml(route):
	with open(viewspath+route+'/index.batik', 'r') as myfile:
	    data=myfile.read().replace('\n', '')
	return data
	
def getHtmlForm():
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

def getWMTS():
	return config.WMTS

def emailAcl(email):
	if email.split('@')[1] == config.domainacl:
		return True
	else:
		return False

def tokenValidation(token):
	html = getTokenData(token)
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

