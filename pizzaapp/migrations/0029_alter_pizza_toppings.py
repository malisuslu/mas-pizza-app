# Generated by Django 4.1.1 on 2023-01-20 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0028_alter_pizza_size_delete_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.CharField(choices=[('pepperoni', 'Pepperoni'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions'), ('pineapple', 'Pineapple'), ('ham', 'Ham'), ('anchovies', 'Anchovies'), ('extra cheese', 'Extra Cheese')], max_length=100),
        ),
    ]