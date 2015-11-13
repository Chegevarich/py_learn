# coding:utf-8
# Echo server program
import socket, sys, time



if sys.argv[1] == 'client':
	# coding:utf-8
	# Echo client program
	import socket

	while True:
		try:
			#HOST = '127.0.0.1'    	  # The remote host
			HOST = '192.168.0.100'    # The remote host
			PORT = 50008              # The same port as used by the server

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((HOST, PORT)) 
			s.sendall(b'El\'Barto') #send to server
			data = s.recv(1024) #recive
			s.close()

			print('Received', (data))
			time.sleep(1)
		except:
			print('die')
			x = input('выключить?')
			if x == '1':
				break

if sys.argv[1] == 'server':

	HOST = ''                 # Symbolic name meaning all available interfaces # 0.0.0.0
	PORT = 50007              # Arbitrary non-privileged port

	s = socket.socket(socket.AF_INET, #тип сокета - IPV4->IPV6 и проч
		socket.SOCK_STREAM #тип сокета - в данном случае потоковое общение
			)

	# резервируем хост - порт 
	s.bind( (HOST, PORT) )

	#ждём подключения
	s.listen(1)

	#принимаем соединение и взнаём параметры
	#conn объект соединения
	#addr - адрес и порт
	conn, addr = s.accept()

	print('Connected by', addr)

	while True:
	    data = conn.recv(1024) #читаем порциями по 1024 байт
	    if not data: 
	    	break
	    #отправка данных обратно
	    conn.sendall(data)

	conn.close()