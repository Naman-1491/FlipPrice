# Generated by Django 4.0.4 on 2022-05-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telegram', '0002_alter_telegramuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
