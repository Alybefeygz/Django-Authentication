from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# CustomUserCreatinForms UserCreationForm'i miras aldığı için normal ir form yapısına ek olarak şifre ve şifre tekrarı gibi özellikler ekler.
class CustomerUserCreationForms(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email','bio','location')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email = email).exists():
            raise forms.ValidationError("This email is already in use.")
        else:
            return email
        
# CustomUserCreatinForms UserCreationForm'i miras almadığı için normal standart bir form yapısına sahiptir.        
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','bio','location')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        #exclude(pk=self.instance.pk) bu kod sayesinde ise kendi email'i dışında kalan emailleri kontrol eder. çünkü kendi e maili hep aynıdır gerksiz hata mesajı yöneltir.
        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        else:
            return email

# Bu form, Django'nun kimlik doğrulama sistemiyle uyumludur ve AuthenticationForm'un temel doğrulama özelliklerini devralır.
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(lable = 'Username', widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput())