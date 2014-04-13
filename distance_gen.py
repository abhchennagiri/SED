import xml.dom.minidom as dom
import sys
import json
import os
import config
import datetime
from scipy.spatial.distance import cosine

xml = dom.parse(sys.argv[1])
os.chdir(config.res)
soccer100= open("soccer100.txt","r").readlines()[0].split(",")
tech100=open("tech100.txt","r").readlines()[0].split(",")
indi100=open("indi100.txt","r").readlines()[0].split(",")

soccer1000= open("soccer1000.txt","r").readlines()[0].split(",")
tech1000=open("tech1000.txt","r").readlines()[0].split(",")
indi1000=open("indi1000.txt","r").readlines()[0].split(",")

data_signal=[]
features = json.load("features.json")

for feature1 in features["signal"].iterkeys():
	for feature2 in features["signal"].iterkeys():
		time1 = datetime.datetime.strptime(features[feature1][0], "%Y-%m-%d %H:%M:%S.%f")
		time2 = datetime.datetime.strptime(features[feature2][0], "%Y-%m-%d %H:%M:%S.%f")
		time = abs((time1-time2).total_seconds())
		location = None
		tags_dist = None
		sift = consine(features[feature1][5],features[feature2][5])
		is_same_class = 1 if features[feature1][4] == features[feature2][4] else 0
		data_signal.append(([time,location,tags_dist,sift],is_same_class))