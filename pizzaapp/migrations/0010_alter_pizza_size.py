# Generated by Django 4.1.1 on 2022-09-12 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0009_alter_pizza_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaapp.size'),
        ),
    ]
