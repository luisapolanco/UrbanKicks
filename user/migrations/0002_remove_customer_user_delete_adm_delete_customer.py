# Generated by Django 4.2.11 on 2024-03-17 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Adm',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]