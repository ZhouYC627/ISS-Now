#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib
import urllib2
import xml.etree.ElementTree as ET
#import web
import json

url = 'http://api.open-notify.org/iss-now.json'
response = urllib2.urlopen(url)
html = response.read()

position = json.loads(html)
pdata_lat = position['iss_position']['latitude']
pdata_lon = position['iss_position']['longitude']

# unicode变为string
pdata_lat = str(pdata_lat)
pdata_lon = str(pdata_lon)

pdata_text = "空间站当前坐标为：\n(" + pdata_lat + ", "  + pdata_lon + ")"
print pdata_text
