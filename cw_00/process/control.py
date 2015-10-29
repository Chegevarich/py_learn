import os, sys

if len(sys.argv) == 3:

	if sys.argv[1] == 'stop':

		try: #try to kill
			f = open(sys.argv[2]+'.die', 'w')
			f.write('1')
			f.close()
		except:
			print('что то пошло не так')
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