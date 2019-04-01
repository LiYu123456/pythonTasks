# coding:UTF-8
print("Start.....")
class Employee:
	"员工基类"
	#定义的类变量
	empCount=0
	
	#定义构造函数，self代表类的实例，相当于this指针
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary
		Employee.empCount+=1
	
	#定义一般方法
	def displayCount(self):
		print("Total Employee:"+str(Employee.empCount))
		
	def displayEmployee(self):
		print("Name:"+self.name+" age:"+str(self.age)+"  salary:"+str(self.salary))
	
	def __del__(self):
		className=self.__class__.__name__
		print("销毁",className)

#创建一个Employee对象
employee=Employee("张飞",15,1000)
print(employee.__class__)
employee.displayCount()
employee.displayEmployee()

employee2=Employee("关羽",20,1000)
print(employee2.__class__)
employee2.displayCount()
employee2.displayEmployee()

employee.gender="female"
print(employee.gender)
employee.gender="male"
print(employee.gender)
print(hasattr(employee,"gender"))
del employee.gender
print(hasattr(employee,"gender"))

print("Employee.__doc__   "+Employee.__doc__)
print("Employee.__dict__   ",employee.__dict__)
print("Employee.__name__   "+Employee.__name__)
print("Employee.__module__   ",Employee.__module__)
print("Employee.__bases__  ",Employee.__bases__)
print("End.......")