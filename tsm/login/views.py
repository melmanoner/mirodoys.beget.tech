from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import AdvUser

from .forms import RegisterUserForm
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView

# Create your views here.


class TSLoginView(LoginView):
    template_name = 'ticketSystem/login.html'

class TSLogoutView(LogoutView):
    template_name = 'ticketSystem/index.html'

class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'ticketSystem/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'ticketSystem/register_done.html'