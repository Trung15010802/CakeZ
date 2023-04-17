from django.shortcuts import render, get_object_or_404
from .models import Category, Cake
from django.shortcuts import redirect

import numpy as np

# Create your views here.
def cake_list(request):
    cakes = Cake.objects.all() #.order_by('-id) # dùng để sắp xếp theo id
    cate = Category.objects.all()
    return render(request, 'cakeshop/cake_list.html', {'cakes': cakes, 'cate': cate})

def cakes_list(request):
    cakes = Cake.objects.all().order_by('-id')
    categories = Category.objects.all()
    cart = get_cart(request)
    count = len(cart)   
    return render(request, 'cakeshop/shop.html', {'categories': categories, 'cakes': cakes, 'count': count})

def cake_detail(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    return render(request, 'cakeshop/cake_detail.html', {'cake': cake})

def cate_detail(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    categories = Category.objects.all()
    cakes = Cake.objects.filter(category=pk)
    cart = get_cart
    count = len(cart)   
    return render(request, 'cakeshop/shop.html', {'categories': categories, 'cakes': cakes, 'count': count})


def add_to_cart(request, pk):
    cakes = Cake.objects.all().order_by('-id')
    categories = Category.objects.all()
    
    cart = get_cart(request)
    
    # cart = json.loads(cart_str)

    product_exists = False
    cake = Cake.objects.get(pk=pk)
    for item in cart:
        if item['id'] == pk:         
            item['quantity'] += 1
            item['price'] = float(cake.price) * item['quantity'] 
            product_exists = True
            break
            
    if not product_exists:
        cake = Cake.objects.get(pk=pk)
        new_item = {'id': pk, 'name': cake.name, 'price': float(cake.price), 'quantity': 1}
        cart.append(new_item)
        
    count = len(cart)

    request.session['count'] = count
    # cart_json = json.dumps(cart)
    request.session['cart'] = cart
    total = np.sum([cart['price'] for cart in cart])
    request.session["total"] = total
    context = {'categories': categories, 'cakes': cakes, 'count': count}
    return render(request, 'cakeshop/shop.html', context)

def cart_update(request, pk):
    query = int(request.POST.get('quantity'))
    cart = get_cart(request)
        
    cake = Cake.objects.get(pk=pk)

    for item in cart:
        if item['id'] == pk:         
            item['quantity'] = query
            item['price'] = float(cake.price) * item['quantity'] 
            break
    request.session['cart'] = cart
    total = np.sum([cart['price'] for cart in cart])
    request.session["total"] = total
    return render(request, 'cakeshop/cart.html', {'cart': cart})

def cart_remove(request, pk):
    cart = get_cart(request)
    for i, item in enumerate(cart):
        if item['id'] == pk:
            cart.pop(i)
            break
    request.session['cart'] = cart
    total = np.sum([cart['price'] for cart in cart])
    request.session["total"] = total
    return render(request, 'cakeshop/cart.html', {'cart': cart})
    
def cart_list(request):
    cart = get_cart(request)    
    return render(request, 'cakeshop/cart.html', {'cart': cart})

def search(request):
    query = request.GET.get('query')
    if query:
        cakes = Cake.search(query)
    else:
        cakes = Cake.objects.all()
        
    categories = Category.objects.all()
    cart = get_cart(request)
    count = len(cart) 
    context = {'categories': categories, 'cakes': cakes, 'count': count}
    return render(request, 'cakeshop/shop.html', context)

def delete_session(request):
    cart = get_cart(request)
    print(cart)
    print(type(cart))
    cart = []
    request.session['cart'] = cart
    cakes = Cake.objects.all().order_by('-id')
    categories = Category.objects.all()
    count = len(cart)
    context = {'categories': categories, 'cakes': cakes, 'count': count}
    return render(request, 'cakeshop/shop.html', context)

def get_cart(request):
    cart = request.session.get('cart', '[]')
    
    if not isinstance(cart, list):
        cart = []
        
    return cart