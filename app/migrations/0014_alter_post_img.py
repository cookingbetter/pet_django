# Generated by Django 3.2.8 on 2023-04-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='dishes/651.jpg', upload_to='dishes/'),
        ),
    ]