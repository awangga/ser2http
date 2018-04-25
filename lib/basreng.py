#!/usr/bin/env python
"""
Basic Regular Expression Engine
basreng.py 
created by Rolly Maulana Awangga

"""
import re
	
	
def dictView(dictv,htmlv):
	rep = dict((re.escape(k), v) for k, v in dictv.iteritems())
	pattern = re.compile("|".join(rep.keys()))
	result = pattern.sub(lambda m: rep[re.escape(m.group(0))], htmlv)
	return result
