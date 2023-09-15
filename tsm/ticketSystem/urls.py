from django.urls import path

from .views import index, create_new_app, completed, balance_template

app_name = 'ticketSystem'
urlpatterns = [
    path('balance', balance_template, name='balance'),
    path('create_new_app', create_new_app, name='create_new_app'),
    path('completed', completed, name='completed'),
    path('', index, name='index')
]