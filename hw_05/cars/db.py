# coding:utf-8
import pickle, os
#обновление объекта (как в памяти - так и в файле)
def renew_pickle(data, file_name):
	f = open(file_name, 'wb')
	pickle.dump(data, f)
	f.close()
	return data

#первичное чтение записи
def read_pickle_object(file_name):
	if not os.path.isfile(file_name):
		f = open(file_name, 'w')
		data = {
		'raw_brands' : [],
		'auto_type' : set()
		}
		f = open(file_name, 'wb')
		pickle.dump(data, f)
		f.close()	
	else:
		 with open(file_name, 'rb') as f:
		 	data = pickle.load(f)
	return data