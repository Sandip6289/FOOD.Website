# Generated by Django 4.0.1 on 2022-04-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_food_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='offer',
            field=models.IntegerField(default=0),
        ),
    ]