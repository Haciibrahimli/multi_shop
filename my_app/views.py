from django.shortcuts import render


def cart_view(request):
   
    context = {
      
    }

    return render(request,'cart.html',context)


def checkout_view(request):

    context = {
        
    }
    return render(request,'checkout.html',context)



def contact_view(request):

    context = {
        
    }
    return render(request,'contact.html',context)



def detail_view(request):

    context = {
        
    }
    return render(request,'detail.html',context)


def index_view(request):

    context = {
        
    }
    return render(request,'index.html',context)



def shop_view(request):

    context = {
        
    }
    return render(request,'shop.html',context)

