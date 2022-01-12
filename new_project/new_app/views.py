from django.shortcuts import render

# Create your views here.
def fnLogin(request):
    return render(request,'login.html')