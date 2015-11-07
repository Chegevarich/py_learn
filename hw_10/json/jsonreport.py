import json, sys, os

class FarmReportJson:

	def __init__(self, file_name='FarmReportsJson.json'):
		self.file_name = file_name

	def all_reports(self):
		for i in open(self.file_name):
			yield FarmReportJson.read(str(i).strip())

	def report_by_number(self, num):
		for i, el in enumerate(open(self.file_name)):
			if i == num-1:
				yield self.read(el)		

	@staticmethod
	def read( report ):
		return json.loads(report)

	@staticmethod
	def write( report, dest ):
		f = open(dest, 'a+')
		f.write(json.dumps(report) + "\n")
		f.close()

if __name__ == '__main__':
			
	FarmReportJson.read('[22]')

	jsn = FarmReportJson('1.txt')

	for i in jsn.all_reports():
		print (i[0])
# 
# FarmReportJson.write('22', '1.txt')
# 
# for i in jsn.all_reports():
# 	print (i)