# Generated by Django 3.2.8 on 2023-04-20 08:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0022_auto_20230419_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
