# Generated by Django 2.2.14 on 2021-11-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211111_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='First_login',
            field=models.BooleanField(default=True),
        ),
    ]
