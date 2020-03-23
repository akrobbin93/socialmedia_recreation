#==============================================================================
#accounts/models.py
#
#
#==============================================================================
#----------------------------
#IMPORTS
#----------------------------
from django.db import models
from django.contrib import auth

#----------------------------
#Class:User
#----------------------------
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
