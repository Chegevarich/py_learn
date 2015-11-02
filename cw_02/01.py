# coding:utf-8
class Worker():
	price = 10000

	def make_remont(self):
		return (self.price)

class badWorker(Worker):
	price = 5000


# Prorab
#     badWorker - Worker - Ingeneer ...

class Prorab:

	price = 40000
	workers = []


	def __init__(self, w=5):
		for i in range(w):
			self.workers.append(Worker())

	def make_remont(self):
		total_price = 0
		for i in self.workers:
			total_price += i.make_remont()
			
		print(total_price+self.price)		

p = Prorab(9)
p.workers.append(badWorker())

p.make_remont()