from django.shortcuts import render

def home(request):
    return render(request, 'hellow_world/sora/home.html')