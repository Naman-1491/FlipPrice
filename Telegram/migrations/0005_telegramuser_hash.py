# Generated by Django 4.0.4 on 2022-05-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telegram', '0004_alter_telegramuser_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='hash',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
