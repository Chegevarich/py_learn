import time, os, sys

f = open('m002.die', 'w')
f.write('')
f.close()		
a = ''

while a=='':
	time.sleep(1)
	print(2)
	try:
		f = open('m002.status', 'w')
		f.write('1')
		f.close()		
	except:
		a = 1

	try:
		f = open('m002.die')
		a = f.read()
		f.close()
	except:
		a = ''