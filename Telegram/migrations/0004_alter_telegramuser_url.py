# Generated by Django 4.0.4 on 2022-05-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telegram', '0003_alter_telegramuser_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='url',
            field=models.URLField(max_length=2048, null=True),
        ),
    ]
