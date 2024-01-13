from django.shortcuts import render
from my_app.forms import  ContactForm,CheckoutForm,CommentForm
from my_app.models import Product,Comment,Category,Partniors,SpecialOffer,Slider,Basket
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def cart_view(request):
    basket = Basket.objects.all()
   
    context = {
        
        'basket':basket,
      
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
    comments = Comment.objects.filter(products=obj1)
    related_product = Product.objects.filter(category=obj1.category).exclude(id=obj1.id)
    
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            product = form.cleaned_data.get("products")
            form.save()
            form = CommentForm()

    context = {
    'obj1':obj1,
    'comments':comments,
    'form':form,
    'related_product':related_product,

    }
    
    return render(request,'detail.html',context)


def index_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(rating__gte=4)[:8]
    recent_products = Product.objects.order_by('-created_at')[:8]
    partniors = Partniors.objects.all()
    specialoffer = SpecialOffer.objects.all()
    slider = Slider.objects.all()
    
  

    context = {
        'categories':categories,
        'products':products,
        'recent_products':recent_products,
        'partniors':partniors,
        'specialoffer':specialoffer,
        'slider':slider
    }
    return render(request,'index.html',context)



def shop_view(request):
    obj = Product.objects.all()

    search = request.GET.get('search') #search
    if search is not None:
     obj =  obj.filter(name__icontains = search)

    cat = request.GET.get('cat')
    if cat :
     obj = obj.filter(category__name__icontains = cat)

    paginator = Paginator(obj, 1)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    context = {
        'obj':obj,
        'p':p,
        'search':search,
        'cat':cat,
    }
    
    return render(request,'shop.html',context)



