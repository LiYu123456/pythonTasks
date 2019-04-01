#coding=UTF-8
#一个异常
try：
	fh=open("testfile","w");
	fh.write("这是一个测试文件，用于测试异常！！")
except IOError:
	print("Error:没有找到文件或读取文件失败")
else:
	print("内容写入文件成功")
	fh.close()
#如果没有发生异常

#不带异常，可以捕捉任何异常，但是不能区分异常类型
try：
	fh=open("testfile","w");
	fh.write("这是一个测试文件，用于测试异常！！")
except:
	print("Error:没有找到文件或读取文件失败")
else:
	print("内容写入文件成功")
	fh.close()

#一次设定多个异常类型，一个except可以捕捉多种类型的异常
try：
	fh=open("testfile","w");
	fh.write("这是一个测试文件，用于测试异常！！")
except IOError,LookupError:
	print("Error:没有找到文件或读取文件失败")
else:
	print("内容写入文件成功")
	fh.close()
	
#finally语句
try：
	fh=open("testfile","w");
	fh.write("这是一个测试文件，用于测试异常！！")
except IOError,LookupError:
	print("Error:没有找到文件或读取文件失败")
else:
	print("内容写入文件成功")
	fh.close()
finally:
	print("finally无论是否发生异常都会执行的代码段")

#使用异常参数
try：
	fh=open("testfile","w");
	fh.write("这是一个测试文件，用于测试异常！！")
except IOError,LookupError,Argument:
	#这个Argument对象，是一个元组，包含了错误字符串，错误数字，错误位置信息
	print("Error:没有找到文件或读取文件失败")
else:
	print("内容写入文件成功")
	fh.close()
finally:
	print("finally无论是否发生异常都会执行的代码段")

#触发异常
raise  ExceptionName("ExceptionMsg",level)

#自定义异常类
class  NetworkError(RuntimeError):
	def  __init__(self,arg):
		self.args=arg
		
try:
	raise NetworkError("Bad hostname")
except NetworkError,e:
	print(e);
else:
	print("else部分")
finally:
	print("finally部分")