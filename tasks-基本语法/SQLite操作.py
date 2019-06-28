#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

#导入SQLite模块
import sqlite3

#链接数据库文件，如果该文件不存在自动在当前目录创建
conn=sqlite3.connect("test.db")

cursor=conn.cursor()

#创建表
cursor.execute("create  table  user  (id varchar(20) primary key,name varchar(20),age int)")
#插入数据
cursor.execute("insert into user(id,name,age)values('1','Michael',10)")

print("插入数据条数：%s"%cursor.rowcount)

cursor.execute("select * from user where id=?",('1',))
values=cursor.fetchall()
print("查询的数据是：",values)
#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭链接
conn.close()

