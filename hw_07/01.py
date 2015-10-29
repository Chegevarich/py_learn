# coding:utf-8
class tank:
	speed = 0
	base = 0
	track = True
	model = ''

	def status(self):

		speed = self.speed
		base = self.base
		track = self.track
		model = self.model

		if (speed > 0 and track == True):
			print( self.model, 'едет')
		elif(track==False):
			print( self.model, 'без гусениц не едет')
		else:
			print( self.model, 'не едет')

class car:
	speed = 0
	model = ''
	wheels = 0

	def status(self):

		speed = self.speed
		model = self.model
		wheels = self.wheels

		if (speed > 0 and wheels >= 4):
			print( self.model, 'едет')
		elif(wheels<=3):
			print( self.model, 'не едет, слишком мало колёс')
		else:
			print( self.model, 'не едет')

class cart:
	speed = 0
	wheels = 0

	def status(self):

		speed = self.speed
		wheels = self.wheels

		if (speed > 0 and wheels >= 4):
			print( 'безымянная телега едет')
		elif(wheels<=3):
			print( 'безымянная телега не едет, слишком мало колёс')
		else:
			print( 'безымянная телега не едет')

dic = {
	'car':[[30, 'модель0', 4],[40, 'модель1', 10], [60, 'модель2', 2], [0, 'модель3', 4]],
	'tank':[[40, 72, True, 't80'], [40, 72, True, 't90'], [40, 72, False, 't80']],
	'cart':[[0,5], [100,3], [10,6]]
}

for i in dic:
	if i=='car':
		for l in dic[i]:

			tmp_class = car()

			tmp_class.speed = l[0]
			tmp_class.model = l[1]
			tmp_class.model = l[2]

			tmp_class.status()
	elif i == 'tank':
		for l in dic[i]:
			tmp_class = tank()

			tmp_class.speed = l[0]
			tmp_class.base = l[1]
			tmp_class.track = l[2]
			tmp_class.model = l[3]

			tmp_class.status()
	else:
		for l in dic[i]:
			tmp_class = cart()

			tmp_class.speed = l[0]
			tmp_class.wheels = l[1]

			tmp_class.status()

