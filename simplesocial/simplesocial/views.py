#==============================================================================
#simplesocial/views.py
#
#
#==============================================================================
#----------------------------
#IMPORTS
#----------------------------
from django.views.generic import TemplateView

#----------------------------
#Class:HomePage
#----------------------------
class HomePage(TemplateView):
    template_name = 'index.html'

#----------------------------
#Class:TestPage
#----------------------------
class TestPage(TemplateView):
    template_name = 'test.html'

#----------------------------
#Class:ThanksPage
#----------------------------
class ThanksPage(TemplateView):
    template_name = 'thanks.html'
