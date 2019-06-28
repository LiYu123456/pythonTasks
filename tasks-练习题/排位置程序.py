#! /usr/bin/evn python3
# -*- coding:UTF-8 -*-

def cal(num):
	return (num//3,num%3)

num=input("请输入要排位的数字：")
print("您输入了：%s"%num)

num=int(num)
row,col=cal(num)

print("位置为：%d行，%d列"%(row,col))