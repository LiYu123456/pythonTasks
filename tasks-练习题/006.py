# -*- coding:UTF-8  -*-
print("Start......")
def fib(n):
	a,b=1,1
	for i in range(n-1):
		a,b=b,a+b
	return a
	
print(fib(10))
print("End....")