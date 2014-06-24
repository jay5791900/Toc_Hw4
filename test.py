# -*- coding: utf-8 -*-
import json
import urllib2
import sys


roadinfo = dict()


if __name__ == '__main__':
	inpu = sys.argv
	url = 'http://www.datagarage.io/api/5385b69de7259bb37d925971'
	data = urllib2.urlopen(url) #get url
	j = json.load(data)			#load json file



	for l in j:  # first loop to establish roadname list
		temp = l[u'土地區段位置或建物區門牌']
		if ( temp.find(u'路')!=(-1) or temp.find(u'街')!=(-1) or temp.find(u'大道')!=(-1) or temp.find(u'巷')!=(-1)):
			if ( temp.find(u'路')!=(-1) ):
				key = u'路'
			elif (temp.find(u'街')!=(-1)):
				key = u'街'
			elif (temp.find(u'大道')!=(-1)):
				key = u'大道'
			else:
				key = u'巷'

			if key == u'大道':			
				name = l[u'土地區段位置或建物區門牌'][:temp.find(key)+2] #get
				year = l[u'交易年月']
			else: 
				name = l[u'土地區段位置或建物區門牌'][:temp.find(key)+1] #get
				year = l[u'交易年月']

			if roadinfo.has_key(name) == False:
				roadinfo[name] = []

			if roadinfo[name].count(year) == 0:
				roadinfo[name].append(year)

		else: continue


	print json.dumps(roadinfo,ensure_ascii=False,indent=2)
	
	max1 = 0
	for i in roadinfo:
		c = len(roadinfo[i])
		if c > max1:
			max1 = c


	#t = u'臺北市北投區中央北路'
	#x = u'臺北市中正區汀州路'

	#for l in j:
#		if x in l[u'土地區段位置或建物區門牌']:
#			print l[u'土地區段位置或建物區門牌']
		


