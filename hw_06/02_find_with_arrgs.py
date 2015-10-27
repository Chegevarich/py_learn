# coding:utf-8
import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', default='.py')
parser.add_argument('-f', '--folder', default='./')
parser.add_argument('-s', '--substr', default='def')

p = parser.parse_args()

def find(d, t):

	for i in os.listdir(d):

		if os.path.isdir(d+'/'+i) == True:
			yield from find(d+i+'/', t)
		else :
			if (i.endswith(t)):
				for fOrDir, line in enumerate(open(d+i)):
					yield d+i, fOrDir, line

def grep(gen, substr):
	for name, i, s in gen:
		if substr in s:
			yield name, i, s

for name, i, s in grep( find(p.folder, p.type) , p.substr):
	print(name, i, s)