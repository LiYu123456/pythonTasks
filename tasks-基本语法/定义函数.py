#coding=UTF-8
#函数定义
def sum(num1,num2):
	"定义一个一般函数"
	return num1+num2
result=sum(1,2)
print("result=",result)

def printInfo(name,age):
	"定义一个函数，演示按顺序传入参数和按参数名传入参数"
	print("name:",name)
	print("age:",age)
#按照参数顺序传参，次序不能乱
printInfo("张飞",12)
#按照参数名传参，顺序可以乱
printInfo(age=12,name="关羽")

#定义默认值参数，如果在调用时不传参，则使用默认值
def printInfo2(name,age=18):
	"定义一个默认值函数"
	print("name",name)
	print("age",age)
	
printInfo2("刘备")
printInfo2("刘备",28)
#可变参数定义，可以传入多个参数,
#1.一个函数只有一个可变参，且必须在最后
#2.可变参会被包装成一个元组
def  printInfo3(age,name,*gender):
	"定义一个可变参函数"
	print("age",age);
	for v in name:
		print(v)
	for k  in  gender:
		print(k)

printInfo3(12,"张飞","刘备","关羽","female","male")

#定义一个匿名函数
sum=lambda arg1,arg2:arg1+arg2;
print(sum(1,2));