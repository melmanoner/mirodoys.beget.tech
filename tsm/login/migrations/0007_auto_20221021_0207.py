# Generated by Django 3.2.11 on 2022-10-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_advuser_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='balance',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Баланс'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='premium',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Премия'),
        ),
    ]
