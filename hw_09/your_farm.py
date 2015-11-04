# coding: utf-8
import farm

x=0

farm = farm.Farm()

farm.report()

wwcd = {
	'append animal' : farm.append,
	'next' : farm.next_month,
	'report' : farm.report,
}

while True:
	try:
		x = input('введите действие')
	except:
		x = 1

	if x in wwcd:
		pass
	else:
		print('действие не определено')



	if x == 1:
		break