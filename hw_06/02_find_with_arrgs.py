# coding:utf-8
import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', default='.py')
parser.add_argument('-f', '--folder', default='./')
parser.add_argument('-s', '--substr', default='def')
parser.add_argument('-r', '--recursive', action='store_const', const=True)
parser.add_argument('-pd', '--printDecore', action='store_true', default=False)

p = parser.parse_args()

def decorator(func):
	def decorated(f, t, r, s):
		if p.printDecore:
			return func(f, t, r, s, True)
		else:
			return func(f, t, r, s)

	return decorated

def find(d, t, r):

	for i in os.listdir(d):

		if os.path.isdir(d+'/'+i) == True and r == True:
			yield from find(d+i+'/', t, r)
		else :
			if (i.endswith(t)):
				for fOrDir, line in enumerate(open(d+i)):
					yield d+i, fOrDir, line

def grep(gen, substr):
	for name, i, s in gen:
		if substr in s:
			yield name, i, s

@decorator
def grefind(f, t, r, s, decorate=False):
	for name, i, s in grep( find(f, t, r) , s):
		if decorate == False:
			print(name, i, s)
		else:
			print('\t', 'Имя файла >>> ', name, '\n\t\t', 'Номер строки >>> ', i, '\n\t\t', 'Вхождение >>> ', s)

grefind(p.folder, p.type, p.recursive, p.substr)