from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from product.models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.save(commit=False)
            username.set_password(form.cleaned_data['password1'])
            #username = form.cleaned_data['username']
            username.save()
            messages.success(
                request, f'تهانينا {username} لقد تم التسجيل بنجاح فضلا قم بتسجيل الدخول')
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {
        'title': 'التسجيل',
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login_user(request):

    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(request, "هناك خطأ في اسم المستخدم أو كلمة المرور!")

    else:
        form = LoginForm()
    context = {
        'title': 'تسجيل الدخول',
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    context = {
        'title':'تسجيل الخروج',
            }
    return render(request, 'accounts/logout.html', context)
def profile(request):
    context = {
        'title': 'الملف الشخصي',
    }
    return render(request, 'accounts/profile.html', context)
