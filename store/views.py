from django.shortcuts import render
from .models import Category,Product

def cateogory(request):
    return({
        'categories' : Category.objects.all()}
    )

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html',{'products':products})

def product_detail(request,slug):
    product = get_object_or_404(product,slug=slug,in_stock=True)
    return render(request,'store/products/detail.html',{'product':product})




