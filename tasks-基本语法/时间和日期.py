# coding:UTF-8
print("Start....")
import time
import calendar

print("得到1970年1月1日到现在的秒数：")
t=time.time()
print("时间戳为:",t)

print("得到时间元组:")
localtime=time.localtime(time.time())
print("本地时间为:",localtime)

print("得到格式化日期:")
t=time.asctime(time.localtime(time.time()))
print(t)
t1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(t1)

print("将格式化日期变为时间戳:")
a="2019-01-16 14:14:01"
b=time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
print(b)

cal=calendar.month(2016,1)
print("2016年1月的日历",cal)
print("End......")