# Generated by Django 4.0.1 on 2022-04-29 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_reviewtab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewtab',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
