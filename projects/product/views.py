from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'product/home.html')

def about(request):
    context={
        'title': 'من نحن',
        
    }
    return render(request, 'product/about.html', context)