# Generated by Django 4.1.1 on 2022-09-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0022_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ManyToManyField(blank=True, to='pizzaapp.pizza')),
            ],
        ),
    ]