# coding:utf-8
import pickle
import os

file_name = 'nondb'

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
	#print(data)

	tmp_set = set()

	brand = 0
	what = ''
	auto = tuple()

	if raw_brand == '':
		raw_brand = input('введите марку : ')

		if raw_brand == 'выход':
			return False

		if raw_brand.isalpha():
			if raw_brand not in data['raw_brands']:
				data['raw_brands'].append(raw_brand)
				renew_pickle()
				insert_into_db(raw_brand)
		else : 
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
			
			#создаём временный сет для использования методов сета
			tmp_set.add(tuple( [brand, int(power)]))
			#если новообразованный сет имеет разницу с текущим - добавляем его
			if data['auto'].difference( tmp_set ):
				print('добавляем')
				data['auto'].add( tuple( [brand, int(power)]) )
				renew_pickle()
			else:
				print('такой вариант уже существует')


def read_from_db(sort_by):
	#x = input('')
	text = 'марка - {brand}, мощность - {power}'

	for i in sorted(data['auto'], key=lambda x:data['raw_brands'][x[0]]):
		print(text.format(brand=data['raw_brands'][i[0]], power=i[1]))


def renew_pickle():
	global data
	f = open(file_name, 'w')
	f = open(file_name, 'wb')
	pickle.dump(data, f)
	f.close()

while True:
	#print(data)
	x = input('Что делать?\n\tдобавить новую запись - 1\n\tпрочитать все - 2\n\tвыход - 0\n')
	if x == '1':
		insert_into_db('')
	elif x=='2':
		read_from_db('')
	elif x=='0':
		break
	else:
		break

# 1. Сделайте простую базу данных: +
# 
# Пользователь вводит команду: ввести, вывести +
# - Ввести - пользователь вводит марку автомобиля и его мощность. +
# Необходимо проверить, что марка состоит только из букв латинского или русского алфавитов. +
# Мощность только из цифр. +
# 
# - Вывести - выводятся все автомобили - по алфавиту. 
# Сортировку сделать сначала стандартным методом. +
# Затем написать свою версию сортировки циклами.
# 
# 2. Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.
# 
# - По мощности - конкретное число, больше, меньше, в промежутке.
# - По вхождению слова в название.
# - По полному соответствию слова.