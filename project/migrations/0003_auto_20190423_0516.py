# Generated by Django 2.1 on 2019-04-23 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190423_0515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category_id',
            new_name='category',
        ),
    ]
