# Generated by Django 4.0.1 on 2022-04-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='foodprice',
        ),
        migrations.AddField(
            model_name='order',
            name='offerprice',
            field=models.IntegerField(default=0),
        ),
    ]
