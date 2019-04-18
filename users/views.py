from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    """ 注销用户 """
    lougt(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))