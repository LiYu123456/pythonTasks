#! /usr/bin/evn python3
# -*- coding:UTF-8 -*-

class AnimalMetaClass(type):
	print("这是AnimalMetaClass的程序体语句")
	def __new__(cls,*args,**kwargs):
		print("AnimalMetaClass类的__new__方法")
		#print(cls)
		#print(args)
		#print(kwargs)
		return super().__new__(cls,*args,**kwargs)
		
	def __init__(self,*args,**kwargs):
		print("这是AnimalMetaClass的init方法")

class PersonMetaClass(type):
	print("这是PersonMetaClass的程序体语句")
	def __new__(cls,*args,**kwargs):
		print("PersonMetaClass类的__new__方法")
		#print(cls)
		#print(args)
		#print(kwargs)
		return super().__new__(cls,*args,**kwargs)
		
class StudentMetaClass(type):
	print("这是StudentMetaClass的程序体语句")
	def __init__(self,*args,**kwargs):
		print("这是元类StudentMetaClass的init方法")
	def __new__(cls,*args,**kwargs):
		print("StudentMetaClass类的__new__方法")
		#print(cls)
		#print(args)
		#print(kwargs)
		return super().__new__(cls,*args,**kwargs)
		

class Animal(metaclass=AnimalMetaClass):
	print("这是Animal的程序体语句")
	def __new__(cls,*args,**kwargs):
		#print(cls)
		#print(args)
		#print(kwargs)
		print("我是Animal的__new__方法")
		return super().__new__(cls,*args,**kwargs)

	def __init__(self):
		print("我是Animal的__init__方法")
	
class Person(metaclass=PersonMetaClass):
	print("这是Person的程序体语句")
	def __init__(self):
		print("我是Person的__init__方法")
		
	def __new__(cls,*args,**kwargs):
		print("我是Person的__new__方法")
		print(cls.__name__)
		#print(args)
		#print(kwargs)
		return super().__new__(cls,*args,**kwargs)

class Student(metaclass=StudentMetaClass):
	print("这是Student的程序体语句")
	def __init__(self):
		print("我是Student的__init__方法")
		
	
	def __new__(cls,*args,**kwargs):
		print("我是Student的__new__方法")
		print(cls.__name__)
		#print(args)
		#print(kwargs)
		return super().__new__(cls)
	
class SmallStudent(Student):
	print("这是SmallStudent的程序体语句")
	
	def __init__(self,name):
		self.name=name
		print("我是SmallStudent的__init__方法")
		
	
	def __new__(cls,*args,**kwargs):
		print("我是SmallStudent的__new__方法")
		print(cls.__name__)
		#print(args)
		#print(kwargs)
		return super().__new__(cls,args,kwargs)	

	def __call__(self,*args,**kwargs):
		print("这是SmallStudent的call方法")

	
print("==========初始化完毕============")		
s1=SmallStudent("张三")
#s1()
