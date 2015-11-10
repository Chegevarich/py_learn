# coding:utf-8
from math import ceil
from random import random
from abstract_animal import SuperAnimal
from abstract_farm import SuperFarm

class Animal(SuperAnimal):
	def __str__(self):
		return(self.about_animal)

	def __repr__(self):
		return(self.about_animal)

	@property
	def about_animal(self):
	    return 'из группы {}, производит {} {} {} в месяц, случайный коэффициент прошлого периода -- {}'.format( self.animal_type, self.main_product, self.main_product_coefficent, self.main_product_unit, self.goods_per_month_coefficent )

	def __init__(self, main_product, main_product_coefficent, main_product_unit, animal_type, speed=0, travel_time_per_day=0):
		#attr by createon
		self.main_product = main_product
		self.main_product_coefficent = main_product_coefficent
		self.main_product_unit = main_product_unit
		self.speed = speed
		self.travel_time_per_day = travel_time_per_day
		self.voice_per_day = 0

		self.animal_type = animal_type

		#temporary results
		self.goods_in_last_month = 0
		self.distance_traveled_in_last_moth = 0
		self.voice_in_last_moth = 0

		#attr for keep result's
		self.distance_traveled = 0
		self.voice_used = 0
		self.goods_ready = 0

		#attr for random coefficent
		self.voice_per_day_coefficent = random()
		self.run_per_day_coefficent = random()
		self.goods_per_month_coefficent = random()
		self.total_moth_in_own = 0

	def make_animal_affairs(self, month=1):
		self.run(month*30)
		self.voice(month*30)
		self.goods(month)
		self.total_moth_in_own +=month

	def run(self, days=1):
		self.distance_traveled_in_last_moth = ceil(self.speed * self.travel_time_per_day * days * self.run_per_day_coefficent)
		self.distance_traveled += self.distance_traveled_in_last_moth

	def voice(self, days=1):
		self.voice_in_last_moth = ceil(days * self.voice_per_day * self.voice_per_day_coefficent)
		self.voice_used += self.voice_in_last_moth

	def goods(self, month, ceil_it=False):

		self.goods_in_last_month = self.main_product_coefficent * month * self.goods_per_month_coefficent
		if ceil_it:
			self.goods_in_last_month = ceil(self.goods_in_last_month)

		self.goods_ready += self.goods_in_last_month



class Duck(Animal):

	#переопределяем инит что бы передать параметры по умолчанию
	def __init__(self, main_product='яйца', main_product_coefficent=10, main_product_unit='штук', speed=3, travel_time_per_day=10, animal_type='утки'):
		super().__init__(main_product, main_product_coefficent, main_product_unit, animal_type, speed, travel_time_per_day)
		self.voice_per_day = 120

	#переопределяем запуск метода для получения целых количеств 
	#произведённых единиц товара (надеюсь утки не делат по половине яйца)
	def goods(self, month):
		super().goods(month, True)

class Dog(Animal):

	#переопределяем инит что бы передать параметры по умолчанию
	def __init__(self, main_product='шерсть', main_product_coefficent=1, main_product_unit='килограмм', speed=20, travel_time_per_day=18, animal_type='собаки'):
		super().__init__(main_product, main_product_coefficent, main_product_unit, animal_type, speed, travel_time_per_day)
		self.voice_per_day = 100

class Cow(Animal):

	#переопределяем инит что бы передать параметры по умолчанию
	def __init__(self, main_product='молоко', main_product_coefficent=100, main_product_unit='литров', speed=5, travel_time_per_day=8, animal_type='коровы'):
		super().__init__(main_product, main_product_coefficent, main_product_unit, animal_type, speed, travel_time_per_day)
		self.voice_per_day = 100


class Farm(SuperFarm):
	last_step = 0

	@property
	def count_of_animal_types(self):
	    return len(self.animals)
	

	def __setattr__(self, name, value):
		if (name == 'animal_types_count'):
			return 'animal_types_count не может быть задан, это расчитываемое значение'
		else:
			super().__setattr__(name, value)

	def __getattr__(self, name):
		if name == 'animal_types_count':
			return len(self.animals) 
		else:
			super().__setattr__(name)


	def duplicate_animal(self, animal_type):
		new_animal = Animal(main_product=self.animals[animal_type][0].main_product, main_product_coefficent=self.animals[animal_type][0].main_product_coefficent, main_product_unit=self.animals[animal_type][0].main_product_unit, animal_type=self.animals[animal_type][0].animal_type, speed=self.animals[animal_type][0].speed, travel_time_per_day=self.animals[animal_type][0].travel_time_per_day)
		return new_animal
		
	def append_animal(self, animal_type='утки', main_product=None, main_product_coefficent=None, main_product_unit=None, speed=None, travel_time_per_day=None):
		if animal_type in ['утки', 'собаки', 'коровы']:
			if animal_type == 'собаки':
				self.dogs.append(Dog())
			elif animal_type == 'коровы':
				self.cows.append(Cow())
			else :
				self.ducks.append(Duck())

		elif animal_type in self.animals:
				self.animals[animal_type].append(self.duplicate_animal(animal_type=animal_type))

		else:
			if (main_product and main_product_coefficent and main_product_unit and speed and travel_time_per_day):
				if animal_type not in self.animals:
					self.animals[animal_type] = []

				self.animals[animal_type].append(Animal(main_product, main_product_coefficent, main_product_unit, speed=0, travel_time_per_day=0, animal_type=animal_type))

	def __init__(self, ducks=0, dogs=0, cows=0 ):

		create_dogs = ceil(random()*10)
		create_cows = ceil(random()*10)
		create_ducks = ceil(random()*10)		

		try:
			x = input('ввести количество животных каждого вида (1) или запустить случайный набор "фермы" (любой другой символ)')
		except:
			x = 0
		finally:
			if x == '1':
				try:
					x = input('введите количество собак на ферме >> ')
					create_dogs = int(x)

					x = input('введите количество уток на ферме >> ')
					create_ducks = int(x)

					x = input('введите количество коров на ферме >> ')
					create_cows = int(x)


				except:
					print("\t\t(!!!) не корректные данные при инициализации - будут созданы случайные количества животных")

			self.dogs = []
			self.cows = []
			self.ducks = []

			self.animals = {
			'собаки' : self.dogs, 
			'коровы' : self.cows,
			'утки' : self.ducks
			}

			print(self.dogs, type(self.dogs))

			for i in (range(create_dogs)):
				self.dogs.append(Dog())

			for i in (range(create_cows)):
				self.cows.append(Cow())

			for i in (range(create_ducks)):
				self.ducks.append(Duck())

	#прошелМесяц
	def next_month(self, month=1, day_in_month=30):
		self.last_step = month

		for animal_type in self.animals.keys():
			for a in self.animals[animal_type]:
				a.make_animal_affairs(month)
		#TODO goods to warehouse

	#своднаяИнформация
	def report(self):
		print('===Начало отчёта===')
		for animal_type in self.animals.keys():

			if len(self.animals[animal_type]) > 0:
				total = 0
				print('==================',animal_type,'==================')

				for i, a in enumerate(self.animals[animal_type]):
					print('=============================================================================')
					print('Животное номер', i+1)
					print ('\tпроизвели ', a.main_product, 'в количестве', a.goods_ready, a.main_product_unit)
					print('\t\tв том числе за последний(е)', self.last_step, 'месяц', a.goods_in_last_month)
					print('\tпробежал', a.distance_traveled, 'км')
					print('\t\tв том числе за последний(е)', self.last_step, 'месяц', a.distance_traveled_in_last_moth)
					print('\tподавал голос', a.voice_used, 'раз(а) за период')
					print('\t\tв том числе за последний(е)', self.last_step, 'месяц', a.voice_in_last_moth)				
					print('=============================================================================')
					total += a.goods_ready

				print('\t', animal_type, 'всего произвели', total, a.main_product_unit, 'продукта', a.main_product, 'за', a.total_moth_in_own, 'месяца на ферме')

		print('===Конец отчёта==\n')

if __name__ == '__main__':

	#объявляем класс фермы
	farm = Farm()

	#выводим репорт с нулевым шагом (0 месяцев прошло)
	farm.report()
#
	#переходим в следующий месяц
	farm.next_month()
	#выводим репорт с первым шагом (1 месяцев прошёл)
	farm.report()

	farm.append_animal(animal_type='овцы', main_product='шерсть', main_product_coefficent=0.4, main_product_unit="кг", speed=2, travel_time_per_day=8)
	farm.append_animal(animal_type='овцы', main_product='шерсть', main_product_coefficent=0.4, main_product_unit="кг", speed=2, travel_time_per_day=8)
#
	farm.next_month()
	#выводим репорт со вторым шагом (2 месяцев прошёл)
	farm.report()	

	#делаем шаг на 5 месяцев
	farm.next_month(5)
	#выводим репорт с шагом +5 месяцев (7 месяцев прошёл)
	farm.report()	

	print(farm.animals['собаки'][0])
'''
№9. 

# 1. добавляем в ферму абстрактный класс - от 1 до 3 +
# 2. переопределяем животным __str__ и __repr__ +
# 3. не забыть делегирование + 

# 4. * __getattr__ и __setattr__ 
# 5. ** property у животных +
'''


'''
Создаем программу-модуль "Жизнь на ферме" с набором классов:+
- Утка +
- Корова +
- Собака +

1. У этих классов есть следующие функциональности (нужные в работе методы нужно придумать):
- бежать +
- голос +
- продукт - молоко (или яйцо...) +
Все эти классы наследованы от базового "Животное". +

2. Также нужен класс Ферма. + 
Программа инициализирует ферму с заданным числом каждого животного. + 

3. Далее запускается метод класса Ферма "прошелМесяц".+
Там циклом проходим по всем животным, запуская их собственный метод "прошелМесяц" (какое животное сколько раз делает продукт, как успешно, +
где использовать random, какие случайные факторы внести в жизнь фермы, решайте сами).+

4. Далее запускается метод класса Ферма "своднаяИнформация", который расскажет нам об изменениях на ферме.+
'''