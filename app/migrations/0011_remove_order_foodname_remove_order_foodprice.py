# Generated by Django 4.0.1 on 2022-05-04 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_reviewtab_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='foodname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='foodprice',
        ),
    ]