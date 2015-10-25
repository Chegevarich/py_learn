#coding:utf-8



def grep(gen, substr):
	for name, i, s in gen:
		if 1==1:
			yield name, i, s


for name, i, s in grep(find('.py'), 'def'):
	print(name,i,s)