from django.shortcuts import render

def home(request):
    return render(request, 'hello_world/fujita/home.html')