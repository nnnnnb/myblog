# Generated by Django 2.0.7 on 2018-07-27 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180727_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='words',
        ),
    ]