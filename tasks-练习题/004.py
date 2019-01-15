# coding:utf-8
print("Start.....")
from sys import argv
argList=argv[1].split("-")
print(argList)
year=int(argList[0])
month=int(argList[1])
day=int(argList[2])
months = (0,31,59,90,120,151,181,212,243,273,304,334)
result=months[month-1]+day
#判断时否是闰年
if ((year%400==0) or (year%4==0 and year % 100 !=0)) and (month>2):
	result+=1
print(result)
print("End......")