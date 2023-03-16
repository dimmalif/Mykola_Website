# Generated by Django 4.1.7 on 2023-03-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mykola', '0002_alter_users_counter_login'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['data_reg'], 'verbose_name': "Mykola's users", 'verbose_name_plural': "Mykola's users"},
        ),
        migrations.AddField(
            model_name='users',
            name='person_password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]