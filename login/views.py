from django.shortcuts import render

# Create your views here.

def loguser(request):
	return render(request,'registrations/login.html')