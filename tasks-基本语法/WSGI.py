#! /usr/bin/env python3
# -*- coding:UTF-8 -*-
from wsgiref.simple_server import make_server

#定义一个HTTP处理类
def applicatioin(environ,start_response):
	start_response("200 OK",[("Content-type","text/html")])
	print(environ)
	body="<h1>Hello,%s!</h1>"%(environ["PATH_INFO"][1:] or "web")
	return [body.encode("UTF-8")]

#启动HTTP处理类
httpd=make_server('',8000,applicatioin)
print("Serving HTTP on port 8000")
httpd.serve_forever()
