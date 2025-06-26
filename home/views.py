from django.core.paginator import Paginator
from django.shortcuts import render
from .models import upcoming_Product, Best_Values,Gallery
from product.models import Category, Products
from blog.models import Post

# Create your views here.

def home(request):
    upcoming_product = upcoming_Product.objects.all()
    category = Category.objects.all()
    bestproduct= Best_Values.objects.order_by('is_big')
    blog = Post.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'home/index.html', {'coming_pr': upcoming_product,
                                              'category': category,
                                              'bestvalue': bestproduct,
                                              'blog': blog,
                                              'gallery': gallery})



def gallery(request):
    gallery = Gallery.objects.all()
    paginator = Paginator(gallery, 4)
    page = request.GET.get('page')
    gallery = paginator.get_page(page)
    return render(request, 'home/video_&_image.html', {'gallery':gallery})


def search(request):
    query = request.GET['search']
    productName = Products.objects.filter(product_name__icontains=query)
    productdetails = Products.objects.filter(Product_details__icontains=query)
    allPost = productName.union(productdetails)
    total = {'allPost': allPost, 'query': query}
    return render(request,'home/search.html', total)


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')


def term_conditions(request):
    return render(request, 'home/term_conditions.html')