from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Username",
        "class":"w-full py-4 px-6 rounded-xl bg-white"
    }))

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Password",
        "class":"w-full py-4 px-6 rounded-xl bg-white"
    }))

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))
    
    mobile = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Mobile No.",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))

    mobile1 = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Alternate Mobile No.",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }), required=False)

    noofpeople = forms.IntegerField(widget=forms.NumberInput(attrs={
        "placeholder": "Number of People",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))

    oldorinf = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Old or Inf.",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))

    address = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Address",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Re-enter Password",
        "class": "w-full py-4 px-6 rounded-xl bg-white"
    }))

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = UserProfile(
                user=user,
                mobile=self.cleaned_data['mobile'],
                mobile1=self.cleaned_data['mobile1'],
                noofpeople=self.cleaned_data['noofpeople'],
                oldorinf=self.cleaned_data['oldorinf'],
                address=self.cleaned_data['address']
            )
            profile.save()
        return user
