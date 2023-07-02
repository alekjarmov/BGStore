from typing import Any

from django import forms
from django.contrib.auth.forms import UserCreationForm, ValidationError
from django.contrib.auth.models import User
from django.forms.utils import ErrorList


class RedErrorList(ErrorList):
    def __str__(self) -> str:
        return self.as_red()

    def as_red(self) -> str:
        if not self:
            return ""
        return f'<ul class="errorlist text-danger">{"".join([f"<li>{e}</li>" for e in self])}</ul>'

    def as_divs(self) -> str:
        if not self:
            return ""
        return self.as_red()

    def as_ul(self):
        if not self:
            return ""
        return self.as_red()

    def as_p(self):
        if not self:
            return ""
        return self.as_red()

    def as_text(self):
        if not self:
            return ""
        return self.as_red()



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def __init__(self, *args, **kwargs):

        super(SignUpForm, self).__init__(*args, **kwargs)
        self.error_class = RedErrorList
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists", code="email_exists")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists", code="username_exists")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match", code="password_mismatch")
        return password2

    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password2")

        cleaned_data["username"] = username
        cleaned_data["email"] = email
        cleaned_data["password"] = password
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'password', )

