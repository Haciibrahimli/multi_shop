from my_app.models import Product,Category,SignUp
from my_app.forms import SignUpForm

def data_sender(request):
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            form.save()
            form = SignUpForm()

    products_ = Product.objects.all()
    categorys_ = Category.objects.all()
    
    return {"products_": products_,"categorys_":categorys_,"form":form}
    
