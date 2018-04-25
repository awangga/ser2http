#!/usr/bin/env python
"""
Session Block arangements Key
seblak.py 
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
myredis = redis.Redis()	
		

def setTTL(token):
	return myredis.setex(token,"valid",config.urltimeout)

def getTTL(token):
	return myredis.get(token)
