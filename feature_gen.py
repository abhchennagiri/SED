import xml.dom.minidom as dom
import sys
import json
import os
import config
import cv2
import numpy as np
from scipy.cluster.vq import *

#from scipy.spatial.distance import cosine
data = {"signal":{},"test":{}}

xml = dom.parse(sys.argv[1])
os.chdir(config.res)
soccer100= open("soccer100.txt","r").readlines()[0].split(",")
tech100= open("tech100.txt","r").readlines()[0].split(",")
indi100= open("indi100.txt","r").readlines()[0].split(",")

soccer1000= open("soccer1000.txt","r").readlines()[0].split(",")
tech1000= open("tech1000.txt","r").readlines()[0].split(",")
indi1000= open("indi1000.txt","r").readlines()[0].split(",")

photos = xml.getElementsByTagName("photo")
for photo in photos:
	title = photo.getAttributeNode("id").nodeValue
	if title in soccer100+soccer1000:
		_class=1
	elif title in tech100+tech1000:
		_class=2
	elif title in indi100+indi1000:
		_class=3
	else:
		continue
	time = photo.getAttributeNode("dateTaken").nodeValue
	try:
		location = photo.getElementsByTagName("location")[0]
		lattitude = location.getAttributeNode("lattitude").nodeValue
		longitude = location.getAttributeNode("longitude").nodeValue

	except:
		lattitude = -1
		longitude = -1
	try:
		tags = [ tag.firstChild.data for tag in photo.getElementsByTagName("tag") ]
	except:
		continue

	if title in soccer100+tech100+indi100:
		data["signal"][title] = [time,lattitude,longitude,tags,_class]
	else:
		data["test"][title] = [time,lattitude,longitude,tags,_class]

json.dump(data,file("features.json","w"))
