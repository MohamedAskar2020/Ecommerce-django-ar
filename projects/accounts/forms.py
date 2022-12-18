from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label="اسم المستخدم")
    email = forms.EmailField(label="البريد الالكتروني")
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label="الاسم الأخير")
    password1 = forms.CharField(label="كلمة المرور",widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label="تأكيد كلمة المرور",widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def cleaned_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("كلمة المرور غير متطابقة!")
        return cd['password2']
    
    def cleaned_user(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError("اسم المستخدم موجود مسبقا")
        return cd['username']
    
class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label="اسم المستخدم")
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = User
        fields = ('username', 'password')
        
class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label="اسم المستخدم")
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label="الاسم الأخير")
    email = forms.EmailField(label="البريد الالكتروني")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')