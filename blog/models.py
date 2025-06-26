from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null= True)
    blog_image = models.ImageField(upload_to='blognew/image', default='')
    time = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    slug = models.SlugField(null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '  |  ' + str(self.author)

    def snippet(self):
        return self.body[:30]

    def get_absolute_url(self):
        return reverse('blog:blogdetails', kwargs={'slug': self.slug})





