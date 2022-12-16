from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import NewComment

# Create your views here.


def products_list(request):

    products_list = Product.objects.all()
    paginator = Paginator(products_list, 4)

    page_number = request.GET.get('page')
    products_list = paginator.get_page(page_number)
    context = {
        'title': 'كل المنتجات',
        'products_list': products_list,
        }
    return render(request, 'product/all_products.html', context)


def product_details(request, slug):
    # product_details = Product.objects.get(prdSlug=slug)
    product_details = get_object_or_404(Product, prdSlug=slug)
    comments = product_details.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product_details
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    context = {
        'title': product_details.prdSlug,
        'product_details': product_details,
        'comments': comments,
        'comment_form': comment_form,
        }
    return render(request, 'product/product_details.html', context)




def home(request):
    
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
    }
    return render(request, 'product/home.html', context)

def about(request):
    context={
        'title': 'من نحن',  
    }
    return render(request, 'product/about.html', context)

