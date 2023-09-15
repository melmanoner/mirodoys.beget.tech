from django import forms
from .models import AdvUser


from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.ModelForm):
    #username = forms.CharField(widget=forms.TextInput(attrs={'class':'user'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput,
                                help_text='Повторите пароль')
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 != password2:
            errors = {'password2': ValidationError(
                'Пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username','phone_number','first_name','last_name' )


class AdvUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password'}))




