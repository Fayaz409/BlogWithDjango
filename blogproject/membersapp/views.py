from django.shortcuts import render
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Create your views here.
class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html', {})