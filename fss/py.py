#coding:utf-8
import os

nums = 1

x = input("уверен? Y/N")

if x == 'Y':
	for i in os.listdir('.'):
		if os.path.isfile(i) and i !=os.path.basename(__file__):
			os.rename(i, str(nums) + "разделительнапишитут" + i)
			nums +=1