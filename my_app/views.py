from django.shortcuts import render
from my_app.forms import  ContactForm,CheckoutForm
from my_app.models import Product


def cart_view(request):
   
    context = {
      
    }

    return render(request,'cart.html',context)


def checkout_view(request):

    form = CheckoutForm()
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            form.save()
            form = CheckoutForm()

    context = {
        'form':form
    }
    return render(request,'checkout.html',context)




def contact_view(request):
   
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            form.save()
            form = ContactForm()

    context ={
      'form':form,
      
      
    }
    return render(request,'contact.html',context)



def detail_view(request,slug):

    obj1 = Product.objects.get(slug=slug)

    context = {
    'obj1':obj1
    }
    
    return render(request,'detail.html',context)


def index_view(request):

    context = {
        
    }
    return render(request,'index.html',context)



def shop_view(request):
    obj = Product.objects.all()

    context = {
        'obj':obj
        
    }
    return render(request,'shop.html',context)

