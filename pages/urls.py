from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog/', views.blog, name = 'blog'),
    path('shop/', views.shop, name = 'shop'),
    path('blog-details/', views.blog_details, name = 'blog-details'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('contact/', views.contact, name = 'contact'),
    path('product-details/', views.product_details, name = 'product-details'),
    path('cart/', views.cart, name = 'shop-cart'),
]