# Generated by Django 4.0.1 on 2022-04-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_food_offerprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.food')),
            ],
        ),
    ]
