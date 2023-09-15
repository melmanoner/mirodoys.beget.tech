from django import forms
from .models import Applications





class ApplicationsForm(forms.Form):
    model = Applications
    exclude = ['counted_eq']

#-------------------------------------------------------------------------------------------------------
#               Создадим форму для создания новой заявки
#-------------------------------------------------------------------------------------------------------

class NewAppForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ('city', 'address','customer','customer_phone',
                  'description','master', 'treaty','monetary','published','deadline','status')
        widgets = {'published' : forms.HiddenInput, 'deadline' : forms.HiddenInput,
                   'status' : forms.HiddenInput,
                   'city' : forms.TextInput(attrs={'class':'create-form'}),
                   'address' : forms.TextInput(attrs={'class':'create-form'}),
                   'customer' : forms.TextInput(attrs={'class':'create-form'}),
                   'customer_phone' : forms.TextInput(attrs={'class':'create-form'}),
                   'description' : forms.TextInput(attrs={'class':'create-form'})}

#-------------------------------------------------------------------------------------------------------
#               Создадим форму для редактирования модели
#-------------------------------------------------------------------------------------------------------

class ChangeAppForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ('treaty','ykp7','ykp12','rf','tm','md','door_closer',
                  'img_door_closer','monetary', 'price', 'premium','change')


#-------------------------------------------------------------------------------------------------------
#               Создадим форму для регистрации пользователей
#-------------------------------------------------------------------------------------------------------

#class RegisterUserForm(forms.ModelForm):
