from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=100, default='')
    emailaddress = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.TextField(default='')

    def __str__(self):
        return self.full_name


class Team(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = ResizedImageField(size=[500, 500], crop=['middle', 'center'], quality=100, upload_to='team/image', default='')
    details = RichTextField(blank=True, null=True)
    facebookId = models.CharField(max_length=225, default='', blank=True)
    linkedinId = models.CharField(max_length=225, default='', blank=True)

    def __str__(self):
        return self.name


class Departments(models.Model):
    department_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.department_name

    def get_absolute_url(self):
        return reverse('others:dept_slug', args=[self.slug, ])


class Circular(models.Model):
    JOB_TYPE = (
        ('FULL-TIME', 'FULL-TIME'),
        ('CONTRACTUAL', 'CONTRACTUAL'),
        ('PART-TIME', 'PART-TIME'),
        ('REMOTE', 'REMOTE'),
    )
    job_title = models.CharField(max_length=255)
    job_details = RichTextField(blank=True, null=True)
    job_type = models.CharField(max_length=11, choices=JOB_TYPE, default='FULL-TIME')
    department_name = models.ForeignKey(Departments, on_delete=models.PROTECT)
    salary = models.CharField(max_length=20)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.job_title


class Job_Apply(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    file = models.FileField(upload_to='file')
    job_title = models.ForeignKey(Circular, on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name
