from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'personal/home.html')

def contact(request):
	return render(request,'personal/basic.html',{'content':['If you would like to email me ,please send us', 'kevalrathod1111@gmail.com']})