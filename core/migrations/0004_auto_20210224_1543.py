# Generated by Django 3.1.6 on 2021-02-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210223_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='exp_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='security_number',
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
