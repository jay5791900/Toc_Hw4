# -*- coding: utf-8 -*-
import json
import urllib2
import sys


roadname = {}
roadid ={}

if __name__ == '__main__':
	inpu = sys.argv
	url = 'http://www.datagarage.io/api/538447a07122e8a77dfe2d86'
	data = urllib2.urlopen(url) #get url
	j = json.load(data)			#load json file


#or temp.find(u'巷')!=(-1)

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
			else: 
				name = l[u'土地區段位置或建物區門牌'][:temp.find(key)+1] #get
			
			#print name

			roadname[name] = 0


		else: continue

	for l in j: # second loop to conut road number
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
			else: 
				name = l[u'土地區段位置或建物區門牌'][:temp.find(key)+1] #get
			
			#print name

			for k in roadname:
				if k == name:
					roadname[k] = roadname[k] + 1
				else: continue					
			#print name		

		else: continue	

	max1 = 0
	for i in roadname:
		if roadname[i] >= max1:
			 	max1 = roadname[i]
		else: continue

	#for k in roadname:
	#	if roadname[k] == max1:
			#print k

	t = u'臺北市北投區中央北路'
	x = u'臺北市中正區汀州路'

	for l in j:
		if x in l[u'土地區段位置或建物區門牌']:
			print l[u'土地區段位置或建物區門牌']
		
				
