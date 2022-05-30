# Generated by Django 4.0.4 on 2022-05-27 05:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_managers_remove_usermodel_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='follow',
            field=models.ManyToManyField(related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
    ]
