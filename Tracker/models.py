from django.db import models


# Create your models here.
class TelegramUser(models.Model):
    id = models.PositiveIntegerField(primary_key=True, null=False)
    username = models.CharField(max_length=25, null=False)
    url = models.URLField(max_length=2048)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
