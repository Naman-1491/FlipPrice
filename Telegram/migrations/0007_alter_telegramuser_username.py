# Generated by Django 4.0.4 on 2022-05-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telegram', '0006_remove_telegramuser_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
