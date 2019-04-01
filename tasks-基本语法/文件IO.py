# coding:UTF-8
#导入文件处理模块
import os

input_val=input("请输入一个值:")
print(input_val)

fo=open("foo.txt","r+")
print("文件名:",fo.name)
print("是否已关闭",fo.closed)
print("访问模式",fo.mode)

#fo.write( "www.runoob.com!\nVery good site!\n")
a=fo.read(1)
print(a)
#print("末尾是否强制加空格:",fo.softspace)
fo.close()
