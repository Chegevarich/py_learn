# coding:utf-8
import xml.etree.ElementTree as ET 

three = ET.parse(open('lentaru.rss'))
root = three.getroot()

for i in root.iter('item'): #итерируем все элементы item, в том числе и вложеные 
	i.set('old', 'yes') # каждому item добавляем атрибут old с значением yes

	for el in i.findall('title'): #поиск по текущему уровню
			#print(el.text)
			b = ET.SubElement(el, 'b'); #добавляем элемент b 
			b.text = 'some text'

#for i in root.iter('description'):
	#root.remove(i) #???

et = ET.ElementTree(root)

et.write('out.rss')

#TODO encoding of RSS