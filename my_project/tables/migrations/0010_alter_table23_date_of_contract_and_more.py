# Generated by Django 4.1.7 on 2023-04-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_alter_table23_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table23',
            name='date_of_contract',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='table23',
            name='end_date',
            field=models.DateField(),
        ),
    ]
