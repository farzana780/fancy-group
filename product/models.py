from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/image')
    slug = models.SlugField()

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('product:cat_slug', args=[self.slug, ])


class Products(models.Model):
    PRODUCT_STATUS = (
        ('AVAILABLE', 'AVAILABLE'),
        ('UNAVAILABLE', 'UNAVAILABLE'),
        ('COMING_SOON', 'COMING_SOON'),
    )
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    product_status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default='AVAILABLE')
    product_summery = models.TextField(default='product')
    Product_details = RichTextField(blank=True, null= True)
    price = models.IntegerField(default=0)
    image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], quality=100,upload_to='product/image', default='')
    post_date = models.DateTimeField(default=timezone.now)
    slug = models.CharField(max_length=255, unique=True, default='abc')


    def __str__(self):
        return self.product_name





