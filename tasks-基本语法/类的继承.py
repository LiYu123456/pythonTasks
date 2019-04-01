#coding=UTF-8
class Parent:
	"父类的定义"
	parentAttr=100
	
	def  __init__(self):
		print("这是父类构造函数")
		
	def parentMethod(self):
		print("这是父类方法")
		
	def setAttr(self,attr):
		Parent.parentAttr=attr
	
	def getAttr(self):
		print("父类的属性:",Parent.parentAttr)
		
class Child(Parent):
	"子类的定义"
	def __init__(self):
		print("这是子类构造函数")
		
	def childMethod(self):
		print("这是子类的方法")
		print(Parent.parentAttr)
		Child.sayHello(self);
		
	def sayHello(self):
		print("这是子类sayHello方法")
	
	def __del__(self):
		print("这是析构函数")
		
c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print(c.__class__)
print(c.__class__.__name__)
print(Child.__name__)
print(c.__module__)
print(c.__class__.__bases__)
print(c.__class__.__doc__)
#判断对象是否是某个类的实例
print(isinstance(c,Parent))
#判断两个类是否有继承关系
print(issubclass(Child,Parent))

print("/**************************************************************/")

class Parent:
	"子类方法定义"
	classAttr=100
	def __init__(self):
		pass
		
	def myMethod(self):
		print("这是父类方法")
		
class Child(Parent):
	"父类方法定义"
	classAttr=200
	def myMethod1(self):
		print("这是子类的方法")
		
c=Child()
p=Parent()
c.myMethod()
print(c.classAttr)
p.myMethod()
print(p.classAttr)

print("/*********************运算符重载**************************/")
class Vector:
	def __init__(self,a,b):
		self.a=a;
		self.b=b;
		
	def __add__(self,other):
		return Vector(self.a+other.a,self.b+other.b)
		
	def __str__(self):
		return "Vector(%d,%d)"%(self.a,self.b)
v1=Vector(2,10)
v2=Vector(5,5)
print(v1+v2)

print("/*********************类属性和方法**************************/")
class JustCounter:
	__secretCount=0
	publicCount=1
	_protectedCount=5
	
	def count(self):
		self.__secretCount+=1
		self.publicCount+=1
		
counter=JustCounter()
counter.count()
#print(counter.__secretCount)
print(counter.publicCount)
print(counter._protectedCount)

print(counter._JustCounter__secretCount)
