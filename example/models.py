from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Template(models.Model):
    #user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    #def __init__(self,*args):
    #   for attr in args:
    #      self.__dict__[attr] = 0

    def __str__(self):
        return self.title

class Copy(models.Model):
    user = models.ForeignKey(User)
    template = models.ForeignKey(Template)
    title = models.CharField(max_length=100)

    #def gettitle(self):
    #    return self.template.title

    def __str__(self):
        return self.title

class Listitem(models.Model):
    template = models.ForeignKey(Template)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Listitemcopy(models.Model):
    copy = models.ForeignKey(Copy)
    #listitem = models.ForeignKey(Listitem)
    text = models.CharField(max_length=200)
    value = models.BooleanField(default=False)

    #def get_text(self):
    #    return self.listitem.text

    def __str__(self):
        return self.text
