from django.urls import path

from .views import TSLoginView, TSLogoutView

from .views import RegisterUserView, RegisterDoneView

app_name = 'login'
urlpatterns = [
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('login/', TSLoginView.as_view(), name='login'),
    path('logout/', TSLogoutView.as_view(), name='logout'),
]