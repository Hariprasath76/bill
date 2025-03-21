# Generated by Django 4.1.2 on 2022-12-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ebBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=15)),
                ('pre_reading', models.IntegerField()),
                ('cur_reading', models.IntegerField()),
                ('units_kwh', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
            options={
                'db_table': 'EB-Bill',
            },
        ),
    ]
