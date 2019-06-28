#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from types import MethodType

class Student(object):
	
	@property
	def birth(self):
		return self._birth
		
	@birth.setter
	def birth(self,value):
		self._birth=value
		
	@property
	def gender(self):
		return "男"

def get_age(self):
	print("年龄是：%s"%self.age)

def set_age(self,age):
	self.age=age

def set_score(self,score):
	self.score=score
	
stu1=Student()
stu1.name="张三"
stu1.age=12
stu1.set_age=MethodType(set_age,stu1)
stu1.get_age=MethodType(get_age,stu1)
stu2=Student()

print(stu1.name)
print(stu1.age)
#print(stu2.name)
stu1.set_age(23)
stu1.get_age()

Student.set_score=set_score

stu1.set_score(100)
stu2.set_score(200)

print(stu1.score)
print(stu2.score)


stu1.birth=400
print("xxxxxx=",stu1.birth)
print(stu1.gender)

