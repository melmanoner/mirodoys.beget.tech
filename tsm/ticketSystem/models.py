from datetime import datetime, timedelta
from django.db import models
from login.models import AdvUser
from phonenumber_field.modelfields import PhoneNumberField
from .utilities import get_timestamp_path
from django.db.models import Sum
from django.db.models import F

# Create your models here.

class Applications(models.Model):

    deadlines = datetime.now() + timedelta(days=3)

    STATUS_CHOICE = (
        ('a', 'В работе'),
        ('b', 'Нужна сварка'),
        ('c', 'Выполнена')
    )

    master = models.ForeignKey(AdvUser, on_delete=models.DO_NOTHING, verbose_name='Мастер')
    city = models.CharField(max_length=30,db_index=True, verbose_name='Город')
    address = models.CharField(max_length=50, db_index=True, verbose_name='Адрес')
    customer = models.CharField(max_length=50,db_index=True, null=True, blank=True, verbose_name='Клиент')
    customer_phone = PhoneNumberField(null=True,db_index=True, blank=True, verbose_name='Телефон клиента')
    description = models.TextField(db_index=True,verbose_name='Описание проблемы')
    treaty = models.BooleanField(default=False, verbose_name='Отметить, если нужен договор')
    ykp7 = models.IntegerField(null=True, blank=True, default=0, verbose_name='УКП-7')
    ykp12 = models.IntegerField(null=True, blank=True, default=0, verbose_name='УКП-12')
    rf = models.IntegerField(null=True, blank=True, default=0, verbose_name='RF')
    tm = models.IntegerField(null=True, blank=True, default=0, verbose_name='TM')
    md = models.IntegerField(null=True, blank=True, default=0, verbose_name='MD')
    door_closer = models.IntegerField(null=True, blank=True, default=0, verbose_name='Доводчик')
    counted_eq  = models.BooleanField(default=False, verbose_name='Инструменты склада рассчитаны?')
    img_door_closer = models.ImageField(default='no_image.jpg',verbose_name='Фото доводчика',
                                        upload_to=get_timestamp_path, null=True, blank=True)
    monetary = models.BooleanField(default=False, verbose_name='Денежная заявка')
    price = models.IntegerField(null=True, blank=True, default=0, verbose_name='Цена')
    premium = models.IntegerField(null=True, blank=True, default=0, verbose_name='Премия')
    change = models.IntegerField(null=True, blank=True, default=0, verbose_name='Сдать')
    published = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Дата подачи заявки')
    deadline = models.DateTimeField(default=deadlines)
    closing_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='a', verbose_name='Статус заявки')
    handed_over = models.BooleanField(default=False,db_index=True, verbose_name='Деньги посчитаны')

    def __str__(self):
        return f'{self.id} - {self.master} - {self.address}'

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'
        ordering = ['-published']


class Balance(models.Model):
    holder = models.ForeignKey(AdvUser, on_delete=models.DO_NOTHING, verbose_name='Владелец')
    price = models.IntegerField(null=True, blank=True, default=0, verbose_name='Баланс')
    premium = models.IntegerField(null=True, blank=True, default=0, verbose_name='Премия')
    change = models.IntegerField(null=True, blank=True, default=0, verbose_name='Сдать')

    # -----------------------------------------------------------------------------------------------------------------------
    #         Подсчёт всех денежных полей в модели заявок и присваивание полученных данных модели юзера.
    # -----------------------------------------------------------------------------------------------------------------------

    def save(self, *args, **kwargs):
        money = Applications.objects.filter(master=self.holder,status='c',handed_over=False)
        select_fields = ('price','premium', 'change')
        for f in select_fields:
            expression = money.aggregate(Sum(f)).get(str(f)+'__sum')
            if expression is not None:
                setattr(self, f, expression)
            else:
                setattr(self, f, 0)
        super().save(args, kwargs)


    def __str__(self):
        return f'{self.holder}'

    class Meta:
        verbose_name_plural = 'Баланс'
        verbose_name = 'Баланс'
        ordering = ['-holder']


class Warehouse(models.Model):
    owner = models.ForeignKey(AdvUser, on_delete=models.DO_NOTHING, verbose_name='Владелец')
    ykp7 = models.FloatField(default=0, verbose_name='УКП-7')
    ykp12 = models.FloatField(default=0, verbose_name='УКП-12')
    rf = models.FloatField( default=0, verbose_name='RF')
    tm = models.FloatField(default=0, verbose_name='TM')
    md = models.FloatField(default=0, verbose_name='MD')
    door_closer = models.FloatField(default=0, verbose_name='Доводчик')

    # -----------------------------------------------------------------------------------------------------------------------
    #         Отбираем нужные нам записи из таблицы, создаем список необходимых полей. Циклом проходим по спску
    #           и проверяем условие, если сумма всех значений этой строки в таблице не пустое значение,
    #               то полям модели склада присваиваем значения равные текущему значению минус сумма всех значений поля.
    # -----------------------------------------------------------------------------------------------------------------------
    def save(self, *args, **kwargs):
        equipment = Applications.objects.filter(master=self.owner, status='c', counted_eq=False)
        select_fields = ('ykp7', 'ykp12', 'rf','tm', 'md', 'door_closer')
        for f in select_fields:
            total_eq = equipment.aggregate(Sum(f)).get(str(f)+'__sum')
            if total_eq is not None:
                current_field = float(getattr(self, f))
                new_field = current_field - total_eq
                setattr(self, f, new_field)
        equipment.update(counted_eq=True)
        super().save(args, kwargs)



    def __str__(self):
        return f'{self.owner.id} {self.owner.first_name} {self.owner.last_name}'

    class Meta:
        verbose_name_plural = 'Склад'
        verbose_name = 'Склад'
        ordering = ['-owner']