import datetime

from django.db import models

# Create your models here.
class Type(models.Model):
    type = models.CharField(10, unique=True)


class User(models.Model):
    name = models.CharField(20, unique=True)


class Record(models.Model):
    cost = models.IntegerField()
    note = models.CharField(100, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)

