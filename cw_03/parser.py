# coding:utf-8
import xml.etree.ElementTree as ET 

three = ET.parse(open('lentaru.rss'))
root = three.getroot()

for child in root[0]:
	if child.tag == 'item':
		for el in child:
			if el.tag == 'title':
				print(el.text)