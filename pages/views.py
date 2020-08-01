from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html', {'title':'Home'})

def blog(request):
    return render(request, 'pages/blog.html', {'title':'Blog'})

def shop(request):
    return render(request, 'pages/shop.html', {'title':'Shop'})

def blog_details(request):
    return render(request, 'pages/blog-details.html', {'title':'Blog Details'})

def checkout(request):
    return render(request, 'pages/checkout.html', {'title':'Checkout'})

def contact(request):
    return render(request, 'pages/contact.html', {'title':'Contact'})

def cart(request):
    return render(request, 'pages/shop-cart.html', {'title':'Cart'})

def product_details(request):
    return render(request, 'pages/product-details.html', {'title':'Product Details'})
    