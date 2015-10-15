# coding:utf-8

what_we_do = 0

file_name = 'sname'
sname_list = []
d=dict()

import os.path

if os.path.isfile(file_name) :
	with open(file_name) as f:
	    for num, i in enumerate(f.readlines()):
	    	sname_list.append(i.strip().split(';'))
	    	d[num] = i.strip().split(';')
	    	print(num, i.strip())
else: 
	print(1)

print(d)


#
def each_el_of_list(l):
	pass
#показать ФИ по индексу
def show_one_by_index(fl):
	x = input('введите индекс элемента : ')
	if x.isnumeric() and len(fl)>int(x):
		print(fl[int(x)])
	else:
		print("введён не иднекс (не число) или индекс вне списка")
		show_one_by_index(fl)
#
def show_comprehensions(fl):
	x = input('введите через точку с запятой (;) требуемый срез: ')
	x = x.split(';')
	for i in range( int(x[0]), int(x[1]) ):
		print(fl[i])

#Находим количество студентов, в именах которых есть буква вводиная пользователем
def show_with_letter_in_name(fl):
	x = input('введите букву искомую в именах: ')
	for f in fl.values():
		if x.lower() in f[1].lower():
			print(f[0],f[1])
#
def group_by_name(fl):
	out = dict()
	for i in fl.keys():
		if out.get(fl[i][1]) == None:
			out[fl[i][1]] = [fl[i]]
		else:
			out[fl[i][1]].append(fl[i])

	print(out)
while True:
	x = input('выберете действие 0-вывод ФИ по индексу, 1-получить срез, 2-ФИ с содержанием в имени какой либо буквы, 3- находим группы студентов с одинаковыми именами и создаем списки этих групп, для выхода нажмите любую кнопку(кроме обозначенных кодов) и ввод')
	if x=='0':
		show_one_by_index(d)
	elif x=='1':
		show_comprehensions(d)
	elif x=='2':
		show_with_letter_in_name(d)
	elif x=='3':
		group_by_name(d)
	else:
		break

#5. Находим группы студентов с одинаковыми именами и создаем списки этих групп.