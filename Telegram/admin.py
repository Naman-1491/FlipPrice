from django.contrib import admin
from .models import TelegramUser


# Register your models here.
class TelegramUserData(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'price', 'date', 'time', 'date_created', 'time_created']


admin.site.register(TelegramUser, TelegramUserData)
