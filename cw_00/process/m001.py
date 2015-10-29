import time, os, sys

f = open('m001.die', 'w')
f.write('')
f.close()		
a = ''

while a=='':
	time.sleep(1)
	print(1)
	try:
		f = open('m001.status', 'w')
		f.write('1')
		f.close()		
	except:
		a = 1

	try:
		f = open('m001.die')
		a = f.read()
		f.close()
	except:
		a = ''