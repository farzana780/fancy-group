from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Products, Category

# Create your views here.

def product(request,slug=None):
    cat = None
    product = Products.objects.all()
    category = Category.objects.all()
    paginator = Paginator(product, 4)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    if slug:
        product = Products.objects.all()
        cat = get_object_or_404(category, slug=slug)
        product = product.filter(category=cat)
        paginator = Paginator(product, 1)
        page = request.GET.get('page')
        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)
    return render(request, 'product/product.html', {'product': product, 'category': category,'cat':cat, 'page': page})


def product_details(request, slug):
    product = get_object_or_404(Products, slug=slug)
    allproduct = Products.objects.filter(category=product.category)
    return render(request, 'product/product_details.html', {'product': product, 'allproduct':allproduct})
