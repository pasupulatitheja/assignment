# Generated by Django 2.2.3 on 2019-10-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='time',
            field=models.TimeField(blank=True, verbose_name='LoginModel Time'),
        ),
    ]
