# coding:utf-8
import pickle
import os

file_name = 'nondb'
text_template_01 = 'марка - {brand}, мощность - {power}'

if not os.path.isfile(file_name):
	f = open(file_name, 'w')
	data = {
	'raw_brands' : [],
	'auto' : set()
	}
	f = open(file_name, 'wb')
	pickle.dump(data, f)
	f.close()	
else:
	 with open(file_name, 'rb') as f:
	 	data = pickle.load(f)

def insert_into_db(raw_brand):
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
				renew_pickle()
				insert_into_db(raw_brand)
			#если бренд подобный уже был - перезапускаем функцию с заполненным брендом
			else:
				insert_into_db(raw_brand)

		else : 
			#исключение - перезапуск функции
			print('марка должна содержать только буквы')
			insert_into_db('')
	else :
	#brand есть - идём дальше 
		brand = data['raw_brands'].index(raw_brand)
		#получаем мощность
		power = input('введите мощность : ')

		#если ввели не цифры - выходим - перезапускаем
		if not power.isnumeric:
			print('введены не цифр')
			insert_into_db(raw_brand)		
		else:
			#если новообразованный сет имеет разницу с текущим - добавляем его
			if not data['auto'] or not data['auto'].intersection( { tuple([brand, int(power)], ) } ):
			#if not data['auto'] or data['auto'].difference( { tuple([brand, int(power)], ) } ):
				print('добавляем')
				data['auto'].add( tuple( [brand, int(power)]) )
				renew_pickle()
			else:
				print('такой вариант уже существует')


def read_from_db(sort_by):
	for i in sorted(data['auto'], key=lambda x:data['raw_brands'][x[0]]):
		print(text_template_01.format(brand=data['raw_brands'][i[0]], power=i[1]))

def print_templ_01(brand, power):
	print(text_template_01.format(brand=data['raw_brands'][brand], power=power))	
	
#обновление объекта (как в памяти - так и в файле)
def renew_pickle():
	global data
	f = open(file_name, 'wb')
	pickle.dump(data, f)
	f.close()

def search_by(s_by):
	if (s_by==''):
		t = input('Поиск \n\r\tпо мощности - 0 \n\r\tпо марке - 1 \n\r')
	else:
		t = s_by

	if (t == '0'):
		power = input('Введите мощность (числом) или диапазон мощностей через тире (например 50-100) : ')

		if power.isnumeric():
			for i in data['auto']:
				if str(i[1]) == power:
					print_templ_01(i[0], i[1])

		elif ';' in power:
			ps = power.split(';')
			if ps[0].isnumeric() and ps[1].isnumeric():
				for i in data['auto']:
					if int(ps[0]) <= int(i[1]) <= int(ps[1]):
						print_templ_01(i[0], i[1])
			else:
				print('введен не корректный диапазон')
				search_by('0')
	elif (t == '1'):
		pass
		brand = input('введите марку автомобиля : ')
		if brand.isalpha():
			for i in data['auto']:
				if data['raw_brands'][i[0]]==brand:
					print_templ_01(i[0], i[1])
		else:
			print("введена не буквенная марка автомобиля - требуется ввести марку состоящую из букв")
			search_by('1')
	else:
		print ("выбран не существующий режим, введите корректный режим")
		search_by('')

while True:
	#print(data)
	x = input('Что делать?\n\tдобавить новую запись - 1\n\tпрочитать все - 2\n\tпоиск - 3\n\tвыход - 0\n')
	if x == '1':
		insert_into_db('')
	elif x=='2':
		read_from_db('')
	elif x=='3':
		search_by('')
	elif x=='0' or x=='exit' or x=='выход':
		break

# 1. Сделайте простую базу данных: +
# 
# Пользователь вводит команду: ввести, вывести +
# - Ввести - пользователь вводит марку автомобиля и его мощность. +
# Необходимо проверить, что марка состоит только из букв латинского или русского алфавитов. +
# Мощность только из цифр. +
# 
# - Вывести - выводятся все автомобили - по алфавиту. +
# Сортировку сделать сначала стандартным методом. +
# Затем написать свою версию сортировки циклами. 
# 
# 2. Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.
# 
# - По мощности - конкретное число, больше, меньше, в промежутке.
# - По вхождению слова в название.
# - По полному соответствию слова.