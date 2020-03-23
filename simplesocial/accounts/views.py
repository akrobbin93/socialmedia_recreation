#==============================================================================
#accounts/views.py
#
#
#==============================================================================
#----------------------------
#IMPORTS
#----------------------------
from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import (TemplateView, ListView,
                                DetailView, CreateView,
                                UpdateView, DeleteView)
#----------------------------
#Class:SignUp
#----------------------------
class SignUp(CreateView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
