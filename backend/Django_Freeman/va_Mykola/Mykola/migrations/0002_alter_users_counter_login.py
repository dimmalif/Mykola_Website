# Generated by Django 4.1.7 on 2023-03-09 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mykola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='counter_login',
            field=models.IntegerField(default=0),
        ),
    ]
