import unittest, db, os, sys

class pathes:
	file_name = 'just4test.pickle'
	data = 'test string'


class test_(unittest.TestCase, pathes):
	#before each test_
	def setUp(self):
		pass
		#self.file_name = 'just4test.pickle'
		#self.data = 'test string'		

		#никаких assert'ов в setUp

	#after each test_
	def tearDown(self):
		#подчищаем тестовые файлы
		os.remove(self.file_name)

	def test_save_pickle(self):

		#проверяем не было ли файла до этого
		self.assertFalse(os.path.exists(self.file_name))

		#проверяемый функционал
		db.renew_pickle(self.data, self.file_name)

		#проверяем - был ли создан файл
		self.assertTrue(os.path.exists(self.file_name))


		#проверка целостности 
		self.assertEqual( db.read_pickle_object(self.file_name), self.data)

	def test_save_pickle_try_big_data(self):
		self.data = [a for a in range(30000)]
		self.data += [ 'hello {}'.format(a) for a in range(30000) ]

		db.renew_pickle(self.data, self.file_name)

		self.assertTrue(os.path.exists(self.file_name))

	def test_save_pickle_try_none(self):
		self.data = None

		db.renew_pickle(self.data, self.file_name)

		self.assertTrue(os.path.exists(self.file_name))

	def test_save_pickle_try_empty(self):
		self.data = ''

		db.renew_pickle(self.data, self.file_name)

		self.assertTrue(os.path.exists(self.file_name))



class std_test(unittest.TestCase, pathes):
	#before each test_
	def setUp(self):

		self.out = []


		#self.file_name = 'just4test.pickle'
		#self.data = 'test string'		

		class stdout():
			def write(self, test):
				self.out.append(test)
				pass
			def flush(self):
				pass

		self.tmp_strout = sys.stdout

		sys.stdout = stdout()
		stdout.out = self.out


		#никаких assert'ов в setUp

	#after each test_
	def tearDown(self):
		#подчищаем тестовые файлы
		os.remove(self.file_name)
		sys.stdout = self.tmp_strout

	def test_save_pickle_on_debug(self):
		#self.data = ''

		db.renew_pickle(self.data, self.file_name)

		#print(''.join(self.out))
		#print(self.out)

		self.assertEqual( ''.join(self.out), 'just for test\n')
		#self.assertTrue(os.path.exists(self.file_name))

#renew_pickle

if __name__ == '__main__':
	unittest.main()