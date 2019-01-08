#coding:UTF-8
print("Start........")
from sys import argv
scriptFileName,args=argv
print("执行python脚本:"+scriptFileName)
argsList=args.split(",")
argsSize=len(argsList)
count=0
for i in argsList:
	for j in argsList:
		for k in argsList:
			if((i!=j)and(j!=k)and(i!=k)):
				print(i+j+k)
				count+=1
print("共能拼接数字："+str(count))
print("End........")