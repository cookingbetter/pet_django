# Generated by Django 3.2.8 on 2023-04-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='1.jpg', upload_to='images/'),
        ),
    ]
