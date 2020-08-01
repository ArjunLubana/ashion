from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html')

def blog(request):
    return render(request, 'pages/blog.html')

def shop(request):
    return render(request, 'pages/shop.html')