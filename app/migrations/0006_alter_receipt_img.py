# Generated by Django 4.1.7 on 2023-04-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_receipt_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='img',
            field=models.CharField(default=1000, max_length=100),
        ),
    ]
