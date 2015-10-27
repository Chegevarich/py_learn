# coding:utf-8
import os, sys


def find(d, t):
	for i in os.listdir(d):
		if (i.endswith(t)):
			for fOrDir, line in enumerate(open(i)):
				pass
				yield fOrDir, line, i

for name, i, s in find('.', '.py'):
	print(name, i, s)