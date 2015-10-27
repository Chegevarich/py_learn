# coding:utf-8
import os, sys

def find(d, t):

	for i in os.listdir(d):
		if os.path.isdir(d+'/'+i) == True:
			for name, i, s in find(d+i+'/', t):
				yield name, i, s
				#TODO or yield from find(d+i+'/', t)
		else :
			if (i.endswith(t)):
				for fOrDir, line in enumerate(open(d+i)):
					yield d+i, fOrDir, line

def grep(gen, substr):
	for name, i, s in gen:
		if substr in s:
			yield name, i, s

try:
	sstr = input('Введите искомую строку >>> ')
except:
	print("Ошибка ввода данных с клавиатуры")

for name, i, s in grep( find('./', '.py') , sstr):
	print(name, i, s)