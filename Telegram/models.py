from django.db import models


# Create your models here.
class TelegramUser(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=25, null=True)
    url = models.URLField(max_length=2048, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
