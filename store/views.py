from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category, Customer
from django.views import View
# from django.contrib.auth import authentication, login, logout

class index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        # print(request.session['cart'])


        return redirect('/home/')



    def get(self, request):
        categories = Category.get_all_category()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_product_by_categoryid(categoryID)
        else:
            product = Product.get_all_product()
        data = {}
        data['products'] = product
        data['categories'] = categories
        return render(request, 'index.html', data)


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phoneno = postData.get('phoneno')
        email = postData.get('email')
        password = postData.get('password')
        
        customer = Customer(
            first_name = first_name,
            last_name = last_name,
            phoneno = phoneno,
            email = email,
            password = password,
        )
        customer.register()
        return redirect('/home/')

def Login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.objects.filter(email=email)
        if user is not None:
            request.session['customer_id'] = customer.id
            request.session['customer_email'] = customer.email
            return redirect('home')
