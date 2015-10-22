# coding:utf-8
import pickle
import os

file_name = 'nondb'
text_template_01 = 'марка - {brand}, мощность - {power}'

#первичное чтение записи
def read_pickle_object():
	global data

	if not os.path.isfile(file_name):
		f = open(file_name, 'w')
		data = {
		'raw_brands' : [],
		'auto_type' : set()
		}
		f = open(file_name, 'wb')
		pickle.dump(data, f)
		f.close()	
	else:
		 with open(file_name, 'rb') as f:
		 	data = pickle.load(f)


#вставить новую запись о новом типе в БД 
def insert_auto_type_into_db(raw_brand):
	global data

	brand = 0
	what = ''
	auto = tuple()

	#если бренд не был передан - запускаем блок заполнения бренда
	if raw_brand == '':
		raw_brand = input('введите марку : ').strip()

		if raw_brand == 'выход':
			return False

		#если вводимый бренд(марка) состоит только из букв
		if raw_brand.isalpha():

			#если ещё не было подобного бренда - добавляем
			if raw_brand not in data['raw_brands']:
				data['raw_brands'].append(raw_brand)
				#обновляем объект
				renew_pickle()
				insert_auto_type_into_db(raw_brand)
			#если бренд подобный уже был - перезапускаем функцию с заполненным брендом
			else:
				insert_auto_type_into_db(raw_brand)

		else : 
			#исключение - перезапуск функции
			print_error_message(3)
			insert_auto_type_into_db('')
	else :
	#brand есть - идём дальше 
		brand = data['raw_brands'].index(raw_brand)
		#получаем мощность
		power = input('введите мощность : ')

		#если ввели не цифры - выходим - перезапускаем
		if not power.isnumeric:
			print_error_message(5)
			insert_auto_type_into_db(raw_brand)		
		else:
			#если новообразованный сет имеет разницу с текущим - добавляем его
			if not data['auto_type'] or not data['auto_type'].intersection( { tuple([brand, int(power)], ) } ):
			#if not data['auto_type'] or data['auto_type'].difference( { tuple([brand, int(power)], ) } ):
				print('новый авто добавлен')
				data['auto_type'].add( tuple( [brand, int(power)]) )
				renew_pickle()
			else:
				print_error_message(6)


def read_from_db(sort_by):
	for i in sorted(data['auto_type'], key=lambda x:data['raw_brands'][x[0]]):
		print(text_template_01.format(brand=data['raw_brands'][i[0]], power=i[1]))

def print_templ_01(brand, power):
	print(text_template_01.format(brand=data['raw_brands'][brand], power=power))	
	
#обновление объекта (как в памяти - так и в файле)
def renew_pickle():
	global data
	f = open(file_name, 'wb')
	pickle.dump(data, f)
	f.close()

def search_by_power(power):
	for i in data['auto_type']:
		if str(i[1]) == power:
			print_templ_01(i[0], i[1])

def search_by_section_of_power(from_power, to_power):
	#если указано в не верном порядке - меняем местами переменные
	if from_power>to_power:
		from_power, to_power = to_power, from_power

	for i in data['auto_type']:
		if from_power <= int(i[1]) <= to_power:
			print_templ_01(i[0], i[1])

def search_by_name(brand):
	for i in data['auto_type']:
		if data['raw_brands'][i[0]]==brand:
			print_templ_01(i[0], i[1])


def search_by(s_by):
	if (s_by==''):
		t = input('Поиск \n\r\tпо мощности - 0 \n\r\tпо марке - 1 \n\r')
	else:
		t = s_by

	#поиск по мощности
	if (t == '0'):
		power = input('Введите мощность (числом) или диапазон мощностей через тире (например 50-100) : ')

		if power.isnumeric():
			search_by_power(power)

		elif ';' in power:
			ps = power.split(';')
			if ps[0].isnumeric() and ps[1].isnumeric():
				search_by_section_of_power(int(ps[0]),int(ps[1]))
			else:
				print_error_message(4)
				search_by('0')

	#поиск по марке
	elif (t == '1'):
		brand = input('введите марку автомобиля : ')
		if brand.isalpha():
			search_by_name(brand)
		else:
			print_error_message(1)
			search_by('1')
	else:
		print_error_message(2)
		search_by('')

def take_auto_by_num():
	pass

def insert_auto_into_db():
	pass


def print_error_message(type_of_error=0):
	error_list = ["произошла ошибка не прошедшая типизацию (всё не очень хорошо)",
		"введена не буквенная марка автомобиля - требуется ввести марку состоящую из букв",
		"выбран не существующий режим, введите корректный режим",
		"марка должна содержать только буквы",
		"введен не корректный диапазон",
		"введены не цифр",
		"такой вариант уже существует",
		"команда не распознана",
		"идентификатор вне диапазона"
	]
	print('\n\t!!!(Ошибка)',error_list[type_of_error],'\n')

def take_false(void):
	return False

#так как хранилище реализовано через не изменяемый тип данных - set 
#воспринимаем редактирование как удаление и добавление
def edit_auto_type(id):
	delete_auto_type(id)
	insert_auto_type_into_db('')

def delete_auto_type(id):
	data['auto_type'].remove(id)
	renew_pickle()

#фукнция выбора действия с записью
def edit_auto_type_controller(void):
	tmp_list = []
	do = {
		'редактировать' : edit_auto_type,
		'удалить' : delete_auto_type
	}

	for key, val in enumerate((data['auto_type'])):
		print(key, data['raw_brands'][val[0]], val[1])
		tmp_list.append(val)
	x = input('введите идентификатор записи для редактирования >>> ')

	if x.isnumeric():
		x = int(x)
		if x > (len(data['auto_type'])-1):
			print_error_message(8)
		else:
			d = input('введите желаемое действие (редактировать или удалить) >>> ')
			if d in do:
				do[d](tmp_list[x])
			else:
				print_error_message(7)


def take_command():
	FUNCS = {
	'ввести' : insert_auto_type_into_db,
	'вывести' : read_from_db,
	'поиск' : search_by,
	'редактировать' : edit_auto_type_controller
	}

	while True:
		#трассировочный вывод данных
		print(data)

		print('Возможные действия')
		#выводим ключи из массива возможных функций
		for i in FUNCS:
			print('\t', i)

		try:
			x = input('>>> ')
			if x in FUNCS:
				FUNCS[x]('')
			elif x == 'выход':
				return False
			else:
				print_error_message(7)
		except:
			print_error_message()

#читаем (в случае отсутствия данных - создаём) pickle объект
read_pickle_object()

#запускаем обрабочик ввода команд
take_command()


'''	
ДЗ №4. Функции
Стараемся как можно меньше создавать и использовать глобавльные переменные. Кому удастся обойтись без них вообще?

1. Берем задачу из дз №3. +
Выделяем следующие процессы в функции: +
- ввод команды - отдельная функция +
- сообщение в случае ошибки ввода команды - отдельная функция +
- Ввести и Вывести - 2 отдельные функции +
- поиски по условию - 3 отдельные функции соответственно +
- сохранение в pickle и загрузка из pickle - 2 отдельные функции +

2. Улучшаем: +
функции Ввести и Вывести добавляем в словарь следующим образом: +
FUNCS = {
'ввести': input_func,
'вывести': output_func,
}
И меняем if-else на поиск в этом словаре и запуск функции по ключу словаря. +

3. Добавляем в программу логику +
"Редактировать" для изменения уже введенных данных, +
а также "Удалить". +
Как с помощью функций сократить программный код в этом случае? +

* 4. А теперь вводим в программу логистику. 
У каждого автомобиля из предыдущей задачи теперь есть номерной знак
 ('o007py' например) и 
 координаты - x и y на плоскости относительно автобазы.

пользователь теперь может также выбрать 
автомобиль по номерному знаку и
 переместить его в другие координаты.

* 5. При этом поставить 2 автомобиля в одинаковые координаты система не позволяет.

* 6. При движении считаем общий пробег автомобиля и сохраняем.

** 7. Стараемся сделать так, чтобы все состояло из функций, и каждая функция была как можно короче (хорошо в районе 3 строк кода).
'''