import time, os, sys

f = open('002.die', 'w')
f.write('')
f.close()		
a = ''

while a=='':
	time.sleep(1)
	print(0)
	try:
		f = open('002.status', 'w')
		f.write('1')
		f.close()		
	except:
		a = 1

	try:
		f = open('002.die')
		a = f.read()
		f.close()
	except:
		a = ''