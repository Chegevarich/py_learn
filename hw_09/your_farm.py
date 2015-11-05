# coding: utf-8
from farm import Farm

x =0

farm = Farm()

farm.report()

wwcd = {
	'append animal' : farm.append_animal,
	'next' : farm.next_month,
	'report' : farm.report,
}

print('возможные действия')
for i in wwcd:
	print('\t',i)

while True:
	try:
		x = input('введите действие >> ')
	except:
		x = 1

	if x in wwcd:
		if x == 'next':
			try:
				y = int(input('введите количество месяцев для шага >> '))
				wwcd[x](y)
			except:
				print('введён не корректный шаг (количество месяцев) >> ')
			finally:
				print(y, wwcd[x])

		elif x == 'report':
			wwcd[x]()
		elif x ==  'append animal':
			y = input('введите тип животных (например утки, коровы) >> ')

			if y in farm.animals:
				wwcd[x](animal_type = y)
			else:
				try:
					animal_type = y
					main_product = input('введите значение параметра главный продукт производимый животным >> ')
					main_product_coefficent = int(input('введите значение параметра количество производимого главного продукта в месяц >> '))
					main_product_unit = input('введите значение параметра единицы измерения главного продукта >> ')
					speed = int(input('введите значение параметра средняя скорость движения животного >> '))
					travel_time_per_day = int(input('введите значение параметра среднее время движения в день >> '))

					wwcd[x](animal_type = animal_type, main_product = main_product, main_product_coefficent = main_product_coefficent, main_product_unit = main_product_unit, speed = speed, travel_time_per_day = travel_time_per_day)
				except:
					print('введены не корректные данные, животное не будет добавлено')
				#

		else:
			print('действие не определено')

	if x == 'eval':
		eval(input('жги >> '))

	if x == 1:
		break