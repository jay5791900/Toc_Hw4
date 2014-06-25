# -*- coding: utf-8 -*- 
#-----------------------
#Name:Guan-Jie Feng
#Id:F74001161
#Description:input url to get road information
#-----------------------
import json
import urllib2
import sys


roadinfo = dict()		#store road information
roadprice = dict()		#soore road price


def findresult(info):	#func to find max and min price , print the result
	max_price = 0
	min_price = 10000000000000000000000
	for item in roadprice:
		if item == info:
			for p in roadprice[info]:
				if p > max_price:
					max_price = p
				if p < min_price:
					min_price = p
	print u"%s, 最高成交價:%d, 最低成交價:%d" % (info,max_price,min_price)

if __name__ == '__main__':
	inpu = sys.argv				#input argv
	url = inpu[1]				#get url
	data = urllib2.urlopen(url) #get parse json file
	j = json.load(data)			#load json file



	for l in j:  				# for loop to establish roadinfo list
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
				name = l[u'土地區段位置或建物區門牌'][:temp.find(key)+2] #get name
				year = l[u'交易年月']
				price = l[u'總價元']

			else: 
				name = l[u'土地區段位置或建物區門牌'][:temp.find(key)+1] 
				year = l[u'交易年月']
				price = l[u'總價元']

			if roadinfo.has_key(name) == False:		#check if roadname exist
				roadinfo[name] = []

			if roadinfo[name].count(year) == 0:		#check if year  exist
				roadinfo[name].append(year)

			if roadprice.has_key(name) == False:	#check if roadname exist
				roadprice[name] = []

			if roadprice[name].count(price) == 0:	#check if price exist
				roadprice[name].append(price)
								
		else: continue


	#print json.dumps(roadinfo,ensure_ascii=False,indent=2)

	max_road = 0				#find the most trade of roadname
	for i in roadinfo:
		c = len(roadinfo[i])
		if c > max_road:
			max_road = c

	#print max_road
	for road in roadinfo:
		if len(roadinfo[road]) == max_road:
			findresult(road)	#find max and min price , print the result
