#encoding:utf-8
#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	#上下文
	content = {}
	content['content'] = 'Hello World'
	#return HttpResponse("Hello world ! ")
	return render(request,'hello.html',content)