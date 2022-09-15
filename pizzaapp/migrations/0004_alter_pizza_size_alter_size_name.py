# Generated by Django 4.1.1 on 2022-09-12 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_rename_key_pizza_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(help_text='Selec the size of the pizza.', null=True, on_delete=django.db.models.deletion.CASCADE, to='pizzaapp.size'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text='Select the size of the pizza.', max_length=100),
        ),
    ]
