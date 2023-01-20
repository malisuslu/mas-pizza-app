# Generated by Django 4.1.1 on 2023-01-20 01:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0031_remove_pizza_topping1_remove_pizza_topping2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('pepperoni', 'Pepperoni'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions'), ('pineapple', 'Pineapple'), ('ham', 'Ham'), ('anchovies', 'Anchovies'), ('extra cheese', 'Extra Cheese')], default=b']', max_length=100),
        ),
    ]