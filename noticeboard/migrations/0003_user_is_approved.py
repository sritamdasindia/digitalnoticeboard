# Generated by Django 2.1.1 on 2018-09-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
