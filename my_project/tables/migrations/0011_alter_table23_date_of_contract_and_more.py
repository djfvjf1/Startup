# Generated by Django 4.1.7 on 2023-04-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0010_alter_table23_date_of_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table23',
            name='date_of_contract',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='table23',
            name='end_date',
            field=models.CharField(max_length=100),
        ),
    ]
