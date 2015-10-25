# coding:utf-8
import os, sys


def find(d, t):

	for i in os.listdir(d):

		if os.path.isdir(d+'/'+i) == True:
			print('\t\t\t\t'+d+i+'/', t)

			for name, i, s in find(d+i+'/', t):
				yield name, i, s
				#TODO why so?
		else :
			if (i.endswith(t)):
				print('\t\t'+i)
				for fOrDir, line in enumerate(open(d+i)):
					yield d+i, fOrDir, line
					pass

def grep(gen, substr):
	for name, i, s in gen:
		if substr in s:
			yield name, i, s


#for name, i, s in find('./', '.py'):
#	print(name, i, s)

try:
	sstr = input('Введите искомую строку >>> ')
except:
	print("Ошибка ввода данных с клавиатуры")


for name, i, s in grep( find('./', '.py') , sstr):
	print(name, i, s)