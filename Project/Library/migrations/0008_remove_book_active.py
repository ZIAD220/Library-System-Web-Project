# Generated by Django 3.2.4 on 2021-07-20 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0007_auto_20210720_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='active',
        ),
    ]
