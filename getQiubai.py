#coding=utf-8

import re
import urllib
import urllib2


def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html


def getImg(html):
	reg = r'src="(.+?\.jpg)" size'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1

html = getHtml("http://tieba.baidu.com/p/5020321663")

print getImg(html)





