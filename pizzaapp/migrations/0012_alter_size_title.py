# Generated by Django 4.1.1 on 2022-09-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0011_alter_size_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=20),
        ),
    ]
