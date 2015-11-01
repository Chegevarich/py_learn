# coding:utf-8
class Car:
	def __init__(self, model='T'):
		self.model = model

class F1car(Car):
	pass

class Truck(Car):
	pass



car=Car(); f1car = F1car(); truck = Truck();

#1st
if (dir(Car()) == dir(F1car()) == dir(Truck()) ):
	print('методы и аттрибуты одинаковы')
else:
	print('не одинаковы')

#2nd
carOpt = set( dir(Car()) )
f1carOpt = set( dir(F1car()) )
truckOpt = set( dir(Truck()) ) 

if (carOpt.intersection(f1carOpt) == truckOpt):
	print('методы и аттрибуты одинаковы')
else:
	print('не одинаковы')	

#3rd
carOptList = dir(car)
f1carOptList = dir(f1car)
truckOptList = dir(truck)

for i, e in enumerate(carOptList):
	eq = 1
	if (carOptList[i] == f1carOptList[i] == truckOptList[i]):
		pass
	else:
		eq = 0

if eq == 1:
	print('методы и аттрибуты одинаковы')
else:
	print('не одинаковы')		