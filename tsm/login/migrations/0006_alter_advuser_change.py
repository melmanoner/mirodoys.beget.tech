# Generated by Django 3.2.11 on 2022-10-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20221020_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='change',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Сдать'),
        ),
    ]