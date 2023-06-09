# Generated by Django 3.2.8 on 2023-04-19 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='images/1.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.ForeignKey(default='Ужин', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.type'),
        ),
    ]
