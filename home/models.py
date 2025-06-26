from django.db import models
from product.models import Category
from django_resized import ResizedImageField

# Create your models here.

class upcoming_Product(models.Model):
    product_title = models.CharField(max_length=50)
    product_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = ResizedImageField(size=[500, 320], crop=['middle', 'center'], quality=100, upload_to='upcoming_Product/image', default='')

    def __str__(self):
        return self.product_title

    def get_absolute_url(self):
        return reversed('home:home')


class Best_Values(models.Model):
    img = models.ImageField(upload_to='best_values/image', help_text='small size=370x200 & big size=1170x370 recommended*')
    is_big = models.BooleanField(default = False)


class Gallery(models.Model):
    gallery_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pv/image', null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.gallery_title

