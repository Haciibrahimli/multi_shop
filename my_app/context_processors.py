from my_app.models import Product,Category

def data_sender(request):
    products_ = Product.objects.all()
    categorys_ = Category.objects.all()
    return {"products_": products_,"categorys_":categorys_,}
    