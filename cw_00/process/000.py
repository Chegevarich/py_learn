import time, os, sys

#убираем записи о команде выключиться
f = open('000.die', 'w')
f.write('')
f.close()		
a = ''

while a=='':
	time.sleep(1)
	print(0)
	try:
		#пишем свой статус
		f = open('000.status', 'w')
		f.write('1')
		f.close()		
	except:
		a = 1

	try: #проверяем нет ли команды прекратить
		f = open('000.die')
		a = f.read()
		f.close()
	except:
		a = ''