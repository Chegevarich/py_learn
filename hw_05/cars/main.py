# coding:utf-8
import os
from debug import print_error_message
from db import renew_pickle, read_pickle_object

file_name = 'nondb'
text_template_01 = 'марка - {brand}, мощность - {power}'


#вставить новую запись о новом типе в БД 
def insert_auto_type_into_db(raw_brand):
	global data

	brand = 0
	what = ''
	auto = tuple()

	#если бренд не был передан - запускаем блок заполнения бренда
	if raw_brand == '':
		raw_brand = take_from_input('введите марку : ').strip()

		if raw_brand == 'выход':
			return False

		#если вводимый бренд(марка) состоит только из букв
		if raw_brand.isalpha():

			#если ещё не было подобного бренда - добавляем
			if raw_brand not in data['raw_brands']:
				data['raw_brands'].append(raw_brand)
				#обновляем объект
				data = renew_pickle(data, file_name)
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
		power = take_from_input('введите мощность : ')

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
				data = renew_pickle(data, file_name)
			else:
				print_error_message(6)


def read_from_db(sort_by):
	for i in sorted(data['auto_type'], key=lambda x:data['raw_brands'][x[0]]):
		print(text_template_01.format(brand=data['raw_brands'][i[0]], power=i[1]))

def print_templ_01(brand, power):
	print(text_template_01.format(brand=data['raw_brands'][brand], power=power))	
	
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

#обёртка для input для избежания падения скрипта при ошибке ввода
def take_from_input(mess='введите данные'):
	x = ''
	try:
		x = input(mess)
	except:
		print_error_message(9)
	finally:
		return x

def search_by(s_by):
	if (s_by==''):
		t = take_from_input('Поиск \n\r\tпо мощности - 0 \n\r\tпо марке - 1 \n\r')
	else:
		t = s_by

	#поиск по мощности
	if (t == '0'):
		power = take_from_input('Введите мощность (числом) или диапазон мощностей через тире (например 50-100) : ')

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
		brand = take_from_input('введите марку автомобиля : ')
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

def take_false(void):
	return False

#так как хранилище реализовано через не изменяемый тип данных - set 
#воспринимаем редактирование как удаление и добавление
def edit_auto_type(id):
	delete_auto_type(id)
	insert_auto_type_into_db('')

def delete_auto_type(id):
	data['auto_type'].remove(id)
	data = renew_pickle(data, file_name)

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
	x = take_from_input('введите идентификатор записи для редактирования >>> ')

	if x.isnumeric():
		x = int(x)
		if x > (len(data['auto_type'])-1):
			print_error_message(8)
		else:
			d = take_from_input('введите желаемое действие (редактировать или удалить) >>> ')
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

		
		x = take_from_input('>>> ')
		if x in FUNCS:
			FUNCS[x]('')
		elif x == 'выход':
			return False
		else:
			print_error_message(7)


if __name__ == '__main__':
	#при запуске данного скрипта исключаем возможность краша
	#для разработки следует запускать импортируя main.py
	try:	
		#читаем (в случае отсутствия данных - создаём) pickle объект
		data = read_pickle_object(file_name)

		#запускаем обрабочик ввода команд
		take_command()
	except:
		print_error_message()

'''	
Дз №5. 

Дополняем программу про машины:

# 1. ищем хотя бы 2 места в своей программе, +
где удобно воспользоваться try - except +
(задаем полную конструкцию try-except-else-finaly) +

# 2. обрабатываем исключения, защищаясь от ошибок +

# 3. при этом программу делим на модули:

# папка cars/
# main.py - сама программа. В main.py предусмотреть возможность его импортирования 
# db.py - чтение и запись данных  +
# debug.py - вывод на экран +
'''