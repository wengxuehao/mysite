# Generated by Django 2.1.8 on 2019-06-28 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190627_1532'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='Q_table',
        ),
    ]
