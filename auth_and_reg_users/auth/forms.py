

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.fullname = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user