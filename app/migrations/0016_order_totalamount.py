# Generated by Django 4.0.1 on 2022-07-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalAmount',
            field=models.IntegerField(default=0),
        ),
    ]
