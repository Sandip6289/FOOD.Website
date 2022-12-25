# Generated by Django 4.0.1 on 2022-04-24 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=200)),
                ('foodtype', models.CharField(max_length=200)),
                ('foodprice', models.IntegerField()),
                ('offer', models.CharField(max_length=20)),
                ('foodpic', models.ImageField(upload_to='app/foodimg')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='foodid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.food'),
        ),
    ]