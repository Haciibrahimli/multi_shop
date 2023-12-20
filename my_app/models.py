from django.db import models
from services.mixin import DateMixin,SlugMixin  
from services.generator import Generator 
from services.uploader import Uploader


# Create your models here.
class Category(SlugMixin,DateMixin):
    name = models.CharField(max_length = 255,verbose_name = 'adi')

    def __str__(self):
        return self.name

    class Meta:
     ordering = ('-created_at',)
     verbose_name = 'category'
     verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Category)
        super(Category, self).save(*args, **kwargs)





class Color(DateMixin,SlugMixin):
      name = models.TextField(verbose_name = 'mehsulun rengi')

      def __str__(self):
        return self.name

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'reng'
       verbose_name_plural = 'rengler'

      def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Color)
        super(Color, self).save(*args, **kwargs)

class Size(DateMixin,SlugMixin):
      name = models.TextField(verbose_name = 'mehsulun olcusu')

      def __str__(self):
        return self.name

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'olcu'
       verbose_name_plural = 'olculer'

      def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Size)
        super(Size, self).save(*args, **kwargs)


class Product(SlugMixin,DateMixin):
     category = models.ForeignKey(Category,on_delete = models.SET_NULL,null = True,blank = True)
     name = models.CharField(max_length = 255,verbose_name = 'mehsulun adi')
     price = models.FloatField(verbose_name ='mehsulun qiymeti')
     description_L = models.TextField(verbose_name = 'kicik movzu')
     description_B = models.TextField(verbose_name = 'boyuk movzu')
     rating = models.FloatField(verbose_name = 'reyting')
     information = models.TextField(verbose_name = 'mehsul haqqinda')
     color = models.ManyToManyField(Color,null=True,blank=True)
     size = models.ManyToManyField(Size,null=True,blank=True)
     is_seen = models.BooleanField(default = False)

     def __str__(self):
        return self.name

     class Meta:
       ordering = ('-created_at',)
       verbose_name = 'mehsul'
       verbose_name_plural = 'mehsullar'

     def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Product)
        super(Product, self).save(*args, **kwargs)

    # partniors model yalniz image fild 
    # contact modeli form ve istifadeci yalniz 20 den az yaza bilr subject
    # chekout modeli
    # base.html
        
class Partniors(SlugMixin,DateMixin):
      image = models.ImageField(upload_to=Uploader.upload_photo_partniors,null=True,blank=True)
      
      def __str__(self):
        return self.image

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'partnior sekil'
       verbose_name_plural = 'partnior sekiller'

class Contact(SlugMixin,DateMixin):
       
    name = models.CharField(max_length=255,verbose_name='ad ve soyad')
    email = models.CharField(max_length=255,verbose_name='email adress')
    subject = models.CharField(max_length=255,verbose_name='movzu')
    mesage = models.TextField(verbose_name='mesaj')
    
    

    def __str__(self):
        return self.name
    
    class Meta:

     ordering = ('name',)
     verbose_name = 'contact'
     verbose_name_plural = 'contactlar'

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=20, model_=Contact)
        super(Contact, self).save(*args, **kwargs)   

