from django.contrib import auth
from django.db import models
from django.utils import timezone


class Expense(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    description = models.TextField()
    username = models.CharField(max_length=200,default="unknown")

    def __str__(self):
        return self.title
