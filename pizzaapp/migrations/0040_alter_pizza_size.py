# Generated by Django 4.1.1 on 2023-02-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0039_alter_pizza_topping1_alter_pizza_topping2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(default='Small', max_length=10),
        ),
    ]
