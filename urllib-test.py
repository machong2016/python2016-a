#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2

url = 'http://www.itdiffer.com/register.py'

values = {'name' : 'qiwsir', 'location' : 'China','language' : 'Python' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)

the_page = response.read()