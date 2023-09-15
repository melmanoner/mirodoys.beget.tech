from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models import Sum

# Create your models here.

#-----------------------------------------------------------------------------------------------------------------------
#          Создаю собственную модель юзера, производную от стандартной абстрактной модели AbstractUser.
#-----------------------------------------------------------------------------------------------------------------------

class AdvUser(AbstractUser):
    chat_id = models.CharField(max_length=9,null=True, blank=True, verbose_name='Чат ID телеграмма', help_text='Чтобы узнать свой chat_id, найдите @getmyid_bot в поиске телеграмма')
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'

    class Meta(AbstractUser.Meta):
        pass

