import os, sys, time

if len(sys.argv) >= 3:

	if sys.argv[1] == 'stop':

		#try: #try to kill

			#проверяем надо ли убивать процесс (есть ли у него статус 1)
			if (open(sys.argv[2]+'.status').read()=='1'):

				while open(sys.argv[2]+'.status').read()=='1':
					#пишем команду на выключение для скрипта 
					f = open(sys.argv[2]+'.die', 'w')
					f.write('1')
					f.close()
					#после отправки команды на убийство пишем в статус процесса 0
					#процесс выключен
					f = open(sys.argv[2]+'.status', 'w')
					f.write('0')
					f.close()


					if (len(sys.argv)==4 and sys.argv[3]=='deepKill'):
						#ждём время выполнения скрипта *2 что бы гарантировать 
						#попадание запущенных скриптов в этап записи своего статуса
						#и определения необходимости убийства данных скриптов
						time.sleep(2)

			else:
				print('данный скрипт не запущен в рамках текущей псевдоэкосистемы')


		#except:
			#print('что то пошло не так')
	else:
		print('не очевидно что может сюда привести')
else:
	# status of all launched
	for i in os.listdir('.'):

		if i.endswith('.status'):
			if open(i).read() == '1':
				module_name = i.split('.')
				module_name = module_name[0]

				print(module_name, 'запущен')